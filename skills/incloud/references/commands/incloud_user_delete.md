## incloud user delete

Delete a user

```
incloud user delete <id> [flags]
```

### Examples

```
  # Delete a user (will prompt for confirmation)
  incloud user delete 507f1f77bcf86cd799439011

  # Skip confirmation
  incloud user delete 507f1f77bcf86cd799439011 --yes
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

* [incloud user](incloud_user.md)	 - Manage users

