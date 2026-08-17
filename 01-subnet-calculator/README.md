# Subnet Calculator

> ✅ **This project is ready to use*

A simple command-line Subnet Calculator written in Python to strengthen my knowledge of **Python**, **Networking**, and **Cyber Security**.
This project is part of my learning journey and is being developed step by step.

---

## Version 2.2
![Subnet Calculator Screenshot](screenshot.png)

---

## Features
- Protocol selection screen (IPv4 / IPv6 / Exit)
- Interactive main menu per protocol (Network Information / Subnet Calculator / Exit)
- Accepts IPv4 addresses in CIDR notation
- Accepts IPv6 addresses in CIDR notation
- Splits a network into a given number of equal-sized subnets
- Calculates network address for each subnet
- Calculates broadcast address for each subnet (IPv4 & IPv6)
- Displays subnet mask and wildcard mask (IPv4)
- Displays binary representation of the subnet mask (IPv4)
- Displays wildcard mask (IPv6)
- Displays CIDR prefix
- Displays network class (IPv4 only)
- Displays first and last usable host
- Displays maximum usable hosts per subnet
- Detects whether the input IP is private
- Interactive "calculate another subnet" loop
- Robust input validation with retry loops

### Planned
- GUI (Tkinter)
- Detection of special address types (multicast, loopback, link-local, etc.)

---

## Technologies
- Python 3
- Standard Library
  - `ipaddress`

No external dependencies are required.

---

## Project Goal
The purpose of this project is **not** simply to build another subnet calculator.
Instead, the goal is to gain a deeper understanding of:
- IPv4 and IPv6 addressing
- CIDR notation
- Network calculations
- Python project structure
- Error handling
- Writing clean, maintainable code

---

## Usage
```bash
python main.py
```
You will first be asked to choose a protocol (IPv4 or IPv6, or type `exit` to leave the program). Afterwards you can choose between viewing network information, running the subnet calculator, or exiting back to the protocol selection.

---

## Example

**Protocol Selection**
```text
================================================================================
                       Welcome to the Subnet Calculator!

        Please choose a protocol or type 'exit' to leave the programm:
================================================================================

IPv4

IPv6

Exit

Choice: ipv4
```

**Main Menu (IPv4)**
```text
================================================================================
                        Welcome to the IPv4 calculator!
================================================================================

1. Network Information

2. Subnet Calculator

3. Exit

Choice: 2

Please input an ip address (CIDR format): 192.168.1.1/24

How many subnets do you need?: 4
```

**Output (IPv4)**
```text
================================================================================
                              Subnet Informations
================================================================================
Network Address     : 192.168.1.0
Broadcast           : 192.168.1.63
Subnet Mask         : 255.255.255.192
Binary Mask         : 11111111.11111111.11111111.11000000
Wildcard Mask       : 0.0.0.63
CIDR Prefix         : 26
First Host          : 192.168.1.1
Last Host           : 192.168.1.62
Usable Hosts        : 62
Private Address     : Yes
Network class       : C
================================================================================
                              Subnet Informations
================================================================================
Network Address     : 192.168.1.64
Broadcast           : 192.168.1.127
Subnet Mask         : 255.255.255.192
Binary Mask         : 11111111.11111111.11111111.11000000
Wildcard Mask       : 0.0.0.63
CIDR Prefix         : 26
First Host          : 192.168.1.65
Last Host           : 192.168.1.126
Usable Hosts        : 62
Private Address     : Yes
Network class       : C

Press Enter to return
```

**Output (IPv6)**
```text
================================================================================
                          Subnet Informations (IPv6)
================================================================================
Network Address     : 2001:db8::
Broadcast           : 2001:db8::ffff:ffff:ffff:ffff
Wildcard Mask       : ::ffff:ffff:ffff:ffff
CIDR Prefix         : 64
First Host          : 2001:db8::1
Last Host           : 2001:db8::ffff:ffff:ffff:fffe
Usable Hosts        : 18446744073709551614
Private Address     : No

Press Enter to return
```

---

## Project Structure
```text
subnet-calculator/
│
├── main.py
├── CHANGELOG.md
├── LICENSE
└── README.md
```
The structure will evolve as the project grows.

---

## Learning Objectives
- Practice Python fundamentals
- Learn to work with the `ipaddress` module
- Improve networking knowledge
- Build software incrementally
- Learn basic software design principles
- Use Git and GitHub for version control

---

## Future Ideas
- Automatic subnet recommendations
- Route summarization
- Supernetting
- GUI version
- Web version using Flask or FastAPI

---

## Author
Claudius B. — Apprentice IT Specialist, System Integration

## License
This project is licensed under the MIT License.
