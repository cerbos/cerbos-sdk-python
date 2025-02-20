## Unreleased

### Bug fixes

- Omit check_request params with None values (#53)
- Validation error path field can be empty (#52)
- Use pre-3.9 dict merge operator (#50)
- Backward compatible type subscriptions/unions (#48)
- Add types-protobuf for editor type support (#42)
- Include generated code in package (#37)
- Format on pre_build to fix publish flow (#30)
- Handle `raise_on_error` correctly in async client (#17)
- Decode PlanResources response into correct types (#15)
- Remove importlib (#11)

### Chores

- Vendor subset of dependencies to avoid namespace collisions (#46)
- Use stable plan API
- Disable telemetry in CI
- Add release metadata

### Documentation

- Fix import statement in README example (#3)
- Update README

### Enhancements

- Support optional gRPC channel options (#39)
- Add support for new `outputs` field in `CheckResources` return (#24)
- Make testcontainers optional (#22)
- Add validation errors to PlanResources (#8)
- Add support for Unix domain sockets (#6)

### Features

- Add support for `exportVariables` policies (#35)
- Add gRPC client and admin API capabilities (#29)
- Async support (#13)
