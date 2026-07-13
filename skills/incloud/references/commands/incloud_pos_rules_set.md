## incloud pos rules set

Replace a device's POS custom rules

### Synopsis

Replace the full set of POS custom rules for a device from a JSON file.

The file may contain either a bare array of rule entries or an object with a "rules" array. Each entry has: type (add|mask), clientType (UPPERCASE), vendor, protocol, address, port. Max 100 entries; this replaces all existing rules.

```
incloud pos rules set <device-id> [flags]
```

### Examples

```
  # Set rules from a file
  incloud pos rules set 507f1f77bcf86cd799439011 --file rules.json

  # Read from stdin
  cat rules.json | incloud pos rules set 507f1f77bcf86cd799439011 --file -
```

### Options

```
      --file string   Path to JSON file with rules (use '-' for stdin)
  -h, --help          help for set
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

* [incloud pos rules](incloud_pos_rules.md)	 - Manage POS custom rules

