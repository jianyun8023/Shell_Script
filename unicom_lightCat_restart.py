import hashlib
import re
import sys

import requests


def get_login_check_token(domain: str):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.get(domain, headers=headers)
    regex = r"getElementById\(\"Frm_Loginchecktoken\"\)\.value.=.(\w+);"
    prog = re.compile(regex)
    result = prog.findall(str(response.text))
    login_check_token = result[0]
    print("获得 login_check_token " + login_check_token)
    regex1 = r"getElementById\(\"Frm_Logintoken\"\)\.value.=.\"(\w+)\";"
    prog1 = re.compile(regex1)
    result1 = prog1.findall(str(response.text))
    login_token = result1[0]
    print("获得 login_token " + login_token)
    return login_check_token, login_token, response.cookies


def login(domain: str, password: str):
    login_check_token, login_token, cookies = get_login_check_token(domain)
    user_random_num = '51621269'
    sha256 = hashlib.sha256()
    sha256.update((password + user_random_num).encode('utf-8'))
    password_sha256 = sha256.hexdigest()
    # print("sha256加密结果:", password_sha256)
    payload = {
        'Frm_Logintoken': login_token,
        'Frm_Loginchecktoken': login_check_token,
        '_cu_url': 0,
        'Right': 2,
        'Username': "",
        'UserRandomNum': user_random_num,
        'Password': password_sha256,
        'action': 'login'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(domain, headers=headers, data=payload, cookies=cookies)
    if "initMenu()" in response.text:
        print("登录成功!")
        return response.cookies
    raise Exception('登录失败: {}'.format(response.text))


def get_session_token(domain: str, cookies):
    url = "%s/getpage.gch" % domain
    params = {
        'pid': 1002,
        'nextpage': 'manager_dev_restart_t_BJ.gch'
    }
    response = requests.get(url,
                            params=params,
                            cookies=cookies)
    html = response.text
    regex = r"var\s+session_token\s+=\s+\"(\w+)\";"
    prog = re.compile(regex)
    result = prog.findall(html)
    session_token = result[0]
    print("获得 SessionToken " + session_token)
    return session_token


def restart_light_cat(domain: str, cookies):
    session_token = get_session_token(domain, cookies)
    print("重启光猫")
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'IF_ACTION': 'devrestart',
               'IF_ERRORSTR': 'SUCC',
               'IF_ERRORPARAM': 'SUCC',
               'IF_ERRORTYPE': -1,
               'flag': 1,
               '_SESSION_TOKEN': session_token
               }
    response = requests.post("%s/getpage.gch?pid=1002&nextpage=manager_dev_restart_t_BJ.gch" % domain,
                             headers=headers,
                             data=payload,
                             cookies=cookies
                             )

    if "Transfer_meaning('flag','1')" in response.text:
        print("重启成功,请等待完成!")


def readArgs():
    global domain, password
    domain = sys.argv[1]
    if str.endswith(domain, '/'):
        domain = domain[:len(domain) - 1]
    password = sys.argv[2]
    return domain, password


if __name__ == '__main__':
    domain, password = readArgs()
    cookie = login(domain, password)
    restart_light_cat(domain, cookie)
