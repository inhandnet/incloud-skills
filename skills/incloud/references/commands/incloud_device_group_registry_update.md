## incloud device group registry update

Update registry configuration for a device group

### Synopsis

Update the container registry configurations for an edge device group. Provide registries as a JSON array.

```
incloud device group registry update <group-id> [flags]
```

### Examples

```
  # Set a single registry
  incloud device group registry update 507f1f77bcf86cd799439011 --registries '[{"url":"registry.example.com","username":"user","password":"pass"}]'

  # Clear all registries
  incloud device group registry update 507f1f77bcf86cd799439011 --registries '[]'
```

### Options

```
  -h, --help                help for update
      --registries string   Registry configurations as JSON array (e.g. '[{"url":"...","username":"...","password":"..."}]')
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

* [incloud device group registry](incloud_device_group_registry.md)	 - Manage device group container registries

