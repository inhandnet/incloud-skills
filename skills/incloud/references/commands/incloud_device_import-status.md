## incloud device import-status

Check the status of a device import job

### Synopsis

Check the status of a device import job by its ID.

If the job is still running, use --wait to poll until completion.
Failed rows are shown with their serial numbers and failure reasons.

```
incloud device import-status <job-id> [flags]
```

### Examples

```
  # Check import status
  incloud device import-status 69c371131e0e4d15c8cb2b25

  # Wait for a running import to complete
  incloud device import-status 69c371131e0e4d15c8cb2b25 --wait

  # Get structured output
  incloud device import-status 69c371131e0e4d15c8cb2b25 -o json
```

### Options

```
  -h, --help   help for import-status
  -w, --wait   Wait for the import to complete if still running
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

