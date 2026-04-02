## incloud connector account update

Update an account in a connector network

```
incloud connector account update <network-id> <account-id> [flags]
```

### Examples

```
  # Update name
  incloud connector account update <network-id> <account-id> --name new-name

  # Enable static IP
  incloud connector account update <network-id> <account-id> --static-ip --vip 10.32.1.100
```

### Options

```
  -h, --help          help for update
      --name string   Account name (max 64 chars)
      --static-ip     Use static IP address
      --vip string    Virtual IP (required when --static-ip is set)
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

* [incloud connector account](incloud_connector_account.md)	 - Manage connector accounts (VPN users)

