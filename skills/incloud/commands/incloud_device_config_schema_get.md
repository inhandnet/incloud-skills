## incloud device config schema get

Get a configuration schema by JSON key

### Synopsis

Get the full configuration schema definition for a specific JSON key,
including JSON Schema content and human-readable descriptions.

The JSON key can be found from 'incloud device config schema list'.

```
incloud device config schema get <json-key> [flags]
```

### Examples

```
  # Get DNS config schema
  incloud device config schema get --device 507f1f77bcf86cd799439011 dns

  # JSON output for AI parsing
  incloud device config schema get --product MR805 --version V2.0.15-111 dns -o json
```

### Options

```
  -d, --device string    Device ID (use 'incloud device list' to find IDs)
  -h, --help             help for get
  -p, --product string   Product code (requires --version; mutually exclusive with --device)
      --version string   Firmware version (requires --product)
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

