## incloud device edge list

List edge devices by IDs

### Synopsis

Retrieve edge-specific properties for one or more devices by their IDs.

```
incloud device edge list <id>[,<id2>,...] [flags]
```

### Examples

```
  # Get edge info for a single device
  incloud device edge list 507f1f77bcf86cd799439011

  # Get edge info for multiple devices
  incloud device edge list 507f1f77bcf86cd799439011,653b1ff2a84e171614d88695
```

### Options

```
  -h, --help   help for list
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

* [incloud device edge](incloud_device_edge.md)	 - Manage edge device properties

