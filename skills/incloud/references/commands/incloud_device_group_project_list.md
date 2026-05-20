## incloud device group project list

List project versions

### Synopsis

List project versions in a device group.

```
incloud device group project list <group-id> [flags]
```

### Examples

```
  # List all projects
  incloud device group project list 507f1f77bcf86cd799439011

  # Filter by published status
  incloud device group project list 507f1f77bcf86cd799439011 --published true

  # Filter by version
  incloud device group project list 507f1f77bcf86cd799439011 --version 0.1

  # Expand related resources
  incloud device group project list 507f1f77bcf86cd799439011 --expand creator,edge-layerfs
```

### Options

```
      --expand string      Expand related resources (e.g. creator,edge-layerfs)
  -f, --fields strings     Fields to return and display
  -h, --help               help for list
      --limit int          Number of items per page (default 20)
      --page int           Page number (starting from 1) (default 1)
      --published string   Filter by published status (true|false)
      --sort string        Sort order (e.g. "createdAt,desc")
      --version string     Filter by version (LIKE search)
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

* [incloud device group project](incloud_device_group_project.md)	 - Manage device group projects

