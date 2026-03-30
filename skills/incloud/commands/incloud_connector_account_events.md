## incloud connector account events

Show account online/offline events

```
incloud connector account events <network-id> <account-id> [flags]
```

### Examples

```
  # Show events in a time range
  incloud connector account events <network-id> <account-id> --after 2025-01-01T00:00:00Z --before 2025-01-31T23:59:59Z
```

### Options

```
      --after string    Start time (ISO 8601, required)
      --before string   End time (ISO 8601, required)
  -h, --help            help for events
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

