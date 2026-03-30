## incloud device import

Bulk import devices from a file

### Synopsis

Bulk import devices from a CSV or Excel (.xlsx) file.

The file must contain a header row with the following columns:
  name          Device name (required)
  serialNumber  Serial number (required, alphanumeric only)
  mac           MAC address (optional, e.g. AA:BB:CC:DD:EE:FF)
  imei          IMEI number (optional)

CSV files are automatically converted to Excel format before upload.

The import is asynchronous: the file is uploaded and validated, then you
confirm the import, and it runs in the background. By default the command
waits for the import to complete and displays the result.

```
incloud device import <file> [flags]
```

### Examples

```
  # Import devices from a CSV file
  incloud device import devices.csv

  # Import from Excel
  incloud device import devices.xlsx

  # Import and assign devices to a group
  incloud device import devices.csv --group 507f1f77bcf86cd799439011

  # Import devices under a sub-organization
  incloud device import devices.csv --org 507f1f77bcf86cd799439022

  # Skip confirmation prompt
  incloud device import devices.csv -y

  # Don't wait for completion
  incloud device import devices.csv -y --no-wait
```

### Options

```
      --group string   Assign imported devices to a group (use 'incloud device group list' to find IDs)
  -h, --help           help for import
      --no-wait        Don't wait for import to complete
      --org string     Create devices under a sub-organization (use 'incloud org list' to find IDs)
  -y, --yes            Skip confirmation prompt
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

