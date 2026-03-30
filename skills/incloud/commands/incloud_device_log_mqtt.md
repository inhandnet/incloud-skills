## incloud device log mqtt

View MQTT communication logs

### Synopsis

View MQTT message logs for a device, including publish, connect, and disconnect events.

```
incloud device log mqtt <device-id> [flags]
```

### Examples

```
  # View recent MQTT logs
  incloud device log mqtt 507f1f77bcf86cd799439011

  # Filter by time range
  incloud device log mqtt 507f1f77bcf86cd799439011 --after 2024-01-01T00:00:00Z --before 2024-01-02T00:00:00Z

  # Filter by message type
  incloud device log mqtt 507f1f77bcf86cd799439011 --type publish

  # Filter by topic
  incloud device log mqtt 507f1f77bcf86cd799439011 --topic shadow

  # Paginate with cursor
  incloud device log mqtt 507f1f77bcf86cd799439011 --next <cursor-token>

  # Show all fields including payload
  incloud device log mqtt 507f1f77bcf86cd799439011 -o table -f timestamp -f logType -f topic -f payload
```

### Options

```
      --after string     Start time (ISO 8601, e.g. 2024-01-01T00:00:00Z)
      --before string    End time (ISO 8601, e.g. 2024-01-02T00:00:00Z)
  -f, --fields strings   Fields to display in table mode
  -h, --help             help for mqtt
      --limit int        Number of results per page (default 20)
      --next string      Cursor token for next page
      --order string     Sort order: asc (oldest first) or desc (newest first) (default "desc")
      --prev string      Cursor token for previous page
      --topic string     Filter by MQTT topic (regex)
      --type string      Filter by log type: publish, connected, disconnected
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

* [incloud device log](incloud_device_log.md)	 - Device logs

