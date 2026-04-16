## incloud device datausage list

List data usage per device

### Synopsis

List aggregated data usage for all devices, broken down by interface type (sim, esim, wan, etc.).

```
incloud device datausage list [flags]
```

### Examples

```
  # List all devices' data usage
  incloud device datausage list

  # Filter by time range
  incloud device datausage list --after 2024-03-01 --before 2024-03-31

  # Filter by device groups
  incloud device datausage list --groups 507f1f77bcf86cd799439011

  # Table with custom fields
  incloud device datausage list -o table -f deviceId -f sim.total -f esim.total
```

### Options

```
      --after string     Start date (e.g. 2025-01-01)
      --before string    End date (e.g. 2025-01-31)
  -f, --fields strings   Fields to display in table mode
      --groups strings   Filter by device group IDs
  -h, --help             help for list
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

