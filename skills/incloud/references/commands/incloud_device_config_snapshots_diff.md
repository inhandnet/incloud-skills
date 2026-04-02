## incloud device config snapshots diff

Compare two configuration snapshots

### Synopsis

Compare two configuration snapshots side by side using unified diff format.

```
incloud device config snapshots diff <device-id> <snapshot-id-1> <snapshot-id-2> [flags]
```

### Examples

```
  # Compare two snapshots
  incloud device config snapshots diff 507f1f77bcf86cd799439011 SNAP_ID_1 SNAP_ID_2

  # JSON output with structured differences
  incloud device config snapshots diff 507f1f77bcf86cd799439011 SNAP_ID_1 SNAP_ID_2 -o json
```

### Options

```
  -h, --help   help for diff
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

