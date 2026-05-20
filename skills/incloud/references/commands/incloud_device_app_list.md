## incloud device app list

List applications on a device

### Synopsis

List container and native applications running on an edge device.

```
incloud device app list <device-id> [flags]
```

### Examples

```
  # List apps on a device
  incloud device app list 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for list
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

* [incloud device app](incloud_device_app.md)	 - Manage device applications

