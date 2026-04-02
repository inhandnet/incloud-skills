## incloud device group list

List device groups

```
incloud device group list [flags]
```

### Examples

```
  # List device groups
  incloud device group list

  # Filter by product
  incloud device group list --product ER805

  # Search by name
  incloud device group list --name "Edge"

  # Show device counts per group
  incloud device group list --summary

  # Filter by organization
  incloud device group list --org 60a1b2c3d4e5f6a7b8c9d0e1

  # Expand device count and org info
  incloud device group list --expand org,nezha-iot-device-summary -o json

  # Paginate
  incloud device group list --page 2 --limit 10
```

### Options

```
      --expand strings        Expand related resources. Supported: org, nezha-iot-device-summary
  -f, --fields strings        Fields to return and display
      --firmware string       Filter by firmware version (fuzzy match)
  -h, --help                  help for list
      --limit int             Number of items per page (default 20)
      --name string           Filter by group name (fuzzy match)
      --org string            Filter by organization ID
      --page int              Page number (starting from 1) (default 1)
      --product stringArray   Filter by product (can be repeated)
      --sort string           Sort order (e.g. "createdAt,desc")
      --summary               Include device counts (online/offline/total) per group
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

* [incloud device group](incloud_device_group.md)	 - Manage device groups

