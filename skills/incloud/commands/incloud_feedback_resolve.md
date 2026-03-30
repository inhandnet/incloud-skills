## incloud feedback resolve

Update the resolution status of a feedback entry

### Synopsis

Update the resolution status of a feedback entry.

Valid resolution values: new, approved, resolved, ignored

```
incloud feedback resolve <feedback-id> [flags]
```

### Examples

```
  # Mark as approved
  incloud feedback resolve 69c3e7bb828ddd389e530a57 --resolution approved

  # Mark as resolved with a reply
  incloud feedback resolve 69c3e7bb828ddd389e530a57 --resolution resolved --reply "Fixed in v2.1.0"

  # Mark as ignored
  incloud feedback resolve 69c3e7bb828ddd389e530a57 --resolution ignored --reply "Works as intended"
```

### Options

```
  -h, --help                help for resolve
      --reply string        Resolution reply or comment
  -r, --resolution string   Resolution status: new, approved, resolved, ignored
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

