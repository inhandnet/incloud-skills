## incloud product get

Get product details

### Synopsis

Get detailed information about a specific product by its ID or name.

```
incloud product get <id-or-name> [flags]
```

### Examples

```
  # Get product by ID (colorized JSON in TTY)
  incloud product get 507f1f77bcf86cd799439011

  # Get product by name
  incloud product get IR615

  # Only specific fields
  incloud product get IR615 -f name -f productType -f status

  # Table output (KEY/VALUE pairs)
  incloud product get IR615 -o table

  # YAML output
  incloud product get IR615 -o yaml
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for get
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

* [incloud product](incloud_product.md)	 - Manage products

