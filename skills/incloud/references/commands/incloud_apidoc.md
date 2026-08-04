## incloud apidoc

Download the InCloud public API spec for integration

### Synopsis

Download the OpenAPI spec for InCloud's public (integration) APIs.

This is the same spec that backs the online API reference. Use it to build
against the platform: generate client SDKs, import into Postman/Insomnia, or
browse the available endpoints, parameters and schemas offline.

Use --lang to choose the language and --app to choose which spec to fetch.

```
incloud apidoc [flags]
```

### Examples

```
  # Print the English InCloud API spec
  incloud apidoc

  # Chinese spec
  incloud apidoc --lang zh

  # Device Live spec, saved to a file for code generation
  incloud apidoc --app devicelive --output-file device-live-api.json

  # List all available endpoints
  incloud apidoc --jq '.paths | keys'
```

### Options

```
      --app string           Which spec to fetch: star (InCloud API), devicelive (Device Live API) (default "star")
  -h, --help                 help for apidoc
      --lang string          Spec language: en, zh (default "en")
      --output-file string   Save the spec to a file instead of printing
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

* [incloud](incloud.md)	 - InCloud Platform CLI

