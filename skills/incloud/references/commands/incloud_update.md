## incloud update

Update incloud CLI to the latest version

### Synopsis

Check for and install newer versions of the incloud CLI.

By default, downloads and installs the latest release.
Use --check to only check without installing.

```
incloud update [flags]
```

### Examples

```
  # Update to latest version
  incloud update

  # Check for updates without installing
  incloud update --check

  # Check for updates (JSON output, useful for scripts)
  incloud update --check -o json

  # Update to a specific version
  incloud update --version v0.3.0

  # Skip confirmation prompt (for scripts/CI)
  incloud update --yes
```

### Options

```
      --check            Only check for updates, don't install
  -h, --help             help for update
  -o, --output string    Output format for --check (json)
      --version string   Update to a specific version (e.g. v0.3.0)
  -y, --yes              Skip confirmation prompt
```

### Options inherited from parent commands

```
      --context string   Override active context (env: INCLOUD_CONTEXT)
      --debug            Enable debug output (env: INCLOUD_DEBUG)
      --jq string        Filter JSON output using a jq expression (implies -o json)
      --tenant string    Switch organization context by ID (env: INCLOUD_TENANT)
```

### SEE ALSO

* [incloud](incloud.md)	 - InCloud Platform CLI

