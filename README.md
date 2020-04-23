# Shell_Script 一些简单的脚本

- `installsoft_macos` 为macos 安装我需要的大部分软件

- `unicom_lightCat_restart.py` 通过命令行重启北京联通光猫，使用python3实现，调用了光猫的http接口。
    使用方式：`python3 unicom_lightCat_restart.py 'http://192.168.1.1' 'mima1'`
    
    ![北京联通光猫的登录界面](image/1587619662449.jpg)
    
- `git-url.sh` 获得当前目录git仓库的远程地址，将`git-url.sh`中的两个函数粘贴到`.zshrc`中，gurl获得URL，god直接打开URL

- `tmfmt.py` 格式化时间戳的简单工具，支持10位和13位时间戳。`python3 tmfmt.py 1586251033958`
