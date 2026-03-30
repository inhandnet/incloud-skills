## incloud tunnel open-web

Open a Web UI tunnel for a device

### Synopsis

Open a remote Web UI access tunnel for a device.

Returns an HTTPS URL that provides browser-based access to the device's web interface.
Automatically opens the URL in the default browser (use --no-open to disable).
Use 'incloud tunnel close <tunnel-id>' to close the tunnel when done.

```
incloud tunnel open-web <device-id> [flags]
```

### Examples

```
  # Open a web tunnel and launch browser
  incloud tunnel open-web 507f1f77bcf86cd799439011

  # Open without launching browser
  incloud tunnel open-web 507f1f77bcf86cd799439011 --no-open
```

### Options

```
  -h, --help      help for open-web
      --no-open   Do not open the URL in the browser
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

* [incloud tunnel](incloud_tunnel.md)	 - Manage remote access tunnels

