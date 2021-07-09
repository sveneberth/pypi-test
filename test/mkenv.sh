#!/usr/bin/env bash

set -ex

# create and active venv
python -m venv venv
source venv/bin/activate

# install package
python -m pip install -i https://test.pypi.org/simple/ first-package-xyz567 -U

echo "Done"
echo "Run: $ python main.py"
