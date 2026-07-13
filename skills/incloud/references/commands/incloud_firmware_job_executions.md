## incloud firmware job executions

List OTA job executions

### Synopsis

List OTA firmware upgrade job executions with optional filtering.

Execution statuses: QUEUED, INPROGRESS, SUCCEEDED, FAILED, CANCELED

Use --firmware to list executions for a specific firmware, or --device to
list completed executions for a specific device.

```
incloud firmware job executions [flags]
```

### Examples

```
  # List all OTA executions
  incloud firmware job executions

  # Filter by status
  incloud firmware job executions --status SUCCEEDED

  # Filter by job ID
  incloud firmware job executions --job 20260318000001

  # Filter by device serial number
  incloud firmware job executions --sn MR805123

  # List executions for a specific firmware
  incloud firmware job executions --firmware 69afb47b2ad10a3f4b20c02f

  # List completed executions for a specific device
  incloud firmware job executions --device 69b24d278760dc6390e28db1

  # Expand related resources
  incloud firmware job executions --expand job,creator

  # Select fields
  incloud firmware job executions -f _id -f status -f device.name
```

### Options

```
      --device string     Filter by device ID (uses /devices/{id}/ota/jobs/completed)
      --expand strings    Expand related resources. Supported: creator, org, job, nezha-device-manager-device
  -f, --fields strings    Fields to return and display
      --firmware string   Filter by firmware ID (uses /firmwares/{id}/job/executions)
  -h, --help              help for executions
      --job string        Filter by job ID
      --limit int         Number of items per page (default 20)
      --module string     Filter by OTA module name (default: "default")
      --page int          Page number (starting from 1) (default 1)
      --sn string         Filter by device serial number (supports regex)
      --sort string       Sort order (e.g. "createdAt,desc")
      --status string     Filter by status (QUEUED|INPROGRESS|SUCCEEDED|FAILED|CANCELED)
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
* [incloud firmware job executions cancel](incloud_firmware_job_executions_cancel.md)	 - Cancel an OTA job execution
* [incloud firmware job executions retry](incloud_firmware_job_executions_retry.md)	 - Retry a failed OTA job execution

