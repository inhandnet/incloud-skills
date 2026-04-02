## incloud device transfer

Transfer a device to another organization

### Synopsis

Transfer a device to another organization.

This is a destructive operation: the device record is deleted from the
source organization and recreated in the target organization.

```
incloud device transfer <device-id> [flags]
```

### Examples

```
  # Transfer device to another organization
  incloud device transfer 507f1f77bcf86cd799439011 --org 60b76cb7ee4e6d5d842429da

  # Skip confirmation
  incloud device transfer 507f1f77bcf86cd799439011 --org 60b76cb7ee4e6d5d842429da -y
```

### Options

```
  -h, --help         help for transfer
      --org string   Target organization ID (required)
  -y, --yes          Skip confirmation prompt
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

