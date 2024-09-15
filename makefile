

.PHONY: server
server:
	${GITHUB_WORKSPACE}/scripts/install/apt/__apt_install.sh $@

.PHONY: client
client:
	./scripts/install/apt/__apt_install.sh $@
