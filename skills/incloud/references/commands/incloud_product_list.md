## incloud product list

List products

### Synopsis

List products on the InCloud platform with optional filtering and pagination.

```
incloud product list [flags]
```

### Examples

```
  # List products with default pagination
  incloud product list

  # Paginate
  incloud product list --page 2 --limit 50

  # Filter by name (LIKE search)
  incloud product list --name IR615

  # Filter by product type
  incloud product list --type router

  # Filter by status
  incloud product list --status PUBLISHED

  # Table output with selected fields
  incloud product list -o table -f name -f productType -f status
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --name string      Filter by name (LIKE search)
      --page int         Page number (starting from 1) (default 1)
      --sort string      Sort order (e.g. "createdAt,desc")
      --status string    Filter by status (INDEVELOPMENT|PUBLISHED)
      --type string      Filter by product type
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

