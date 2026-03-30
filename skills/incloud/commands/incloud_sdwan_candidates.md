## incloud sdwan candidates

Find candidate devices for SD-WAN networks

```
incloud sdwan candidates [flags]
```

### Examples

```
  # Find hub candidates
  incloud sdwan candidates --role hub

  # Find spoke candidates, filter by name or serial number
  incloud sdwan candidates --role spoke --name-or-sn ER805

  # Exclude specific devices
  incloud sdwan candidates --role hub --exclude <id1> --exclude <id2>
```

### Options

```
      --exclude stringArray   Device IDs to exclude (repeatable)
  -f, --fields strings        Fields to return and display
  -h, --help                  help for candidates
      --limit int             Number of items per page (default 20)
      --name-or-sn string     Filter by device name or serial number
      --network-id string     Filter by network ID
      --page int              Page number (starting from 1) (default 1)
      --role string           Device role: hub or spoke (required)
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

* [incloud sdwan](incloud_sdwan.md)	 - Manage SD-WAN networks and devices

