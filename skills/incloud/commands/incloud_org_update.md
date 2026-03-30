## incloud org update

Update an organization

### Synopsis

Update an existing organization on the InCloud platform.

```
incloud org update <id> [flags]
```

### Examples

```
  # Update name
  incloud org update 61259f8f4be3e571fcfa4d75 --name "New Name"

  # Update multiple fields
  incloud org update 61259f8f4be3e571fcfa4d75 --name "New Name" --description "Updated" --country-code CN

  # Set labels
  incloud org update 61259f8f4be3e571fcfa4d75 --label region=east --label tier=premium
```

### Options

```
      --biz-category string    Business category (e.g. TRANSPORTATION, INFORMATION_TECHNOLOGY, HEALTHCARE_MEDICINE)
      --contact-email string   Contact email
      --contactor string       Contact person name
      --country-code string    Country code (e.g. US, CN)
      --description string     Description (max 256 chars)
      --email string           Organization email
  -h, --help                   help for update
      --label stringArray      Label in key=value format (repeatable, max 10)
      --name string            Organization name
      --phone string           Phone number
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

