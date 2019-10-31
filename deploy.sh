#!/usr/bin/env bash
git add .
git ci -m "$1"
git push

rm -r dist
rm -r build
python setup.py sdist bdist_wheel
twine upload  dist/*