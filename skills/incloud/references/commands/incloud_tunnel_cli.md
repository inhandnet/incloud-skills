## incloud tunnel cli

Run a device CLI command through a tunnel

### Synopsis

Login to a device through an existing CLI tunnel, execute a command, and return clean output.

This command connects directly to the device's CLI (via telnet over tunnel) and runs
an INOS or shell command. Use this for information not exposed through the platform API,
such as INOS running-config, routing tables, or system-level diagnostics.

For platform-level operations (ping, reboot, packet capture, etc.), prefer 'device exec'
which works through the API without requiring a tunnel.

Requires a tunnel created by 'tunnel open-cli'. The tunnel is NOT closed after execution,
allowing multiple cli calls against the same tunnel for multi-round diagnostics.

Supports INOS CLI commands (default) and BusyBox shell mode (--shell).
In shell mode, use && or ; to chain multiple commands in one call.
Output is cleaned: telnet negotiation, ANSI escapes, command echo,
and prompt are stripped. stdout contains only the command output.

```
incloud tunnel cli <tunnel-id> <command> [flags]
```

### Examples

```
  # Create a tunnel first
  incloud tunnel open-cli <device-id> --no-open

  # Run an INOS CLI command
  incloud tunnel cli <tunnel-id> --token <token> --user adm --password 123456 "show interface"

  # Run a shell command via BusyBox
  incloud tunnel cli <tunnel-id> --token <token> --user adm --password 123456 \
    --shell --shell-password xxx "uname -a && free -m && ip route"

  # With longer timeout for slow commands (e.g. ping)
  incloud tunnel cli <tunnel-id> --token <token> --user adm --password 123456 \
    --timeout 60 "ping 8.8.8.8"

  # Close the tunnel when done
  incloud tunnel close <tunnel-id>
```

### Options

```
  -h, --help                    help for cli
      --ngrok-port int          Ngrok TCP proxy port (default 4443)
      --password string         Login password (required)
      --shell                   Enter BusyBox shell mode (via 'inhand' command)
      --shell-password string   Password for shell mode (required with --shell)
      --shell-prompt string     Shell prompt regex pattern (default "\\S+\\s*[#$]\\s*$")
      --timeout int             Command timeout in seconds (default 30)
      --token string            Auth token for the tunnel (from open-cli output)
      --user string             Login username (required)
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

* [incloud tunnel](incloud_tunnel.md)	 - Manage remote access tunnels

