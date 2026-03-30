## incloud device get

Get device details

### Synopsis

Get detailed information about a specific device by its ID.

```
incloud device get <device-id> [flags]
```

### Examples

```
  # Get device details (colorized JSON in TTY)
  incloud device get 507f1f77bcf86cd799439011

  # Only specific fields
  incloud device get 507f1f77bcf86cd799439011 -f name -f serialNumber -f online

  # Table output (KEY/VALUE pairs)
  incloud device get 507f1f77bcf86cd799439011 -o table

  # YAML output
  incloud device get 507f1f77bcf86cd799439011 -o yaml

  # Extract specific fields with jq
  incloud device get 507f1f77bcf86cd799439011 --jq '{name, sn: .serialNumber, online}'
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for get
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

* [incloud device](incloud_device.md)	 - Manage devices

