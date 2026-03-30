## incloud device client rssi

Client Wi-Fi signal strength (RSSI)

### Synopsis

Display RSSI (Received Signal Strength Indicator) time-series data for a wireless client.

```
incloud device client rssi <client-id> [flags]
```

### Options

```
      --after string     Start time (ISO 8601, required)
      --before string    End time (ISO 8601, required)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for rssi
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

