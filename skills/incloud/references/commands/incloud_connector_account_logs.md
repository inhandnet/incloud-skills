## incloud connector account logs

Show account connection logs

```
incloud connector account logs <network-id> <account-id> [flags]
```

### Examples

```
  # Show connection logs
  incloud connector account logs <network-id> <account-id> --after 2025-01-01T00:00:00Z --before 2025-01-31T23:59:59Z
```

### Options

```
      --after string    Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string   End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
  -h, --help            help for logs
      --limit int       Number of items per page (default 20)
      --page int        Page number (starting from 1) (default 1)
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

