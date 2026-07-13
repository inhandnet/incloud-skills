## incloud device assign

Assign a device to a device group

```
incloud device assign <device-id> [flags]
```

### Examples

```
  # Assign device to a group
  incloud device assign 507f1f77bcf86cd799439011 --group 653b1ff2a84e171614d88695
```

### Options

```
      --group string   Target device group ID (required)
  -h, --help           help for assign
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

