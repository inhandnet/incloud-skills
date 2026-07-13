## incloud touch connection disconnect

Disconnect touch connections

### Synopsis

Disconnect remote access connections for specified clients on a device.

```
incloud touch connection disconnect [flags]
```

### Examples

```
  # Disconnect clients
  incloud touch connection disconnect --device-id 507f1f77bcf86cd799439011 --client-ids id1,id2
```

### Options

```
      --client-ids strings   Client IDs to disconnect (required, comma-separated)
      --device-id string     Target device ID (required)
  -h, --help                 help for disconnect
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

