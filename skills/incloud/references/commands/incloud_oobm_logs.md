## incloud oobm logs

List OOBM tunnel connection logs

### Synopsis

List tunnel connection logs for a device, with optional filtering by type, protocol, and business resource.

```
incloud oobm logs <device-id> [flags]
```

### Examples

```
  # List logs for a device
  incloud oobm logs 507f1f77bcf86cd799439011

  # Filter by protocol
  incloud oobm logs 507f1f77bcf86cd799439011 --protocol ssh --protocol tcp

  # Filter by type and business ID
  incloud oobm logs 507f1f77bcf86cd799439011 --type oobm --business-id abc123

  # Paginate and sort
  incloud oobm logs 507f1f77bcf86cd799439011 --page 2 --limit 50 --sort "createdAt,desc"
```

### Options

```
      --business-id string   Business resource ID filter
  -f, --fields strings       Fields to return and display
  -h, --help                 help for logs
      --limit int            Number of items per page (default 20)
      --page int             Page number (starting from 1) (default 1)
      --protocol strings     Protocol filter (can be repeated)
      --sort string          Sort order (e.g. "createdAt,desc")
      --type string          Tunnel type filter
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

* [incloud oobm](incloud_oobm.md)	 - Manage Out-of-Band Management resources

