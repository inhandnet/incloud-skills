## incloud device client datausage-hourly

Client hourly data usage

### Synopsis

Display hourly data usage (tx/rx) time-series for a client.

```
incloud device client datausage-hourly <client-id> [flags]
```

### Options

```
      --after string     Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string    End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for datausage-hourly
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

