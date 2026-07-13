## incloud pos marked-clients

List POS-marked clients on a device

### Synopsis

List clients on a specific device that carry a POS priority level (priority/bypass).

```
incloud pos marked-clients <device-id> [flags]
```

### Examples

```
  # All marked clients on a device
  incloud pos marked-clients 507f1f77bcf86cd799439011

  # Only bypassed clients
  incloud pos marked-clients 507f1f77bcf86cd799439011 --level bypass
```

### Options

```
  -h, --help           help for marked-clients
      --level string   Filter by level (priority/bypass)
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

* [incloud pos](incloud_pos.md)	 - Manage POS Ready traffic prioritization

