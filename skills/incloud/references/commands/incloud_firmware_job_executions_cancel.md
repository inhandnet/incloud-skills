## incloud firmware job executions cancel

Cancel an OTA job execution

### Synopsis

Cancel a queued or in-progress OTA job execution for a specific device.

```
incloud firmware job executions cancel <executionId> [flags]
```

### Examples

```
  # Cancel an execution
  incloud firmware job executions cancel 507f1f77bcf86cd799439011
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

* [incloud firmware job executions](incloud_firmware_job_executions.md)	 - List OTA job executions

