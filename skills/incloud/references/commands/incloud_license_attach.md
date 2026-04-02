## incloud license attach

Attach a license to a device

### Synopsis

Attach a license to a device.

If the device already has an active license of the same type, the new license
duration will be added to the existing one (overlay). This operation is irreversible.

```
incloud license attach <license-id> [flags]
```

### Examples

```
  # Attach a license to a device
  incloud license attach 64a1b2c3d4e5f6a7b8c9d0e1 --device 507f1f77bcf86cd799439011

  # Skip confirmation for overlay
  incloud license attach 64a1b2c3d4e5f6a7b8c9d0e1 --device 507f1f77bcf86cd799439011 --yes
```

### Options

```
      --device string   Target device ID (required)
  -h, --help            help for attach
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

* [incloud license](incloud_license.md)	 - Manage licenses

