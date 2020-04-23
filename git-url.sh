#!/usr/bin/env bash

# 获得当前目录git仓库的网页地址，测试支持github、gitlab
function gurl() {
  git_url=$(git remote get-url origin | sed -E 's|^ssh://git@|http://|' | sed 's/\.git//g' | sed -E '    s/:2222//')
  current_branch=$(git branch -v | grep '\*' | awk '{print $2}')
  if [ "$current_branch" != 'master' ]; then
    git_url="$git_url/tree/$current_branch"
  fi
  $git_url
}
# mac上使用open命令打开链接
function gob() {
  open $(gurl)
}

export -f gurl
export -f gob