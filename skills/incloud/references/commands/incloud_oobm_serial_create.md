## incloud oobm serial create

Create an OOBM serial port configuration

### Synopsis

Create a new OOBM serial port configuration for remote console access.

Parity values: 0=None, 1=Odd, 2=Even
Usage types: web (browser-based terminal), cli (SSH tunnel)

```
incloud oobm serial create [flags]
```

### Examples

```
  # Create a serial port with defaults
  incloud oobm serial create \
    --device-id 507f1f77bcf86cd799439011 \
    --name "Console Port"

  # Create with custom serial settings
  incloud oobm serial create \
    --device-id 507f1f77bcf86cd799439011 \
    --name "RS232" \
    --speed 115200 --data-bits 8 --stop-bits 1 --parity 0 \
    --usage cli --idle-time 600
```

### Options

```
      --conn-time int      Connection timeout in seconds (3600-604800) (default 3600)
      --data-bits int      Data bits (5-8) (default 8)
      --device-id string   Device ID (required; use 'incloud device list' to find IDs)
  -h, --help               help for create
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

