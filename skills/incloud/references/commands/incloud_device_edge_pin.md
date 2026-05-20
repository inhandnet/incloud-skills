## incloud device edge pin

Pin a device to a specific project version

### Synopsis

Pin an edge device to a specific project version so it does not follow group-wide deployments.
Use --unpin to remove the pin and let the device follow group deployments again.

```
incloud device edge pin <device-id> [flags]
```

### Examples

```
  # Pin device to version 0.1.3
  incloud device edge pin 507f1f77bcf86cd799439011 --version 0.1.3

  # Unpin device (follow group deployments)
  incloud device edge pin 507f1f77bcf86cd799439011 --unpin
```

### Options

```
  -h, --help             help for pin
      --unpin            Remove pin and follow group deployments
      --version string   Project version to pin to
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

* [incloud device edge](incloud_device_edge.md)	 - Manage edge device properties

