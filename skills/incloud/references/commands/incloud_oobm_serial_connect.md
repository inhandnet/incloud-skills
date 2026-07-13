## incloud oobm serial connect

Connect an OOBM serial port

### Synopsis

Connect an OOBM serial port to establish a remote console tunnel.

On success, prints the connection URL and credentials. For CLI usage,
the URL is an SSH command you can run directly.

```
incloud oobm serial connect <id> [flags]
```

### Examples

```
  # Connect a serial port
  incloud oobm serial connect 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for connect
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

* [incloud oobm serial](incloud_oobm_serial.md)	 - Manage OOBM serial port configurations

