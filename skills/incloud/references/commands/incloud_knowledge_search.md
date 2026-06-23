## incloud knowledge search

Search the knowledge base

### Synopsis

Search device documentation and return matching results.

```
incloud knowledge search <query> [flags]
```

### Examples

```
  # Search for configuration guides
  incloud knowledge search "how to configure VPN"

  # Filter by device model
  incloud knowledge search "factory reset" --model IR915L

  # Enable query rewriting for better results
  incloud knowledge search "VPN setup" --rewrite

  # Limit results and output as JSON
  incloud knowledge search "firewall rules" --limit 3 -o json
```

### Options

```
  -h, --help           help for search
      --limit int      Max number of results (1-20) (default 6)
      --model string   Filter by device model (e.g. IR915L)
      --rewrite        Enable LLM query rewriting
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

* [incloud knowledge](incloud_knowledge.md)	 - Search and query the knowledge base

