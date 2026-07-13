## incloud auth login

Login via browser OAuth flow

```
incloud auth login [flags]
```

### Examples

```
  # Quick start — zero config, logs into global region
  incloud login

  # Login to China region
  incloud login --host cn

  # Use a named context for multi-environment setups
  incloud login --context prod --host global
  incloud login --context cn --host cn

  # Custom domain also works
  incloud login --host inhandcloud.com
```

### Options

```
      --client-id string   OAuth client ID (auto-detected from host if omitted)
      --context string     Context name to create/update (default "default")
  -h, --help               help for login
      --host string        Platform host or region: "global", "cn", or a custom domain (default "global")
      --port int           Local callback server port (default 18920)
      --timeout duration   Timeout waiting for browser callback (default 2m0s)
```

### Options inherited from parent commands

```
      --debug           Enable debug output (env: INCLOUD_DEBUG)
      --jq string       Filter JSON output using a jq expression (implies -o json)
  -o, --output string   Output format: json, table, yaml (default: table for TTY, json otherwise)
      --tenant string   Switch organization context by ID (env: INCLOUD_TENANT)
```

### SEE ALSO

* [incloud auth](incloud_auth.md)	 - Manage authentication

