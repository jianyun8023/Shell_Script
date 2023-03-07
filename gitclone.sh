set -e

cloneUrl=$1
callBin=$2

if [[ "$cloneUrl" =~ github.com.* ]]; then
  repo=$(echo "$cloneUrl" | sed 's#https://github.com/##g' | sed 's/git@github.com://g' | sed 's/\.git$//')
  serverDir="github"
  repoAuthor=$(echo "$repo" | awk -F '/' '{print $(NF-1)}')
  repoName=$(echo "$repo" | awk -F '/' '{print $NF}')
elif [[ "$cloneUrl" =~ gitlab.com.* ]]; then
  repo=$(echo "$cloneUrl" | sed 's#https://gitlab.com/##g' | sed 's/git@gitlab.com://g' | sed 's/\.git$//')
  serverDir="github"
  repoAuthor=$(echo "$repo" | awk -F '/' '{print $(NF-1)}')
  repoName=$(echo "$repo" | awk -F '/' '{print $NF}')
elif [[ "$cloneUrl" =~ gitee.com.* ]]; then
  repo=$(echo "$cloneUrl" | sed 's#https://gitee.com/##g' | sed 's/git@gitee.com://g' | sed 's/\.git$//')
  serverDir="github"
  repoAuthor=$(echo "$repo" | awk -F '/' '{print $(NF-1)}')
  repoName=$(echo "$repo" | awk -F '/' '{print $NF}')

else
  repo=$(echo "$cloneUrl" | sed 's/\.git$//')
  serverDir=$(echo "$cloneUrl" | awk -F '/' '{print $(NF-2)}')
  repoAuthor=$(echo "$repo" | awk -F '/' '{print $(NF-1)}')
  repoName=$(echo "$repo" | awk -F '/' '{print $NF}')
fi

echo "repo $repo"
echo "serverDir $serverDir"
echo "repoAuthor $repoAuthor"
echo "repoName $repoName"

baseDir="$HOME/Developer/project"

if [ ! -d "$baseDir/$serverDir/$repoAuthor" ]; then
  echo "路径不存在，将创建 $baseDir/$serverDir/$repoAuthor"
  mkdir -p "$baseDir/$serverDir/$repoAuthor"
fi

echo "保存路径: $baseDir/$serverDir/$repoAuthor/$repoName"

if [ ! -d "$baseDir/$serverDir/$repoAuthor/$repoName" ]; then
    cd "$baseDir/$serverDir/$repoAuthor"
    git clone "$cloneUrl"
else
    echo "$repoName 已存在,跳过clone"
fi

if [ ! -n "$callBin" ]; then
  exit 0
fi


echo "$callBin $baseDir/$serverDir/$repoAuthor/$repoName"
$callBin "$baseDir/$serverDir/$repoAuthor/$repoName"

