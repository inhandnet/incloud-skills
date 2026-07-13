## incloud webhook list

List webhooks

### Synopsis

List message webhooks with pagination and optional provider filter.

```
incloud webhook list [flags]
```

### Examples

```
  # List all webhooks
  incloud webhook list

  # Filter by provider
  incloud webhook list --provider wechat

  # Paginate
  incloud webhook list --page 2 --limit 50
```

### Options

```
      --expand strings    Expand related resources
  -f, --fields strings    Fields to return and display
  -h, --help              help for list
      --limit int         Number of items per page (default 20)
      --page int          Page number (starting from 1) (default 1)
      --provider string   Filter by provider (supported: wechat)
      --sort string       Sort order (e.g. "createdAt,desc")
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

* [incloud webhook](incloud_webhook.md)	 - Manage message webhooks

