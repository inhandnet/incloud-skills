## incloud device exec ping

Run ping diagnostic on a device

### Synopsis

Run ping from a remote device and stream results in real time.

The command starts a ping task on the device, subscribes to the result stream,
and prints each line as it arrives — similar to running ping locally.
Press Ctrl+C to cancel.

```
incloud device exec ping <device-id> [flags]
```

### Examples

```
  # Ping a host from the device (uses default interface "any", 4 packets)
  incloud device exec ping 507f1f77bcf86cd799439011 --host 8.8.8.8

  # With specific interface and count
  incloud device exec ping 507f1f77bcf86cd799439011 --host 8.8.8.8 --interface eth0 --count 10
```

### Options

```
      --count int          Number of ping packets (1-1000) (default 4)
  -h, --help               help for ping
      --host string        Target host to ping (required)
      --interface string   Network interface to use (use 'incloud device exec interfaces <device-id>' to list available interfaces) (default "any")
      --packet-size int    Packet size in bytes (1-65535) (default 64)
      --source string      Source address (only effective when interface is "any")
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

