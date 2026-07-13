## incloud sdwan network update

Update an SD-WAN network

### Synopsis

Update an SD-WAN network. Fetches the current state first and merges your changes,
so you only need to specify the fields you want to change.

When --hub or --spoke is specified, the device list is replaced entirely.
Existing device configurations (subnets, tunnel ports, etc.) are preserved
for devices that remain in the network.

```
incloud sdwan network update <id> [flags]
```

### Examples

```
  # Update name
  incloud sdwan network update <id> --name new-name

  # Change tunnel mode
  incloud sdwan network update <id> --tunnel-mode symmetric

  # Replace hub devices
  incloud sdwan network update <id> --hub new-hub-id

  # Add spokes (replaces existing spoke list)
  incloud sdwan network update <id> --spoke spoke1 --spoke spoke2
```

### Options

```
      --force-all-traffic    Force send all traffic through tunnels
  -h, --help                 help for update
      --hub stringArray      Hub device ID (repeatable, replaces existing hubs)
      --name string          Network name (max 64 chars)
      --spoke stringArray    Spoke device ID (repeatable, replaces existing spokes)
      --tunnel-mode string   Tunnel creation mode: mesh or symmetric
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

