## incloud oobm delete

Delete OOBM resources

```
incloud oobm delete <id> [<id>...] [flags]
```

### Examples

```
  # Delete a single resource
  incloud oobm delete 507f1f77bcf86cd799439011

  # Delete multiple resources
  incloud oobm delete 507f1f77bcf86cd799439011 507f1f77bcf86cd799439012

  # Skip confirmation
  incloud oobm delete 507f1f77bcf86cd799439011 -y
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

* [incloud oobm](incloud_oobm.md)	 - Manage Out-of-Band Management resources

