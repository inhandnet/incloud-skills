## incloud file presign

Generate a pre-signed URL for file upload

### Synopsis

Generate a pre-signed URL that can be used to upload files to the platform.

```
incloud file presign [flags]
```

### Examples

```
  # Generate a pre-signed URL
  incloud file presign

  # Generate a pre-signed URL for a specific filename
  incloud file presign --filename artifact.tar.gz
```

### Options

```
      --filename string   Filename for the pre-signed URL
  -h, --help              help for presign
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

* [incloud file](incloud_file.md)	 - Manage files

