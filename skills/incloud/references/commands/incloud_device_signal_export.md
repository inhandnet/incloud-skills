## incloud device signal export

Export signal data to Excel

### Synopsis

Export signal quality data as a server-generated Excel file.

```
incloud device signal export <device-id> [flags]
```

### Examples

```
  # Export signal data to file
  incloud device signal export 507f1f77bcf86cd799439011 --file signal.xlsx

  # Export with time range
  incloud device signal export 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-01-07T00:00:00Z --file signal.xlsx

  # Export to stdout (pipe to file)
  incloud device signal export 507f1f77bcf86cd799439011 > signal.xlsx
```

### Options

```
      --after string    Start time (ISO 8601, e.g. 2024-01-01T00:00:00Z)
      --before string   End time (ISO 8601, e.g. 2024-01-02T00:00:00Z)
      --file string     Write output to file instead of stdout
  -h, --help            help for export
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

* [incloud device signal](incloud_device_signal.md)	 - Device signal quality

