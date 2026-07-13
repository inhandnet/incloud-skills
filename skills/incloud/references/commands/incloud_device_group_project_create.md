## incloud device group project create

Create a project version

### Synopsis

Create a new project version for a device group with docker-compose and/or systemd configurations.

```
incloud device group project create <group-id> [flags]
```

### Examples

```
  # Create with docker-compose
  incloud device group project create 507f1f77bcf86cd799439011 --docker-compose "version: '3'\nservices:\n  app:\n    image: myapp:latest"

  # Create with systemd units
  incloud device group project create 507f1f77bcf86cd799439011 --systemd '[{"name":"myservice","content":"[Unit]\nDescription=My Service\n[Service]\nExecStart=/usr/bin/myapp"}]'

  # Create with artifact and layerfs
  incloud device group project create 507f1f77bcf86cd799439011 --docker-compose "..." --artifact-key "path/to/artifact" --layerfs-id 653b1ff2a84e171614d88695
```

### Options

```
      --artifact-key string     S3 artifact key
      --docker-compose string   Docker Compose file content
  -h, --help                    help for create
      --layerfs-id string       Layerfs snapshot ID to use as base
      --systemd string          Systemd unit definitions as JSON array (e.g. '[{"name":"svc","content":"..."}]')
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

