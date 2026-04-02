## incloud org self

Show current organization

```
incloud org self [flags]
```

### Examples

```
  # Show current organization
  incloud org self

  # Table output
  incloud org self -o table

  # YAML output
  incloud org self -o yaml
```

### Options

```
  -h, --help   help for self
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

