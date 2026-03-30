## incloud sdwan network create

Create an SD-WAN network

```
incloud sdwan network create [flags]
```

### Examples

```
  # Create a hub-spoke network
  incloud sdwan network create --name my-sdwan --hub <deviceId>

  # Multiple hubs and spokes
  incloud sdwan network create --name office-vpn \
    --hub hub1-id --hub hub2-id --spoke spoke1-id --spoke spoke2-id

  # Symmetric tunnel mode with custom CIDR
  incloud sdwan network create --name site-vpn \
    --tunnel-mode symmetric --hub hub-id \
    --loopback-cidr 10.0.0.0/17 --tunnel-cidr 10.0.128.0/17
```

### Options

```
      --force-all-traffic      Force send all traffic through tunnels
  -h, --help                   help for create
      --hub stringArray        Hub device ID (required, repeatable, max 5; use 'incloud sdwan candidates --role hub' to find IDs)
      --loopback-cidr string   Loopback address CIDR pool (default "10.113.0.0/17")
      --name string            Network name (required, max 64 chars)
      --spoke stringArray      Spoke device ID (repeatable, max 500; use 'incloud sdwan candidates --role spoke' to find IDs)
      --tunnel-cidr string     Tunnel address CIDR pool (default "10.113.128.0/17")
      --tunnel-mode string     Tunnel creation mode: mesh (default) or symmetric
      --type string            Network type (default "hub_spoke")
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

* [incloud sdwan network](incloud_sdwan_network.md)	 - Manage SD-WAN networks

