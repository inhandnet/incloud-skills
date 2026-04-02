## incloud license upgrade

Upgrade license type on devices

### Synopsis

Upgrade licenses on devices from one type to a higher tier.

All selected devices must have the same current license type, and none can have
an expired license. Remaining days are recalculated based on the price ratio
between the current and target license types.

```
incloud license upgrade [flags]
```

### Examples

```
  # Upgrade licenses on two devices to professional type
  incloud license upgrade --device-id DEV_ID1,DEV_ID2 --to professional

  # Upgrade with confirmation skipped
  incloud license upgrade --device-id DEV_ID1 --to enterprise --yes
```

### Options

```
      --device-id strings   Device IDs to upgrade (required, comma-separated)
  -h, --help                help for upgrade
      --to string           Target license type slug (required)
  -y, --yes                 Skip confirmation prompt
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

* [incloud license](incloud_license.md)	 - Manage licenses

