## incloud device group get

Get device group details

```
incloud device group get <id> [flags]
```

### Examples

```
  # Get a device group
  incloud device group get 507f1f77bcf86cd799439011

  # Output as JSON
  incloud device group get 507f1f77bcf86cd799439011 -o json
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

* [incloud device group](incloud_device_group.md)	 - Manage device groups

