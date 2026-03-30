## incloud alert rule list

List alert rules

### Synopsis

List alert rules with pagination.

```
incloud alert rule list [flags]
```

### Examples

```
  # List alert rules
  incloud alert rule list

  # Paginate
  incloud alert rule list --page 2 --limit 50

  # Table output
  incloud alert rule list -o table

  # Table with selected fields
  incloud alert rule list -o table -f _id -f groupIds -f rules
```

### Options

```
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

* [incloud alert rule](incloud_alert_rule.md)	 - Manage alert rules

