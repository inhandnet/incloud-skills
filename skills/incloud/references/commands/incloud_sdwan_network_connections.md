## incloud sdwan network connections

List connections in an SD-WAN network

```
incloud sdwan network connections <networkId> [flags]
```

### Examples

```
  # List all connections
  incloud sdwan network connections <id>

  # Filter by device name
  incloud sdwan network connections <id> --name ER805
```

### Options

```
  -f, --fields strings   Fields to return and display
  -h, --help             help for connections
      --limit int        Number of items per page (default 20)
      --name string      Filter by device name
      --page int         Page number (starting from 1) (default 1)
      --sort string      Sort order (e.g. "createdAt,desc")
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

