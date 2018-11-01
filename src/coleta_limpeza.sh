#!/usr/bin/env bash

cd scraping

python extractor.py

cd ..
cd sanitization

python clean.py
