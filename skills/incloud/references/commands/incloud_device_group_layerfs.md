## incloud device group layerfs

Manage device group filesystem snapshots

### Synopsis

Create, list, update, and delete filesystem snapshots (layerfs) captured from edge devices within a device group.

### Options

```
  -h, --help   help for layerfs
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

* [incloud device group](incloud_device_group.md)	 - Manage device groups
* [incloud device group layerfs create](incloud_device_group_layerfs_create.md)	 - Create a filesystem snapshot
* [incloud device group layerfs delete](incloud_device_group_layerfs_delete.md)	 - Delete filesystem snapshots
* [incloud device group layerfs list](incloud_device_group_layerfs_list.md)	 - List filesystem snapshots in a device group
* [incloud device group layerfs update](incloud_device_group_layerfs_update.md)	 - Update a filesystem snapshot

