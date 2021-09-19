# Xdebug-OS-Command-Execution

## Descripción
Remote Command Execution 
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
