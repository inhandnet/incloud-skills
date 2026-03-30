## incloud alert export

Export alerts

### Synopsis

Export alerts as a server-generated file (CSV). Supports the same filters as 'alert list'.

```
incloud alert export [flags]
```

### Examples

```
  # Export all alerts to stdout
  incloud alert export

  # Export to a file
  incloud alert export -f alerts.csv

  # Export unacknowledged alerts
  incloud alert export --ack false -f unacked.csv

  # Export alerts within a time range
  incloud alert export --after 2024-01-01T00:00:00Z --before 2024-01-31T23:59:59Z

  # Pipe to other commands
  incloud alert export | head -20
```

### Options

```
      --ack string         Filter by acknowledgement status (true/false)
      --after string       Filter alerts after this time (e.g. 2024-01-01T00:00:00Z)
      --before string      Filter alerts before this time (e.g. 2024-01-31T23:59:59Z)
      --device string      Filter by device ID
  -f, --file string        Write output to file instead of stdout
      --group string       Filter by device group ID
  -h, --help               help for export
      --priority int       Filter by priority level
  -q, --query string       Search by entity name (fuzzy match)
      --status string      Filter by status (ACTIVE/CLOSED)
      --type stringArray   Filter by alert type (can be repeated)
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

* [incloud alert](incloud_alert.md)	 - Manage alerts

