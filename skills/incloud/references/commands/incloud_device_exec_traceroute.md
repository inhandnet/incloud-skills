## incloud device exec traceroute

Run traceroute diagnostic on a device

### Synopsis

Run traceroute from a remote device and stream results in real time.

The command starts a traceroute task on the device, subscribes to the result stream,
and prints each line as it arrives. Press Ctrl+C to cancel.

```
incloud device exec traceroute <device-id> [flags]
```

### Examples

```
  # Traceroute to a host from the device
  incloud device exec traceroute 507f1f77bcf86cd799439011 --host 8.8.8.8
```

### Options

```
  -h, --help               help for traceroute
      --host string        Target host (required)
      --interface string   Network interface to use (use 'incloud device exec interfaces <device-id>' to list available interfaces) (default "any")
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

