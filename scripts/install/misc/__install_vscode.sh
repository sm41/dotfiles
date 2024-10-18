# !/bin/bash
set -eu

# VSCode
curl -L https://go.microsoft.com/fwlink/?LinkID=760868 -o vscode.deb

sudo apt-get install ./vscode.deb
rm ./vscode.deb
