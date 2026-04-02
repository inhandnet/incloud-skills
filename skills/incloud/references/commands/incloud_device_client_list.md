## incloud device client list

List connected clients

### Synopsis

List all clients (Wi-Fi/LAN devices) connected to your routers.

```
incloud device client list [flags]
```

### Examples

```
  # List all clients
  incloud device client list

  # Filter by type
  incloud device client list --type wireless

  # Filter by online status
  incloud device client list --online true

  # Filter by device
  incloud device client list --device 507f1f77bcf86cd799439011

  # Search by name
  incloud device client list -q "desktop"
```

### Options

```
      --asset string     Filter by asset status (true/false)
      --device string    Filter by device ID
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --ip string        Filter by IP address
      --limit int        Number of items per page (default 20)
      --mac string       Filter by MAC address
      --online string    Filter by online status (true/false)
      --page int         Page number (starting from 1) (default 1)
  -q, --query string     Search by client name
      --sort string      Sort order (e.g. "createdAt,desc")
      --type string      Filter by type (wireless/wired)
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

