

.PHONY: server
server:
	${GITHUB_WORKSPACE}/scripts/install/apt/__apt_install.sh server

.PHONY: client
client:
	echo "piyopiyo"
