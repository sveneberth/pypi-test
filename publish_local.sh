#!/usr/bin/env bash

set -ex

# cleanup first
rm -rf build dist *.egg-info

# build
python -m build

if [ "$1" == "test" ];
then
  # publish to test
  python -m twine upload --repository testpypi dist/*
else
  # publish
  python -m twine upload dist/*
fi

echo "Done"
