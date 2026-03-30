## incloud device perf

Show device performance (CPU, memory, disk)

### Synopsis

Show device performance metrics.

By default, displays the current performance snapshot (CPU usage, memory, disk).
With --after/--before, displays historical performance time series.
With --refresh, triggers a real-time collection from the device (online only).

```
incloud device perf <device-id> [flags]
```

### Examples

```
  # Current performance snapshot
  incloud device perf 507f1f77bcf86cd799439011

  # Real-time collection (device must be online)
  incloud device perf 507f1f77bcf86cd799439011 --refresh

  # Historical time series
  incloud device perf 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-01-02T00:00:00Z

  # Select specific fields
  incloud device perf 507f1f77bcf86cd799439011 -f cpu.usage -f memory.free -f memory.total

  # JSON output
  incloud device perf 507f1f77bcf86cd799439011 -o json
```

### Options

```
      --after string     Start time (ISO 8601, e.g. 2024-01-01T00:00:00Z)
      --before string    End time (ISO 8601, e.g. 2024-01-02T00:00:00Z)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for perf
      --refresh          Trigger real-time collection (device must be online)
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

* [incloud device](incloud_device.md)	 - Manage devices

