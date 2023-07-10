Cerbos Python SDK
=================

Python clients for accessing [Cerbos](https://cerbos.dev).

Cerbos is the open core, language-agnostic, scalable authorization solution that makes user permissions and authorization simple to implement and manage by writing context-aware access control policies for your application resources.

## Usage

This library is available from PyPI as `cerbos`. It supports both async and non-async modes.

```sh
pip install cerbos
```

There are two clients available; [gRPC](#grpc-client) and [HTTP](#http-client). New projects should use the gRPC client.

### gRPC Client

(Available from v0.8.0 onwards)

**Making a request**

```python
from cerbos.sdk.grpc.client import CerbosClient
from cerbos.engine.v1 import engine_pb2
from cerbos.request.v1 import request_pb2
from google.protobuf.struct_pb2 import Value

principal = engine_pb2.Principal(
    id="john",
    roles={"employee"},
    policy_version="20210210",
    attr={
        "department": Value(string_value="marketing"),
        "geography": Value(string_value="GB"),
        "team": Value(string_value="design"),
    },
)

resource = engine_pb2.Resource(
    id="XX125",
    kind="leave_request",
    attr={
        "id": Value(string_value="XX125"),
        "department": Value(string_value="marketing"),
        "geography": Value(string_value="GB"),
        "team": Value(string_value="design"),
        "owner": Value(string_value="john"),
    }
)

plan_resource = engine_pb2.PlanResourcesInput.Resource(
    kind="leave_request",
    policy_version="20210210"
)

with CerbosClient("localhost:3593", tls_verify=False) as c:
    # Check a single action on a single resource
    if c.is_allowed("view", principal, resource):
        # perform some action
        pass

    # Get the query plan for "view" action
    plan = c.plan_resources(action="view", principal=principal, resource=plan_resource)
````

**Async usage**

```python
from cerbos.sdk.grpc.client import AsyncCerbosClient

async with AsyncCerbosClient("localhost:3593", tls_verify=False) as c:
    ...

    allowed = await c.is_allowed("view:public", p, r)
    print(allowed)

    # Get the query plan for "view" action
    ...
    plan = await c.plan_resources("view", p, rd)
    print(plan.filter.to_json())

```

**Admin API**

There is also a client available for interacting with the Admin API. See [the docs](https://docs.cerbos.dev/cerbos/latest/api/admin_api.html) for information on how to configure your PDP to enable this.

```python
from cerbos.policy.v1 import policy_pb2
from cerbos.sdk.grpc.client import AdminCredentials, AsyncCerbosAdminClient

admin_credentials = AdminCredentials(username="admin", password="some_password")
async with AsyncCerbosAdminClient("localhost:3593", admin_credentials=admin_credentials) as c:
    await c.add_or_update_policy(
        [
            policy_pb2.Policy(
                api_version="api.cerbos.dev/v1",
                principal_policy=policy_pb2.PrincipalPolicy(
                    principal="terry", version="default"
                ),
            )
        ]
    )
```

**Connecting to a Unix domain socket**

```python
with CerbosClient("unix:/var/cerbos.sock", tls_verify=False) as c:
  ...
```

### HTTP client

We maintain this for backwards compatibility. It is recommended to use the [gRPC client](#grpc-client).

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

## Contributing

The gRPC client uses protoc generated python classes from definitions retrieved from our [buf registry](https://buf.build/cerbos/cerbos-api).
When making changes to this library, be sure to run the `./proto/generate_protos.sh` to update definitions and generate python classes.

## Get help

- Visit the [Cerbos website](https://cerbos.dev)
- Read the [documentation](https://docs.cerbos.dev)
- [Join the Cerbos community on Slack](http://go.cerbos.io/slack)
- Email us at help@cerbos.dev
