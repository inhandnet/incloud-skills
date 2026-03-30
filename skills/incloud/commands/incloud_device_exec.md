## incloud device exec

Execute remote methods and diagnostics on devices

### Synopsis

Execute remote methods, built-in operations, and diagnostic tools on devices.

Remote methods:
  method             Invoke a custom remote method
  reboot             Reboot a device
  restore-defaults   Restore factory defaults

Diagnostics:
  ping               Ping a host from the device
  traceroute         Traceroute to a host
  speedtest          Run speed test
  speedtest-config   Get speed test configuration
  speedtest-history  View speed test history
  capture            Start packet capture (tcpdump)
  flowscan           Start flow scan
  flowscan-status    Get flow scan status
  cancel             Cancel a diagnostic task
  interfaces         List network interfaces

These operations run through the platform API. To run arbitrary CLI commands
directly on the device (e.g. show running-config, routing tables), use
'tunnel cli' instead.

### Options

```
  -h, --help   help for exec
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
* [incloud device exec cancel](incloud_device_exec_cancel.md)	 - Cancel a running diagnostic task
* [incloud device exec capture](incloud_device_exec_capture.md)	 - Start packet capture (tcpdump) on a device
* [incloud device exec cli](incloud_device_exec_cli.md)	 - Run a CLI command directly on a device
* [incloud device exec flowscan](incloud_device_exec_flowscan.md)	 - Start flow scan (traffic analysis) on a device
* [incloud device exec flowscan-status](incloud_device_exec_flowscan-status.md)	 - Get flow scan status for a device
* [incloud device exec interfaces](incloud_device_exec_interfaces.md)	 - List available network interfaces on a device
* [incloud device exec method](incloud_device_exec_method.md)	 - Invoke a custom remote method on device(s)
* [incloud device exec ping](incloud_device_exec_ping.md)	 - Run ping diagnostic on a device
* [incloud device exec reboot](incloud_device_exec_reboot.md)	 - Reboot a device
* [incloud device exec restore-defaults](incloud_device_exec_restore-defaults.md)	 - Restore a device to factory defaults
* [incloud device exec speedtest](incloud_device_exec_speedtest.md)	 - Run speed test on a device
* [incloud device exec speedtest-config](incloud_device_exec_speedtest-config.md)	 - Get speed test configuration (available interfaces and server nodes)
* [incloud device exec speedtest-history](incloud_device_exec_speedtest-history.md)	 - View speed test history for a device
* [incloud device exec traceroute](incloud_device_exec_traceroute.md)	 - Run traceroute diagnostic on a device

