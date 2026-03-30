## incloud device interface

Show device network interfaces

### Synopsis

Show network interface information for a specific device.

```
incloud device interface <device-id> [flags]
```

### Examples

```
  # Show interfaces as JSON
  incloud device interface 507f1f77bcf86cd799439011

  # Real-time refresh (device must be online)
  incloud device interface 507f1f77bcf86cd799439011 --refresh

  # Table output
  incloud device interface 507f1f77bcf86cd799439011 -o table

  # Table with selected fields
  incloud device interface 507f1f77bcf86cd799439011 -o table -f name -f type -f state -f gateway
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for interface
      --refresh          Trigger real-time collection (device must be online)
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

