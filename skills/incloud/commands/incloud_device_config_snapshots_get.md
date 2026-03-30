## incloud device config snapshots get

Get a configuration history snapshot

### Synopsis

Get the full details of a configuration history snapshot, including the merged configuration at that point in time.

```
incloud device config snapshots get <device-id> <snapshot-id> [flags]
```

### Examples

```
  # View a snapshot
  incloud device config snapshots get 507f1f77bcf86cd799439011 69ba26b4ed93070787cea168

  # YAML output
  incloud device config snapshots get 507f1f77bcf86cd799439011 69ba26b4ed93070787cea168 -o yaml
```

### Options

```
  -h, --help   help for get
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

