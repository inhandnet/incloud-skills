## incloud device group create

Create a device group

### Synopsis

Create a new device group on the InCloud platform.

```
incloud device group create [flags]
```

### Examples

```
  # Create a device group
  incloud device group create --name "Edge Routers" --product ER805 --firmware V2.0.26

  # Output as JSON
  incloud device group create --name test --product IR915L --firmware V1.0.0 -o json
```

### Options

```
      --firmware string   Firmware version (required)
  -h, --help              help for create
      --name string       Group name (required, 1-128 chars)
      --product string    Product model (required)
```

### Options inherited from parent commands

```
      --context string   Override active context (env: INCLOUD_CONTEXT)
      --debug            Enable debug output (env: INCLOUD_DEBUG)
      --jq string        Filter JSON output using a jq expression (implies -o json)
  -o, --output string    Output format: json, table, yaml (default: table for TTY, json otherwise)
      --tenant string    Switch organization context by ID (env: INCLOUD_TENANT)
```

### SEE ALSO

* [incloud device group](incloud_device_group.md)	 - Manage device groups

