Cerbos Python SDK
=================

Python client for accessing [Cerbos](https://cerbos.dev).

Cerbos is the open core, language-agnostic, scalable authorization solution that makes user permissions and authorization simple to implement and manage by writing context-aware access control policies for your application resources.

## Usage

This library is available from PyPI as `cerbos`. It supports both async and non-async modes.

```sh
pip install cerbos
```

**Making a request**

```python
from cerbos.sdk.model import *
from cerbos.sdk.client import CerbosClient

with CerbosClient("https://localhost:3592", debug=True, tls_verify=False) as c:
    p = Principal(
        "john",
        roles={"employee"},
        policy_version="20210210",
        attr={"department": "marketing", "geography": "GB", "team": "design"},
    )

    # Check a single action on a single resource
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

    allowed = c.is_allowed("view:public", p, r)
    print(allowed)

    # Get the query plan for "view" action
    rd = ResourceDesc("leave_request", policy_version="20210210")
    plan = c.plan_resources("view", p, rd)
    print(plan.filter.to_json())
```

**Async usage**


```python
from cerbos.sdk.model import *
from cerbos.sdk.client import AsyncCerbosClient

async with AsyncCerbosClient("https://localhost:3592", debug=True, tls_verify=False) as c:
    ...

    # Check a single action on a single resource
    ...
    allowed = await c.is_allowed("view:public", p, r)
    print(allowed)

    # Get the query plan for "view" action
    ...
    plan = await c.plan_resources("view", p, rd)
    print(plan.filter.to_json())

```

**Connecting to a Unix domain socket**

Use `unix+http:///path/to/sock` for HTTP over UDS or `unix+https:///path/to/sock` for HTTPS over UDS.

```python
with CerbosClient("unix+https:///var/cerbos.sock", debug=True, tls_verify=False) as c:
  ...
```

**Testing with [TestContainers](https://github.com/testcontainers/testcontainers-python)**

NOTE: Requires `cerbos[testcontainers]` dependency to be installed.

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


See the tests available in the `tests` directory for more examples.

## Get help

- Visit the [Cerbos website](https://cerbos.dev)
- Read the [documentation](https://docs.cerbos.dev)
- [Join the Cerbos community on Slack](http://go.cerbos.io/slack)
- Email us at help@cerbos.dev
