import re
from datetime import datetime


def parse_log_file(filename):
    with open(filename, 'r') as f:
        log_lines = f.readlines()

    target_key = 'Key TSTFEED0300|7E3E|0400'
    return [line for line in log_lines if target_key in line]


def analyze_heartbeat(log_lines):
    timestamps = []

    for line in log_lines:
        timestamp_match = re.search(r'Timestamp (\d{2}:\d{2}:\d{2})', line)
        if timestamp_match:
            timestamps.append(datetime.strptime(timestamp_match.group(1), '%H:%M:%S'))

    with open('hb_test.log', 'w') as log_file:
        for i in range(1, len(timestamps)):
            interval = abs((timestamps[i] - timestamps[i - 1]).total_seconds())

            if 31 < interval < 33:
                log_file.write(
                    f"WARNING: Heartbeat at {timestamps[i].strftime('%H:%M:%S')} is {interval:.1f} seconds (31-33 sec range)\n")
            elif interval >= 33:
                log_file.write(
                    f"ERROR: Heartbeat at {timestamps[i].strftime('%H:%M:%S')} is {interval:.1f} seconds (>=33 sec)\n")


def main():
    log_lines = parse_log_file('hblog.txt')
    analyze_heartbeat(log_lines)


if __name__ == "__main__":
    main()