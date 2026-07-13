## incloud device config task get

Get a CLI configuration task

### Synopsis

Get details of a CLI configuration task by its job ID.

```
incloud device config task get <job-id> [flags]
```

### Examples

```
  # Get task details
  incloud device config task get 507f1f77bcf86cd799439011

  # Get task details with job expansion
  incloud device config task get 507f1f77bcf86cd799439011 --expand cliJob
```

### Options

```
      --expand string   Expand related resources (e.g. cliJob)
  -h, --help            help for get
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

* [incloud device config task](incloud_device_config_task.md)	 - Manage CLI configuration tasks

