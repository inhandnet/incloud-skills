## incloud org delete

Delete an organization

### Synopsis

Delete an organization and cascade-delete its roles, invitations, and customers.

```
incloud org delete <id> [flags]
```

### Examples

```
  # Delete an organization (will prompt for confirmation)
  incloud org delete 61259f8f4be3e571fcfa4d75

  # Skip confirmation
  incloud org delete 61259f8f4be3e571fcfa4d75 --yes
```

### Options

```
  -h, --help   help for delete
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

* [incloud org](incloud_org.md)	 - Manage organizations

