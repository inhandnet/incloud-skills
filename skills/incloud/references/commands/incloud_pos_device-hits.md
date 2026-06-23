## incloud pos device-hits

Show POS application hits aggregated for a device

### Synopsis

Show POS application traffic hits for a device, aggregated by vendor or by client.

```
incloud pos device-hits <device-id> [flags]
```

### Examples

```
  # Vendor-grouped hits in the last 24h
  incloud pos device-hits 507f1f77bcf86cd799439011

  # Client-grouped hits over the last 7 days
  incloud pos device-hits 507f1f77bcf86cd799439011 --group-by client --active-within 7d
```

### Options

```
      --active-within string   Time window: 1h, 6h, 24h (default), 7d
      --group-by string        Aggregation: vendor (default) or client
  -h, --help                   help for device-hits
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

