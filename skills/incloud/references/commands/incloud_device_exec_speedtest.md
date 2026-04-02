## incloud device exec speedtest

Run speed test on a device

### Synopsis

Run speed test from a remote device and stream results in real time.

If --interface or --server-node is not specified, the command fetches available
options from the device and prompts you to select. Press Ctrl+C to cancel.

```
incloud device exec speedtest <device-id> [flags]
```

### Examples

```
  # Run speed test (prompts for interface and server node)
  incloud device exec speedtest 507f1f77bcf86cd799439011

  # With specific interface and server node (no prompts)
  incloud device exec speedtest 507f1f77bcf86cd799439011 --interface eth0 --server-node node1

  # View available interfaces and server nodes
  incloud device exec speedtest-config 507f1f77bcf86cd799439011

  # View historical results
  incloud device exec speedtest-history 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help                 help for speedtest
      --interface string     Network interface to use (use 'incloud device exec speedtest-config <device-id>' to list)
      --server-node string   Speed test server node ID (use 'incloud device exec speedtest-config <device-id>' to list)
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

