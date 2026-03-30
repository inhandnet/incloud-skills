## incloud overview traffic

Traffic overview and top devices

### Synopsis

Show global traffic statistics and top-K devices by data usage.

```
incloud overview traffic [flags]
```

### Examples

```
  # Show traffic overview
  incloud overview traffic

  # Filter by time range
  incloud overview traffic --after 2024-01-01 --before 2024-01-31

  # Filter by traffic type
  incloud overview traffic --type cellular

  # Top 5 devices
  incloud overview traffic --n 5

  # JSON output (summary + trend + topDevices)
  incloud overview traffic -o json
```

### Options

```
      --after string     Start date (e.g. 2024-01-01)
      --before string    End date (e.g. 2024-01-31)
  -f, --fields strings   Fields to display in table output
  -h, --help             help for traffic
      --n int            Number of top devices to return (default 10)
      --type string      Traffic type: cellular|wifi|wired|all
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

* [incloud overview](incloud_overview.md)	 - Platform overview dashboard

