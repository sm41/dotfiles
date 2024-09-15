

.PHONY: all
all: client server


.PHONY: client
client:
	./scripts/install/apt/__apt_install.sh $@
	./scripts/install/misc/__install_vscode.sh
	# ./scripts/install/pip/__pip_install.sh


.PHONY: server
server:
	./scripts/install/apt/__apt_install.sh $@
	# ./scripts/install/misc/__install_docker.sh
	./scripts/install/git/__git_clone.sh


.PHONY: network
network:
	./scripts/deploy/cp/__cp_etc_netplan.sh
	./scripts/deploy/cp/__cp_etc_sysctl.d.sh
	./scripts/deploy/cp/__cp_etc_systemd_system.sh


.PHONY: link
link:
	./scripts/deploy/ln/hard/__ln_hard_home_config_systemd.sh
	./scripts/deploy/ln/soft/__ln_soft_home_config.sh
	./scripts/deploy/ln/soft/__ln_soft_home_local.sh
	./scripts/deploy/ln/soft/__ln_soft_home_mozilla.sh