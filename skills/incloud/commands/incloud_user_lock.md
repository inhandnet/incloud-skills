## incloud user lock

Lock a user account

### Synopsis

Lock a user account to prevent login. The user's data is preserved.

```
incloud user lock <id> [flags]
```

### Examples

```
  # Lock a user (will prompt for confirmation)
  incloud user lock 507f1f77bcf86cd799439011

  # Skip confirmation
  incloud user lock 507f1f77bcf86cd799439011 --yes
```

### Options

```
  -h, --help   help for lock
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

