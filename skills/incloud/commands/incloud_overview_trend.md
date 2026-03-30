## incloud overview trend

Device online count trend

### Synopsis

Show daily online and total device count trend over time.

```
incloud overview trend [flags]
```

### Examples

```
  # Show trend for the last 30 days (default)
  incloud overview trend

  # Custom time range
  incloud overview trend --after 2024-01-01 --before 2024-03-31

  # JSON output
  incloud overview trend -o json

  # Show only online count
  incloud overview trend -f date -f online
```

### Options

```
      --after string     Start date (e.g. 2024-01-01 or 2024-01-01T00:00:00Z)
      --before string    End date (e.g. 2024-03-31 or 2024-03-31T23:59:59Z)
  -f, --fields strings   Fields to return and display
  -h, --help             help for trend
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

