.DEFAULT_GOAL := help
# Self-Documented Makefile

# all targets are phony
PHONY_TARGETS := $(shell grep -E '^[a-zA-Z_-]+:' $(MAKEFILE_LIST) | sed 's/://')
.PHONY: $(PHONY_TARGETS)


help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


apt-package-desktop: ## install - "apt-package-desktop"
	@ls ./apt/apt_installer.sh  desktop


apt-package-server: ## install - "apt-package-server"
	@ls ./apt/apt_installer.sh  server


docker: ## install - docker
	@ls ./docker/docker_installer.sh


git-self-host: ## git clone - "self host apps" container
	@ls ./self-host/git_clone.sh


samba: ## create samba user
	@ls ./samba/setup_samba.sh


uv: ## install - uv
	@ls ./uv/uv_installer.sh
# 	@ls ./uv/uv_tool_installer.sh


vscode: ## install - vscode
	@ls ./vscode/vscode_installer.sh