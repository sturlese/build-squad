# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- A self-contained Codex plugin with the complete Build Squad skill suite, a
  Codex safety hook, and installable custom-agent profiles.
- A repository-local Codex marketplace and CI validation for both supported
  platforms.

### Changed

- Renamed the project from Claude Squad to Build Squad while retaining the
  Claude Code `squad` plugin identifier for installation compatibility.

## [2.1.0] - 2026-08-21

### Added

- Five specialized engineering roles: UX, Developer, Tester, Auditor, and
  Documentator.
- Define, build, fix, refactor, and review pipelines with explicit human gates.
- Reproduce-first bug fixing, contract-focused testing, and reusable
  architecture, breaking-change, and final-validation playbooks.
- A tested guard against direct cluster access and destructive Git commands.

### Changed

- Strengthened role boundaries, testability guidance, and the security guard's
  coverage.
- Removed the obsolete environment-file restriction from the security guard.
