## incloud oobm serial delete

Delete OOBM serial port configurations

```
incloud oobm serial delete <id> [<id>...] [flags]
```

### Examples

```
  # Delete a single serial configuration
  incloud oobm serial delete 507f1f77bcf86cd799439011

  # Delete multiple, skip confirmation
  incloud oobm serial delete id1 id2 -y
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

* [incloud oobm serial](incloud_oobm_serial.md)	 - Manage OOBM serial port configurations

