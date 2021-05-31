# Changelog
All notable changes in **salt-lint** are documented below.

## [Unreleased]

## [0.6.0] (2021-06-01)
### Deprecated
- Drop Python 2.7 support ([#239](https://github.com/warpnet/salt-lint/pull/239)).

### Added
- Rule 216, 217 and 218 for catching common typographical errors ([#249](https://github.com/warpnet/salt-lint/pull/249)).

## [0.5.2] (2021-01-29)
### Fixed
- Append the contents of the `CHANGELOG.md` file to the long description of the package instead of the duplicate `README.md` contents ([#234](https://github.com/warpnet/salt-lint/pull/234)).
- Ignore Jinja specific rules in Jinja escaped blocks ([#236](https://github.com/warpnet/salt-lint/pull/236)).

## [0.5.1] (2021-01-19)
### Fixed
- Ensure all excluded paths from both the CLI and configuration are passed to the runner ([#231](https://github.com/warpnet/salt-lint/pull/231)).

## [0.5.0] (2021-01-17)
### Added
- Rule 213 to recommend using cmd.run together with onchanges ([#207](https://github.com/warpnet/salt-lint/pull/207)).
- Rule 214 to check SLS file with a period in the name (besides the suffix period) as they can not be referenced by Salt ([#209](https://github.com/warpnet/salt-lint/pull/209)).
- Rules 901-915 to check for deprecated states and state options ([#214](https://github.com/warpnet/salt-lint/pull/214)).
- This `CHANGELOG.md` file to be able to list all notable changes for each version of **salt-lint** ([#223](https://github.com/warpnet/salt-lint/pull/223)).

[Unreleased]: https://github.com/warpnet/salt-lint/compare/v0.6.0...HEAD
[0.6.0]: https://github.com/warpnet/salt-lint/compare/v0.5.2...v0.6.0
[0.5.2]: https://github.com/warpnet/salt-lint/compare/v0.5.1...v0.5.2
[0.5.1]: https://github.com/warpnet/salt-lint/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/warpnet/salt-lint/compare/v0.4.2...v0.5.0
