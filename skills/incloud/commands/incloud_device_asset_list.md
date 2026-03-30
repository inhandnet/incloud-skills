## incloud device asset list

List network assets

### Synopsis

List all network assets in the current organization.

```
incloud device asset list [flags]
```

### Examples

```
  # List all assets
  incloud device asset list

  # Filter by category
  incloud device asset list --category router,ap

  # Filter by status
  incloud device asset list --status in_use,in_stock

  # Search by name
  incloud device asset list --name "office"

  # Search by MAC address
  incloud device asset list --mac "00:18:05"
```

### Options

```
      --category strings   Filter by category (router,gateway,ap,cash_register,barcode_scanner,voip_phone,printer,camera,mobile_phone,pc,pad,others)
  -f, --fields strings     Fields to return and display
  -h, --help               help for list
      --limit int          Number of items per page (default 20)
      --mac string         Filter by MAC address (partial match)
      --name string        Filter by asset name (partial match)
      --number string      Filter by asset number (partial match)
      --page int           Page number (starting from 1) (default 1)
      --sort string        Sort order (e.g. "createdAt,desc")
      --status strings     Filter by status (in_stock,in_use,in_repair,decommissioned)
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

* [incloud device asset](incloud_device_asset.md)	 - Manage network assets

