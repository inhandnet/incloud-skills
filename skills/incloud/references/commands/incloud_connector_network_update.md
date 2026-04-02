## incloud connector network update

Update a connector network

```
incloud connector network update <id> [flags]
```

### Examples

```
  # Update name
  incloud connector network update 66827b3ccfb1842140f4222f --name new-name

  # Update description
  incloud connector network update 66827b3ccfb1842140f4222f --description "Updated desc"
```

### Options

```
      --description string   Network description (max 256 chars)
  -h, --help                 help for update
      --name string          Network name (max 128 chars)
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

* [incloud connector network](incloud_connector_network.md)	 - Manage connector networks

