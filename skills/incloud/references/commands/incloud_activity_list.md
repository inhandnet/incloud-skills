## incloud activity list

List activity logs

### Synopsis

List audit activity logs on the InCloud platform with optional filtering and pagination.

```
incloud activity list [flags]
```

### Examples

```
  # List recent activity logs
  incloud activity list

  # Paginate
  incloud activity list --page 2 --limit 50

  # Filter by action type
  incloud activity list --action device_created

  # Filter by actor
  incloud activity list --actor 5f1e5605cf562757b857a7b9

  # Filter by time range
  incloud activity list --after 2024-01-01T00:00:00Z --before 2024-01-31T23:59:59Z

  # Filter by application
  incloud activity list --app nezha

  # Sort by timestamp ascending
  incloud activity list --sort "timestamp,asc"

  # Table output with selected fields
  incloud activity list -o table -f action -f actor.name -f entity.name
```

### Options

```
      --action string    Filter by action type (e.g. device_created, device_deleted)
      --actor string     Filter by actor ID
      --after string     Filter logs after this time (e.g. 2024-01-01T00:00:00Z)
      --app string       Filter by application name
      --before string    Filter logs before this time (e.g. 2024-01-31T23:59:59Z)
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
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

* [incloud activity](incloud_activity.md)	 - View activity logs

