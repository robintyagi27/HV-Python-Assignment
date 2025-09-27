Here’s a well-structured documentation in **Markdown (.md)** format for your **Password Strength Checker** script:
---
#  Password Strength Checker

This Python script checks the strength of a given password based on multiple security criteria and provides feedback to help users improve weak passwords.
---
## Features

* Ensures password has a **minimum length** (8 characters).
* Requires at least **one uppercase letter**.
* Requires at least **one lowercase letter**.
* Requires at least **one digit**.
* Requires at least **one special character** (`!@#$%^&*()_+{}[]:;"'<>,.?/~`-=|\`).
* Provides **feedback messages** if the password does not meet criteria.
* Interactive CLI loop until the user types `quit`.

---

##  Requirements

* Python 3.x
* Standard library (`re` for regular expressions)

---

## File Structure

```
password_checker.py   # Main script
README.md             # Documentation (this file)
```

---

##  Usage

1. Save the script as `password_checker.py`.
2. Run it in your terminal:

   ```bash
   python password_checker.py
   ```
3. Enter a password when prompted.

   * To exit, type `quit`.

---

##  Example Run

```text
--- Password Strength Checker ---
Enter a password to check (or 'quit' to exit): weak123

Password Strength: WEAK
Your password does NOT meet the required criteria. Please address the following:
- Password must contain at least one uppercase letter.
- Password must contain at least one special character (!@#$%^&* etc.).
------------------------------

Enter a password to check (or 'quit' to exit): Strong@123

Password Strength: STRONG
Your password meets all the required criteria.
------------------------------
```
<img width="601" height="237" alt="image" src="https://github.com/user-attachments/assets/bb83d406-582d-4ad2-95bd-fd9fad61d63a" />

---

##  Code Overview

### Function: `check_password_strength(password)`

* **Input:** A string (the password).
* **Output:** Boolean (`True` if strong, `False` if weak).
* **Logic:**

  * Checks length (≥ 8).
  * Scans for uppercase, lowercase, digits, and special characters.
  * Prints feedback accordingly.

---

## Security Notes

* This is a **basic password strength checker**.
* For real-world applications, consider additional rules:
  * Prevent dictionary words or usernames.
  * Use password entropy calculations.
  * Integrate with libraries like `zxcvbn`.

 

CPU Health Monitor

This Python script uses the psutil library to monitor CPU usage in real-time and triggers alerts when the usage exceeds a defined threshold.

Features

Continuously monitors CPU usage.

Triggers an alert message if CPU usage exceeds a specified percentage.

Configurable threshold (default: 80%).

Configurable monitoring interval in seconds (default: 2s).

Gracefully stops with Ctrl + C.

Requirements

Python 3.x

Install psutil:

pip install psutil

Usage

Save the script as cpu_monitor.py.

Run it in your terminal:

python cpu_monitor.py


The script will display real-time CPU usage.

If usage crosses the threshold, an alert will appear.

Press Ctrl + C to stop monitoring.

Configuration

You can modify the default values directly in the script or pass them via function call:

CPU_THRESHOLD = 80    # Set CPU usage threshold (%)
MONITOR_INTERVAL = 2  # Set interval between checks (seconds)

monitor_cpu_health(threshold_percent=CPU_THRESHOLD, interval_seconds=MONITOR_INTERVAL)

Example Run
Monitoring CPU usage... (Alert threshold: 80%)
Press Ctrl+C to stop monitoring.
Current CPU usage: 15.2%
Current CPU usage: 27.8%
Alert! CPU usage exceeds threshold: 82.5%
Current CPU usage: 45.6%

Code Overview
Function: monitor_cpu_health(threshold_percent=80, interval_seconds=2)

Parameters:

threshold_percent (int) → CPU usage limit for alerts.

interval_seconds (int) → Interval between usage checks.

Process:

Uses psutil.cpu_percent(interval) to get CPU usage.

Compares usage against threshold.

Prints either current usage or alert message.

Error Handling:

KeyboardInterrupt → Stops monitoring gracefully.

Other exceptions → Displays error message.

Notes

psutil.cpu_percent(interval) blocks for the given interval and gives a smoothed average over that period.

The script is intended for local monitoring. For production or server monitoring, consider integrating with:

Logging frameworks

System monitoring tools (Prometheus, Grafana, etc.)

Notification systems (Slack, Email, etc.)
