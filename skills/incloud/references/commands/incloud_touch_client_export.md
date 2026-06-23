## incloud touch client export

Export touch clients

### Synopsis

Export touch clients to a file (CSV/Excel).

```
incloud touch client export [flags]
```

### Examples

```
  # Export all clients to a file
  incloud touch client export --out clients.csv

  # Export clients for a specific device
  incloud touch client export --device-id 507f1f77bcf86cd799439011 --out clients.csv
```

### Options

```
      --device-id string   Filter by device ID
  -h, --help               help for export
      --name string        Filter by name
      --out string         Output file path (default "clients.csv")
      --status string      Filter by connection status
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

