## incloud webhook update

Update a webhook

### Synopsis

Update an existing webhook's URL or provider.

```
incloud webhook update <webhook-id> [flags]
```

### Examples

```
  # Update webhook URL
  incloud webhook update 507f1f77bcf86cd799439011 --url https://example.com/new-hook

  # Update provider
  incloud webhook update 507f1f77bcf86cd799439011 --provider wechat
```

### Options

```
  -h, --help              help for update
      --provider string   Webhook provider (supported: wechat)
      --url string        Webhook URL
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

