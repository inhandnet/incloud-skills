## incloud device config schema

Browse and validate device configuration schemas

### Synopsis

Discover configuration schemas for a device's product/firmware,
and validate JSON payloads before writing.

AI tools workflow:
  1. incloud device config schema overview --device <id>
  2. incloud device config schema list --device <id>
  3. incloud device config schema get --device <id> <json-key>
  4. incloud device config schema validate --device <id> --key <json-key> --payload '{...}'
  5. incloud device config update <id> --payload '{...}'

### Options

```
  -h, --help   help for schema
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
* [incloud device config schema get](incloud_device_config_schema_get.md)	 - Get a configuration schema by JSON key
* [incloud device config schema list](incloud_device_config_schema_list.md)	 - List configuration schemas
* [incloud device config schema overview](incloud_device_config_schema_overview.md)	 - View product configuration overview
* [incloud device config schema validate](incloud_device_config_schema_validate.md)	 - Validate JSON payload against a config schema

