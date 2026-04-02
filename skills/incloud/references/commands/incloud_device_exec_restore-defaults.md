## incloud device exec restore-defaults

Restore a device to factory defaults

```
incloud device exec restore-defaults <id>[,<id2>,...] [flags]
```

### Examples

```
  # Restore a single device
  incloud device exec restore-defaults 507f1f77bcf86cd799439011

  # Restore multiple devices
  incloud device exec restore-defaults 507f1f77bcf86cd799439011,653b1ff2a84e171614d88695

  # Skip confirmation
  incloud device exec restore-defaults 507f1f77bcf86cd799439011 --yes
```

### Options

```
  -h, --help   help for restore-defaults
  -y, --yes    Skip confirmation prompt
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

* [incloud device exec](incloud_device_exec.md)	 - Execute remote methods and diagnostics on devices

