## incloud device location set

Set device location (pin)

### Synopsis

Set a fixed location for a device. This pins the location and disables automatic positioning.

```
incloud device location set <device-id> [flags]
```

### Examples

```
  # Set device location
  incloud device location set 507f1f77bcf86cd799439011 \
    --longitude 119.26 --latitude 30.92 --address "Hangzhou, China"
```

### Options

```
      --address string    Address description (required)
  -h, --help              help for set
      --latitude float    Latitude coordinate (required)
      --longitude float   Longitude coordinate (required)
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

* [incloud device location](incloud_device_location.md)	 - Manage device location

