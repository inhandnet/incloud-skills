## incloud connector device delete

Remove devices from a connector network

```
incloud connector device delete <network-id> <device-id> [device-id...] [flags]
```

### Examples

```
  # Remove single device
  incloud connector device delete <network-id> <device-id>

  # Remove multiple
  incloud connector device delete <network-id> id1 id2 id3
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Skip confirmation prompt
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

* [incloud connector device](incloud_connector_device.md)	 - Manage devices in connector networks

