## incloud device datausage daily

Show daily data usage

### Synopsis

Display daily data usage (traffic) for a device. Defaults to the current month if no month is specified.

```
incloud device datausage daily <device-id> [flags]
```

### Examples

```
  # Daily data usage for current month
  incloud device datausage daily 507f1f77bcf86cd799439011

  # Specify month
  incloud device datausage daily 507f1f77bcf86cd799439011 --month 2024-03

  # Filter by traffic type
  incloud device datausage daily 507f1f77bcf86cd799439011 --type all
```

### Options

```
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for daily
      --month string     Month to query (YYYY-MM, e.g. 2024-03)
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

