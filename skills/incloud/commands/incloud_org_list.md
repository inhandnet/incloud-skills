## incloud org list

List organizations

### Synopsis

List organizations on the InCloud platform with optional filtering and pagination.

```
incloud org list [flags]
```

### Examples

```
  # List organizations
  incloud org list

  # Search by name
  incloud org list --search "Acme"

  # Filter by ancestor
  incloud org list --ancestor 61259f8f4be3e571fcfa4d75

  # Paginate
  incloud org list --page 2 --limit 50

  # Select fields
  incloud org list -f _id -f name -f email
```

### Options

```
      --ancestor string        Filter by ancestor organization ID (use 'incloud org list' or 'incloud org self' to find IDs)
      --contact-email string   Filter by contact email (LIKE search)
      --depth int              Organization tree depth (default: API returns depth 1)
      --email string           Filter by email (LIKE search)
      --expand strings         Expand related resources
  -f, --fields strings         Fields to return and display
  -h, --help                   help for list
      --limit int              Number of items per page (default 20)
      --name string            Filter by name (LIKE search)
      --page int               Page number (starting from 1) (default 1)
  -q, --search string          General search query
      --sort string            Sort order (e.g. "createdAt,desc")
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

* [incloud org](incloud_org.md)	 - Manage organizations

