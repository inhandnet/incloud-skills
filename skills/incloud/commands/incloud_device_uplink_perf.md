## incloud device uplink perf

Show uplink performance trend

### Synopsis

Show uplink performance metrics (throughput, latency, jitter, loss) over time for a specific device uplink.

```
incloud device uplink perf <device-id> [flags]
```

### Examples

```
  # Show performance trend for wan1
  incloud device uplink perf 507f1f77bcf86cd799439011 --name wan1

  # Filter by time range
  incloud device uplink perf 507f1f77bcf86cd799439011 --name cellular1 --after 2024-01-01T00:00:00Z --before 2024-01-02T00:00:00Z

  # JSON output
  incloud device uplink perf 507f1f77bcf86cd799439011 --name wan1 -o json
```

### Options

```
      --after string     Start time (ISO 8601, e.g. 2024-01-01T00:00:00Z)
      --before string    End time (ISO 8601, e.g. 2024-01-02T00:00:00Z)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for perf
      --name string      Uplink name (required, e.g. wan1, cellular1)
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

* [incloud device uplink](incloud_device_uplink.md)	 - Show device uplinks

