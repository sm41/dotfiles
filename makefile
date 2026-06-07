# include ./scripts/_etc/makefile
include ./scripts/_home/makefile
# include ./scripts/app/makefile


.DEFAULT_GOAL := help
# Self-Documented Makefile

# all targets are phony
PHONY_TARGETS := $(shell grep -E '^[a-zA-Z_-]+:' $(MAKEFILE_LIST) | sed 's/://')
.PHONY: $(PHONY_TARGETS)


help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


all: ## none
	@echo "hogefuga"