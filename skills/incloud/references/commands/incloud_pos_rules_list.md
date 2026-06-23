## incloud pos rules list

List devices with POS custom rules

### Synopsis

List devices that have POS custom rules configured, across all your devices.

```
incloud pos rules list [flags]
```

### Examples

```
  # All devices with custom rules
  incloud pos rules list

  # Filter by device
  incloud pos rules list --device 507f1f77bcf86cd799439011
```

### Options

```
      --device string    Filter by device ID
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

* [incloud pos rules](incloud_pos_rules.md)	 - Manage POS custom rules

