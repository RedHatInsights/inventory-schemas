#!/bin/bash
set -e

cd ./tools/simple-test/
source venv/bin/activate
python tester.py ../../schemas/system_profile/v1.yaml ../../scratch/sample.json