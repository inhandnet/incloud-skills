## incloud user list

List users

### Synopsis

List users on the InCloud platform with optional filtering and pagination.

```
incloud user list [flags]
```

### Examples

```
  # List users with default pagination
  incloud user list

  # Paginate
  incloud user list --page 2 --limit 50

  # Search by email
  incloud user list --email example.com

  # Search by name
  incloud user list --name john

  # General search
  incloud user list --search admin

  # Filter by type
  incloud user list --type INTERNAL

  # Expand roles
  incloud user list --expand roles

  # Table output with selected fields
  incloud user list -o table -f username -f email -f name
```

### Options

```
      --email string     Filter by email (LIKE search)
      --expand strings   Expand related resources. Supported: roles, org
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --name string      Filter by name (LIKE search)
      --page int         Page number (starting from 1) (default 1)
  -q, --search string    General search query
      --sort string      Sort order (e.g. "createdAt,desc")
      --type string      Filter by user type (INTERNAL=org members, EXTERNAL=collaborators)
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

* [incloud user](incloud_user.md)	 - Manage users

