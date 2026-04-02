## incloud feedback create

Create a feedback entry

### Synopsis

Submit feedback about the InCloud platform or CLI.

The --content flag accepts a string or a file reference with @ prefix (e.g. @feedback.md).

```
incloud feedback create [flags]
```

### Examples

```
  # Submit feedback with inline content
  incloud feedback create --content "Signal rating is inaccurate"

  # Submit feedback from a file
  incloud feedback create --content @feedback.md

  # Submit with attachments
  incloud feedback create --content "See screenshot" --file screenshot.png --file log.txt

  # Submit a suggestion
  incloud feedback create --type suggestion --content "Add batch export feature"
```

### Options

```
  -c, --content string     Feedback content (use @file to read from file)
      --file stringArray   Attachment file paths (repeatable)
  -h, --help               help for create
  -t, --type string        Feedback type: issue, question, comment, suggestion (default "issue")
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

