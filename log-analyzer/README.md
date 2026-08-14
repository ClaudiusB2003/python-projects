# Log Analyzer
A command-line Log Analyzer written in Python to strengthen my knowledge of **Python (OOP)**, **Networking**, and **Cyber Security**.
This project builds on my previous Subnet Calculator project and is my first attempt at working with **classes**.

---

## Project Goal
The goal of this project is to parse and analyze real switch log files (Aruba AOS-CX) in order to:
- Practice writing and using **Python classes** (constructors, attributes, methods)
- Learn how to parse semi-structured log data
- Detect suspicious patterns, such as repeated failed SSH login attempts (brute-force indicators)
- Deepen my understanding of network security monitoring

---

## Status
🚧 Early development — currently working on the `LogEntry` class to parse individual log lines.

---

## Planned Features
- `LogEntry` class representing a single parsed log line (timestamp, host, process, event ID, severity, message)
- `LogAnalyzer` class to read a log file and manage a collection of `LogEntry` objects
- Filtering of SSH-related events (successful logins, failed password logins, rejected public key attempts)
- Brute-force detection (e.g. X failed logins from the same IP within Y minutes)
- Summary report of suspicious activity

---

## Technologies
- Python 3
- Standard Library only (planned: `datetime`, possibly `re`)

No external dependencies are required so far.

---

## Example Log Source
Log data is collected manually from an Aruba AOS-CX switch via SSH (`show logging` or similar), then saved to a local `.txt` file for analysis.

Example log line:
```text
2026-08-13T13:49:00.716220+02:00 SW13 log-proxyd[754]: Event|5210|LOG_ERR|CDTR|1|User cibadmin login from 10.30.1.43 for SSH session failed during password based authentication.
```

---

## Project Structure
```text
log-analyzer/
│
├── main.py
├── switch_log.txt
├── CHANGELOG.md
└── README.md
```
The structure will evolve as the project grows.

---

## Learning Objectives
- Learn Python classes and object-oriented programming
- Practice parsing and structuring semi-structured text data
- Improve understanding of SSH-related log events
- Build software incrementally, starting from a single small class

---

## Author
Claudius B. — Apprentice IT Specialist, System Integration

## License
This project is licensed under the MIT License.