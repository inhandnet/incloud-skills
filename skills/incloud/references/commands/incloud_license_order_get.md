## incloud license order get

Get order details

### Synopsis

Get detailed information about a specific order by its ID.

```
incloud license order get <order-id> [flags]
```

### Examples

```
  # View order details
  incloud license order get 64a1b2c3d4e5f6a7b8c9d0e1

  # YAML output
  incloud license order get 64a1b2c3d4e5f6a7b8c9d0e1 -o yaml
```

### Options

```
      --expand strings   Expand related resources (supported: creator, org)
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

* [incloud license order](incloud_license_order.md)	 - Manage license orders

