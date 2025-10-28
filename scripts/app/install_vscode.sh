# !/bin/bash
set -eu

curl -L https://go.microsoft.com/fwlink/?LinkID=760868 -o vscode.deb

sudo apt-get install ./vscode.deb
rm ./vscode.deb
