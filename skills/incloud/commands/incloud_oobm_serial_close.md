## incloud oobm serial close

Close an OOBM serial port connection

```
incloud oobm serial close <id> [flags]
```

### Examples

```
  # Close a serial port connection
  incloud oobm serial close 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for close
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

