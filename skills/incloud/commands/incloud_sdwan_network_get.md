## incloud sdwan network get

Get SD-WAN network details

```
incloud sdwan network get <id> [flags]
```

### Examples

```
  # Get network details (includes tunnel counts by default)
  incloud sdwan network get <id>

  # Without tunnel counts
  incloud sdwan network get <id> --expand ""
```

### Options

```
      --expand strings   Expand related data (e.g. "tunnels" for tunnel counts) (default [tunnels])
  -f, --fields strings   Fields to return and display
  -h, --help             help for get
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

