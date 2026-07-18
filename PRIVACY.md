# Privacy Policy

_Last updated: 2026-07-19_

`claude-squad` (the `squad` plugin) does not collect, store, or transmit any personal
data or usage data.

## What the plugin does with your data

The plugin consists of Markdown agent and skill definitions, a `hooks.json`
configuration, and one Python script (`hooks/guard.py`). None of these components
open a network connection, and the plugin has no third-party dependencies.

- **No data collection.** The plugin does not gather personal information, project
  contents, prompts, or usage metrics.
- **No telemetry or analytics.** No usage reporting of any kind is performed.
- **No network access.** No component of the plugin contacts any server. It has no
  API keys, accounts, or backend service.
- **No persistent storage.** The security hook receives one tool call on standard
  input, decides whether to allow or deny it, and writes nothing to disk. It keeps
  no logs and no history.

## Your project's contents

Your code and files are read and written by Claude Code's own tools, under whatever
permissions you have granted in your Claude Code configuration. The plugin adds
agent instructions and tool restrictions on top of that; it does not add any new
destination for your data. Files that agents create — specification documents,
tests, documentation — are written to your own working directory and nowhere else.

Handling of the data you send to Claude is governed by Anthropic's privacy policy,
not by this plugin: https://www.anthropic.com/legal/privacy

## Third parties

The plugin sends no data to any third party, because it sends no data anywhere.

## Changes

Any change to this policy will be published in this file in the plugin's public
repository: https://github.com/sturlese/claude-squad

## Contact

Questions about this policy can be raised as an issue at
https://github.com/sturlese/claude-squad/issues
