## incloud touch connection create

Create touch connections

### Synopsis

Create remote access connections to one or more touch clients on a device.

```
incloud touch connection create [flags]
```

### Examples

```
  # Connect to clients on a device
  incloud touch connection create --device-id 507f1f77bcf86cd799439011 --username 653b1ff2a84e171614d88695 --client-ids id1,id2
```

### Options

```
      --client-ids strings   Client IDs to connect to (required, comma-separated)
      --device-id string     Target device ID (required)
  -h, --help                 help for create
      --username string      User token ID (required)
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

* [incloud touch connection](incloud_touch_connection.md)	 - Manage touch connections

