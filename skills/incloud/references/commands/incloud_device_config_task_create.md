## incloud device config task create

Create a CLI configuration task

### Synopsis

Create a task to push CLI configuration commands to edge devices. Target by device IDs or group ID.

```
incloud device config task create [flags]
```

### Examples

```
  # Push config to specific devices
  incloud device config task create --product IR615 --device-ids id1,id2 --config "interface cellular 1\n ip nat inside"

  # Push config to a device group
  incloud device config task create --product IR615 --group-id 507f1f77bcf86cd799439011 --config "interface cellular 1\n ip nat inside"
```

### Options

```
      --config string        CLI configuration commands to push (required)
      --device-ids strings   Target device IDs (comma-separated, max 100)
      --group-id string      Target device group ID
  -h, --help                 help for create
      --product string       Product type (required)
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

* [incloud device config task](incloud_device_config_task.md)	 - Manage CLI configuration tasks

