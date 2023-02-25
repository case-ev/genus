#!/bin/bash

# Build the source code and documentation

upload=0
build_docs=0

while getopts "ud" arg
do
    case "$arg" in
        u)
            upload=1
            ;;
        d)
            build_docs=1
            ;;
    esac
done

python -m pip install --upgrade pip
pip install build
python -m build

if [ $build_docs -eq 1 ]; then
    sys/doc.sh
fi

if [ $upload -eq 1 ]; then
    # Code to upload to PyPI
    echo -e "\x1b[31;20mWARNING\x1b[0m Uploading package to PyPI"
    echo -e "UPLOADING NOT CURRENTLY IMPLEMENTED"
    echo -e "\x1b[32;20mSuccesfully uploaded to PyPI\x1b[0m"
fi
