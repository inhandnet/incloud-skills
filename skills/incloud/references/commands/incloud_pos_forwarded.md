## incloud pos forwarded

List clients with recently forwarded POS traffic

### Synopsis

List clients whose POS traffic was matched/forwarded within a recent time window, with the matched vendor tags.

```
incloud pos forwarded [flags]
```

### Examples

```
  # Clients with POS hits in the last 24h
  incloud pos forwarded

  # Last 7 days, filter by vendor
  incloud pos forwarded --active-within 7d --vendor Verifone
```

### Options

```
      --active-within string   Time window: 1h, 6h, 24h (default), 7d
      --client-type string     Filter by client type (e.g. POS_TERMINAL)
      --device string          Filter by device ID
  -f, --fields strings         Fields to return and display
  -h, --help                   help for forwarded
      --limit int              Number of items per page (default 20)
      --oid string             Filter by organization ID
      --page int               Page number (starting from 1) (default 1)
      --sort string            Sort order (e.g. "createdAt,desc")
      --vendor string          Filter by matched vendor
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

