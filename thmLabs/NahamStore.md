
![NahamStore Image](/Assets/Images/nahamstore.png)

> In this room you will learn the basics of bug bounty hunting and web application hacking

# Setup

To start the challenge you'll need to add an entry into your  /etc/hosts or c:\windows\system32\drivers\etc\hosts file pointing to your deployed TryHackMe box.

When enumerating subdomains you should perform it against the **nahamstore.com** domain. When you find a subdomain you'll need to add an entry into your /etc/hosts or c:\windows\system32\drivers\etc\hosts file pointing towards your deployed TryHackMe box IP address and substitute .com for .thm . For example if you discover the subdomain whatever.nahamstore.com you would add the following entry:

`MACHINE_IP         something.nahamstore.thm`

# Recon

**Nmap Scan Results -** 
```shell
 ➥ $ nmap -sCV -p- nahamstore.thm

Nmap scan report for nahamstore.thm (10.80.142.133)
Host is up (0.015s latency).
Not shown: 65532 closed tcp ports (reset)

PORT     STATE SERVICE VERSION

22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 84:6e:52:ca:db:9e:df:0a:ae:b5:70:3d:07:d6:91:78 (RSA)
|   256 1a:1d:db:ca:99:8a:64:b1:8b:10:df:a9:39:d5:5c:d3 (ECDSA)
|_  256 f6:36:16:b7:66:8e:7b:35:09:07:cb:90:c9:84:63:38 (ED25519)

80/tcp   open  http    nginx 1.14.0 (Ubuntu)
|_http-title: NahamStore - Home
|_http-server-header: nginx/1.14.0 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     session: 
|_      httponly flag not set

8000/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

**Gobuster Scan Results -** 
```shell
 ➥ $ gobuster dir -u http://nahamstore.thm -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt 

===============================================================
Starting gobuster in directory enumeration mode
===============================================================
basket               (Status: 200) [Size: 2465]
css                  (Status: 301) [Size: 178] [--> http://127.0.0.1/css/]
js                   (Status: 301) [Size: 178] [--> http://127.0.0.1/js/]
login                (Status: 200) [Size: 3099]
logout               (Status: 302) [Size: 0] [--> /]
register             (Status: 200) [Size: 3138]
returns              (Status: 200) [Size: 3628]
robots.txt           (Status: 200) [Size: 13]
search               (Status: 200) [Size: 3351]
staff                (Status: 200) [Size: 2287]
uploads              (Status: 301) [Size: 178] [--> http://127.0.0.1/uploads/]
Progress: 20481 / 20481 (100.00%)
===============================================================
Finished
===============================================================

```

**FFUF Scan Results -** 
```shell

 ➥ $ ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/namelist.txt -u http://nahamstore.thm/ -H 'Host: FUZZ.nahamstore.thm' -fw 125


marketing       [Status: 200, Size: 2025, Words: 692, Lines: 42, Duration: 13ms]
shop            [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 13ms]
stock           [Status: 200, Size: 67, Words: 1, Lines: 1, Duration: 13ms]
www             [Status: 301, Size: 194, Words: 7, Lines: 8, Duration: 13ms]
```






# Task 4 - XSS

We've put quite a few XSS vulnerabilities into the web application. See if you can find them all and answer the questions below.

