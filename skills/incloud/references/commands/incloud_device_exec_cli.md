## incloud device exec cli

Run a CLI command directly on a device

### Synopsis

Create a tunnel, login to the device CLI, execute a command, and return clean output.

This is a convenience wrapper that automatically manages the tunnel lifecycle:
creates a CLI tunnel, runs the command, then closes the tunnel.

For multi-round diagnostics where you need to run commands across multiple
invocations, use 'tunnel open-cli' + 'tunnel cli' + 'tunnel close' instead.

Supports INOS CLI commands (default) and BusyBox shell mode (--shell).
In shell mode, use && or ; to chain multiple commands in one call.
Output is cleaned: telnet negotiation, ANSI escapes, command echo,
and prompt are stripped. stdout contains only the command output.

```
incloud device exec cli <device-id> <command> [flags]
```

### Examples

```
  # Run an INOS CLI command
  incloud device exec cli 507f1f77bcf86cd799439011 --user adm --password 123456 "show interface"

  # Run shell commands via BusyBox (chain with &&)
  incloud device exec cli 507f1f77bcf86cd799439011 --user adm --password 123456 \
    --shell --shell-password xxx "uname -a && free -m && ip route"

  # With longer timeout for slow commands
  incloud device exec cli 507f1f77bcf86cd799439011 --user adm --password 123456 \
    --timeout 60 "ping 8.8.8.8"
```

### Options

```
  -h, --help                    help for cli
      --ngrok-port int          Ngrok TCP proxy port (default 4443)
      --password string         Device login password (required)
      --shell                   Enter BusyBox shell mode (via 'inhand' command)
      --shell-password string   Password for shell mode (required with --shell)
      --shell-prompt string     Shell prompt regex pattern (default "\\S+\\s*[#$]\\s*$")
      --timeout int             Command timeout in seconds (default 30)
      --user string             Device login username (required)
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

* [incloud device exec](incloud_device_exec.md)	 - Execute remote methods and diagnostics on devices

