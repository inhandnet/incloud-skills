## incloud model list

List AI models

### Synopsis

List AI models in the current tenant.

```
incloud model list [flags]
```

### Examples

```
  # List all models
  incloud model list

  # Search by name (fuzzy match)
  incloud model list --name detect

  # Filter by tags
  incloud model list --tags edge,ai

  # Filter by product model
  incloud model list --product-models IR315-xxx

  # Show specific fields
  incloud model list --fields _id,name,tags
```

### Options

```
  -f, --fields strings           Fields to return and display
  -h, --help                     help for list
      --limit int                Number of items per page (default 20)
      --name string              Filter by name (fuzzy match)
      --page int                 Page number (starting from 1) (default 1)
      --product-models strings   Filter by product models (format: product-pn)
      --sort string              Sort order (e.g. "createdAt,desc")
      --tags strings             Filter by tags
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

