# Python Copier Template

Opinionated template for new python projects.

## Features 

- ✅ build with setuptools 
- ✅ `pyproject.toml` 
- ✅ `requirements.txt`
- ✅ `requirements.dev.txt`
- ✅ ruff
- ✅ vscode sensible settings for a python project
- ✅ tbump for python pkg versioning
- ✅ (optional) devcontainer
- ✅ (optional) namespace (can have nested namespaces)

i might add more feature in the future like other build systems (poetry, pdm, hatch, nuitka) or lockfile (if what discussed in https://discuss.python.org/t/lock-files-again-but-this-time-w-sdists/ becomes a thing)


### Customize devcontainer

As of now copier does not support multiple/repeated prompts, so to gather multiple values I use json prompt in for `devcontainer_host_env` and `devcontainer_extra_mounts`. You can automate it passing a yaml file with the values (`--data-file file.yml`).

## How To Use It

install copier

```bash
pipx install copier
```

run copier over this repo
```bash
copier copy gh:matteo-bruni/python-pkg-template.git my_project
```
