zeile = "2026-08-13T13:49:08.296312+02:00 SW13 poe-protod[2950]: Event|7901|LOG_INFO|CDTR|1|Detected powered device on interface 1/1/23. Type:1, Class:3"

class LogEntry:

    def __init__(self, line):
        self.raw_line = line
        line.split(":")

log: LogEntry = LogEntry(zeile)
print(log.raw_line)