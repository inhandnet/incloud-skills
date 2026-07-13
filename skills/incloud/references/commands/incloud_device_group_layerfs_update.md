## incloud device group layerfs update

Update a filesystem snapshot

### Synopsis

Update the name or description of a filesystem snapshot (layerfs).

```
incloud device group layerfs update <group-id> <layerfs-id> [flags]
```

### Examples

```
  # Update name
  incloud device group layerfs update 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --name new-name

  # Update description
  incloud device group layerfs update 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --description "Updated desc"
```

### Options

```
      --description string   New description (max 128 chars)
  -h, --help                 help for update
      --name string          New name (1-64 chars)
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

