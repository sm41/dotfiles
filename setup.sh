#!/usr/bin/bash
set -eu

work_path=$(realpath $(dirname "$0"))

echo $work_path
exit 0

# cp
bash "${work_path}/scripts/deploy/cp/__cp_etc_netplan.sh"
bash "${work_path}/scripts/deploy/cp/__cp_etc_samba.sh"
bash "${work_path}/scripts/deploy/cp/__cp_etc_sysctl.d.sh"
bash "${work_path}/scripts/deploy/cp/__cp_etc_systemd_system.sh"

# ln
bash "${work_path}/scripts/deploy/ln/__ln_soft_home_bin.sh"
bash "${work_path}/scripts/deploy/ln/__ln_soft_home_config.sh"
bash "${work_path}/scripts/deploy/ln/__ln_soft_home_local.sh"
bash "${work_path}/scripts/deploy/ln/__ln_soft_home_mozilla.sh"
bash "${work_path}/scripts/deploy/ln/__ln_soft_home_profile.sh"

# mkdir
bash "${work_path}/scripts/deploy/mkdir/__mkdir.sh"

# install
bash "${work_path}/scripts/install/apt/__apt_install.sh"
bash "${work_path}/scripts/install/misc/__install_vscode.sh"
bash "${work_path}/scripts/install/pip/__pip_install.sh"


