## incloud pos rules get

Get a device's POS custom rules

### Synopsis

Display the POS custom rules configured for a specific device.

```
incloud pos rules get <device-id> [flags]
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

* [incloud pos rules](incloud_pos_rules.md)	 - Manage POS custom rules

