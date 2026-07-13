## incloud oobm serial list

List OOBM serial port configurations

```
incloud oobm serial list [flags]
```

### Examples

```
  # List serial port configurations
  incloud oobm serial list

  # Filter by device
  incloud oobm serial list --device-id 507f1f77bcf86cd799439011

  # Table with selected fields
  incloud oobm serial list -o table -f _id -f name -f speed -f connected
```

### Options

```
      --device-id string   Filter by device ID (use 'incloud device list' to find IDs)
  -f, --fields strings     Fields to return and display
  -h, --help               help for list
      --limit int          Number of items per page (default 20)
      --name string        Filter by name
      --page int           Page number (starting from 1) (default 1)
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

* [incloud oobm serial](incloud_oobm_serial.md)	 - Manage OOBM serial port configurations

