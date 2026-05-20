## incloud device edge cli-config

Get the current CLI configuration from a device

### Synopsis

Retrieve the current running CLI configuration from an edge device.

If the device is online, the configuration is fetched directly from the device.
If the device is offline, the last cached configuration is returned instead.

```
incloud device edge cli-config <device-id> [flags]
```

### Examples

```
  # Get current CLI config
  incloud device edge cli-config 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for cli-config
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

* [incloud device edge](incloud_device_edge.md)	 - Manage edge device properties

