## incloud device client sinr

Client signal-to-interference ratio (SINR)

### Synopsis

Display SINR (Signal to Interference plus Noise Ratio) time-series data for a wireless client.

```
incloud device client sinr <client-id> [flags]
```

### Options

```
      --after string     Start time (ISO 8601, required)
      --before string    End time (ISO 8601, required)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for sinr
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

