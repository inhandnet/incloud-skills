## incloud license history

View license operation history

### Synopsis

View the operation log for a specific license, including attach, detach, upgrade, align, and expire events.

```
incloud license history <license-id> [flags]
```

### Examples

```
  # View operation history
  incloud license history YFE5QYOTHKHBMSX

  # YAML output
  incloud license history YFE5QYOTHKHBMSX -o yaml

  # Filter with jq
  incloud license history YFE5QYOTHKHBMSX --jq '.[] | {type, createdAt}'
```

### Options

```
  -h, --help   help for history
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

* [incloud license](incloud_license.md)	 - Manage licenses

