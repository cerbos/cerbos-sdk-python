## Development

### Async and non-async

[Unasync](https://unasync.readthedocs.io/en/latest/index.html) is used to generate non-async code based on the async implementation. Only make changes to files in `cerbos/sdk/_async`. Then run `./pw generate` to re-generate the code in `cerbos/sdk/_sync`.


### Package management
This project uses [PDM](https://pdm.fming.dev) with [Pyprojectx](https://pyprojectx.github.io) for package management. The `pw` script should be used when working with this project.

Adding a new dependency

```shell
./pw pdm add dataclasses-json
```

Adding a tool

```shell
# Add black to lint group
./pw pdm add -dG lint black
```

Formatting code

```shell
./pw format
```

Running tests

```shell
./pw test
```

Running a REPL

```shell
./pw pdm run python
```

Publishing to PyPI

```shell
./pw pdm build

# Test PyPI
./pw twine upload -r testpypi dist/*

# PyPI
./pw twine upload dist/*
```

