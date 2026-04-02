## incloud device location get

Get device location

### Synopsis

Display the current location information for a device.

```
incloud device location get <device-id> [flags]
```

### Examples

```
  # Get device location
  incloud device location get 507f1f77bcf86cd799439011

  # Table output
  incloud device location get 507f1f77bcf86cd799439011 -o table
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

* [incloud device location](incloud_device_location.md)	 - Manage device location

