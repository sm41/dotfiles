# !/bin/bash
set -eux






input_file=git_repo.txt
work_path=$(cd $(dirname $0) && pwd)

# cd /opt


while read repository_url
do

  [ -z ${repository_url} ] && continue
  [ ${repository_url::1} = "#" ] && continue

  git clone ${repository_url}.git

done < ${work_path}/${input_file}

