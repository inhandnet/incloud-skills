## incloud device group project get

Get a project version

### Synopsis

Get details of a project version in a device group.

```
incloud device group project get <group-id> <project-id> [flags]
```

### Examples

```
  # Get project details
  incloud device group project get 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695

  # With expanded resources
  incloud device group project get 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --expand creator,edge-layerfs
```

### Options

```
      --expand string   Expand related resources (e.g. creator,edge-layerfs)
  -h, --help            help for get
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

