## incloud connector account tendency

Show account connection usage trend

```
incloud connector account tendency <network-id> <account-id> [flags]
```

### Examples

```
  # Show usage trend
  incloud connector account tendency <network-id> <account-id> --after 2025-01-01T00:00:00Z --before 2025-01-31T23:59:59Z
```

### Options

```
      --after string    Start time (ISO 8601, required)
      --before string   End time (ISO 8601, required)
  -h, --help            help for tendency
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

