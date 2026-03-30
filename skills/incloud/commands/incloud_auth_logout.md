## incloud auth logout

Clear authentication tokens

### Synopsis

Remove tokens from a context. Defaults to current context.

```
incloud auth logout [context] [flags]
```

### Options

```
  -h, --help   help for logout
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

* [incloud auth](incloud_auth.md)	 - Manage authentication

