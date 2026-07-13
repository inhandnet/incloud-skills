## incloud device config schema overview

View product configuration overview

### Synopsis

View the configuration overview for a product/firmware, including
dependency rules and business constraints between config sections.

AI tools should read this before modifying configurations to understand
which config sections depend on each other.

```
incloud device config schema overview [flags]
```

### Examples

```
  # View overview for a device
  incloud device config schema overview --device 507f1f77bcf86cd799439011

  # View by product/version
  incloud device config schema overview --product CPE02 --version V2.0.8

  # JSON output
  incloud device config schema overview --product CPE02 --version V2.0.8 -o json
```

### Options

```
  -d, --device string    Device ID (use 'incloud device list' to find IDs)
  -h, --help             help for overview
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

