## incloud device exec speedtest-history

View speed test history for a device

```
incloud device exec speedtest-history <device-id> [flags]
```

### Examples

```
  # View recent speed test results
  incloud device exec speedtest-history 507f1f77bcf86cd799439011

  # Filter by date range
  incloud device exec speedtest-history 507f1f77bcf86cd799439011 --after 2024-01-01 --before 2024-02-01
```

### Options

```
      --after string     Start date (ISO 8601)
      --before string    End date (ISO 8601)
  -f, --fields strings   Fields to display (comma-separated)
  -h, --help             help for speedtest-history
      --limit int        Results per page (default 20)
      --page int         Page number (1-based) (default 1)
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

