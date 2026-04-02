## incloud connector device list

List devices in a connector network

```
incloud connector device list <network-id> [flags]
```

### Examples

```
  # List devices in a network
  incloud connector device list 66827b3ccfb1842140f4222f

  # Filter connected devices
  incloud connector device list 66827b3ccfb1842140f4222f --connected true
```

### Options

```
      --connected string   Filter by connected status (true/false)
  -f, --fields strings     Fields to return and display
  -h, --help               help for list
      --limit int          Number of items per page (default 20)
      --name string        Filter by device name
      --page int           Page number (starting from 1) (default 1)
  -q, --search string      Search by name or serial number
      --sn string          Filter by serial number
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

* [incloud connector device](incloud_connector_device.md)	 - Manage devices in connector networks

