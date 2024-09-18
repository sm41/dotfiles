# !/bin/bash
set -eu

target_file=.gitconfig
submodule_file=piyo.conf

# check .gitconfig
if   [[ -e ${HOME}/${target_file} ]] && [[ -e ${HOME}/${submodule_file} ]] ; then
  echo "${target_file} and ${submodule_file} is already exist"
  echo "check both file"
  exit 1

elif [[ -e ${HOME}/${target_file} ]] && [[ ! -e ${HOME}/${submodule_file} ]] ; then
  mv ${HOME}/${target_file}  ${HOME}/${submodule_file}
  echo "rename file ${target_file}  ===>  ${submodule_file}"
  exit 0

elif [[ ! -e ${HOME}/${target_file} ]] && [[ -e ${HOME}/${submodule_file} ]] ; then
  echo "${submodule_file} is already exist"
  exit 1

elif [[ ! -e ${HOME}/${target_file} ]] && [[ ! -e ${HOME}/${submodule_file} ]] ; then
  echo "Start initial settings"
  echo "make ${target_file}"

fi


echo "----------------------------------------------------------------"
echo "# (1/2) Please input data"
read -p  "┣━ NAME  : 👤 [ git config --global user.name  ]  ==>  "  name_data
read -p  "┗━ EMAIL : 📧 [ git config --global user.email ]  ==>  "  mail_data
echo "----------------------------------------------------------------"
echo "# (2/2) check input data"
read -p  "┗━ setting is ok?  ==>  [y/n] "  bbb
echo "----------------------------------------------------------------"

function section_of_user(){
cat << EOF > ${submodule_file}
[user]
	name  = ${name_data}
	email = ${mail_data}
EOF
}

case ${bbb} in

  [Yy])
    echo "# ✅ Setup successful"
    echo
    section_of_user
    cat ${HOME}/${submodule_file}
    echo
    ;;

  [Nn])
    echo "# ❌ Setup failed"
    ;;

  *)
    echo "# ⚠️  Invalid input"
    ;;

esac

echo "----------------------------------------------------------------"
