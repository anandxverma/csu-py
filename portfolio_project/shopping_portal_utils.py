import time

"""Utility functions for the shopping portal project."""

# Function to print blinking text in the console
def print_blinking_text(text, duration_sec, interval_sec=0.5):
    """Prints blinking text for a specified duration.
    Args:
        text: The text to blink.
        duration_sec: The total duration for blinking in seconds.
        interval_sec: The interval between blinks in seconds.
    """
    start_time = time.time()
    while time.time() - start_time < duration_sec:
        print(text, end="\r")  # Print text, carriage return to overwrite
        time.sleep(interval_sec)
        print(" " * len(text), end="\r")  # Print spaces to clear text
        time.sleep(interval_sec)