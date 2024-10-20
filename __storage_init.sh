# !/#/bash
set -eu

# chown
while read jjj
do
  echo  "sudo chown -R "${USER}":"${USER}"   "${jjj}"  "

done < <(grep -oP "(LOCAL_STORAGE.*=)\K.*"  <<<  $(printenv))
