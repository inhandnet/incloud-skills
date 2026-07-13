## incloud connector account download-ovpn

Download OpenVPN configuration file for an account

```
incloud connector account download-ovpn <account-id> [flags]
```

### Examples

```
  # Download to current directory
  incloud connector account download-ovpn <account-id>

  # Specify output path
  incloud connector account download-ovpn <account-id> --output-file /tmp/client.ovpn
```

### Options

```
  -h, --help                 help for download-ovpn
      --output-file string   Output file path (default: <account-id>.ovpn)
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

* [incloud connector account](incloud_connector_account.md)	 - Manage connector accounts (VPN users)

