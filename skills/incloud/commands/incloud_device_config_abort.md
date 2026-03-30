## incloud device config abort

Abort pending configuration delivery

### Synopsis

Abort pending configuration delivery for a device, clearing the delta between desired and reported state so the cloud accepts the device's current configuration.

```
incloud device config abort <device-id> [flags]
```

### Examples

```
  # Abort pending config delivery (with confirmation)
  incloud device config abort 507f1f77bcf86cd799439011

  # Skip confirmation
  incloud device config abort 507f1f77bcf86cd799439011 --yes
```

### Options

```
  -h, --help            help for abort
      --module string   Module name (defaults to 'default' on the server)
  -y, --yes             Skip confirmation prompt
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

