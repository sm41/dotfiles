.DEFAULT_GOAL := help
# Self-Documented Makefile

# all targets are phony
PHONY_TARGETS := $(shell grep -E '^[a-zA-Z_-]+:' $(MAKEFILE_LIST) | sed 's/://')
.PHONY: $(PHONY_TARGETS)


help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


all: netplan samba sysctl systemd


netplan: ## generate "netplan config.yaml"
	@ls ./envsubst_etc_netplan.sh


samba: ## generate "smb.conf"
	@ls ./envsubst_etc_samba.sh


sysctl: ## generate "ipv6-privacy.conf"
	@ls ./envsubst_etc_sysctl.d.sh


systemd: ## generate "systemd mount unit"
	@ls ./envsubst_etc_systemd_system.sh