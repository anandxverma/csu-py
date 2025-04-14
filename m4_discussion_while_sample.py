import time

__ACCESS_CODE = "Welcome@1"
__MAX_RETRIES = 3
__SLEEP_TIME = 10  # seconds

failed_attempts = 0
while True:
    access_code = input("Enter your access code: ")
    if access_code == __ACCESS_CODE:
        print("Access granted.")
        break
    else:
        failed_attempts += 1
        print(f"Incorrect password. You have {__MAX_RETRIES - failed_attempts} attempts left.")
        end_time = time.time()
    if failed_attempts == __MAX_RETRIES:
        print("Access denied. Too many failed attempts. Try after " + str(int(__SLEEP_TIME)) + " seconds.")
        time.sleep(__SLEEP_TIME)
        failed_attempts = 0
