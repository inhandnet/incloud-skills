## incloud alert ack

Acknowledge alerts

### Synopsis

Acknowledge one or more alerts by ID, or acknowledge all alerts with --all.

```
incloud alert ack [<id>...] [flags]
```

### Examples

```
  # Acknowledge specific alerts
  incloud alert ack 507f1f77bcf86cd799439011 507f1f77bcf86cd799439012

  # Acknowledge all alerts
  incloud alert ack --all

  # Acknowledge all alerts of specific types
  incloud alert ack --all --type offline --type reboot
```

### Options

```
      --all                Acknowledge all alerts
  -h, --help               help for ack
      --type stringArray   Filter by alert type (can be specified multiple times)
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

* [incloud alert](incloud_alert.md)	 - Manage alerts

