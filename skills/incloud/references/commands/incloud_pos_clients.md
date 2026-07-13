## incloud pos clients

List POS-marked clients across all devices

### Synopsis

List clients marked with a POS priority level (priority/bypass) across all your devices.

```
incloud pos clients [flags]
```

### Examples

```
  # List all marked clients (priority + bypass)
  incloud pos clients

  # Only prioritized clients
  incloud pos clients --level priority

  # Filter by device, expand device and org info
  incloud pos clients --device 507f1f77bcf86cd799439011 --expand device,org
```

### Options

```
      --device string    Filter by device ID
      --expand strings   Expand related resources. Supported: device, org
  -f, --fields strings   Fields to return and display
  -h, --help             help for clients
      --level string     Filter by level (priority/bypass)
      --limit int        Number of items per page (default 20)
      --oid string       Filter by organization ID
      --page int         Page number (starting from 1) (default 1)
      --sort string      Sort order (e.g. "createdAt,desc")
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

* [incloud pos](incloud_pos.md)	 - Manage POS Ready traffic prioritization

