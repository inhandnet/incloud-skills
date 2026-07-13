## incloud device log local

Read log files directly from the device (requires device online)

### Synopsis

Read log files directly from the device filesystem in real time.

The device must be online. This command sends a direct method to the device to read
its local log files and prints the content to stdout.

```
incloud device log local <device-id> [flags]
```

### Examples

```
  # Read the last 100 lines (default)
  incloud device log local 507f1f77bcf86cd799439011

  # Read the last 50 lines
  incloud device log local 507f1f77bcf86cd799439011 --lines 50

  # Read a specific log file
  incloud device log local 507f1f77bcf86cd799439011 --path /var/log/messages

  # Get full log content
  incloud device log local 507f1f77bcf86cd799439011 --all

  # Save to a file for repeated access
  incloud device log local 507f1f77bcf86cd799439011 --file /tmp/device.log

  # With a longer timeout for slow connections
  incloud device log local 507f1f77bcf86cd799439011 --timeout 60
```

### Options

```
      --all           Get full log content
      --file string   Save log content to a file instead of stdout
  -h, --help          help for local
      --lines int     Number of log lines to read (default 100)
      --path string   Log file path on the device (e.g. /var/log/messages)
      --timeout int   Timeout in seconds for device response (default 30)
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

* [incloud device log](incloud_device_log.md)	 - Device logs

