.DEFAULT_GOAL := help
# Self-Documented Makefile

# all targets are phony
PHONY_TARGETS := $(shell grep -E '^[a-zA-Z_-]+:' $(MAKEFILE_LIST) | sed 's/://')
.PHONY: $(PHONY_TARGETS)


help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


deno: ## install - deno
	@ls ./deno/deno_installer.sh


docker: ## install - docker
	@ls ./docker/docker_installer.sh


github-my-repository: ## git clone -



github-self-host: ## git clone - "self host apps" container
	@ls ./github-self-host/github-self-host_installer.sh


package:  ## install - package
	@ls ./package/package_installer.sh


samba: ## create samba user
	@ls ./samba/setup_samba.sh


uv: ## install - uv
	@ls ./uv/uv_installer.sh
# 	@ls ./uv/uv_tool_installer.sh


vscode: ## install - vscode
	@ls ./vscode/vscode_installer.sh