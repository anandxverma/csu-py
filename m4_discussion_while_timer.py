import time

# Constants
__ACCESS_CODE = "Welcome@1" # The access code to be guessed
__MAX_RETRIES = 3 # Maximum number of attempts before lockout
__SLEEP_TIME = 10 # Time (in seconds) to wait before allowing another attempt

failed_attempts = 0
while True:
    access_code = input("Enter your access code: ")
    # Allow access if the access code macthes
    # Else increment the failed attempts
    if access_code == __ACCESS_CODE:
        print("Access granted.")
        break
    else:
        failed_attempts += 1
        print(f"Incorrect password. You have {__MAX_RETRIES - failed_attempts} attempts left.")
    # If the maximum number of attempts has reached, wait for a while before allowing another attempt
    if failed_attempts == __MAX_RETRIES:
        print("Access denied. Too many failed attempts. Try after " + str(int(__SLEEP_TIME)) + " seconds.")
        time.sleep(__SLEEP_TIME)
        failed_attempts = 0
