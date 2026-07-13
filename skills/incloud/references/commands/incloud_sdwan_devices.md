## incloud sdwan devices

List devices in an SD-WAN network

```
incloud sdwan devices <networkId> [flags]
```

### Examples

```
  # List all devices in a network
  incloud sdwan devices <networkId>

  # Filter by role
  incloud sdwan devices <networkId> --role hub

  # Filter by name
  incloud sdwan devices <networkId> --name ER805

  # Filter by product
  incloud sdwan devices <networkId> --product ER805 --product MR805
```

### Options

```
  -f, --fields strings         Fields to return and display
  -h, --help                   help for devices
      --limit int              Number of items per page (default 20)
      --name string            Filter by device name
      --page int               Page number (starting from 1) (default 1)
      --product stringArray    Filter by product model (repeatable)
      --role string            Filter by role: hub or spoke
      --serial-number string   Filter by serial number
      --sort string            Sort order (e.g. "createdAt,desc")
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

* [incloud sdwan](incloud_sdwan.md)	 - Manage SD-WAN networks and devices

