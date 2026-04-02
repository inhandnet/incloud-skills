## incloud license list

List licenses

### Synopsis

List licenses with optional filtering by status, type, attachment, and organization.

```
incloud license list [flags]
```

### Examples

```
  # List all activated licenses
  incloud license list --status activated

  # List unattached licenses of a specific type
  incloud license list --status inactivated --attached false --type basic

  # List licenses for a specific organization (admin)
  incloud license list --org-id 64a1b2c3d4e5f6a7b8c9d0e1

  # List expiring licenses
  incloud license list --status to_be_expired -o yaml

  # Filter by order
  incloud license list --order-id 64a1b2c3d4e5f6a7b8c9d0e1
```

### Options

```
      --attached string   Filter by attachment status (true/false)
      --expand strings    Expand related resources. Supported: type, device, org
  -f, --fields strings    Fields to return and display
  -h, --help              help for list
      --limit int         Number of items per page (default 20)
      --order-id string   Filter by order ID
      --org-id string     Filter by organization ID
      --page int          Page number (starting from 1) (default 1)
      --sort string       Sort order (e.g. "createdAt,desc")
      --status string     Filter by status (activated/inactivated/to_be_expired/expired)
      --type string       Filter by license type slug
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

