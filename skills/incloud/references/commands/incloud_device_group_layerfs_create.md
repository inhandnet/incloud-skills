## incloud device group layerfs create

Create a filesystem snapshot

### Synopsis

Create a filesystem snapshot (layerfs) by capturing the current filesystem state from a specified edge device.

```
incloud device group layerfs create <group-id> [flags]
```

### Examples

```
  # Create a layerfs from a device
  incloud device group layerfs create 507f1f77bcf86cd799439011 --name my-snapshot --device-id 653b1ff2a84e171614d88695

  # With description
  incloud device group layerfs create 507f1f77bcf86cd799439011 --name my-snapshot --device-id 653b1ff2a84e171614d88695 --description "Base image v1"
```

### Options

```
      --description string   Snapshot description (max 128 chars)
      --device-id string     Source device ID to capture from (required)
  -h, --help                 help for create
      --name string          Snapshot name (required, 1-64 chars)
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

