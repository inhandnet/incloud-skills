## incloud device app restart

Restart applications on a device

### Synopsis

Restart container or native applications on an edge device.

```
incloud device app restart <device-id> [flags]
```

### Examples

```
  # Restart container apps by name
  incloud device app restart 507f1f77bcf86cd799439011 --app-type container --app-names myapp

  # Restart all native apps
  incloud device app restart 507f1f77bcf86cd799439011 --app-type native
```

### Options

```
      --app-names strings   Application names to restart (comma-separated)
      --app-type string     Application type (e.g. container, native)
  -h, --help                help for restart
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

