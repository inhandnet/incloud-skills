## incloud knowledge ask

Ask a question to the knowledge base

### Synopsis

Ask a question and get an AI-generated answer based on device documentation.

```
incloud knowledge ask <question> [flags]
```

### Examples

```
  # Ask a question
  incloud knowledge ask "How do I set up a VPN tunnel on IR915L?"

  # Specify device model for better context
  incloud knowledge ask "How to configure SNMP?" --model IR305

  # Get raw JSON output
  incloud knowledge ask "What is the default IP address?" -o json
```

### Options

```
  -h, --help           help for ask
      --model string   Filter by device model (e.g. IR915L)
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

