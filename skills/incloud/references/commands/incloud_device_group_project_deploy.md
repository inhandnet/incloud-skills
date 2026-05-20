## incloud device group project deploy

Deploy a project version to the device group

### Synopsis

Deploy a published project version to all devices in the group. Pinned devices will not be affected.

```
incloud device group project deploy <group-id> <project-id> [flags]
```

### Examples

```
  # Deploy a project
  incloud device group project deploy 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695

  # Skip confirmation
  incloud device group project deploy 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --yes
```

### Options

```
  -h, --help   help for deploy
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

