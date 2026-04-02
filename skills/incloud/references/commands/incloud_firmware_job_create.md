## incloud firmware job create

Create an OTA firmware upgrade job

### Synopsis

Create an OTA firmware upgrade job for specified target devices or groups.

The job will push the specified firmware to target devices. Devices without
a valid license are automatically excluded (reported as "unlicensed" in ignored).

Target types:
  DEVICE  - target specific devices by ID
  GROUP   - target device groups by ID

```
incloud firmware job create <firmwareId> [flags]
```

### Examples

```
  # Upgrade a device to a specific firmware
  incloud firmware job create 6989afd5eeb72121455dc104 \
    --target-type DEVICE --target 6989ad34a7455f3f0bf9dce2

  # Upgrade multiple devices
  incloud firmware job create 6989afd5eeb72121455dc104 \
    --target-type DEVICE \
    --target 6989ad34a7455f3f0bf9dce2 \
    --target 691bde8c96946b3e64095380

  # Upgrade a device group with version filter
  incloud firmware job create 6989afd5eeb72121455dc104 \
    --target-type GROUP --target 507f1f77bcf86cd799439011 \
    --version V2.0.22

  # Schedule for later with smart filtering
  incloud firmware job create 6989afd5eeb72121455dc104 \
    --target-type DEVICE --target 6989ad34a7455f3f0bf9dce2 \
    --scheduled-at 2026-04-01T10:00:00Z --filter

  # Set upgradable time window
  incloud firmware job create 6989afd5eeb72121455dc104 \
    --target-type DEVICE --target 6989ad34a7455f3f0bf9dce2 \
    --upgradable-start 02:00 --upgradable-end 05:00
```

### Options

```
      --filter                    Enable smart filtering (skip devices already at target version)
  -h, --help                      help for create
      --scheduled-at string       Scheduled execution time (ISO 8601, must be 30min-31days from now)
      --target stringArray        Target device or group ID (required, repeatable)
      --target-type string        Target type: DEVICE or GROUP (required)
      --upgradable-end string     Upgradable period end time (HH:mm)
      --upgradable-start string   Upgradable period start time (HH:mm)
      --version stringArray       Source firmware version to match (repeatable)
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

