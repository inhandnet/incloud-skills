## incloud role list

List roles

### Synopsis

List roles on the InCloud platform with optional filtering and pagination.

```
incloud role list [flags]
```

### Examples

```
  # List roles
  incloud role list

  # Filter by application
  incloud role list --app portal

  # Table output with selected fields
  incloud role list -o table -f _id -f name -f builtInRole
```

### Options

```
      --app string       Filter by application (e.g. portal, console)
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

* [incloud role](incloud_role.md)	 - Manage roles

