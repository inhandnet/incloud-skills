## incloud pos vendor-summary

POS vendor hit summary for a client

### Synopsis

Show the aggregated POS vendor hit summary for a client on a device over a time range.

```
incloud pos vendor-summary <device-id> <client-id> [flags]
```

### Examples

```
  # Summary over a day
  incloud pos vendor-summary 507f1f77bcf86cd799439011 69b8c537e7f8d2c1e5fffdbc \
    --after 2026-03-17T00:00:00Z --before 2026-03-18T00:00:00Z
```

### Options

```
      --after string    Start time (RFC3339 or YYYY-MM-DD), required
      --before string   End time (RFC3339 or YYYY-MM-DD), required
  -h, --help            help for vendor-summary
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

* [incloud pos](incloud_pos.md)	 - Manage POS Ready traffic prioritization

