## incloud connector endpoint update

Update an endpoint in a connector network

```
incloud connector endpoint update <network-id> <endpoint-id> [flags]
```

### Examples

```
  # Update endpoint name
  incloud connector endpoint update 66827b3ccfb1842140f4222f ep123 --name new-name

  # Update LAN IP
  incloud connector endpoint update 66827b3ccfb1842140f4222f ep123 --lan-ip 192.168.2.0/24

  # Update VIP
  incloud connector endpoint update 66827b3ccfb1842140f4222f ep123 --vip 10.32.0.10
```

### Options

```
  -h, --help            help for update
      --lan-ip string   LAN IP or subnet (e.g. 192.168.1.0/24)
      --name string     Endpoint name
      --vip string      Virtual IP address
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

