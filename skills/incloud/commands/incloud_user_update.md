## incloud user update

Update a user

### Synopsis

Update an existing user on the InCloud platform.

```
incloud user update <id> [flags]
```

### Examples

```
  # Update display name
  incloud user update 507f1f77bcf86cd799439011 --name "New Name"

  # Update email and contact
  incloud user update 507f1f77bcf86cd799439011 --email new@example.com --contact "+1234567890"

  # Update role
  incloud user update 507f1f77bcf86cd799439011 --role-id 5f1e5605fe20f674c2d14d45

  # Update labels
  incloud user update 507f1f77bcf86cd799439011 --label dept=engineering --label level=senior
```

### Options

```
      --contact string      Contact information
      --email string        User email
  -h, --help                help for update
      --label stringArray   Label in key=value format (repeatable, max 10)
      --locale string       Locale (e.g. zh_CN, en_US)
      --name string         Display name
      --role-id string      Role ID to assign (use 'incloud role list' to find IDs)
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

