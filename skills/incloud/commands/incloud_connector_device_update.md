## incloud connector device update

Update a device in a connector network

```
incloud connector device update <network-id> <device-id> [flags]
```

### Examples

```
  # Update device subnet
  incloud connector device update <network-id> <device-id> --subnet 10.32.35.0/24
```

### Options

```
  -h, --help            help for update
      --subnet string   Device subnet (e.g. 10.32.35.0/24)
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

