## incloud pos rules

Manage POS custom rules

### Synopsis

Get, set, and list per-device POS custom rules (add/mask entries layered on the global rule file).

### Options

```
  -h, --help   help for rules
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

* [incloud pos](incloud_pos.md)	 - Manage POS Ready traffic prioritization
* [incloud pos rules get](incloud_pos_rules_get.md)	 - Get a device's POS custom rules
* [incloud pos rules list](incloud_pos_rules_list.md)	 - List devices with POS custom rules
* [incloud pos rules set](incloud_pos_rules_set.md)	 - Replace a device's POS custom rules

