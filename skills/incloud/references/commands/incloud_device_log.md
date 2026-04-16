## incloud device log

Device logs

### Synopsis

View and download device logs from the InCloud platform.

### Options

```
  -h, --help   help for log
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
* [incloud device log diagnostic](incloud_device_log_diagnostic.md)	 - Download and decrypt diagnostic log from device
* [incloud device log local](incloud_device_log_local.md)	 - Read log files directly from the device (requires device online)
* [incloud device log mqtt](incloud_device_log_mqtt.md)	 - View MQTT communication logs
* [incloud device log syslog](incloud_device_log_syslog.md)	 - View device syslog

