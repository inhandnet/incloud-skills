## incloud device shadow delete

Delete a shadow document

### Synopsis

Delete a named shadow document from a device.

```
incloud device shadow delete <device-id> [flags]
```

### Examples

```
  # Delete a shadow (with confirmation)
  incloud device shadow delete 507f1f77bcf86cd799439011 --name test

  # Skip confirmation
  incloud device shadow delete 507f1f77bcf86cd799439011 --name test --yes
```

### Options

```
  -h, --help          help for delete
      --name string   Shadow name (required)
  -y, --yes           Skip confirmation prompt
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

