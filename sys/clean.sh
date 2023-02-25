#!/bin/bash

# Clean the directory

rm -rf ./.pytest_cache ./build ./logs ./src/genus.egg-info ./dist ./book
find . -name __pycache__ -exec rm -rf {} +
