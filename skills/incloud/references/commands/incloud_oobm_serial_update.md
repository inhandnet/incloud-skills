## incloud oobm serial update

Update an OOBM serial port configuration

### Synopsis

Update an OOBM serial port configuration. This is a full replacement of all fields.

```
incloud oobm serial update <id> [flags]
```

### Examples

```
  # Update serial port settings
  incloud oobm serial update 507f1f77bcf86cd799439011 \
    --device-id 607f1f77bcf86cd799439022 \
    --name "Console" --speed 115200 --usage cli
```

### Options

```
      --conn-time int      Connection timeout in seconds (3600-604800) (default 3600)
      --data-bits int      Data bits (5-8) (default 8)
      --device-id string   Device ID (required; use 'incloud device list' to find IDs)
  -h, --help               help for update
      --idle-time int      Idle timeout in seconds (60-3600) (default 300)
      --name string        Name (required, 1-32 chars)
      --parity int         Parity: 0=None, 1=Odd, 2=Even
      --speed int          Baud rate (300-230400) (default 9600)
      --stop-bits int      Stop bits (1-2) (default 1)
      --usage string       Usage type: web or cli (default "web")
      --xonxoff            XON/XOFF flow control
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

* [incloud oobm serial](incloud_oobm_serial.md)	 - Manage OOBM serial port configurations

