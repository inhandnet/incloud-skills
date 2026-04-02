## incloud device unassign

Remove a device from its device group

```
incloud device unassign <device-id> [flags]
```

### Examples

```
  # Remove device from its group
  incloud device unassign 507f1f77bcf86cd799439011

  # Remove but retain group configuration
  incloud device unassign 507f1f77bcf86cd799439011 --retain-config
```

### Options

```
  -h, --help            help for unassign
      --retain-config   Retain group configuration after removal
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

