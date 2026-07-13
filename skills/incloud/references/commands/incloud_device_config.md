## incloud device config

Device configuration management

### Synopsis

View, update, and manage device configurations including layered config, history snapshots, and error diagnostics.

### Options

```
  -h, --help   help for config
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

* [incloud device](incloud_device.md)	 - Manage devices
* [incloud device config abort](incloud_device_config_abort.md)	 - Abort pending configuration delivery
* [incloud device config copy](incloud_device_config_copy.md)	 - Copy configuration to other devices or groups
* [incloud device config error](incloud_device_config_error.md)	 - Get configuration delivery errors
* [incloud device config get](incloud_device_config_get.md)	 - Get device configuration
* [incloud device config schema](incloud_device_config_schema.md)	 - Browse and validate device configuration schemas
* [incloud device config snapshots](incloud_device_config_snapshots.md)	 - Configuration snapshots
* [incloud device config task](incloud_device_config_task.md)	 - Manage CLI configuration tasks
* [incloud device config update](incloud_device_config_update.md)	 - Update device configuration

