## incloud device update

Update a device

### Synopsis

Update an existing device on the InCloud platform.

```
incloud device update <id> [flags]
```

### Examples

```
  # Update device name
  incloud device update 507f1f77bcf86cd799439011 --name "New Name"

  # Update description
  incloud device update 507f1f77bcf86cd799439011 --description "Updated description"

  # Update labels
  incloud device update 507f1f77bcf86cd799439011 --label env=staging --label region=eu

  # Update metadata
  incloud device update 507f1f77bcf86cd799439011 --metadata key1=val1
```

### Options

```
      --description string     Device description (max 256 chars)
  -h, --help                   help for update
      --label stringArray      Label in key=value format (repeatable, max 10)
      --metadata stringArray   Metadata in key=value format (repeatable)
      --name string            Device name
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

