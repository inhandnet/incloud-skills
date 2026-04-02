## incloud device client set-pos-ready

Set POS Ready status for a client

### Synopsis

Enable or disable POS Ready status for a client on the specified device.

```
incloud device client set-pos-ready <device-id> [flags]
```

### Examples

```
  # Enable POS Ready for a client
  incloud device client set-pos-ready DEVICE_ID --mac FC:5C:EE:8C:90:93 --enabled

  # Disable POS Ready
  incloud device client set-pos-ready DEVICE_ID --mac FC:5C:EE:8C:90:93 --enabled=false

  # Short form
  incloud dev client set-pos-ready DEVICE_ID --mac FC:5C:EE:8C:90:93 --enabled
```

### Options

```
      --enabled      Enable or disable POS Ready
  -h, --help         help for set-pos-ready
      --mac string   Client MAC address (required)
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

