## incloud device exec flowscan

Start flow scan (traffic analysis) on a device

```
incloud device exec flowscan <device-id> [flags]
```

### Examples

```
  # Start flow scan
  incloud device exec flowscan 507f1f77bcf86cd799439011

  # With duration and type filter
  incloud device exec flowscan 507f1f77bcf86cd799439011 --duration 7200 --type DOMAIN
```

### Options

```
      --duration int         Scan duration in seconds (3600-259200)
  -h, --help                 help for flowscan
      --interface string     Network interface to use
      --src-filter strings   Source IP filters (comma-separated)
      --type string          Flow type: ALL or DOMAIN
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

