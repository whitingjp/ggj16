#!/bin/bash
set -x
set -e
rm -rf build
cp -r www build
python src/ritual.py
