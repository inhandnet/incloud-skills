## incloud feedback list

List feedback entries

### Synopsis

List feedback entries with optional filtering and pagination. Use this command to review submitted feedback and check which entries have attachments.

```
incloud feedback list [flags]
```

### Examples

```
  # List all feedback
  incloud feedback list

  # List feedback with attachments visible (default fields include attachments)
  incloud feedback list

  # Filter by resolution status
  incloud feedback list --resolution new

  # Filter by type
  incloud feedback list --type suggestion

  # Filter by app
  incloud feedback list --app portal

  # Show only feedback that has attachments (using jq)
  incloud feedback list --jq '[.result[] | select(.attachments | length > 0)]'

  # Paginate results
  incloud feedback list --page 2 --limit 10
```

### Options

```
      --app string          Filter by app (e.g. star, portal)
      --expand strings      Expand related resources. Supported: user, org
  -f, --fields strings      Fields to return and display
  -h, --help                help for list
      --limit int           Number of items per page (default 20)
      --page int            Page number (starting from 1) (default 1)
      --resolution string   Filter by resolution status (new, resolved)
      --sort string         Sort order (e.g. "createdAt,desc")
      --type string         Filter by feedback type (issue, question, comment, suggestion)
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

* [incloud feedback](incloud_feedback.md)	 - Submit feedback about the InCloud platform

