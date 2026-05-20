## incloud device group project devices-summary

Get deployed devices summary for a device group

### Synopsis

Get a summary of deployed project versions across devices in a device group.

```
incloud device group project devices-summary <group-id> [flags]
```

### Examples

```
  # Get devices summary
  incloud device group project devices-summary 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for devices-summary
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

* [incloud device group project](incloud_device_group_project.md)	 - Manage device group projects

