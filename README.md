# Shell_Script 一些简单的脚本

## macOS使用brew自动安装一些软件
- `installsoft_macos` 为macos 安装我需要的大部分软件

## Git相关
- `git-url.sh` 获得当前目录git仓库的远程地址，将`git-url.sh`中的两个函数粘贴到`.zshrc`中，gurl获得URL，god直接打开URL
- `tag.py` git打tag简易工具，`python tag.py 分支名 后缀`，直接执行tag会打出 当前分支名-当前年月日-版本，master-20200423-v1.0.0这样的tag并提交。
当设置分支名时，tag会使用该值，指定后缀时，会在tag名后拼接上该后缀。版本号，从1.0.0开始，依次递增。从1.0.9升级时，版本会变为1.1.0

## 时间戳
- `tmfmt.py` 格式化时间戳的简单工具，支持10位和13位时间戳。
  `python3 tmfmt.py 1586251033958`


## 未分类
- `unicom_lightCat_restart.py` 通过命令行重启北京联通光猫，使用python3实现，调用了光猫的http接口。
    使用方式：`python3 unicom_lightCat_restart.py 'http://192.168.1.1' 'mima1'`
    
    ![北京联通光猫的登录界面](image/1587619662449.jpg)
    

