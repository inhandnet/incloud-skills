## incloud user identity list

List identities across organizations

### Synopsis

List the current user's identities (roles) across all accessible organizations.

Each identity represents the user's membership in an organization, including
the assigned roles and optional expiration date for external organizations.

```
incloud user identity list [flags]
```

### Examples

```
  # List all identities
  incloud user identity list

  # Filter by organization name
  incloud user identity list --org-name "Acme"

  # JSON output
  incloud user identity list -o json

  # Table with custom fields
  incloud user identity list -f oid -f orgName -f roles
```

### Options

```
      --expand strings    Expand related resources
  -f, --fields strings    Fields to return and display
  -h, --help              help for list
      --limit int         Number of items per page (default 20)
      --org-name string   Filter by organization name
      --page int          Page number (starting from 1) (default 1)
      --sort string       Sort order (e.g. "createdAt,desc")
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

* [incloud user identity](incloud_user_identity.md)	 - Manage user identities across organizations

