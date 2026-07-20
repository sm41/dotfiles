# !/#/bash
set -eu

find "${HOME}" -xtype l |xargs rm
