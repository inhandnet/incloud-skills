## incloud device log diagnostic

Download and decrypt diagnostic log from device

### Synopsis

Download diagnostic log from a device, automatically decrypt it, and save as a .tar.gz file.
The device will be asked to collect and upload the log, which may take up to a few minutes
depending on network conditions.

```
incloud device log diagnostic <device-id> [flags]
```

### Examples

```
  # Download to an auto-generated temp file
  incloud device log diagnostic 507f1f77bcf86cd799439011

  # Save to a specific file
  incloud device log diagnostic 507f1f77bcf86cd799439011 --file diag.tar.gz
```

### Options

```
      --file string   Output file path (default: auto-generated temp file)
  -h, --help          help for diagnostic
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

* [incloud device log](incloud_device_log.md)	 - Device logs

