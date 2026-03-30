## incloud connector endpoint create

Create an endpoint in a connector network

```
incloud connector endpoint create <network-id> [flags]
```

### Examples

```
  # Create an endpoint
  incloud connector endpoint create 66827b3ccfb1842140f4222f --device-id abc123 --name my-ep --lan-ip 192.168.1.0/24

  # With optional VIP
  incloud connector endpoint create 66827b3ccfb1842140f4222f --device-id abc123 --name my-ep --lan-ip 192.168.1.0/24 --vip 10.32.0.5
```

### Options

```
      --device-id string   Device ID (required; use 'incloud connector device list <network-id>' to find IDs)
  -h, --help               help for create
      --lan-ip string      LAN IP or subnet (required, e.g. 192.168.1.0/24)
      --name string        Endpoint name (required)
      --vip string         Virtual IP address
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

