## incloud device client set-pos-ready

Set POS priority level for a client

### Synopsis

Set the POS traffic priority level for a client.

Levels:
  priority  prioritize this client's POS traffic
  default   no special handling (equivalent to unmarked)
  bypass    exclude this client from POS handling

```
incloud device client set-pos-ready <client-id> [flags]
```

### Examples

```
  # Prioritize a client's POS traffic
  incloud device client set-pos-ready 69b8c537e7f8d2c1e5fffdbc --level priority

  # Reset to default
  incloud device client set-pos-ready 69b8c537e7f8d2c1e5fffdbc --level default

  # Bypass a client
  incloud dev client set-pos-ready 69b8c537e7f8d2c1e5fffdbc --level bypass
```

### Options

```
  -h, --help           help for set-pos-ready
      --level string   POS priority level: priority, default, or bypass (required)
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

