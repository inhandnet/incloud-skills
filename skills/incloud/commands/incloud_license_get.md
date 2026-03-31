## incloud license get

Get license details

### Synopsis

Get detailed information about a specific license by its ID.

```
incloud license get <license-id> [flags]
```

### Examples

```
  # View license details
  incloud license get 64a1b2c3d4e5f6a7b8c9d0e1

  # View only status and expiry
  incloud license get 64a1b2c3d4e5f6a7b8c9d0e1 -f status -f expiresAt

  # YAML output
  incloud license get 64a1b2c3d4e5f6a7b8c9d0e1 -o yaml
```

### Options

```
      --expand strings   Expand related resources (supported: licenseType, device, org)
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

* [incloud license](incloud_license.md)	 - Manage licenses

