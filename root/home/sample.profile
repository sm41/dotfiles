# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022


# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# XDG Base Directory - ArchWiki
# https://wiki.archlinux.jp/index.php/XDG_Base_Directory

# XDG Base Directory - ArchWiki
# https://wiki.archlinux.org/title/XDG_Base_Directory

# XDG
export XDG_CONFIG_HOME=${HOME}/.config
export  XDG_CACHE_HOME=${HOME}/.cache
export   XDG_DATA_HOME=${HOME}/.local/share
export  XDG_STATE_HOME=${HOME}/.local/state


# set PATH so it includes user's private bin if it exists
if [ -d "${HOME}/bin" ] ; then
    PATH=$PATH:${HOME}/bin
fi

if [ -d "${HOME}/bin/sh" ] ; then
    PATH=$PATH:${HOME}/bin/sh
fi

# python
export      PYTHON_HISTORY=${XDG_STATE_HOME}/python/history
export PYTHONPYCACHEPREFIX=${XDG_CACHE_HOME}/python
export      PYTHONUSERBASE=${XDG_DATA_HOME}/python



export PATH=$PATH:${HOME}/bin





# hogefuga=/etc/profile.d





# if [ -d ${hogefuga} ]; then
#   for i in /etc/profile.d/*.sh; do
#     if [ -r $i ]; then
#       . $i
#     fi
#   done
#   unset i
# fi
