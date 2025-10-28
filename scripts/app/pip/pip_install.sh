# !/bin/bash
set -eu

input_file="requirements.txt"
work_path="$(realpath $(dirname "$0"))"

mkdir -p "${HOME}/.local/bin"

curl "https://bootstrap.pypa.io/get-pip.py" -o get-pip.py
python3 get-pip.py --user
rm ./get-pip.py

python3 -m pip install \
  --user \
  --requirement \
  "${work_path}/${input_file}"
