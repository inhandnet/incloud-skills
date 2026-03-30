## incloud connector account delete

Delete accounts from a connector network

```
incloud connector account delete <network-id> <account-id> [account-id...] [flags]
```

### Examples

```
  # Delete single account
  incloud connector account delete <network-id> <account-id>

  # Delete multiple accounts
  incloud connector account delete <network-id> id1 id2 id3

  # Skip confirmation
  incloud connector account delete <network-id> <account-id> -y
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

* [incloud connector account](incloud_connector_account.md)	 - Manage connector accounts (VPN users)

