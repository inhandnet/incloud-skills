## incloud connector usage trend

Show daily traffic trend

```
incloud connector usage trend [flags]
```

### Examples

```
  # Show daily traffic trend for a date range
  incloud connector usage trend --after 2025-01-01 --before 2025-01-31
```

### Options

```
      --after string    Start date (e.g. 2025-01-01, required)
      --before string   End date (e.g. 2025-01-31, required)
  -h, --help            help for trend
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

