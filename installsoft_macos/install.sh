# !/usr/bash
# 安装macos的软件

sudo echo '获取权限:'

echo '安装homebrew'
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo '开启homebrew cask-versions监听'
brew tap homebrew/cask-versions

cat ./data.txt | while read line
do
    echo "brew cask install $line"
    brew cask install $line
done