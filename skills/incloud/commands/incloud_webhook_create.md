## incloud webhook create

Create a webhook

### Synopsis

Create a new message webhook configuration.

```
incloud webhook create [flags]
```

### Examples

```
  # Create a WeChat webhook
  incloud webhook create --name "WeChat Alert" \
    --url https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx \
    --provider wechat

  # Create a generic webhook (receives JSON payload)
  incloud webhook create --name "Custom Alert" \
    --url https://example.com/webhook \
    --provider generic
```

### Options

```
  -h, --help              help for create
      --name string       Webhook name (required)
      --provider string   Webhook provider (required; supported: wechat, generic)
      --url string        Webhook URL (required)
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

