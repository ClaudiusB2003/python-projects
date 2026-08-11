# Subnet Calculator
A simple command-line Subnet Calculator written in Python to strengthen my knowledge of **Python**, **Networking**, and **Cyber Security**.
This project is part of my learning journey and is being developed step by step.

---

## Version 2
![Subnet Calculator Screenshot](screenshot.png)

---

## Features
- Interactive main menu (Network Information / Subnet Calculator / Exit)
- Accepts IPv4 addresses in CIDR notation
- Splits a network into a given number of equal-sized subnets
- Calculates network address for each subnet
- Calculates broadcast address for each subnet
- Displays subnet mask and wildcard mask
- Displays CIDR prefix and network class
- Displays first and last usable host
- Displays maximum usable hosts per subnet
- Detects whether the input IP is private
- Interactive "calculate another subnet" loop

### Planned
- Variable Length Subnet Masking (VLSM)
- Input validation with helpful error messages
- IPv6 support
- Binary representation of subnet masks
- Export results as JSON or CSV
- Colorized terminal output
- Unit tests

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
- IPv4 addressing
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
You will be greeted by the main menu and can choose between viewing network information, running the subnet calculator, or exiting the program.

---

## Example

**Main Menu**
```text
========================================
      Welcome to the Subnet Calculator
========================================

1. Network Information

2. Subnet Calculator

3. Exit

Choice: 2

Please input an ip address (CIDR format): 192.168.1.1/24

How many subnets do you need?: 4
```

**Output**
```text
========================================
            Subnet Information
========================================
Network Address     : 192.168.1.0
Broadcast           : 192.168.1.63
Subnet Mask         : 255.255.255.192
Wildcard Mask       : 0.0.0.63
CIDR Prefix         : 26
First Host          : 192.168.1.1
Last Host           : 192.168.1.62
Usable Hosts        : 62
Private Address     : Yes
Network class       : C
========================================
            Subnet Information
========================================
Network Address     : 192.168.1.64
Broadcast           : 192.168.1.127
Subnet Mask         : 255.255.255.192
Wildcard Mask       : 0.0.0.63
CIDR Prefix         : 26
First Host          : 192.168.1.65
Last Host           : 192.168.1.126
Usable Hosts        : 62
Private Address     : Yes
Network class       : C
========================================
            Subnet Information
========================================
Network Address     : 192.168.1.128
Broadcast           : 192.168.1.191
Subnet Mask         : 255.255.255.192
Wildcard Mask       : 0.0.0.63
CIDR Prefix         : 26
First Host          : 192.168.1.129
Last Host           : 192.168.1.190
Usable Hosts        : 62
Private Address     : Yes
Network class       : C
========================================
            Subnet Information
========================================
Network Address     : 192.168.1.192
Broadcast           : 192.168.1.255
Subnet Mask         : 255.255.255.192
Wildcard Mask       : 0.0.0.63
CIDR Prefix         : 26
First Host          : 192.168.1.193
Last Host           : 192.168.1.254
Usable Hosts        : 62
Private Address     : Yes
Network class       : C

Press Enter to return
```

---

## Project Structure
```text
subnet-calculator/
│
├── main.py
├── CHANGELOG.md
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
