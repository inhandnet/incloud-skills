## incloud api

Make an authenticated API request

### Synopsis

Make an authenticated API request to the InCloud platform.

The path is appended to the current context's host URL.
Authorization header is automatically injected.

```
incloud api <path> [flags]
```

### Examples

```
  # GET current user
  incloud api /api/v1/users/me

  # List devices with query params
  incloud api /api/v1/devices -q page=0 -q limit=10

  # Output formats
  incloud api /api/v1/devices -o json
  incloud api /api/v1/devices -o table -c name -c status -c product
  incloud api /api/v1/devices -o yaml

  # Create device
  incloud api /api/v1/devices -X POST -f name=test -f product=router

  # POST with JSON from stdin
  echo '{"name":"test"}' | incloud api /api/v1/devices -X POST --input -

  # Custom header
  incloud api /api/v1/users/me -H "Sudo: user@example.com"

  # Download a file
  incloud api /api/v1/devices/DEVICE_ID/files/capture_result.pcap --output-file capture.pcap
```

### Options

```
  -c, --column stringArray   Columns to show in table output
  -f, --field stringArray    Body field (key=value), sent as JSON
  -H, --header stringArray   Additional header (Key: Value)
  -h, --help                 help for api
      --input string         Read body from file (use - for stdin)
  -X, --method string        HTTP method (default: GET)
      --output-file string   Save response body to file (for binary downloads)
  -q, --query stringArray    Query parameter (key=value)
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

