#!/bin/bash

set -euo pipefail
shopt -s inherit_errexit

conda index ./conda-bld

export CONDA_BLD_PATH="$PWD/conda-bld"

conda mambabuild \
  --skip-existing \
  --python 3.9 \
  --numpy 1.23 \
  --no-anaconda-upload \
  -c nodefaults -c conda-forge -c $CONDA_BLD_PATH \
  ./recipes

conda index ./conda-bld
