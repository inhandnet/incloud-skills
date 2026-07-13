## incloud product update

Update a product

### Synopsis

Update an existing product on the InCloud platform.

```
incloud product update <id> [flags]
```

### Examples

```
  # Update description
  incloud product update 507f1f77bcf86cd799439011 --description "Updated"

  # Publish a product
  incloud product update 507f1f77bcf86cd799439011 --status PUBLISHED

  # Update validated field
  incloud product update 507f1f77bcf86cd799439011 --validated-field IMEI

  # Update labels and metadata
  incloud product update 507f1f77bcf86cd799439011 --label env=staging --metadata key1=val1
```

### Options

```
      --description string       Product description
  -h, --help                     help for update
      --label stringArray        Label in key=value format (repeatable, max 10)
      --metadata stringArray     Metadata in key=value format (repeatable, max 100)
      --status string            Product status: INDEVELOPMENT or PUBLISHED
      --validated-field string   Validated field: MAC or IMEI
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

