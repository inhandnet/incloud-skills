## incloud firmware job cancel

Cancel an OTA firmware upgrade job

### Synopsis

Cancel a queued or in-progress OTA firmware upgrade job.

All pending executions under this job will also be canceled.

```
incloud firmware job cancel <jobId> [flags]
```

### Examples

```
  # Cancel an OTA job
  incloud firmware job cancel 20260318000001
```

### Options

```
  -h, --help   help for cancel
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

* [incloud firmware job](incloud_firmware_job.md)	 - Manage OTA firmware upgrade jobs

