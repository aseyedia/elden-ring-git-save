import psutil
import time
import os


def is_elden_ring_running():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if 'eldenring.exe' in process.info['name']:  # Assuming the process name is 'EldenRing.exe'
            return True
    return False


def main():
    elden_ring_was_running = False

    while True:
        elden_ring_is_running = is_elden_ring_running()

        if elden_ring_was_running and not elden_ring_is_running:
            print("Elden Ring has just closed. Initiating backup...")
            os.system("python main.py")
        elif elden_ring_is_running:
            print("Elden Ring is currently running...")

        elden_ring_was_running = elden_ring_is_running

        time.sleep(10)  # check every 10 seconds


if __name__ == "__main__":
    print("Monitoring script started.")
    main()
