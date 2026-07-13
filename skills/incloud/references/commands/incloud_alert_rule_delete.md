## incloud alert rule delete

Delete alert rules

### Synopsis

Delete one or more alert rules by ID. Multiple IDs triggers bulk delete.

```
incloud alert rule delete <rule-id> [<rule-id>...] [flags]
```

### Examples

```
  # Delete a single rule (will prompt for confirmation)
  incloud alert rule delete 507f1f77bcf86cd799439011

  # Delete multiple rules
  incloud alert rule delete 507f1f77bcf86cd799439011 507f1f77bcf86cd799439012

  # Skip confirmation
  incloud alert rule delete 507f1f77bcf86cd799439011 --yes
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Skip confirmation prompt
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

