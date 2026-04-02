## incloud license transfer

Transfer licenses to another organization

### Synopsis

Transfer one or more licenses to another organization.

Only inactivated and unattached licenses can be transferred.
Maximum 1000 licenses per operation.

```
incloud license transfer <license-id> [<license-id>...] [flags]
```

### Examples

```
  # Transfer licenses to another organization
  incloud license transfer LIC_ID1 LIC_ID2 LIC_ID3 --org ORG_ID

  # Skip confirmation
  incloud license transfer LIC_ID1 --org ORG_ID --yes
```

### Options

```
  -h, --help         help for transfer
      --org string   Target organization ID (required)
  -y, --yes          Skip confirmation prompt
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

