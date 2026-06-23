## incloud touch client list

List touch clients

### Synopsis

List remote access clients with optional filtering by device, status, or name.

```
incloud touch client list [flags]
```

### Examples

```
  # List all clients
  incloud touch client list

  # Filter by device
  incloud touch client list --device-id 507f1f77bcf86cd799439011

  # Filter by connection status
  incloud touch client list --status CONNECTED

  # Filter by name
  incloud touch client list --name my-plc
```

### Options

```
      --device-id string   Filter by device ID
  -f, --fields strings     Fields to return and display
  -h, --help               help for list
      --limit int          Number of items per page (default 20)
      --name string        Filter by name (LIKE search)
      --page int           Page number (starting from 1) (default 1)
      --sort string        Sort order (e.g. "createdAt,desc")
      --status string      Filter by connection status (CONNECTED|DISCONNECTED|CONNECTING)
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

* [incloud touch client](incloud_touch_client.md)	 - Manage touch clients

