## incloud device client online-events

Client connect/disconnect events

### Synopsis

List online/offline events (connect and disconnect history) for a client.

```
incloud device client online-events <client-id> [flags]
```

### Options

```
      --after string     Start time (ISO 8601)
      --before string    End time (ISO 8601)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for online-events
      --limit int        Number of items per page (default 20)
      --page int         Page number (starting from 1) (default 1)
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

