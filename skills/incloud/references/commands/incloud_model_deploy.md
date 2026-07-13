## incloud model deploy

Deploy AI models to devices or groups

### Synopsis

Create batch deployment jobs for AI models to edge devices or device groups.

The --jobs flag accepts a JSON array of job definitions, each with "targets" (device/group IDs) and "model" (model ID).
When using --scheduled-at, the time must be at least 30 minutes from now and no more than 31 days in the future.

```
incloud model deploy [flags]
```

### Examples

```
  # Deploy a model to devices
  incloud model deploy --jobs '[{"targets":["device-id-1"],"model":"model-id"}]' --target-type DEVICE

  # Deploy to a group with scheduling
  incloud model deploy --jobs '[{"targets":["group-id-1"],"model":"model-id"}]' --target-type GROUP --scheduled-at 2024-06-01T10:00:00Z

  # Deploy with license filter
  incloud model deploy --jobs '[{"targets":["device-id-1"],"model":"model-id"}]' --target-type DEVICE --filter
```

### Options

```
      --filter                Enable license filtering
  -h, --help                  help for deploy
      --jobs string           Job definitions as JSON array (e.g. '[{"targets":["id"],"model":"model-id"}]') (required)
      --scheduled-at string   Scheduled deployment time (ISO 8601, must be 30min-31days from now)
      --target-type string    Target type: DEVICE or GROUP (required)
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

* [incloud model](incloud_model.md)	 - Manage AI models

