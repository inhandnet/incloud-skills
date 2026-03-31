## incloud license type get

Get license type details

### Synopsis

Get detailed information about a specific license type by its slug.

```
incloud license type get <slug> [flags]
```

### Examples

```
  # View license type details
  incloud license type get professional

  # YAML output
  incloud license type get professional -o yaml

  # Only specific fields
  incloud license type get professional -f name -f features -f prices
```

### Options

```
      --expand strings   Expand related resources (e.g. prices)
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

* [incloud license type](incloud_license_type.md)	 - Manage license types

