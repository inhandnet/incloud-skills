## incloud device group project update

Update a project version

### Synopsis

Update a project version's configuration. Published projects can only have their description updated.

```
incloud device group project update <group-id> <project-id> [flags]
```

### Examples

```
  # Update docker-compose
  incloud device group project update 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --docker-compose "version: '3'\nservices: ..."

  # Update description only (works for published projects)
  incloud device group project update 507f1f77bcf86cd799439011 653b1ff2a84e171614d88695 --description "Updated release"
```

### Options

```
      --artifact-key string     S3 artifact key (empty to clear)
      --description string      Project description (1-256 chars)
      --docker-compose string   Docker Compose file content
  -h, --help                    help for update
      --layerfs-id string       Layerfs snapshot ID (empty to clear)
      --systemd string          Systemd unit definitions as JSON array
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

* [incloud device group project](incloud_device_group_project.md)	 - Manage device group projects

