Cerbos Python SDK
=================

Python client for accessing [Cerbos](https://cerbos.dev).

Cerbos is the open core, language-agnostic, scalable authorization solution that makes user permissions and authorization simple to implement and manage by writing context-aware access control policies for your application resources.

## Usage

Making a request

```python
import cerbos.sdk.model.*
from cerbos.sdk.client import CerbosClient

with CerbosClient("https://localhost:3592", debug=True, tls_verify=False) as c:
    p = Principal(
        "john",
        roles={"employee"},
        policy_version="20210210",
        attr={"department": "marketing", "geography": "GB", "team": "design"},
    )
    r = Resource(
        "XX125",
        "leave_request",
        policy_version="20210210",
        attr={
            "id": "XX125",
            "department": "marketing",
            "geography": "GB",
            "team": "design",
            "owner": "john",
        },
    )
    print(c.is_allowed("view:public", p, r))
```

Testing with [TestContainers](https://github.com/testcontainers/testcontainers-python)

```python
from cerbos.sdk.client import CerbosClient
from cerbos.sdk.container import CerbosContainer

container = CerbosContainer()
policy_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "store")
container.with_volume_mapping(policy_dir, "/policies")

with container:
    container.wait_until_ready()

    host = container.http_host()
    with CerbosClient(host) as c:
        ...
```

## Get help

- Visit the [Cerbos website](https://cerbos.dev)
- Read the [documentation](https://docs.cerbos.dev)
- [Join the Cerbos community on Slack](http://go.cerbos.io/slack)
- Email us at help@cerbos.dev


## Development

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

