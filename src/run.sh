#!/bin/bash -l

python3 -m venv .venv 
source .venv/bin/activate
pip3 install colored
python3 ./src/main.py
