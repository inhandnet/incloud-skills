## incloud device export

Export devices to CSV

### Synopsis

Export devices as a server-generated CSV file. Supports filtering by device attributes.

```
incloud device export [flags]
```

### Examples

```
  # Export all devices to stdout
  incloud device export

  # Export to a file
  incloud device export --file devices.csv

  # Export online devices only
  incloud device export --online true --file online.csv

  # Filter by product and search
  incloud device export --product IR915L -q "router"

  # Export devices with specific firmware
  incloud device export --firmware V1.0.0 --file fw100.csv

  # Export devices with pending config
  incloud device export --config-status PENDING

  # Pipe to other commands
  incloud device export | head -20
```

### Options

```
      --config-status stringArray   Filter by config status: SYNCED/PENDING/SUSPENDED/ERROR/NONE (can be repeated)
      --file string                 Write output to file instead of stdout
      --firmware string             Filter by firmware version (fuzzy match)
      --group stringArray           Filter by device group ID (can be repeated)
  -h, --help                        help for export
      --ip string                   Filter by IP address (fuzzy match)
      --mac string                  Filter by MAC address (fuzzy match)
      --name string                 Filter by device name (fuzzy match)
      --online string               Filter by online status (true/false)
      --product stringArray         Filter by product (can be repeated)
  -q, --query string                Search by name or serial number
      --serial-number string        Filter by serial number (fuzzy match)
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

