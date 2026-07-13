## incloud device datausage

Device data usage statistics

### Synopsis

View device data usage (traffic) statistics at hourly, daily, or monthly granularity.

```
incloud device datausage [device-id] [flags]
```

### Examples

```
  # Daily data usage (default interval)
  incloud device datausage 507f1f77bcf86cd799439011

  # Hourly data usage
  incloud device datausage 507f1f77bcf86cd799439011 --interval hourly

  # Monthly data usage for a specific year
  incloud device datausage 507f1f77bcf86cd799439011 --interval monthly --year 2024
```

### Options

```
      --after string      Start time (e.g. 2025-01-01, 2025-01-01T08:00:00, 2025-01-01T00:00:00Z)
      --before string     End time (e.g. 2025-01-31, 2025-01-31T08:00:00, 2025-01-31T23:59:59Z)
  -f, --fields strings    Fields to display in table mode
  -h, --help              help for datausage
      --interval string   Granularity: hourly, daily, monthly (default "daily")
      --month string      Month to query (YYYY-MM, e.g. 2024-03)
      --type string       Traffic type: cellular (default), wired, wireless, sim, esim, all, etc.
      --year string       Year to query (YYYY, e.g. 2024)
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
* [incloud device datausage daily](incloud_device_datausage_daily.md)	 - Show daily data usage
* [incloud device datausage hourly](incloud_device_datausage_hourly.md)	 - Show hourly data usage
* [incloud device datausage list](incloud_device_datausage_list.md)	 - List data usage per device
* [incloud device datausage monthly](incloud_device_datausage_monthly.md)	 - Show monthly data usage

