## incloud tunnel logs

List tunnel connection logs

### Synopsis

List tunnel connection logs for a device, with optional filtering by type and protocol.

```
incloud tunnel logs <device-id> [flags]
```

### Examples

```
  # List tunnel logs for a device
  incloud tunnel logs 507f1f77bcf86cd799439011

  # Filter by protocol
  incloud tunnel logs 507f1f77bcf86cd799439011 --protocol local_web

  # Paginate
  incloud tunnel logs 507f1f77bcf86cd799439011 --page 2 --limit 50
```

### Options

```
      --business-id string   Business resource ID filter
  -f, --fields strings       Fields to return and display
  -h, --help                 help for logs
      --limit int            Number of items per page (default 20)
      --page int             Page number (starting from 1) (default 1)
      --protocol strings     Protocol filter: local_web, local_cli (can be repeated)
      --sort string          Sort order (e.g. "createdAt,desc")
      --type string          Tunnel type filter (default "local")
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

* [incloud tunnel](incloud_tunnel.md)	 - Manage remote access tunnels

