## incloud device exec method

Invoke a custom remote method on device(s)

### Synopsis

Invoke a custom remote method on one or more devices.

When multiple device IDs are provided (comma-separated), the bulk endpoint
is used and the request is processed asynchronously.

```
incloud device exec method <id>[,<id2>,...] <method> [flags]
```

### Examples

```
  # Invoke a custom method
  incloud device exec method 507f1f77bcf86cd799439011 getConfig --payload '{"module":"wan"}'

  # Bulk invoke a method on multiple devices
  incloud device exec method 507f1f77bcf86cd799439011,653b1ff2a84e171614d88695 syncTime
```

### Options

```
  -h, --help             help for method
  -p, --payload string   JSON payload for the method
  -t, --timeout int      Timeout in seconds (5-300, single device only) (default 30)
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

