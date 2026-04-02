## incloud device antenna

Antenna signal data

### Synopsis

Display per-antenna signal metrics (RSRP, RSRQ, SINR, ssRsrp, ssRsrq, ssSinr) with GPS correlation.

```
incloud device antenna <device-id> [flags]
```

### Examples

```
  # Show antenna signal data for a device
  incloud device antenna 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-01-02T00:00:00Z

  # Table output with selected fields
  incloud device antenna 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-01-02T00:00:00Z -o table -f time -f antenna -f rsrp
```

### Options

```
      --after string     Start time (ISO 8601, e.g. 2024-01-01T00:00:00Z) [required]
      --before string    End time (ISO 8601, e.g. 2024-01-02T00:00:00Z) [required]
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for antenna
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

* [incloud device](incloud_device.md)	 - Manage devices

