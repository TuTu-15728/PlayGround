---
topic:
date: "{{date}}"
tags:
links:
---
**TOC**:
- [Example Module](#ExampleModule)
	1. [Room 1](#Room1)
	2. [Room 2](#Room2)
	3. [Room 3](#Room3)


Enumerate a running internal service, exploit a vulnerable web application, pivot through the system, and crack your way to root.

Nmap Scan:
```raw
Nmap scan report for 10.82.130.212
Host is up (0.024s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 d9:b8:f5:96:4a:7a:bd:1f:67:09:11:e9:db:fb:35:1d (ECDSA)
|_  256 f6:cd:e9:82:8f:38:6a:92:24:94:6e:bf:f6:2f:35:7a (ED25519)
5050/tcp open  http    Werkzeug httpd 2.0.2 (Python 3.10.12)
|_http-server-header: Werkzeug/2.0.2 Python/3.10.12
|_http-title: CorpNet \xE2\x80\x94 Network Operations Centre
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

Gobuster Scan:
```shell
$ gobuster dir -u http://10.82.130.212:5050/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.82.130.212:5050/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/internal             (Status: 200) [Size: 8770]
Progress: 20481 / 20482 (100.00%)
===============================================================
Finished
===============================================================

```

`/internal`
```shell
$ gobuster dir -u http://10.82.130.212:5050/internal/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -x py,txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.82.130.212:5050/internal/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              py,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/dashboard            (Status: 302) [Size: 224] [--> http://10.82.130.212:5050/internal]
/health               (Status: 302) [Size: 224] [--> http://10.82.130.212:5050/internal]
/logout               (Status: 302) [Size: 224] [--> http://10.82.130.212:5050/internal]
Progress: 61443 / 61446 (100.00%)
===============================================================
Finished
===============================================================

```

`/dashboard` - nothing

Server: Werkzeug/2.0.2 Python/3.10.12

