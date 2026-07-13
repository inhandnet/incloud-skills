## incloud touch client connections

List connections for a touch client

### Synopsis

List connection history for a specific touch client.

```
incloud touch client connections <client-id> [flags]
```

### Examples

```
  # List connections
  incloud touch client connections 507f1f77bcf86cd799439011

  # Filter by time range
  incloud touch client connections 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-12-31T23:59:59Z
```

### Options

```
      --after string     Filter connections after this time (ISO 8601)
      --before string    Filter connections before this time (ISO 8601)
  -f, --fields strings   Fields to return and display
  -h, --help             help for connections
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

* [incloud touch client](incloud_touch_client.md)	 - Manage touch clients

