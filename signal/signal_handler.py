import signal
import time


# Define a signal handler // sig = signal number

def signal_handler(sig, frame):

    print(f'Received signal: {sig}. Exiting gracefully.')
    exit(0)


# Register the signal handler //SIGINT: interuption

signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to exit the process.')

# Main loop

while True:
    time.sleep(1)

