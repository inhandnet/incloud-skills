## incloud firmware status

List device firmware upgrade status

### Synopsis

List device firmware and OTA module upgrade status with optional filtering.

```
incloud firmware status [flags]
```

### Examples

```
  # List all devices' firmware status
  incloud firmware status

  # Filter by product
  incloud firmware status --product ER805

  # Filter by upgrade status
  incloud firmware status --status queued

  # Show all OTA modules for a specific device
  incloud firmware status --device 6989ad34a7455f3f0bf9dce2

  # Show a specific module for a device
  incloud firmware status --device 6989ad34a7455f3f0bf9dce2 --module modem

  # Output as JSON
  incloud firmware status -o json
```

### Options

```
      --device string    Filter by device ID (shows all OTA modules for the device)
  -f, --fields strings   Fields to return and display
  -h, --help             help for status
      --limit int        Number of items per page (default 20)
      --module string    Filter by module name
      --page int         Page number (starting from 1) (default 1)
      --product string   Filter by product name
      --sort string      Sort order (e.g. "createdAt,desc")
      --status string    Filter by status (up_to_date|new_firmware_available|queued|in_progress)
      --version string   Filter by current firmware version
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

* [incloud firmware](incloud_firmware.md)	 - Manage firmwares

