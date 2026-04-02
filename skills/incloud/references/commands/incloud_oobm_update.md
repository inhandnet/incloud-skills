## incloud oobm update

Update an OOBM resource

### Synopsis

Update an Out-of-Band Management resource.

All fields are required because the API performs a full replacement.
Service format: protocol:port[:usage]

```
incloud oobm update <id> [flags]
```

### Examples

```
  # Update a resource (all fields required — full replacement)
  incloud oobm update 507f1f77bcf86cd799439011 \
    --device-id 607f1f77bcf86cd799439022 \
    --name "Router SSH" \
    --client-ip 192.168.1.1 \
    --service ssh:22:cli

  # Update with multiple services
  incloud oobm update 507f1f77bcf86cd799439011 \
    --device-id 607f1f77bcf86cd799439022 \
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
  -h, --help                  help for update
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

