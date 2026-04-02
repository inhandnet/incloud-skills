## incloud webhook test

Send a test message to a webhook

### Synopsis

Send a test message to verify the webhook is working correctly.
Either provide a webhook ID as argument, or use --url to test a URL directly.

```
incloud webhook test [id] [flags]
```

### Examples

```
  # Test a saved webhook by ID
  incloud webhook test 507f1f77bcf86cd799439011

  # Test a webhook URL directly
  incloud webhook test --url https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx
```

### Options

```
  -h, --help         help for test
      --url string   Webhook URL to test directly
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

