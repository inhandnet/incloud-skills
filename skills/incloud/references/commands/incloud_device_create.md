## incloud device create

Create a device

### Synopsis

Create a new device on the InCloud platform.

The serial number is validated before creation to detect the product model
and determine whether a MAC address or IMEI is required. If the required
credential is not provided via flags and the terminal is interactive, you
will be prompted to enter it.

```
incloud device create [flags]
```

### Examples

```
  # Create a device (product auto-detected from serial number)
  incloud device create --name "My Router" --sn "ABC123456789012" --mac "AA:BB:CC:DD:EE:FF"

  # MAC or IMEI will be prompted in TTY if required but not provided
  incloud device create --name "My Router" --sn "ABC123456789012"

  # With device group and labels
  incloud device create --name "My Router" --sn "ABC123456789012" --mac "AA:BB:CC:DD:EE:FF" \
    --group "group-id" --label env=prod --label region=us

  # With metadata
  incloud device create --name "My Router" --sn "ABC123456789012" --mac "AA:BB:CC:DD:EE:FF" \
    --metadata key1=val1
```

### Options

```
      --description string     Device description (max 256 chars)
      --group string           Device group ID (use 'incloud device group list' to find IDs)
  -h, --help                   help for create
      --imei string            IMEI (required for some products; prompted if omitted in TTY)
      --label stringArray      Label in key=value format (repeatable, max 10)
      --mac string             MAC address (required for some products; prompted if omitted in TTY)
      --metadata stringArray   Metadata in key=value format (repeatable)
      --name string            Device name (required)
      --product string         Product model (auto-detected from serial number)
      --sn string              Serial number (required)
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

* [incloud device](incloud_device.md)	 - Manage devices

