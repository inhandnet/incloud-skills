## incloud device exec interfaces

List available network interfaces on a device

```
incloud device exec interfaces <device-id> [flags]
```

### Examples

```
  incloud device exec interfaces 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for interfaces
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

* [incloud device exec](incloud_device_exec.md)	 - Execute remote methods and diagnostics on devices

