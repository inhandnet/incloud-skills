## incloud device datausage hourly

Show hourly data usage

### Synopsis

Display hourly data usage (traffic) for a device. Defaults to today if no time range is specified.

```
incloud device datausage hourly <device-id> [flags]
```

### Examples

```
  # Hourly data usage for today (default)
  incloud device datausage hourly 507f1f77bcf86cd799439011

  # Filter by time range
  incloud device datausage hourly 507f1f77bcf86cd799439011 --after 2024-03-01T00:00:00Z --before 2024-03-02T00:00:00Z

  # Filter by traffic type
  incloud device datausage hourly 507f1f77bcf86cd799439011 --type all

  # Table output with selected fields
  incloud device datausage hourly 507f1f77bcf86cd799439011 -o table -f time -f tx -f rx
```

### Options

```
      --after string     Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string    End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for hourly
      --type string      Traffic type: cellular (default), wired, wireless, sim, esim, all, etc.
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

* [incloud device datausage](incloud_device_datausage.md)	 - Device data usage statistics

