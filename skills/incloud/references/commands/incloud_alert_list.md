## incloud alert list

List alerts

### Synopsis

List alerts on the InCloud platform with optional filtering, searching, and pagination.

```
incloud alert list [flags]
```

### Examples

```
  # List alerts with default pagination
  incloud alert list

  # Paginate
  incloud alert list --page 2 --limit 50

  # Filter by status
  incloud alert list --status ACTIVE

  # Filter by priority
  incloud alert list --priority 1

  # Filter by device
  incloud alert list --device 507f1f77bcf86cd799439011

  # Filter by time range
  incloud alert list --after 2024-01-01T00:00:00Z --before 2024-01-31T23:59:59Z

  # Filter by alert type (use 'incloud alert rule types' to list available types)
  incloud alert list --type disconnected --type reboot

  # Filter by acknowledgement status
  incloud alert list --ack false

  # Search by entity name
  incloud alert list -q "router"

  # Sort results
  incloud alert list --sort "createdAt,desc"

  # Table output with selected fields
  incloud alert list -o table -f type -f status -f entityName

  # Aggregate alert types with jq
  incloud alert list --limit 100 --jq '[.result[].type] | group_by(.) | map({type: .[0], count: length})'
```

### Options

```
      --ack string         Filter by acknowledgement status (true/false)
      --after string       Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string      End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
      --device string      Filter by device ID
  -f, --fields strings     Fields to return and display
      --group string       Filter by device group ID
  -h, --help               help for list
      --limit int          Number of items per page (default 20)
      --page int           Page number (starting from 1) (default 1)
      --priority int       Filter by priority level
  -q, --query string       Search by entity name (fuzzy match)
      --sort string        Sort order (e.g. "createdAt,desc")
      --status string      Filter by status (ACTIVE/CLOSED)
      --type stringArray   Filter by alert type (use 'incloud alert rule types' to list available types; can be repeated)
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

* [incloud alert](incloud_alert.md)	 - Manage alerts

