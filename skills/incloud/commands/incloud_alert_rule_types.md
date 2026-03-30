## incloud alert rule types

List alert rule types and their parameters

### Synopsis

List all supported alert rule types and their parameters.

Without arguments, displays a summary table of all types.
With a type name argument, displays detailed parameter information for that type.

```
incloud alert rule types [type] [flags]
```

### Examples

```
  # List all alert rule types
  incloud alert rule types

  # Show details for a specific type
  incloud alert rule types disconnected

  # JSON output of all types
  incloud alert rule types -o json

  # JSON output of a specific type
  incloud alert rule types disconnected -o json
```

### Options

```
  -h, --help   help for types
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

