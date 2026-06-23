## incloud touch client update

Update a touch client

### Synopsis

Update a remote access client's name, IP address, or serial configuration.

```
incloud touch client update <client-id> [flags]
```

### Examples

```
  # Update name
  incloud touch client update 507f1f77bcf86cd799439011 --name new-name

  # Update IP address
  incloud touch client update 507f1f77bcf86cd799439011 --ip 192.168.1.200
```

### Options

```
  -h, --help            help for update
      --ip string       New IP address for ETHERNET type
      --name string     New client name (1-128 chars)
      --serial string   New serial configuration as JSON
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

* [incloud touch client](incloud_touch_client.md)	 - Manage touch clients

