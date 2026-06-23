## incloud touch client create

Create a touch client

### Synopsis

Create a new remote access client (downstream endpoint) on an edge device. Supports ETHERNET and SERIAL types.

```
incloud touch client create [flags]
```

### Examples

```
  # Create an Ethernet client
  incloud touch client create --name my-plc --type ETHERNET --device-id 507f1f77bcf86cd799439011 --ip 192.168.1.100

  # Create a Serial client
  incloud touch client create --name my-serial --type SERIAL --device-id 507f1f77bcf86cd799439011 --serial '{"name":"ttyS0","type":"rs232","baudRate":"9600","dataBit":8,"stopBit":1,"parityBit":"NONE"}'
```

### Options

```
      --device-id string   Edge device ID (required)
  -h, --help               help for create
      --ip string          IP address for ETHERNET type
      --name string        Client name (required, 1-128 chars)
      --serial string      Serial configuration as JSON for SERIAL type
      --type string        Client type: ETHERNET or SERIAL (required)
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

* [incloud touch client](incloud_touch_client.md)	 - Manage touch clients

