## incloud overview offline

Offline analysis and top devices

### Synopsis

Show top-N offline devices and offline statistics list.

```
incloud overview offline [flags]
```

### Examples

```
  # Show offline dashboard
  incloud overview offline

  # Custom time range
  incloud overview offline --after 2024-01-01 --before 2024-01-31

  # Top 5 devices, page 2 of statistics
  incloud overview offline --n 5 --page 2

  # Filter by device group
  incloud overview offline --group 507f1f77bcf86cd799439011

  # JSON output
  incloud overview offline -o json

  # Table output (statistics only)
  incloud overview offline -o table
```

### Options

```
      --after string                   Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string                  End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
  -f, --fields strings                 Fields to return and display
      --group stringArray              Filter by device group ID (can be repeated)
  -h, --help                           help for offline
      --limit int                      Statistics list page size (default 20)
      --min-max-offline-duration int   Filter devices with daily max offline duration >= N seconds
      --min-max-offline-times int      Filter devices with daily max offline times >= N
      --min-offline-times int          Filter devices with total offline times >= N
      --n int                          Number of top devices to show (default 10)
      --page int                       Statistics list page number (1-based) (default 1)
  -q, --query string                   Filter by device name or serial number
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

