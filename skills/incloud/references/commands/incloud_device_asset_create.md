## incloud device asset create

Create a network asset

### Synopsis

Create a new network asset with the given properties.

```
incloud device asset create [flags]
```

### Examples

```
  # Create a router asset
  incloud device asset create --name "Office Router" --mac "00:18:05:AB:CD:EF" --category router --status in_use

  # Create with all fields
  incloud device asset create --name "Printer" --mac "AA:BB:CC:DD:EE:FF" \
    --category printer --status in_stock --number "AST-001" \
    --warranty-expiration "2027-12-31" --notes "2nd floor"
```

### Options

```
      --category string              Asset category (required: router,gateway,ap,cash_register,barcode_scanner,voip_phone,printer,camera,mobile_phone,pc,pad,others)
  -h, --help                         help for create
      --mac string                   MAC address (required, e.g. 00:18:05:AB:CD:EF)
      --name string                  Asset name (required)
      --notes string                 Additional notes
      --number string                Asset number
      --status string                Asset status (required: in_stock,in_use,in_repair,decommissioned)
      --warranty-expiration string   Warranty expiration date (YYYY-MM-DD)
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

