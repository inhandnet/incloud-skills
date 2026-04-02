## incloud device config copy

Copy configuration to other devices or groups

### Synopsis

Copy a device or group configuration to one or more target devices or groups.

```
incloud device config copy [flags]
```

### Examples

```
  # Copy from device to device
  incloud device config copy --source DEV1 --target DEV2

  # Copy from device to multiple targets
  incloud device config copy --source DEV1 --target DEV2 --target DEV3

  # Copy from device to groups
  incloud device config copy --source DEV1 --target-group GRP1 --target-group GRP2

  # Copy from group to groups
  incloud device config copy --source-group GRP1 --target-group GRP2
```

### Options

```
  -h, --help                       help for copy
      --module string              Module name (defaults to 'default' on the server)
      --source string              Source device ID
      --source-group string        Source group ID (mutually exclusive with --source)
      --target stringArray         Target device ID (can be repeated)
      --target-group stringArray   Target group ID (can be repeated)
  -y, --yes                        Skip confirmation prompt
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

