#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run unit tests
python -m unittest discover -s tests