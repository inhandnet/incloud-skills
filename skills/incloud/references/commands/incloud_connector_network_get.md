## incloud connector network get

Get connector network details

```
incloud connector network get <id> [flags]
```

### Examples

```
  # Get network details
  incloud connector network get 66827b3ccfb1842140f4222f

  # With live connected counts
  incloud connector network get 66827b3ccfb1842140f4222f --expand counts
```

### Options

```
      --expand strings   Expand related data (e.g. "counts" for live connected counts)
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

* [incloud connector network](incloud_connector_network.md)	 - Manage connector networks

