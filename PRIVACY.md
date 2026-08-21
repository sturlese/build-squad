# Privacy Policy

_Last updated: 2026-08-21_

`Build Squad` (the Claude Code `squad` plugin and Codex `build-squad` plugin) does not collect, store, or transmit any personal
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

Your code and files are read and written by Claude Code or Codex under the permissions
you grant to that host. The plugins add agent instructions and tool restrictions on top
of that; they do not add any new destination for your data. Files that agents create —
specification documents, tests, documentation — are written to your own working directory
and nowhere else.

Handling of data sent to Claude Code or Codex is governed by the respective host's
privacy policy, not by this plugin.

## Third parties

The plugin sends no data to any third party, because it sends no data anywhere.

## Changes

Any change to this policy will be published in this file in the plugin's public
repository: https://github.com/sturlese/build-squad

## Contact

Questions about this policy can be raised as an issue at
https://github.com/sturlese/build-squad/issues
