## incloud product compatibility

List product compatibilities

### Synopsis

List all compatibilities defined for a product, including minimum firmware version requirements.

```
incloud product compatibility <product-id-or-name> [flags]
```

### Examples

```
  # List compatibilities for a product
  incloud product compatibility IR915

  # JSON output
  incloud product compatibility IR915 -o json
```

### Options

```
  -h, --help   help for compatibility
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

