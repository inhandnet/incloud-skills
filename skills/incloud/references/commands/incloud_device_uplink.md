## incloud device uplink

Show device uplinks

### Synopsis

Show uplink (WAN/Cellular/WiFi) information for a specific device.

```
incloud device uplink <device-id> [flags]
```

### Examples

```
  # Show uplinks for a device
  incloud device uplink 507f1f77bcf86cd799439011

  # Table output
  incloud device uplink 507f1f77bcf86cd799439011 -o table

  # Table with selected fields
  incloud device uplink 507f1f77bcf86cd799439011 -o table -f name -f type -f status -f latency
```

### Options

```
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for uplink
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
* [incloud device uplink get](incloud_device_uplink_get.md)	 - Get uplink details
* [incloud device uplink perf](incloud_device_uplink_perf.md)	 - Show uplink performance trend

