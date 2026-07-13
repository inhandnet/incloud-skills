## incloud device config schema list

List configuration schemas

### Synopsis

List configuration schema documents for a device's product/firmware.
Shows schema name, JSON keys, and a brief description for each config section.

Use --device to auto-detect product/version, or --product/--version to specify directly.

```
incloud device config schema list [flags]
```

### Examples

```
  # List schemas for a device
  incloud device config schema list --device 507f1f77bcf86cd799439011

  # List by product/version
  incloud device config schema list --product MR805 --version V2.0.15-111

  # Filter by name (regex)
  incloud device config schema list --device 507f1f77bcf86cd799439011 --name "DNS|WiFi"

  # JSON output for AI tools
  incloud device config schema list --device 507f1f77bcf86cd799439011 -o json
```

### Options

```
  -d, --device string    Device ID (use 'incloud device list' to find IDs)
  -h, --help             help for list
      --name string      Filter by schema name (case-insensitive regex)
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

