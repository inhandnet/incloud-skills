## incloud oobm close

Close an OOBM connection

### Synopsis

Close an Out-of-Band Management connection to tear down remote access tunnels.

Without --service, all services on the resource are closed.
Use --service to close only specific services (protocol:port[:usage] format).

```
incloud oobm close <id> [flags]
```

### Examples

```
  # Close all services on the resource
  incloud oobm close 507f1f77bcf86cd799439011

  # Close only SSH service
  incloud oobm close 507f1f77bcf86cd799439011 --service ssh:22:cli
```

### Options

```
  -h, --help                  help for close
      --service stringArray   Service in protocol:port[:usage] format (omit to close all)
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

* [incloud oobm](incloud_oobm.md)	 - Manage Out-of-Band Management resources

