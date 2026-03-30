## incloud device datausage monthly

Show monthly data usage

### Synopsis

Display monthly data usage (traffic) for a device. Defaults to the current year if no year is specified.

```
incloud device datausage monthly <device-id> [flags]
```

### Examples

```
  # Monthly data usage for current year
  incloud device datausage monthly 507f1f77bcf86cd799439011

  # Specify year
  incloud device datausage monthly 507f1f77bcf86cd799439011 --year 2024

  # Filter by traffic type
  incloud device datausage monthly 507f1f77bcf86cd799439011 --type all
```

### Options

```
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for monthly
      --type string      Traffic type: cellular (default), wired, wireless, sim, esim, all, etc.
      --year string      Year to query (YYYY, e.g. 2024)
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

