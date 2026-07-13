## incloud connector device add

Add a device to a connector network

```
incloud connector device add <network-id> [flags]
```

### Examples

```
  # Add device to network
  incloud connector device add <network-id> --device-id <device-id>

  # With subnet
  incloud connector device add <network-id> --device-id <device-id> --subnet 10.32.34.0/24
```

### Options

```
      --device-id string   Device ID to add (required; use 'incloud connector device candidates' to find IDs)
  -h, --help               help for add
      --subnet string      Device subnet (e.g. 10.32.34.0/24)
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

* [incloud connector device](incloud_connector_device.md)	 - Manage devices in connector networks

