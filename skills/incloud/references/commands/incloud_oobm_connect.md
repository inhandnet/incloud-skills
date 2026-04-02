## incloud oobm connect

Connect an OOBM resource

### Synopsis

Connect an Out-of-Band Management resource to establish remote access tunnels.

Without --service, all services defined on the resource are connected.
Use --service to connect only specific services (protocol:port[:usage] format).

The response includes tunnelId and token. Use 'incloud tunnel forward' to
forward the tunnel to a local port for direct ssh/telnet/curl access.

```
incloud oobm connect <id> [flags]
```

### Examples

```
  # Connect all services on the resource
  incloud oobm connect 507f1f77bcf86cd799439011

  # Connect only SSH service
  incloud oobm connect 507f1f77bcf86cd799439011 --service ssh:22:cli

  # Forward to local port for direct access
  incloud oobm connect 507f1f77bcf86cd799439011 --service ssh:22:cli -o json
  incloud tunnel forward <tunnelId> --token <token> --port 2222
  ssh root@localhost -p 2222
```

### Options

```
  -h, --help                  help for connect
      --service stringArray   Service in protocol:port[:usage] format (omit to connect all)
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

* [incloud oobm](incloud_oobm.md)	 - Manage Out-of-Band Management resources

