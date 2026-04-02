## incloud alert rule create

Create an alert rule

### Synopsis

Create a new alert rule with specified targets, alert types, and notification settings.

Target types: org, group, device

The --type flag accepts three formats:
  - Type name only:       --type reboot
  - With parameters:      --type "disconnected,retention=600"
  - JSON object:          --type '{"type":"disconnected","param":{"retention":600}}'

Use 'incloud alert rule types' to see all supported types and their parameters.

Supported notification channels:
  SMS, APP, EMAIL, WEBHOOK, SUBSCRIPTION

```
incloud alert rule create [flags]
```

### Examples

```
  # Create a rule for an org
  incloud alert rule create \
    --target-type org --target 507f1f77bcf86cd799439011 \
    --type disconnected \
    --channel EMAIL --channel APP

  # Create a rule with parameters
  incloud alert rule create \
    --target-type org --target 507f1f77bcf86cd799439011 \
    --type "disconnected,retention=600" \
    --channel EMAIL

  # Create with JSON format
  incloud alert rule create \
    --target-type device --target 507f1f77bcf86cd799439011 \
    --type '{"type":"high_average_cpu_utilization","param":{"retention":600,"threshold":80}}' \
    --channel APP

  # Create a rule for device groups with multiple types
  incloud alert rule create \
    --target-type group --target 507f1f77bcf86cd799439011 \
    --type disconnected --type reboot \
    --channel EMAIL \
    --user 607f1f77bcf86cd799439022

  # Create a rule with active time window
  incloud alert rule create \
    --target-type device --target 507f1f77bcf86cd799439011 \
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
  -h, --help                  help for create
      --start-time string     Active start time (HH:mm, default 00:00)
      --target stringArray    Target ID (required, can be repeated)
      --target-type string    Target type: org, group, or device (required)
      --type stringArray      Alert type with optional params (required, can be repeated; use 'incloud alert rule types' to list)
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

