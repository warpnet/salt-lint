# Changelog
All notable changes in **salt-lint** are documented below.

## [Unreleased]
### Fixed
- Ensure all excluded paths from both the CLI and configuration are passed to the runner ([#231](https://github.com/warpnet/salt-lint/pull/231)).

## [0.5.0] (2021-01-17)
### Added
- Rule 213 to recommend using cmd.run together with onchanges ([#207](https://github.com/warpnet/salt-lint/pull/207)).
- Rule 214 to check SLS file with a period in the name (besides the suffix period) as they can not be referenced by Salt ([#209](https://github.com/warpnet/salt-lint/pull/209)).
- Rules 901-915 to check for deprecated states and state options ([#214](https://github.com/warpnet/salt-lint/pull/214)).
- This `CHANGELOG.md` file to be able to list all notable changes for each version of **salt-lint** ([#223](https://github.com/warpnet/salt-lint/pull/223)).

[Unreleased]: https://github.com/warpnet/salt-lint/compare/v0.4.2...HEAD
[0.5.0]: https://github.com/warpnet/salt-lint/compare/v0.4.2...v0.5.0
