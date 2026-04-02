## incloud device config snapshots

Configuration snapshots

### Synopsis

View, inspect, and restore configuration snapshots for a device.

### Options

```
  -h, --help   help for snapshots
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

* [incloud device config](incloud_device_config.md)	 - Device configuration management
* [incloud device config snapshots diff](incloud_device_config_snapshots_diff.md)	 - Compare two configuration snapshots
* [incloud device config snapshots get](incloud_device_config_snapshots_get.md)	 - Get a configuration history snapshot
* [incloud device config snapshots list](incloud_device_config_snapshots_list.md)	 - List configuration change history
* [incloud device config snapshots restore](incloud_device_config_snapshots_restore.md)	 - Restore configuration from a snapshot

