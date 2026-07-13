## incloud device exec speedtest-config

Get speed test configuration (available interfaces and server nodes)

```
incloud device exec speedtest-config <device-id> [flags]
```

### Examples

```
  # List available interfaces and server nodes
  incloud device exec speedtest-config 507f1f77bcf86cd799439011

  # Refresh server nodes for a specific interface
  incloud device exec speedtest-config 507f1f77bcf86cd799439011 --interface eth0
```

### Options

```
  -h, --help               help for speedtest-config
      --interface string   Network interface to scan server nodes for
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

