## incloud tunnel

Manage remote access tunnels

### Synopsis

Open and close remote access tunnels (Web UI / CLI) for devices.

### Options

```
  -h, --help   help for tunnel
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

* [incloud](incloud.md)	 - InCloud Platform CLI
* [incloud tunnel cli](incloud_tunnel_cli.md)	 - Run a device CLI command through a tunnel
* [incloud tunnel close](incloud_tunnel_close.md)	 - Close a tunnel
* [incloud tunnel forward](incloud_tunnel_forward.md)	 - Forward a tunnel to a local port
* [incloud tunnel get](incloud_tunnel_get.md)	 - Get tunnel details
* [incloud tunnel logs](incloud_tunnel_logs.md)	 - List tunnel connection logs
* [incloud tunnel open-cli](incloud_tunnel_open-cli.md)	 - Open a CLI tunnel for a device
* [incloud tunnel open-web](incloud_tunnel_open-web.md)	 - Open a Web UI tunnel for a device

