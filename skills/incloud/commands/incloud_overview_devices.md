## incloud overview devices

Device status distribution

### Synopsis

Show device status distribution including online/offline/inactive counts and product breakdown.

```
incloud overview devices [flags]
```

### Examples

```
  # Show device status summary
  incloud overview devices

  # Show specific sections
  incloud overview devices -f product -f upgrade

  # JSON output
  incloud overview devices -o json

  # YAML output
  incloud overview devices -o yaml
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for devices
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

* [incloud overview](incloud_overview.md)	 - Platform overview dashboard

