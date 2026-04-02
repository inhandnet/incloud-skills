## incloud device location refresh

Refresh device location

### Synopsis

Trigger a location refresh using LBS (cell tower positioning).

```
incloud device location refresh <device-id> [flags]
```

### Examples

```
  # Refresh device location
  incloud device location refresh 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for refresh
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

* [incloud device location](incloud_device_location.md)	 - Manage device location

