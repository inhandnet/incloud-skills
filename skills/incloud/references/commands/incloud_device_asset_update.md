## incloud device asset update

Update a network asset

### Synopsis

Update the properties of an existing network asset. Name, category, and status are required by the API; omitting them will result in a server-side validation error.

```
incloud device asset update <asset-id> [flags]
```

### Examples

```
  # Update status only (name and category still required by API)
  incloud device asset update 507f1f77bcf86cd799439011 \
    --name "Office Router" --category router --status decommissioned

  # Update just the notes
  incloud device asset update 507f1f77bcf86cd799439011 --notes "moved to 3rd floor"

  # Clear warranty expiration
  incloud device asset update 507f1f77bcf86cd799439011 --warranty-expiration ""
```

### Options

```
      --category string              Asset category (router,gateway,ap,cash_register,barcode_scanner,voip_phone,printer,camera,mobile_phone,pc,pad,others)
  -h, --help                         help for update
      --name string                  Asset name
      --notes string                 Additional notes
      --number string                Asset number
      --status string                Asset status (in_stock,in_use,in_repair,decommissioned)
      --warranty-expiration string   Warranty expiration date (YYYY-MM-DD, empty to clear)
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

