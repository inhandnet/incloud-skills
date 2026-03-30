## incloud alert get

Get alert details

### Synopsis

Get detailed information about a specific alert by its ID.

```
incloud alert get <alert-id> [flags]
```

### Examples

```
  # Get alert details (colorized JSON in TTY)
  incloud alert get 507f1f77bcf86cd799439011

  # Only specific fields
  incloud alert get 507f1f77bcf86cd799439011 -f type -f status -f entityName

  # Table output (KEY/VALUE pairs)
  incloud alert get 507f1f77bcf86cd799439011 -o table

  # YAML output
  incloud alert get 507f1f77bcf86cd799439011 -o yaml
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for get
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

* [incloud alert](incloud_alert.md)	 - Manage alerts

