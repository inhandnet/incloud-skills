## incloud device config get

Get device configuration

### Synopsis

Get the device configuration. By default returns the fully merged configuration
(combining default, group, and individual layers). Use --layer to view specific
configuration layers instead (actual, target, pending, group, individual).

```
incloud device config get <device-id> [flags]
```

### Examples

```
  # Get merged configuration (default)
  incloud device config get 507f1f77bcf86cd799439011

  # Get only the actual layer
  incloud device config get 507f1f77bcf86cd799439011 --layer actual

  # Get actual and pending layers
  incloud device config get 507f1f77bcf86cd799439011 --layer actual --layer pending

  # YAML output
  incloud device config get 507f1f77bcf86cd799439011 -o yaml

  # Get only the DNS config section
  incloud device config get 507f1f77bcf86cd799439011 --key dns
```

### Options

```
  -h, --help                help for get
      --key string          Return only the specified config key (e.g. dns, wan, cellular)
      --layer stringArray   Config layers to return: actual, target, pending, group, individual (can be repeated)
      --module string       Module name (defaults to 'default' on the server)
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

* [incloud device config](incloud_device_config.md)	 - Device configuration management

