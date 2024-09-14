#!/bin/bash

#-install---------------------------------------------------------------------------------------
.PHONY: install_apt
install_apt:
	bash install_apt.sh

.PHONY: install_pip
install_pip:
	bash install_pip.sh

#----------------------------------------------------------------------------------------------
.PHONY: export_path
export_path:
	bash export_path.sh

#-symlink---------------------------------------------------------------------------------------
.PHONY: symlink_xxx
symlink_xxx:
	bash symlink_xxx.sh

.PHONY: symlink_firefox
symlink_firefox:
	bash symlink_firefox.sh

#-backup----------------------------------------------------------------------------------------
.PHONY: backup_firefox
backup_firefox:
	bash backup_firefox.sh