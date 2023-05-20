#!/bin/bash

# RUN EXAMPLE to prepare venv: source prepare_venv.sh
# RUN EXAMPLE to run-tests: source prepare_venv.sh test

if [ -z "$1" ]; then
  ARGUMENT=""
else
  ARGUMENT="$1"
fi


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
python3 -m venv venv
source "${SCRIPT_DIR}"/venv/bin/activate
python3 setup.py install || true
pip3 install -r requirements.txt

if [ "$ARGUMENT" = "test" ]; then
  python3 -m pytest test_json_handler.py
fi