## incloud device client mark-asset

Mark clients as assets

### Synopsis

Convert one or more connected clients into tracked network assets.

```
incloud device client mark-asset <client-id> [client-id...] [flags]
```

### Examples

```
  # Mark a single client as asset
  incloud device client mark-asset 507f1f77bcf86cd799439011

  # Mark multiple clients
  incloud device client mark-asset id1 id2 id3
```

### Options

```
  -h, --help   help for mark-asset
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

* [incloud device client](incloud_device_client.md)	 - Connected clients (Wi-Fi/LAN)

