## incloud feedback download

Download attachments from a feedback entry

### Synopsis

Download all attachments from a feedback entry to the current directory (or --dir).

Use 'incloud feedback list' to find feedback IDs and see which entries have attachments.

Note: this command searches the latest 100 feedback entries to locate the given ID.
Very old entries may not be found; use 'incloud feedback list --page N' to verify.

```
incloud feedback download <feedback-id> [flags]
```

### Examples

```
  # Download attachments from a feedback entry
  incloud feedback download 69c3e7bb828ddd389e530a57

  # Download to a specific directory
  incloud feedback download 69c3e7bb828ddd389e530a57 --dir /tmp/attachments
```

### Options

```
      --dir string   Output directory for downloaded files (default: current directory)
  -h, --help         help for download
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

