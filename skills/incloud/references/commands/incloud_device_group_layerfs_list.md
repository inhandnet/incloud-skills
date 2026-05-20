## incloud device group layerfs list

List filesystem snapshots in a device group

### Synopsis

List filesystem snapshots (layerfs) within a device group.

```
incloud device group layerfs list <group-id> [flags]
```

### Examples

```
  # List layerfs in a group
  incloud device group layerfs list 507f1f77bcf86cd799439011

  # Filter by status
  incloud device group layerfs list 507f1f77bcf86cd799439011 --status SUCCEEDED

  # Expand related resources
  incloud device group layerfs list 507f1f77bcf86cd799439011 --expand device,creator
```

### Options

```
      --expand string    Expand related resources (e.g. device,creator)
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --page int         Page number (starting from 1) (default 1)
      --sort string      Sort order (e.g. "createdAt,desc")
      --status string    Filter by status (QUEUED|INPROGRESS|SUCCEEDED|FAILED|CANCELED)
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

* [incloud device group layerfs](incloud_device_group_layerfs.md)	 - Manage device group filesystem snapshots

