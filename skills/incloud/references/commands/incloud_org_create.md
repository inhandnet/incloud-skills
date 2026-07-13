## incloud org create

Create an organization

### Synopsis

Create a new organization on the InCloud platform.

For root organizations (no --parent), --email and --password are required
to create the admin user. For sub-organizations, only --name is required.

```
incloud org create [flags]
```

### Examples

```
  # Create a root organization with admin user
  incloud org create --name "Acme Corp" --email admin@acme.com --password P@ssw0rd

  # Create a sub-organization
  incloud org create --name "Acme Branch" --parent 61259f8f4be3e571fcfa4d75

  # With additional details
  incloud org create --name "Acme Corp" --email admin@acme.com --password P@ssw0rd \
    --country-code US --biz-category TRANSPORTATION --phone "+1234567890"
```

### Options

```
      --biz-category string   Business category (e.g. TRANSPORTATION, INFORMATION_TECHNOLOGY, HEALTHCARE_MEDICINE)
      --country-code string   Country code (e.g. US, CN)
      --description string    Organization description (max 256 chars)
      --email string          Admin email (required for root orgs)
  -h, --help                  help for create
      --locale string         Locale (e.g. en_US, zh_CN)
      --logo string           Logo URL
      --name string           Organization name (required, 2-64 chars)
      --parent string         Parent organization ID (use 'incloud org list' to find IDs)
      --password string       Admin password (required for root orgs, 6-64 chars)
      --phone string          Phone number
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

* [incloud org](incloud_org.md)	 - Manage organizations

