## incloud tunnel forward

Forward a tunnel to a local port

### Synopsis

Forward an existing tunnel to a local TCP port.

Connects to the tunnel via TLS and starts a local TCP listener.
Connect to the local port with ssh, telnet, curl, or any TCP client.

Works with tunnels created by any command: open-cli, open-web, oobm connect, etc.

Press Ctrl+C to stop.

```
incloud tunnel forward <tunnel-id> [flags]
```

### Examples

```
  # Forward a tunnel to a random local port
  incloud tunnel forward nhcqr3rzpxqfiviqdu3c7x4o

  # Forward to a specific port
  incloud tunnel forward nhcqr3rzpxqfiviqdu3c7x4o --port 2222

  # Forward with token (required when server has JWT enabled)
  incloud tunnel forward nhcqr3rzpxqfiviqdu3c7x4o --token <jwt>

  # Use with OOBM: connect a resource, then forward its tunnel
  incloud oobm connect <resource-id> --service ssh:22:cli -o json
  incloud tunnel forward <tunnelId-from-output> --token <token-from-output> --port 2222
  ssh root@localhost -p 2222
```

### Options

```
  -h, --help             help for forward
      --ngrok-port int   Ngrok TCP proxy port (default 4443)
  -p, --port int         Local port to listen on (0 = random)
      --token string     Auth token for the tunnel (from tunnel creation response)
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

* [incloud tunnel](incloud_tunnel.md)	 - Manage remote access tunnels

