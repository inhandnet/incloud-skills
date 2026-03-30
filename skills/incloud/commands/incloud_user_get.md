## incloud user get

Get user details

### Synopsis

Get detailed information about a specific user by ID.

```
incloud user get <id> [flags]
```

### Examples

```
  # Get user by ID
  incloud user get 69798301dfd35d106920c7b8

  # Only specific fields
  incloud user get 69798301dfd35d106920c7b8 -f name -f email -f username

  # Without expanding roles
  incloud user get 69798301dfd35d106920c7b8 --expand ""

  # Table output (KEY/VALUE pairs)
  incloud user get 69798301dfd35d106920c7b8 -o table

  # YAML output
  incloud user get 69798301dfd35d106920c7b8 -o yaml
```

### Options

```
      --expand strings   Expand related resources. Supported: org, mfa, roles, phoneNumberDetails, members (default [org,mfa,roles])
  -f, --fields strings   Fields to return and display
  -h, --help             help for get
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

