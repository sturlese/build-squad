# Build Squad for Codex

This package ports the Build Squad skills, safety guard, and five specialized roles to Codex.

Install the repository marketplace, then the plugin:

```sh
codex plugin marketplace add sturlese/build-squad
codex plugin add build-squad@build-squad
```

To install the optional `build-squad-*` agent profiles, run `python3 plugins/build-squad/scripts/install_agents.py` from a local clone. It copies the profiles into `~/.codex/agents/`. Start a new Codex thread after installing or updating the plugin.
