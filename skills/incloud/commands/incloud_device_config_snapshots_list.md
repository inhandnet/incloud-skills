## incloud device config snapshots list

List configuration change history

### Synopsis

List configuration change history snapshots for a device, with pagination and time range filtering.

The mergedConfig field is omitted by default to keep output concise.
Use 'incloud device config snapshots get' to view the full snapshot including merged configuration.

```
incloud device config snapshots list <device-id> [flags]
```

### Examples

```
  # List recent config history
  incloud device config snapshots list 507f1f77bcf86cd799439011

  # Filter by time range
  incloud device config snapshots list 507f1f77bcf86cd799439011 --after 2024-01-01 --before 2024-02-01

  # Paginate
  incloud device config snapshots list 507f1f77bcf86cd799439011 --page 2 --limit 10
```

### Options

```
      --after string     Filter history after this time (ISO 8601)
      --before string    Filter history before this time (ISO 8601)
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --module string    Module name (defaults to 'default' on the server)
      --page int         Page number (starting from 1) (default 1)
      --sort string      Sort order (e.g. "createdAt,desc")
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

* [incloud device config snapshots](incloud_device_config_snapshots.md)	 - Configuration snapshots

