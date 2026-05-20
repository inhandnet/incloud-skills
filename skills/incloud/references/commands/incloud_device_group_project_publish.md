## incloud device group project publish

Publish a project version

### Synopsis

Publish a project version, making it immutable and eligible for deployment.

```
incloud device group project publish <group-id> <project-id> [flags]
```

### Examples

```
  # Publish a project
  incloud device group project publish 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695
```

### Options

```
  -h, --help   help for publish
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

