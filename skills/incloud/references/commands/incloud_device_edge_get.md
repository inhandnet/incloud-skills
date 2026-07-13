## incloud device edge get

Get edge properties of a device

### Synopsis

Get edge-specific properties of a device including project status, environment variables, and CLI configuration.

```
incloud device edge get <device-id> [flags]
```

### Examples

```
  # Get edge device info
  incloud device edge get 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for get
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

