## incloud firmware get

Get firmware details

### Synopsis

Get detailed information about a specific firmware by its ID.

```
incloud firmware get <id> [flags]
```

### Examples

```
  # Get firmware by ID
  incloud firmware get 507f1f77bcf86cd799439011

  # Table output
  incloud firmware get 507f1f77bcf86cd799439011 -o table

  # Select fields
  incloud firmware get 507f1f77bcf86cd799439011 -f product -f version -f status
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

* [incloud firmware](incloud_firmware.md)	 - Manage firmwares

