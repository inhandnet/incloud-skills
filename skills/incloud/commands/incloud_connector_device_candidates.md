## incloud connector device candidates

List candidate devices that can be added to a connector network

```
incloud connector device candidates [flags]
```

### Examples

```
  # List all candidates
  incloud connector device candidates

  # Search by name or serial number
  incloud connector device candidates -q ER805
```

### Options

```
  -h, --help            help for candidates
      --limit int       Number of items per page (default 20)
      --page int        Page number (starting from 1) (default 1)
  -q, --search string   Search by name or serial number
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

