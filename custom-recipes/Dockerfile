FROM mambaorg/micromamba:1.1.0

RUN micromamba install -y \
  -c conda-forge -n base "python=3.9" \
  boa \
  conda-verify \
  git \
  grayskull \
  openssh

ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN conda config --set channel_priority 'strict'
RUN conda config --prepend channels conda-forge
RUN conda config --prepend channels nodefaults

RUN micromamba clean --all --yes
