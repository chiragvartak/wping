"Continuously monitor specified servers; if you wish to store output to a file, use this module instead of wping.py."

import subprocess
import signal
import sys
import time
from wping import servers, get_print_ping_string

def signal_handler(signal, frame):
    sys.exit(0)

def main():
    while(True):
        print(time.strftime('%d %b %Y, %H:%M'), flush=True)
        for server in servers:
            print(get_print_ping_string(server), flush=True)
        print('', flush=True)
        time.sleep(120)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
