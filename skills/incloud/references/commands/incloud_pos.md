## incloud pos

Manage POS Ready traffic prioritization

### Synopsis

Inspect and manage POS Ready traffic prioritization.

POS Ready lets you mark which clients' point-of-sale traffic a device should prioritize, bypass, or treat normally, and observe which POS applications are matched.

To change a single client's level, use 'incloud device client set-pos-ready'.

### Options

```
  -h, --help   help for pos
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

* [incloud](incloud.md)	 - InCloud Platform CLI
* [incloud pos client-types](incloud_pos_client-types.md)	 - List the POS client-type dictionary
* [incloud pos clients](incloud_pos_clients.md)	 - List POS-marked clients across all devices
* [incloud pos device-hits](incloud_pos_device-hits.md)	 - Show POS application hits aggregated for a device
* [incloud pos forwarded](incloud_pos_forwarded.md)	 - List clients with recently forwarded POS traffic
* [incloud pos marked-clients](incloud_pos_marked-clients.md)	 - List POS-marked clients on a device
* [incloud pos rules](incloud_pos_rules.md)	 - Manage POS custom rules
* [incloud pos vendor-hits](incloud_pos_vendor-hits.md)	 - POS vendor hit time series for a client
* [incloud pos vendor-summary](incloud_pos_vendor-summary.md)	 - POS vendor hit summary for a client

