## incloud device config schema products

List products and versions with configuration schemas

### Synopsis

List all product/version combinations that have configuration schemas.

Use this to discover which devices support AI-assisted configuration
before using 'incloud device config schema overview/get/validate'.

```
incloud device config schema products [flags]
```

### Examples

```
  # List all products with config schemas
  incloud device config schema products

  # Filter by product
  incloud device config schema products --product MR805

  # JSON output for AI parsing
  incloud device config schema products -o json
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for products
      --limit int        Number of items per page (default 20)
      --page int         Page number (starting from 1) (default 1)
  -p, --product string   Filter by product code
      --sort string      Sort order (e.g. "createdAt,desc")
      --version string   Filter by firmware version
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

* [incloud device config schema](incloud_device_config_schema.md)	 - Browse and validate device configuration schemas

