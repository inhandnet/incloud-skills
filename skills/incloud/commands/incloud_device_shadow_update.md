## incloud device shadow update

Update a shadow document

### Synopsis

Update the desired state of a device shadow document.

```
incloud device shadow update <device-id> [flags]
```

### Examples

```
  # Update shadow with inline JSON
  incloud device shadow update 507f1f77bcf86cd799439011 --name default \
    --payload '{"state":{"desired":{"temperature":25}}}'

  # Update shadow from a file
  incloud device shadow update 507f1f77bcf86cd799439011 --name default \
    --file shadow.json
```

### Options

```
      --file string      Path to JSON file containing shadow payload
  -h, --help             help for update
      --name string      Shadow name (required)
      --payload string   Shadow JSON payload
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

