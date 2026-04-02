## incloud device list

List devices

### Synopsis

List devices on the InCloud platform with optional filtering, searching, and pagination.

```
incloud device list [flags]
```

### Examples

```
  # Search by name or serial number
  incloud device list -q "router"

  # Filter by online status, product, org
  incloud device list --online true --product IR615 --org <org-id>

  # Expand related resources and output as JSON
  incloud device list --expand org,license -o json

  # Export offline devices as CSV
  incloud device list --online false --jq '.result[] | [.name, .serialNumber] | @csv'
```

### Options

```
      --expand strings         Expand related resources. Supported: org, license, licenseType
  -f, --fields strings         Fields to return and display
      --firmware string        Filter by firmware version
      --group stringArray      Filter by device group ID (can be repeated)
  -h, --help                   help for list
      --iccid string           Filter by ICCID
      --ip string              Filter by IP address
      --label stringArray      Filter by label key=value (can be repeated)
      --limit int              Number of items per page (default 20)
      --mac string             Filter by MAC address
      --name string            Filter by device name (exact match)
      --online string          Filter by online status (true/false)
      --org string             Filter by organization ID
      --page int               Page number (starting from 1) (default 1)
      --product stringArray    Filter by product (can be repeated)
  -q, --query string           Search by name or serial number
      --serial-number string   Filter by serial number (exact match)
      --sort string            Sort order (e.g. "createdAt,desc")
      --status string          Filter by status (online/offline)
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

* [incloud device](incloud_device.md)	 - Manage devices

