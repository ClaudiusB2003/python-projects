# Subnet Calculator

A simple command-line Subnet Calculator written in Python to strengthen my knowledge of **Python**, **Networking**, and **Cyber Security**.

This project is part of my learning journey and is being developed step by step.

---

## Features

### Current

* take user input
* return network object
* Display network address
* Display subnet mask
* Display broadcast address
* Display the maximum number of usable hosts

### Planned

* Parse IPv4 addresses in CIDR notation
* Input validation with helpful error messages
* IPv6 support
* Binary representation of subnet masks
* Variable Length Subnet Masking (VLSM)
* Export results as JSON or CSV
* Colorized terminal output
* Unit tests

---

## Technologies

* Python 3
* Standard Library

  * `ipaddress`

No external dependencies are required.

---

## Project Goal

The purpose of this project is **not** simply to build another subnet calculator.

Instead, the goal is to gain a deeper understanding of:

* IPv4 addressing
* CIDR notation
* Network calculations
* Python project structure
* Error handling
* Writing clean, maintainable code

---

## Example

**Input**

```text
192.168.1.42/24
```

**Output**

```text
Network Address  : 192.168.1.0
Subnet Mask      : 255.255.255.0
Broadcast        : 192.168.1.255
Usable Hosts     : 254
```

---

## Project Structure

```text
subnet-calculator/
│
├── main.py
└── README.md
```

The structure will evolve as the project grows.

---

## Learning Objectives

* Practice Python fundamentals
* Learn to work with the `ipaddress` module
* Improve networking knowledge
* Build software incrementally
* Learn basic software design principles
* Use Git and GitHub for version control

---

## Future Ideas

* Automatic subnet recommendations
* Route summarization
* Supernetting
* Interactive menu
* GUI version
* Web version using Flask or FastAPI

---

##Author 

Claudius B. Apprentice IT Specialist – System Integration

## License

This project is licensed under the MIT License.
