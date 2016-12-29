import subprocess
import signal
import sys

servers = [ '192.168.1.1',
            '192.168.1.190',
            'www.google.com',
            'www.yahoo.com',
            'www.yahoo.in',
            'www.snapchat.com',
            'www.facebook.com',
            'www.instagram.com',
            'www.oracle.com',
            'www.youtube.com',
            'www.whatsapp.com',
            'www.ozee.com',
            'www.hotstar.com',
            'people.us.oracle.com',
            'slc11bxs.us.oracle.com',
            'inexistentwebsite832439.com'
            ]

def get_ping_time(server):
    "Returns the ping time of 'server' in milliseconds"
    p = subprocess.Popen(['ping', '-n', '1', '-w', '1000', server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode('utf-8')
    err = err.decode('utf-8')

    # Find the position of the word 'Average' to get ping time
    ping_time = out.find('Average')
    try:
        return round(float(out[(ping_time+10):].strip()[:-2]))
    except ValueError:
        return -1

def get_print_ping_string(server):
    "Get the printable line that displays the ping of the server"
    ping_time = str(get_ping_time(server))
    if ping_time == '-1':
        ping_time = '*'
    return '{:30}:'.format(server) + ' ' + '{:>10}'.format(ping_time) + ' ' + 'ms'

def signal_handler(signal, frame):
    subprocess.call('cls', shell=True)
    sys.exit(0)

def main():
    while(True):
        buf = ''
        for server in servers:
            buf = buf + get_print_ping_string(server) + '\n'
        print(buf)
        for i in range(len(servers) + 1):
            print("\033[F", end='')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    subprocess.call('cls', shell=True)
    main()
