## incloud device group project delete

Delete project versions

### Synopsis

Delete one or more project versions from a device group.

```
incloud device group project delete <group-id> <project-id>[,<id2>,...] [flags]
```

### Examples

```
  # Delete a project
  incloud device group project delete 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695

  # Delete multiple
  incloud device group project delete 507f1f77bcf86cd799439011 id1,id2

  # Skip confirmation
  incloud device group project delete 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --yes
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Skip confirmation prompt
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

