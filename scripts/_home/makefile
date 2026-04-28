.DEFAULT_GOAL := help
# Self-Documented Makefile

# all targets are phony
PHONY_TARGETS := $(shell grep -E '^[a-zA-Z_-]+:' $(MAKEFILE_LIST) | sed 's/://')
.PHONY: $(PHONY_TARGETS)


help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


profile: ## deploy the .profile file (${HOME}/.profile)
	@ls ./cp_home_profile.sh


config: ## deploy the .config files (${HOME}/.[Any_Apps])
	@ls ./ln_soft_home_config.sh


firefox:



mkdir: ## make directory
	@ls ./mkdir.sh