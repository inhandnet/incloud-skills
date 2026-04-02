## incloud connector network create

Create a connector network

```
incloud connector network create [flags]
```

### Examples

```
  # Create with name only
  incloud connector network create --name my-vpn

  # With subnet and description
  incloud connector network create --name my-vpn --subnet 10.32.0.0/12 --description "Office VPN"
```

### Options

```
      --description string   Network description (max 256 chars)
  -h, --help                 help for create
      --name string          Network name (required, max 128 chars)
      --subnet string        Network subnet (e.g. 10.32.0.0/12)
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

* [incloud connector network](incloud_connector_network.md)	 - Manage connector networks

