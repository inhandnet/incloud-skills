## incloud connector usage topk

Show top-K traffic consumption ranking

```
incloud connector usage topk [flags]
```

### Examples

```
  # Show top 10 devices by traffic
  incloud connector usage topk --after 2025-01-01 --before 2025-01-31

  # Show top 5 accounts by traffic
  incloud connector usage topk --after 2025-01-01 --before 2025-01-31 --type ACCOUNT --n 5
```

### Options

```
      --after string    Start date (YYYY-MM-DD, required)
      --before string   End date (YYYY-MM-DD, required)
  -h, --help            help for topk
      --n int           Number of top results to return (default 10)
      --type string     Filter by type: DEVICE or ACCOUNT (default: DEVICE)
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

* [incloud connector usage](incloud_connector_usage.md)	 - Connector traffic usage statistics

