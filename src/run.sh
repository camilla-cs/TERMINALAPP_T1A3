#!/bin/bash -l

python3 -m venv .venv 
source .venv/bin/activate

python3 ./src/main.py
