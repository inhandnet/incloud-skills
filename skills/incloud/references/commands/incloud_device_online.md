## incloud device online

Device online/offline history

### Synopsis

View device online/offline history.

By default, shows individual connect/disconnect events (paginated).
Use --daily to show daily offline statistics instead (last 30 days).

```
incloud device online <device-id> [flags]
```

### Examples

```
  # List online/offline events
  incloud device online 507f1f77bcf86cd799439011

  # Filter by time range
  incloud device online 507f1f77bcf86cd799439011 --after 2025-01-01T00:00:00Z --before 2025-01-31T23:59:59Z

  # Daily offline statistics
  incloud device online 507f1f77bcf86cd799439011 --daily

  # Daily stats for a specific month
  incloud device online 507f1f77bcf86cd799439011 --daily --after 2025-03-01T00:00:00Z --before 2025-03-31T00:00:00Z
```

### Options

```
      --after string     Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string    End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
      --daily            Show daily offline statistics instead of individual events
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for online
      --limit int        Number of items per page (events mode only) (default 20)
      --page int         Page number, starting from 1 (events mode only) (default 1)
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

