#%Module 1.0
proc ModulesHelp {} {
    puts stdout    "Mamba environment for cycle 202301"
}

module-whatis  "Module loads the mamba environment for cycle 202301"

if { [ module-info mode load ] } {
    system    "/gpfs/exfel/sw/software/local/etc/metrics.sh 'mamba/202301'"
    puts stderr "Default module version changed from 1.1.2 to 202301"
    puts stderr "Use `module load exfel_anaconda3/1.1.2` to revert to previous version if required"
    puts stderr "For more information on the new approach to environment management see the documentation here: https://european-xfel.github.io/environments/"
}

module load mambaforge

prepend-path    PATH /gpfs/exfel/sw/software/mambaforge/22.11/envs/202301/bin
prepend-path    XML_CATALOG_FILES file {///gpfs/exfel/sw/software/mambaforge/22.11/envs/202301/etc/xml/catalog file} ///etc/xml/catalog
setenv          CONDA_DEFAULT_ENV 202301
setenv          CONDA_PREFIX /gpfs/exfel/sw/software/mambaforge/22.11/envs/202301
setenv          CONDA_PROMPT_MODIFIER {(202301) }
setenv          CONDA_SHLVL 1
setenv          GSETTINGS_SCHEMA_DIR /gpfs/exfel/sw/software/mambaforge/22.11/envs/202301/share/glib-2.0/schemas
setenv          GSETTINGS_SCHEMA_DIR_CONDA_BACKUP {}

