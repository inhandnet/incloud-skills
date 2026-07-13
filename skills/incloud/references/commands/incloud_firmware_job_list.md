## incloud firmware job list

List OTA firmware upgrade jobs

### Synopsis

List OTA firmware upgrade jobs with optional filtering and pagination.

```
incloud firmware job list [flags]
```

### Examples

```
  # List recent OTA jobs
  incloud firmware job list

  # Filter by firmware ID
  incloud firmware job list --firmware 6989afd5eeb72121455dc104

  # Filter by status
  incloud firmware job list --status succeeded

  # Filter by module
  incloud firmware job list --module default

  # Paginate and sort
  incloud firmware job list --page 2 --limit 50 --sort createdAt,desc

  # Select fields
  incloud firmware job list -f _id -f status -f document.version
```

### Options

```
      --expand strings    Expand related resources
  -f, --fields strings    Fields to return and display
      --firmware string   Filter by firmware ID
  -h, --help              help for list
      --limit int         Number of items per page (default 20)
      --module string     Filter by module name
      --page int          Page number (starting from 1) (default 1)
      --sort string       Sort order (e.g. "createdAt,desc")
      --status string     Filter by status (queued|inprogress|succeeded|canceled)
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

