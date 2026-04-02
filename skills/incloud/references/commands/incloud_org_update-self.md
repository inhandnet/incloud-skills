## incloud org update-self

Update current organization

### Synopsis

Update the organization that the current user belongs to.

```
incloud org update-self [flags]
```

### Examples

```
  # Update organization name
  incloud org update-self --name "New Name"

  # Update multiple fields
  incloud org update-self --name "New Name" --description "Updated desc" --phone "+1234567890"
```

### Options

```
      --biz-category string   Business category (e.g. TRANSPORTATION, INFORMATION_TECHNOLOGY, HEALTHCARE_MEDICINE)
      --contactor string      Contact person name
      --country-code string   Country code (e.g. US, CN)
      --description string    Description (max 256 chars)
      --email string          Organization email
  -h, --help                  help for update-self
      --name string           Organization name
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

