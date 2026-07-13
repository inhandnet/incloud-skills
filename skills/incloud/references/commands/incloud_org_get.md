## incloud org get

Get organization details

```
incloud org get <id> [flags]
```

### Examples

```
  # Get organization by ID
  incloud org get 61259f8f4be3e571fcfa4d75

  # With specific fields
  incloud org get 61259f8f4be3e571fcfa4d75 -f name -f email -f userCount

  # YAML output
  incloud org get 61259f8f4be3e571fcfa4d75 -o yaml
```

### Options

```
      --expand strings   Expand related resources. Supported: parent
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

* [incloud org](incloud_org.md)	 - Manage organizations

