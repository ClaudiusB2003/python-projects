# Changelog

All notable changes to this project will be documented in this file.

This project follows Semantic Versioning.

---

## [Unreleased]

### Planned
- IPv6 support
- network_types
---

## [1.0.0] - 2026-08-06

### Added
- User input validation
- CIDR notation support
- Network address calculation
- Broadcast address calculation
- Subnet mask display
- Maximum usable host calculation
- Private IP detection using `is_private`
- Modular code structure with separate functions

### Fixed
- Correct handling of host addresses using `strict=False`

## [1.1.0] - 2026-08-06
- Improved console output readability
- Refactored code into separate functions

## [1.2.0] - 2026-08-06

### Added
- Display first usable host address
- Display last usable host address
- Display CIDR prefix length

### Changed
- Correct handling of /31 point-to-point networks
- Correct handling of /32 single-host networks
- Improved internal calculation of host information
- Cleaner console output implementation

## [1.3.0] - 2026-08-07

### Changed
- Refactoring of the python code
- improved input handling

## [2.0.0] - 2026-08-11

### Added
- Subnet calculator: split a network into subnets based on a desired subnet count
- Automatic calculation of the required new prefix length (CIDR)
- Per-subnet display of network address, broadcast address, subnet mask, wildcard mask, first/last usable host and usable host count
- Input validation for the number of subnets (must be a positive integer)
- Validation preventing prefix lengths beyond /32

### Changed
- Reused `calculate_informations()` and `display_informations()` for subnet output to avoid code duplication

## [2.1.0] - 2026-08-11

### Added
- Binary representation of subnet mask

### Notes
- Initial public release.
