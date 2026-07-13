## incloud model get

Get an AI model

### Synopsis

Get details of an AI model by ID.

```
incloud model get <id> [flags]
```

### Examples

```
  # Get model details
  incloud model get 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for get
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

* [incloud model](incloud_model.md)	 - Manage AI models

