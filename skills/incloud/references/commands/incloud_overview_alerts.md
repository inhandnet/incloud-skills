## incloud overview alerts

Alert statistics and top rankings

### Synopsis

Show alert summary stats, top devices by alert count, and top alert types.

```
incloud overview alerts [flags]
```

### Examples

```
  # Show alert overview
  incloud overview alerts

  # Filter by time range
  incloud overview alerts --after 2024-01-01 --before 2024-01-31

  # Top 5 with device group filter
  incloud overview alerts --n 5 --group 507f1f77bcf86cd799439011

  # JSON output
  incloud overview alerts -o json
```

### Options

```
      --after string        Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string       End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
  -f, --fields strings      Fields to display in tables
      --group stringArray   Filter by device group ID (can be repeated)
  -h, --help                help for alerts
      --n int               Number of top items to show (default 10)
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

* [incloud overview](incloud_overview.md)	 - Platform overview dashboard

