## incloud device location unpin

Unpin device location

### Synopsis

Remove the pinned location and restore automatic positioning (GPS/cell towers).

```
incloud device location unpin <device-id> [flags]
```

### Examples

```
  # Unpin device location
  incloud device location unpin 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for unpin
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

* [incloud device location](incloud_device_location.md)	 - Manage device location

