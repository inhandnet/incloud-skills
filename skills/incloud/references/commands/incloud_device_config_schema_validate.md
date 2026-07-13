## incloud device config schema validate

Validate JSON payload against a config schema

### Synopsis

Validate a JSON configuration payload against the device's config schema
before writing it with 'incloud device config update'.

Uses JSON Schema draft-07 validation. Exits with code 0 on success, 1 on
validation failure. Useful for AI tools to pre-check generated config.

```
incloud device config schema validate [flags]
```

### Examples

```
  # Validate a JSON payload
  incloud device config schema validate --device 507f1f77bcf86cd799439011 \
    --key dns --payload '{"dns":{"primary":"8.8.8.8"}}'

  # Validate from file
  incloud device config schema validate --product MR805 --version V2.0.15-111 \
    --key dns --file dns-config.json

  # Use in pipeline: validate then apply
  incloud device config schema validate -d <id> --key dns --payload '...' && \
  incloud device config update <id> --payload '...'
```

### Options

```
  -d, --device string    Device ID (use 'incloud device list' to find IDs)
      --file string      Path to JSON file to validate
  -h, --help             help for validate
  -k, --key string       JSON key identifying the config schema to validate against (required; use 'incloud device config schema list' to find keys)
      --payload string   JSON payload to validate
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

