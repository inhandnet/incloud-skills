## incloud alert rule update

Update an alert rule

### Synopsis

Update an existing alert rule. This is a full replacement of rules and notification
settings — all flags must be provided (use "alert rule get" to view current values).

Target bindings (type and targetIds) are preserved from the existing rule.

The --type flag accepts three formats:
  - Type name only:       --type reboot
  - With parameters:      --type "disconnected,retention=600"
  - JSON object:          --type '{"type":"disconnected","param":{"retention":600}}'

Use 'incloud alert rule types' to see all supported types and their parameters.

```
incloud alert rule update <rule-id> [flags]
```

### Examples

```
  # Update rule types and channels
  incloud alert rule update 507f1f77bcf86cd799439011 \
    --type reboot --type firmware_upgrade \
    --channel EMAIL --channel APP

  # Update with type parameters
  incloud alert rule update 507f1f77bcf86cd799439011 \
    --type "disconnected,retention=600" \
    --channel EMAIL

  # Update with JSON format
  incloud alert rule update 507f1f77bcf86cd799439011 \
    --type '{"type":"high_average_cpu_utilization","param":{"retention":600,"threshold":80}}' \
    --channel APP

  # Update with active time window
  incloud alert rule update 507f1f77bcf86cd799439011 \
    --type disconnected \
    --channel EMAIL \
    --day MONDAY --day TUESDAY --day WEDNESDAY --day THURSDAY --day FRIDAY \
    --start-time 09:00 --end-time 18:00
```

### Options

```
      --channel stringArray   Notification channel (required, can be repeated: SMS/APP/EMAIL/WEBHOOK/SUBSCRIPTION)
      --day stringArray       Active day of week (can be repeated: MONDAY..SUNDAY, default all)
      --end-time string       Active end time (HH:mm, default 23:59)
  -h, --help                  help for update
      --start-time string     Active start time (HH:mm, default 00:00)
      --type stringArray      Alert type (required, can be repeated; use 'incloud alert rule types' to list all)
      --user stringArray      User ID to notify (can be repeated)
      --webhook stringArray   Webhook ID for notification (can be repeated)
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

* [incloud alert rule](incloud_alert_rule.md)	 - Manage alert rules

