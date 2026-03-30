## incloud device client datausage-daily

Client daily data usage

### Synopsis

Display daily data usage (tx/rx) for a client in a given month.

```
incloud device client datausage-daily <client-id> [flags]
```

### Examples

```
  # Current month
  incloud device client datausage-daily 507f1f77bcf86cd799439011

  # Specific month
  incloud device client datausage-daily 507f1f77bcf86cd799439011 --month 2026-03
```

### Options

```
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for datausage-daily
      --month string     Month in YYYY-MM format (e.g. 2026-03)
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

* [incloud device client](incloud_device_client.md)	 - Connected clients (Wi-Fi/LAN)

