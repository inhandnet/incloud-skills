## incloud connector endpoint delete

Delete endpoints from a connector network

```
incloud connector endpoint delete <network-id> <endpoint-id> [endpoint-id...] [flags]
```

### Examples

```
  # Delete single endpoint
  incloud connector endpoint delete 66827b3ccfb1842140f4222f ep123

  # Delete multiple endpoints
  incloud connector endpoint delete 66827b3ccfb1842140f4222f ep1 ep2 ep3

  # Skip confirmation
  incloud connector endpoint delete 66827b3ccfb1842140f4222f ep123 -y
```

### Options

```
  -h, --help   help for delete
  -y, --yes    Skip confirmation prompt
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

* [incloud connector endpoint](incloud_connector_endpoint.md)	 - Manage endpoints in connector networks

