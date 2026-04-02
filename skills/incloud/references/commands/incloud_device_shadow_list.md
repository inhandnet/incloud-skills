## incloud device shadow list

List shadow document names

### Synopsis

List all named shadow documents for a device.

```
incloud device shadow list <device-id> [flags]
```

### Examples

```
  # List shadow names
  incloud device shadow list 507f1f77bcf86cd799439011

  # Output as JSON
  incloud device shadow list 507f1f77bcf86cd799439011 -o json
```

### Options

```
  -h, --help   help for list
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

* [incloud device shadow](incloud_device_shadow.md)	 - Device shadow documents

