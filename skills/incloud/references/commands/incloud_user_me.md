## incloud user me

Show current user profile

### Synopsis

Show the profile of the currently authenticated user.

```
incloud user me [flags]
```

### Examples

```
  # Show current user profile
  incloud user me

  # Table output with default fields
  incloud user me -o table

  # Only specific fields
  incloud user me -f username -f email -f locale

  # Expand roles
  incloud user me --expand phoneNumberDetails

  # JSON output
  incloud user me -o json

  # Extract email with jq
  incloud user me --jq '.email'
```

### Options

```
      --expand strings   Expand related resources. Supported: phoneNumberDetails, mfa
  -f, --fields strings   Fields to return and display
  -h, --help             help for me
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

