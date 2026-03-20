Agent skills for managing InHand Networks [InCloud Manager](https://www.inhandnetworks.com/products/incloud-manager.html) platform via the `incloud` CLI.

These skills follow the [Agent Skills specification](https://agentskills.io/specification) so they can be used by any skills-compatible agent, including Claude Code and Codex CLI.

## Installation

### Claude Code Plugin

```
/plugin marketplace add https://gitlab.inhand.design/nezha/incloud-skills.git
/plugin install incloud@incloud-skills
```

### Manually

#### Claude Code

```bash
claude --plugin-dir /path/to/incloud-skills
```

Or add to your project's `.claude/settings.json`:

```json
{
  "plugins": ["/path/to/incloud-skills"]
}
```

#### Codex CLI

Copy the `skills/` directory into your Codex skills path (typically `~/.codex/skills`).

## Prerequisites

- [`incloud` CLI](https://gitlab.inhand.design/nezha/incloud-cli) installed and configured (`incloud config use-context`)

## Skills

| Skill | Description |
|-------|-------------|
| [incloud](skills/incloud) | Manage InCloud Manager platform resources — device monitoring, remote diagnostics, configuration, alerts, firmware upgrades, SD-WAN, InCloud Connector, and platform administration |
