## incloud license detach

Detach a license from its device

### Synopsis

Detach a license from the device it is currently attached to.

```
incloud license detach <license-id> [flags]
```

### Examples

```
  # Detach a license (will prompt for confirmation)
  incloud license detach 64a1b2c3d4e5f6a7b8c9d0e1

  # Skip confirmation
  incloud license detach 64a1b2c3d4e5f6a7b8c9d0e1 --yes
```

### Options

```
  -h, --help   help for detach
  -y, --yes    Skip confirmation prompt
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

* [incloud license](incloud_license.md)	 - Manage licenses

