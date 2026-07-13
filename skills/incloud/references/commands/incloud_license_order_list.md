## incloud license order list

List orders

### Synopsis

List license orders with optional filtering by status, type, and date range.

```
incloud license order list [flags]
```

### Examples

```
  # List completed orders
  incloud license order list --status complete

  # List renewal orders in a date range
  incloud license order list --type license_renewal --after 2026-01-01 --before 2026-03-31

  # List all orders as YAML
  incloud license order list -o yaml
```

### Options

```
      --after string     Start date (e.g. 2025-01-01)
      --before string    End date (e.g. 2025-01-31)
      --expand strings   Expand related resources. Supported: creator, org
  -f, --fields strings   Fields to return and display
  -h, --help             help for list
      --limit int        Number of items per page (default 20)
      --page int         Page number (starting from 1) (default 1)
      --sort string      Sort order (e.g. "createdAt,desc")
      --status string    Filter by status (open/complete/cancelled)
      --type string      Filter by order type (license_purchase/license_renewal/sim_bill/service_purchase/service_renewal/service_upgrade)
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

* [incloud license order](incloud_license_order.md)	 - Manage license orders

