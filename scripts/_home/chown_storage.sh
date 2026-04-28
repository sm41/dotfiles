# !/#/bash
set -eu

# chown
while read jjj
do
  echo  "sudo chown -R "${USER}":"${USER}"   "${jjj}"  "

done < <(grep -oP "(STORAGE.*=)\K.*"  <<<  $(printenv)  )
# done < <(grep STORAGE <<< $(env))