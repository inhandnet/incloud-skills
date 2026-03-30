## incloud device log syslog

View device syslog

### Synopsis

View device syslog from the InCloud platform.

By default, queries syslog already uploaded to the platform (requires --after and --before).
With --fetch, actively requests the device to upload its current syslog; --after defaults to
start of today (UTC) and --before defaults to now if not specified.

```
incloud device log syslog <device-id> [flags]
```

### Examples

```
  # Query stored syslog for a time range
  incloud device log syslog 60af...id --after 2024-01-01T00:00:00Z --before 2024-01-01T01:00:00Z

  # Actively fetch latest syslog from device (last 15 minutes)
  incloud device log syslog 60af...id --fetch

  # Fetch syslog for a specific time range from device
  incloud device log syslog 60af...id --fetch --after 2024-01-01T00:00:00Z --before 2024-01-01T01:00:00Z

  # Fetch with a longer timeout (default 40s)
  incloud device log syslog 60af...id --fetch --timeout 120

  # Filter by keywords
  incloud device log syslog 60af...id --after 2024-01-01T00:00:00Z --before 2024-01-01T01:00:00Z --keywords error --keywords warning
```

### Options

```
      --after string       Start time in ISO 8601 format (required without --fetch)
      --before string      End time in ISO 8601 format (required without --fetch)
      --fetch              Actively request syslog from device (--after defaults to start of today)
  -h, --help               help for syslog
      --keywords strings   Filter by keywords
      --limit int          Maximum number of log lines (default 10000)
      --timeout int        Timeout in seconds for device to upload syslog (only with --fetch) (default 40)
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

