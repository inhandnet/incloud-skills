## incloud device config error

Get configuration delivery errors

### Synopsis

Get the most recent configuration delivery errors and pending changes for a device.

```
incloud device config error <device-id> [flags]
```

### Examples

```
  # Check for config errors
  incloud device config error 507f1f77bcf86cd799439011

  # JSON output with full pending details
  incloud device config error 507f1f77bcf86cd799439011 -o json
```

### Options

```
  -h, --help            help for error
      --module string   Module name (defaults to 'default' on the server)
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

* [incloud device config](incloud_device_config.md)	 - Device configuration management

