## incloud device signal list

Show signal quality over time

### Synopsis

Display signal quality metrics (RSRP, RSRQ, SINR, etc.) for a device over time.

```
incloud device signal list <device-id> [flags]
```

### Examples

```
  # Show signal data for a device
  incloud device signal list 507f1f77bcf86cd799439011

  # Filter by time range
  incloud device signal list 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-01-02T00:00:00Z

  # Select specific fields
  incloud device signal list 507f1f77bcf86cd799439011 -f time -f rsrp -f sinr

  # JSON output
  incloud device signal list 507f1f77bcf86cd799439011 -o json
```

### Options

```
      --after string     Start time (ISO 8601, e.g. 2024-01-01T00:00:00Z)
      --before string    End time (ISO 8601, e.g. 2024-01-02T00:00:00Z)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for list
      --order string     Sort order: asc (oldest first) or desc (newest first) (default "desc")
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

* [incloud device signal](incloud_device_signal.md)	 - Device signal quality

