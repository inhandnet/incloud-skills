## incloud device group update

Update a device group

```
incloud device group update <id> [flags]
```

### Examples

```
  # Rename a device group
  incloud device group update 507f1f77bcf86cd799439011 --name "New Name"

  # Update firmware
  incloud device group update 507f1f77bcf86cd799439011 --firmware V2.0.30

  # Set tags
  incloud device group update 507f1f77bcf86cd799439011 --tag env=prod --tag region=us
```

### Options

```
      --firmware string   Firmware version
  -h, --help              help for update
      --name string       Group name (1-128 chars)
      --tag stringArray   Tag in key=value format (can be repeated, replaces all tags)
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

