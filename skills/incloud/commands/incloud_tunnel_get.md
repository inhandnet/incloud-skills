## incloud tunnel get

Get tunnel details

### Synopsis

Show details of an active tunnel, including protocol, token, and metadata.

```
incloud tunnel get <tunnel-id> [flags]
```

### Examples

```
  # Get tunnel details
  incloud tunnel get nhddruohqziaxu6nvvibfwwn

  # Get as JSON
  incloud tunnel get nhddruohqziaxu6nvvibfwwn -o json

  # Get specific fields
  incloud tunnel get nhddruohqziaxu6nvvibfwwn -o json --fields id,protocol,token
```

### Options

```
      --fields strings   Fields to display
  -h, --help             help for get
  -o, --output string    Output format: json, yaml
```

### Options inherited from parent commands

```
      --context string   Override active context (env: INCLOUD_CONTEXT)
      --debug            Enable debug output (env: INCLOUD_DEBUG)
      --jq string        Filter JSON output using a jq expression (implies -o json)
      --tenant string    Switch organization context by ID (env: INCLOUD_TENANT)
```

### SEE ALSO

* [incloud tunnel](incloud_tunnel.md)	 - Manage remote access tunnels

