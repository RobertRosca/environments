# Quick Start

How to start using our environments quickly via terminal or Jupyter.

## Terminal (SSH)

```shell
$ ssh $USER@max-exfl-display.desy.de

$ module load exfel  # Enable our modules
- EXFEL modulepath enabled

$ module load exfel-python  # Load current python environment
Loading exfel-python/202301
  Loading requirement: mambaforge/22.11

$ python3 ...
```

!!! info "More Information"

    - [SSH Access](https://rtd.xfel.eu/docs/data-analysis-user-documentation/en/latest/offline/#ssh-access).
    - [Module System](./environments.md#module-system).
    - [Environment List](./environments.md#environment-list).
    - [Remote Desktop - EuXFEL DA Documentation](https://rtd.xfel.eu/docs/data-analysis-user-documentation/en/latest/offline/#remote-desktop).
    - [Interactive Login - DESY Documentation](https://confluence.desy.de/display/MXW/Interactive+Login).

## Jupyter

1. Got to <https://max-jhub.desy.de>.
2. Start a session.
3. Select `exfel` to get our current environment.

!!! info "More Information"

    - [JupyterHub - EuXFEL DA Documentation](https://rtd.xfel.eu/docs/data-analysis-user-documentation/en/latest/jhub/).
    - [JupyterHub on Maxwell - DESY Documentation](https://confluence.desy.de/display/MXW/JupyterHub+on+Maxwell).
