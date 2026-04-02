## incloud oobm create

Create an OOBM resource

### Synopsis

Create a new Out-of-Band Management resource to establish remote access tunnels.

Supported protocols: http, https, tcp, telnet, ssh
Service usage types: web (browser-based), cli (command-line)

Service format: protocol:port[:usage]
  When usage is omitted, the server determines the default based on protocol.

```
incloud oobm create [flags]
```

### Examples

```
  # Create a resource with SSH access
  incloud oobm create \
    --device-id 507f1f77bcf86cd799439011 \
    --name "Router SSH" \
    --client-ip 192.168.1.1 \
    --service ssh:22:cli

  # Create with multiple services
  incloud oobm create \
    --device-id 507f1f77bcf86cd799439011 \
    --name "Router Web+SSH" \
    --client-ip 192.168.1.1 \
    --service https:443 \
    --service ssh:22:web \
    --idle-time 600 --conn-time 7200
```

### Options

```
      --client-ip string      Client IP address (required)
      --conn-time int         Connection timeout in seconds (3600-604800) (default 3600)
      --device-id string      Device ID (required; use 'incloud device list' to find IDs)
  -h, --help                  help for create
      --idle-time int         Idle timeout in seconds (60-3600) (default 300)
      --name string           Resource name (required, 1-32 chars)
      --service stringArray   Service in protocol:port[:usage] format (required, can be repeated)
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

