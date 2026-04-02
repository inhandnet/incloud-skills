## incloud license align-expiry

Align expiry dates of multiple licenses

### Synopsis

Align (co-terminate) multiple licenses to the same expiry date.

This is a free operation that redistributes remaining license time so all
selected licenses expire on the same date. Only activated or to-be-expired
licenses can be aligned.

```
incloud license align-expiry <license-id> [<license-id>...] [flags]
```

### Examples

```
  # Align expiry dates for multiple licenses
  incloud license align-expiry LIC_ID1 LIC_ID2 LIC_ID3

  # Skip confirmation
  incloud license align-expiry LIC_ID1 LIC_ID2 --yes
```

### Options

```
  -h, --help   help for align-expiry
  -y, --yes    Skip confirmation prompt
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

* [incloud license](incloud_license.md)	 - Manage licenses

