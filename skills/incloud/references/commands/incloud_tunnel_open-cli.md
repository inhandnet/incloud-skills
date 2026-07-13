## incloud tunnel open-cli

Open a CLI tunnel for a device

### Synopsis

Open a remote CLI access tunnel for a device.

By default, opens the web-based terminal in the browser.
Use --forward to start a local TCP port forward instead.
Use 'incloud tunnel close <tunnel-id>' to close the tunnel when done.

```
incloud tunnel open-cli <device-id> [flags]
```

### Examples

```
  # Open a CLI tunnel in the browser
  incloud tunnel open-cli 507f1f77bcf86cd799439011

  # Forward to a local port for ssh/telnet access
  incloud tunnel open-cli 507f1f77bcf86cd799439011 --forward
  incloud tunnel open-cli 507f1f77bcf86cd799439011 --forward --port 2222

  # Just create the tunnel without opening anything
  incloud tunnel open-cli 507f1f77bcf86cd799439011 --no-open
```

### Options

```
      --forward          Forward tunnel to a local port instead of opening browser
  -h, --help             help for open-cli
      --ngrok-port int   Ngrok TCP proxy port (default 4443)
      --no-open          Do not open the URL in the browser
  -p, --port int         Local port for --forward (0 = random)
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

