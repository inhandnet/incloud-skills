## incloud device shadow get

Get a shadow document

### Synopsis

Get the full state of a named shadow document, including desired, reported, and delta states.

```
incloud device shadow get <device-id> [flags]
```

### Examples

```
  # Get shadow document
  incloud device shadow get 507f1f77bcf86cd799439011 --name default

  # Output as YAML
  incloud device shadow get 507f1f77bcf86cd799439011 --name default -o yaml
```

### Options

```
  -h, --help          help for get
      --name string   Shadow name (required)
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

* [incloud device shadow](incloud_device_shadow.md)	 - Device shadow documents

