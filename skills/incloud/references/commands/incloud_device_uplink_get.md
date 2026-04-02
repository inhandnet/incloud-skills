## incloud device uplink get

Get uplink details

### Synopsis

Get detailed information for a specific uplink by its ID.

```
incloud device uplink get <uplink-id> [flags]
```

### Examples

```
  # Get uplink details
  incloud device uplink get 69b27e3e6e65fb572c20fab4

  # Table output
  incloud device uplink get 69b27e3e6e65fb572c20fab4 -o table
```

### Options

```
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for get
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

* [incloud device uplink](incloud_device_uplink.md)	 - Show device uplinks

