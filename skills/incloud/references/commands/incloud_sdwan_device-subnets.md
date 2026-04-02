## incloud sdwan device-subnets

Get subnets for a device

```
incloud sdwan device-subnets <deviceId> [flags]
```

### Examples

```
  # View subnets reported by a device
  incloud sdwan device-subnets <deviceId>
```

### Options

```
  -h, --help   help for device-subnets
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

* [incloud sdwan](incloud_sdwan.md)	 - Manage SD-WAN networks and devices

