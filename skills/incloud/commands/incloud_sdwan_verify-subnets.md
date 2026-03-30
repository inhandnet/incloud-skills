## incloud sdwan verify-subnets

Verify subnets for conflicts

```
incloud sdwan verify-subnets <subnet> [subnet...] [flags]
```

### Examples

```
  # Check if subnets conflict with each other
  incloud sdwan verify-subnets 10.0.0.0/24 10.0.0.0/16 192.168.1.0/24
```

### Options

```
  -h, --help   help for verify-subnets
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

