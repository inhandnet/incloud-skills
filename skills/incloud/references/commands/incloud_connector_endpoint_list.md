## incloud connector endpoint list

List endpoints in a connector network

```
incloud connector endpoint list <network-id> [flags]
```

### Examples

```
  # List all endpoints in a network
  incloud connector endpoint list 66827b3ccfb1842140f4222f

  # Filter by name
  incloud connector endpoint list 66827b3ccfb1842140f4222f --name my-endpoint

  # Search by name or LAN IP
  incloud connector endpoint list 66827b3ccfb1842140f4222f -q 192.168

  # Custom fields
  incloud connector endpoint list 66827b3ccfb1842140f4222f -f _id -f name -f lanIp
```

### Options

```
      --device-id string   Filter by device ID (use 'incloud connector device list <network-id>' to find IDs)
  -f, --fields strings     Fields to return and display
  -h, --help               help for list
      --lan-ip string      Filter by LAN IP
      --limit int          Number of items per page (default 20)
      --name string        Filter by name
      --page int           Page number (starting from 1) (default 1)
  -q, --search string      Search by name or LAN IP
      --sort string        Sort order (e.g. "createdAt,desc")
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

* [incloud connector endpoint](incloud_connector_endpoint.md)	 - Manage endpoints in connector networks

