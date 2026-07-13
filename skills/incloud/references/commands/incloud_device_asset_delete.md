## incloud device asset delete

Delete network assets

### Synopsis

Delete one or more network assets. Supports both single and batch deletion.

```
incloud device asset delete <asset-id> [asset-id...] [flags]
```

### Examples

```
  # Delete a single asset
  incloud device asset delete 507f1f77bcf86cd799439011

  # Delete multiple assets
  incloud device asset delete id1 id2 id3

  # Skip confirmation
  incloud device asset delete 507f1f77bcf86cd799439011 -y
```

### Options

```
  -h, --help   help for delete
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

* [incloud device asset](incloud_device_asset.md)	 - Manage network assets

