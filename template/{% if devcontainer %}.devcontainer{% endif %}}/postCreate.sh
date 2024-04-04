# force using `setup.py develop` when installing with `-e`
export SETUPTOOLS_ENABLE_FEATURES="legacy-editable"
# alternatively, one could use
#   --config-settings editable_mode=compat
# but it's only a transitional solution and will be removed
# in future setuptools releases.
# https://setuptools.pypa.io/en/latest/userguide/development_mode.html
# problem with editable mode
# https://github.com/pypa/setuptools/issues/3557
# https://github.com/pypa/setuptools/issues/3518
# https://github.com/microsoft/pylance-release/issues/3473
# https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#editable-install-modules-not-found

# Install project packages locally
python3 -m pip install -e /code[dev]
