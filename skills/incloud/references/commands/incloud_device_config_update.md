## incloud device config update

Update device configuration

### Synopsis

Directly update a device's configuration using a JSON merge patch. This creates a session, applies the patch, and commits in one step.

```
incloud device config update <device-id> [flags]
```

### Examples

```
  # Update hostname
  incloud device config update 507f1f77bcf86cd799439011 \
    --payload '{"system":{"hostname":"new-name"}}'

  # Update from a file
  incloud device config update 507f1f77bcf86cd799439011 --file config-patch.json
```

### Options

```
      --file string      Path to JSON file containing the merge patch
  -h, --help             help for update
      --module string    Module name (defaults to 'default' on the server)
      --payload string   JSON merge patch payload
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

* [incloud device config](incloud_device_config.md)	 - Device configuration management

