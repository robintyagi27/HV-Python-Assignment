import psutil
import time

def monitor_cpu_health(threshold_percent=80, interval_seconds=2):
    """
    Continuously monitors CPU usage and displays an alert if it exceeds a threshold.

    Args:
        threshold_percent (int): The CPU usage percentage beyond which an alert is triggered.
                                 Default is 80%.
        interval_seconds (int): The time interval (in seconds) between CPU usage checks.
                                Default is 2 seconds.
    """
    print(f"Monitoring CPU usage... (Alert threshold: {threshold_percent}%)")
    print("Press Ctrl+C to stop monitoring.")

    try:
        while True:
            # Get current CPU usage as a percentage
            # interval=None means non-blocking, but psutil recommends using a small interval
            # for more accurate initial readings if this is the first call.
            # Here, we pass 'interval_seconds' to cpu_percent to make it block
            # for that duration, which helps in getting accurate usage over time.
            cpu_usage = psutil.cpu_percent(interval=interval_seconds)

            # Check if CPU usage exceeds the predefined threshold
            if cpu_usage >= threshold_percent:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"Current CPU usage: {cpu_usage}%")

            # Wait for the specified interval before the next check (already handled by cpu_percent's interval)
            # time.sleep(interval_seconds) # Not needed here as cpu_percent handles it
    except KeyboardInterrupt:
        # Handle user interruption (Ctrl+C)
        print("\nCPU monitoring stopped by user.")
    except Exception as e:
        # Handle other potential exceptions during monitoring
        print(f"\nAn error occurred during CPU monitoring: {e}")

# Main execution block
if __name__ == "__main__":
    # You can change the threshold and interval here if needed
    CPU_THRESHOLD = 80  # Percentage
    MONITOR_INTERVAL = 2 # Seconds

    monitor_cpu_health(threshold_percent=CPU_THRESHOLD, interval_seconds=MONITOR_INTERVAL)