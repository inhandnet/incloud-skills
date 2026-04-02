## incloud firmware list

List firmwares

### Synopsis

List firmwares on the InCloud platform with optional filtering and pagination.

```
incloud firmware list [flags]
```

### Examples

```
  # List firmwares with default pagination
  incloud firmware list

  # Filter by product
  incloud firmware list --product IR915L

  # Filter by status
  incloud firmware list --status published

  # Paginate
  incloud firmware list --page 2 --limit 50

  # Select fields
  incloud firmware list -f product -f version -f latest
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --module string    Filter by module name
      --page int         Page number (starting from 1) (default 1)
      --product string   Filter by product name
      --sort string      Sort order (e.g. "createdAt,desc")
      --status string    Filter by status (published|unpublished|deprecated)
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

* [incloud firmware](incloud_firmware.md)	 - Manage firmwares

