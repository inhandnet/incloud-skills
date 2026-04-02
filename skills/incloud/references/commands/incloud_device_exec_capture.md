## incloud device exec capture

Start packet capture (tcpdump) on a device

```
incloud device exec capture <device-id> [flags]
```

### Examples

```
  # Capture on a specific interface
  incloud device exec capture 507f1f77bcf86cd799439011 --interface eth0

  # With duration and source filter
  incloud device exec capture 507f1f77bcf86cd799439011 --interface eth0 --duration 60 --source 192.168.1.1

  # Capture and download the pcap file
  incloud device exec capture 507f1f77bcf86cd799439011 --interface eth0 --download capture.pcap
```

### Options

```
  -d, --download string         Download pcap file to local path after capture
      --duration int            Capture duration in seconds
      --expert-options string   Advanced tcpdump options
  -h, --help                    help for capture
      --interface string        Network interface (required)
      --source string           Source IP filter
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

* [incloud device exec](incloud_device_exec.md)	 - Execute remote methods and diagnostics on devices

