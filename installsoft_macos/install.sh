#! /bin/bash
# 安装macos的软件
USER_HOME=$(cd ~/ | pwd)


# 安装或者更新Homebrew
installOrUpgrade_Homebrew(){
if type brew >/dev/null 2>&1; then 
  echo 'Homebrew已经存在,检查更新...' 
  brew update
else 
  echo 'Homebrew已经存在,进行安装...' 
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
}

# 安装常用命令库
installExtlib(){
echo '安装常用的库'
cat ./extlib.txt | while read line
do
    echo "$(brew list| grep -c $line)"
    if [ $(brew list| grep -c $line) -gt 0 ] ;
    then
         echo "软件 $line 已经安装,检查更新..."
         brew upgrade $line
    else
         echo "软件 $line 未安装,进行安装..."
         #brew install $line
    fi
done
}

# 安装GUI软件
installApps(){
echo '开启homebrew cask-versions监听'
brew tap homebrew/cask-versions

echo '安装常用软件'
cat ./apps.txt | while read line
do
    echo "$(brew cask list| grep -c $line)"
    if [ $(brew cask list| grep -c $line) -gt 0 ] ;
    then
         echo "软件 $line 已经安装,检查更新..."
         brew cask upgrade $line
    else
         echo "软件 $line 未安装,进行安装..."
         #brew cask install $line
    fi
done
}

sudo echo '获取管理员权限'
installOrUpgrade_Homebrew
installExtlib
installApps