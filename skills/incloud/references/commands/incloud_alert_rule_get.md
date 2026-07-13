## incloud alert rule get

Get alert rule details

### Synopsis

Get detailed information about a specific alert rule by its ID.

```
incloud alert rule get <rule-id> [flags]
```

### Examples

```
  # Get rule details
  incloud alert rule get 507f1f77bcf86cd799439011

  # Table output
  incloud alert rule get 507f1f77bcf86cd799439011 -o table

  # YAML output
  incloud alert rule get 507f1f77bcf86cd799439011 -o yaml
```

### Options

```
  -h, --help   help for get
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

