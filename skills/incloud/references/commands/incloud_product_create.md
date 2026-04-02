## incloud product create

Create a product

### Synopsis

Create a new product on the InCloud platform.

```
incloud product create [flags]
```

### Examples

```
  # Create a product with required fields
  incloud product create --name IR615 --type router

  # With validated field
  incloud product create --name IR615 --type router --validated-field IMEI

  # With description and labels
  incloud product create --name IR615 --type router --description "Edge router" --label env=prod
```

### Options

```
      --description string       Product description
  -h, --help                     help for create
      --label stringArray        Label in key=value format (repeatable, max 10)
      --metadata stringArray     Metadata in key=value format (repeatable, max 100)
      --name string              Product name (required, 1-128 chars)
      --type string              Product type (required)
      --validated-field string   Validated field: MAC or IMEI (default "MAC")
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

