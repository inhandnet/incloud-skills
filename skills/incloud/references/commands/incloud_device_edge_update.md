## incloud device edge update

Update edge properties of a device

### Synopsis

Update edge-specific properties of a device, such as environment variables.

```
incloud device edge update <device-id> [flags]
```

### Examples

```
  # Set environment variables
  incloud device edge update 507f1f77bcf86cd799439011 --env '[{"name":"KEY","value":"val"}]'
```

### Options

```
      --env string   Environment variables as JSON array (e.g. '[{"name":"KEY","value":"val"}]')
  -h, --help         help for update
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

