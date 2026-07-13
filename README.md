Agent skills for managing InHand Networks [InCloud Manager](https://www.inhandnetworks.com/products/incloud-manager.html) platform via the `incloud` CLI.

These skills follow the [Agent Skills specification](https://agentskills.io/specification) so they can be used by any skills-compatible agent, including Claude Code and Codex CLI.

## What can it do?

Once installed, talk to your AI agent in natural language to manage your InCloud Manager platform — no need to memorize CLI commands.

- **Device monitoring** — check device status, find offline devices, view connection history
- **Remote diagnostics** — ping, traceroute, packet capture, speed test
- **Signal analysis** — cellular signal quality (RSSI/SINR/RSRP), antenna history, trend analysis
- **Configuration** — read/update device config, copy between devices, snapshot & restore
- **Firmware upgrades** — check available firmware, schedule OTA upgrades, track progress
- **Alerts** — view/acknowledge alerts, create/manage alert rules
- **SD-WAN & Connector** — manage SD-WAN networks, InCloud Connector VPN accounts & endpoints
- **Remote access** — open device Web UI or CLI terminal, SSH tunnel forwarding
- **License management** — query/bind/transfer licenses, upgrade types, align expiry dates
- **Platform admin** — manage users, orgs, roles, view activity logs, configure webhooks

## Prerequisites

- An [InCloud Manager](https://www.inhandnetworks.com/products/incloud-manager.html) account

> [!NOTE]
> The [`incloud` CLI](https://github.com/inhandnet/incloud-cli) is required but you don't need to install it beforehand — the skill will guide Claude through the CLI installation and login automatically on first use. You can also [install it manually](https://github.com/inhandnet/incloud-cli) if you prefer.

## Installation

### Claude Code Plugin

Works on all Claude Code platforms — CLI, Desktop App, Web ([claude.ai/code](https://claude.ai/code)), and IDE extensions (VS Code, JetBrains).

1. **Add the marketplace** (only needed once):

   ```
   /plugin marketplace add inhandnet/incloud-skills
   ```

2. **Install the plugin**:

   ```
   /plugin install incloud@incloud-skills
   ```

3. **Activate** — start a new session for the plugin to take effect:
   - **CLI**: exit and re-run `claude`
   - **Desktop App / Web**: open a new conversation
   - **IDE extensions**: restart the Claude Code panel

4. **Verify** — the plugin is loaded when you see `incloud` listed in `/plugin > Installed`.

> [!TIP]
> **Desktop App**: click the **+** button next to the prompt box → **Plugins** → **Add plugin** to browse and install from the plugin manager UI.

> [!TIP]
> **Interactive browser (CLI / IDE)**: run `/plugin`, go to the **Discover** tab, find **incloud**, and select your preferred installation scope (User / Project / Local).

> [!TIP]
> **Terminal commands** (outside the REPL):
> ```bash
> claude plugin marketplace add inhandnet/incloud-skills
> claude plugin install incloud@incloud-skills
> ```
> The plugin will be active on the next Claude Code session.

#### Install for your team

To share the plugin with all project collaborators, install with **project scope**:

In the REPL, run `/plugin`, go to **Discover**, select **incloud**, and choose **Project** scope. This adds the marketplace and plugin to `.claude/settings.json`, so teammates get it automatically when they trust the project folder.

#### Update

```
/plugin update incloud@incloud-skills
```

#### Uninstall

```
/plugin uninstall incloud@incloud-skills
```

### Codex CLI

Copy the `skills/incloud` directory into one of the [Codex skills directories](https://developers.openai.com/codex/skills):

```bash
# User-level (available in all projects)
cp -r skills/incloud ~/.agents/skills/

# Or project-level (shared with team via git)
cp -r skills/incloud .agents/skills/
```

### Load without installing (session only)

If you have a local clone of this repo, you can load it into Claude Code for a single session:

```bash
claude --plugin-dir /path/to/incloud-skills
```

## Usage

The skill supports both English and Chinese. In most cases, just describe what you need — Claude automatically activates the skill when it detects requests related to:

- Device management (list, status, offline troubleshooting)
- Network diagnostics (ping, traceroute, signal analysis)
- Configuration, firmware upgrades, alerts
- SD-WAN, InCloud Connector, remote access
- License management, platform administration

```
You:    Show me all offline devices
Claude: [Automatically loads the incloud skill, lists offline devices]

You:    When did MR8051234502461 go offline?
Claude: [Checks device online history]

You:    Ping its gateway for me
Claude: [Runs remote ping diagnostic]
```

> [!TIP]
> **How to tell the skill is active:**
> - **CLI / IDE**: look for the loading indicator in the output:
>   ```
>   ⏺ Skill(incloud:incloud)
>     ⎿  Successfully loaded skill
>   ```
> - **Desktop App / Web**: the skill name appears highlighted in the prompt area when invoked, or Claude starts running `incloud` commands in its response.

You can also invoke it explicitly — type `/` in the prompt box to browse available skills, or type `/incloud` directly:

```
/incloud What's the signal quality of device MR8051234502461?
/incloud Schedule a firmware upgrade for all ER805 devices
/incloud Are there any unacknowledged alerts?
/incloud Open a remote terminal to MR8051234502461
/incloud Copy the config from device A to device B
```

## Troubleshooting

### "incloud: command not found"

The `incloud` CLI is not installed. Follow the installation instructions at [incloud CLI](https://github.com/inhandnet/incloud-cli).

### "unauthorized" or "401" errors

Your CLI session has expired. Run `incloud auth login` to re-authenticate.

### Plugin skills not appearing after installation

1. Run `/reload-plugins` to reload all plugins
2. Check `/plugin > Errors` for any loading errors
3. If the issue persists, try `claude plugin uninstall incloud@incloud-skills` and reinstall

## Skills

| Skill | Description |
|-------|-------------|
| [incloud](skills/incloud) | Manage InCloud Manager platform resources — device monitoring, remote diagnostics, configuration, alerts, firmware upgrades, SD-WAN, InCloud Connector, and platform administration |
