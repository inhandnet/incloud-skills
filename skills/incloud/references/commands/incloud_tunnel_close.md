## incloud tunnel close

Close a tunnel

### Synopsis

Close an active remote access tunnel and release its resources.

```
incloud tunnel close <tunnel-id> [flags]
```

### Examples

```
  # Close a tunnel
  incloud tunnel close abc123def456
```

### Options

```
  -h, --help   help for close
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

* [incloud tunnel](incloud_tunnel.md)	 - Manage remote access tunnels

