## incloud connector network stats

Show connector statistics overview

```
incloud connector network stats [flags]
```

### Examples

```
  # Show total counts of networks, accounts, devices, endpoints
  incloud connector network stats
```

### Options

```
  -h, --help   help for stats
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

