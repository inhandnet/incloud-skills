## incloud user create

Create a user

### Synopsis

Create a new user on the InCloud platform.

```
incloud user create [flags]
```

### Examples

```
  # Create a user with required fields
  incloud user create --email user@example.com --password P@ssw0rd --role-id 5f1e5605fe20f674c2d14d45

  # With display name and locale
  incloud user create --email user@example.com --password P@ssw0rd --role-id 5f1e5605fe20f674c2d14d45 --name "John Doe" --locale en_US

  # With labels
  incloud user create --email user@example.com --password P@ssw0rd --role-id 5f1e5605fe20f674c2d14d45 --label dept=engineering --label level=senior
```

### Options

```
      --email string        User email (required)
  -h, --help                help for create
      --label stringArray   Label in key=value format (repeatable, max 10)
      --locale string       Locale (e.g. zh_CN, en_US)
      --name string         Display name (defaults to email)
      --password string     User password (required, 6-64 chars)
      --role-id string      Role ID to assign (required; use 'incloud role list' to find IDs)
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

