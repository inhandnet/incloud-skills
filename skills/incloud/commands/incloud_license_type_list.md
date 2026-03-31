## incloud license type list

List license types

### Synopsis

List available license types with optional filtering by product and status.

```
incloud license type list [flags]
```

### Examples

```
  # List all published license types
  incloud license type list

  # Filter by product
  incloud license type list --product IR915

  # Include unpublished types
  incloud license type list --status unpublished

  # YAML output
  incloud license type list -o yaml
```

### Options

```
      --expand strings   Expand related resources. Supported: prices
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --page int         Page number (starting from 1) (default 1)
      --product string   Filter by product name
      --sort string      Sort order (e.g. "createdAt,desc")
      --status string    Filter by status (published/unpublished, default: published)
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

* [incloud license type](incloud_license_type.md)	 - Manage license types

