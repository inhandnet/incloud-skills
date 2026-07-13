## incloud device compatibility

Check device compatibility support

### Synopsis

Query which capabilities a device supports based on its product and firmware version.

```
incloud device compatibility <device-id> [flags]
```

### Examples

```
  # Check all compatibilities for a device
  incloud device compatibility 507f1f77bcf86cd799439011

  # Show only supported compatibilities
  incloud device compatibility 507f1f77bcf86cd799439011 --supported

  # JSON output
  incloud device compatibility 507f1f77bcf86cd799439011 -o json
```

### Options

```
  -h, --help        help for compatibility
      --supported   Show only supported compatibilities
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

