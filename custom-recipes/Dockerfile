FROM docker://mambaorg/micromamba:1.5.3

ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN micromamba install -y \
    -n "base" \
    -c conda-forge \
    boa \
    "conda-build<3.28.0" \
    conda-verify \
    git \
    grayskull \
    openssh \
    vim && \
  micromamba clean --all --yes

RUN conda config --system --set channel_priority 'strict' && \
  conda config --system --prepend channels conda-forge && \
  conda config --system --prepend channels nodefaults
