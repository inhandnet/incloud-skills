## incloud device config snapshots restore

Restore configuration from a snapshot

### Synopsis

Restore a device's configuration from a history snapshot. This replaces the current device-level configuration with the snapshot's merged config.

```
incloud device config snapshots restore <device-id> <snapshot-id> [flags]
```

### Examples

```
  # Restore with confirmation
  incloud device config snapshots restore 507f1f77bcf86cd799439011 69ba26b4ed93070787cea168

  # Skip confirmation
  incloud device config snapshots restore 507f1f77bcf86cd799439011 69ba26b4ed93070787cea168 --yes
```

### Options

```
  -h, --help   help for restore
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

* [incloud device config snapshots](incloud_device_config_snapshots.md)	 - Configuration snapshots

