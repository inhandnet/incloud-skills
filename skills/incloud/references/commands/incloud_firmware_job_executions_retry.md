## incloud firmware job executions retry

Retry a failed OTA job execution

### Synopsis

Retry a failed OTA job execution. This creates a new OTA job targeting
the same device with the same firmware.

Only executions in FAILED status can be retried.

```
incloud firmware job executions retry <executionId> [flags]
```

### Examples

```
  # Retry a failed execution
  incloud firmware job executions retry 507f1f77bcf86cd799439011
```

### Options

```
  -h, --help   help for retry
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

