| ![Nibbles](/Assets/Images/nibbles.png) | <br><br>Name - Nibbles<br>Difficulty - Easy<br>Type - Linux<br> |
| -------------------------------------- | --------------------------------------------------------------- |

```
$ echo 'MACHINE_IP nibbles.htb' | sudo tee -a /etc/hosts
```

# ⚝ Enumeration

Let's Start with a `nmap` scan - 

**Nmap Scan Result** - 
```
$ nmap -sCV -p- nibbles.htb

Nmap scan report for nibbles.htb (10.129.96.84)
Host is up (0.033s latency).
Not shown: 65533 closed tcp ports (conn-refused)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
|_  256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)

80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.81 seconds
```

"http://nibbles.htb/", the page source - 
```
<b>Hello world!</b> 

<!-- /nibbleblog/ directory. Nothing interesting here! -->
```

I did a simple gobuster scan on `http://nibbles.htb/`, but as expected nothing interesting. Let's target the `/nibbleblog/` directory as mentioned.

**Gobuster Scan Result** - 

```
$ gobuster dir -u http://nibbles.htb/nibbleblog/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -x php,js,txt -b 404,403
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://nibbles.htb/nibbleblog/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404,403
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,js,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
LICENSE.txt          (Status: 200) [Size: 35148]
README               (Status: 200) [Size: 4628]
admin                (Status: 301) [Size: 321] [--> http://nibbles.htb/nibbleblog/admin/]
admin.php            (Status: 200) [Size: 1401]
content              (Status: 301) [Size: 323] [--> http://nibbles.htb/nibbleblog/content/]
feed.php             (Status: 200) [Size: 302]
index.php            (Status: 200) [Size: 2987]
install.php          (Status: 200) [Size: 78]
languages            (Status: 301) [Size: 325] [--> http://nibbles.htb/nibbleblog/languages/]
plugins              (Status: 301) [Size: 323] [--> http://nibbles.htb/nibbleblog/plugins/]
sitemap.php          (Status: 200) [Size: 402]
themes               (Status: 301) [Size: 322] [--> http://nibbles.htb/nibbleblog/themes/]
update.php           (Status: 200) [Size: 1622]
Progress: 81924 / 81924 (100.00%)
===============================================================
Finished
===============================================================
```

Some Notes from `README` file - 
```
====== Nibbleblog ======
Version: v4.0.3
Codename: Coffee
Release date: 2014-04-01

===== System Requirements =====
* PHP v5.2 or higher
* PHP module - DOM
* PHP module - SimpleXML
* PHP module - GD
* Directory â€œcontentâ€ writable by Apache/PHP

Optionals requirements

* PHP module - Mcrypt

===== Installation guide =====
1- Download the last version from http://nibbleblog.com
2- Unzip the downloaded file
3- Upload all files to your hosting or local server via FTP, Shell, Cpanel, others.
4- With your browser, go to the URL of your web. Example: www.domain-name.com
5- Complete the form
6- Done! you have installed Nibbleblog
```

I quickly googled for possible exploits for the specific nibbleblog version. And, found CVE-2015-6967(https://www.exploit-db.com/exploits/38489) for Arbitrary File Upload vulnerability.

Possibly, we can upload a php to get a reverse shell. But, this exploit needs login access (i.e., Username and Password).

Let's try to get some more information -

"http://nibbles.htb/nibbleblog/admin/" shows a few directories and files but not getting any clue from there.

Found the login page (Require - Username and Password) -
![Login Page](/Assets/Images/nibbles-1.png)

Further scan with gobuster reveals -
```
$ gobuster dir -u http://nibbles.htb/nibbleblog/content/private/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -x php,js,txt,xml -b 404,403
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://nibbles.htb/nibbleblog/content/private/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404,403
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              xml,php,js,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
categories.xml       (Status: 200) [Size: 325]
comments.xml         (Status: 200) [Size: 431]
config.xml           (Status: 200) [Size: 1935]
keys.php             (Status: 200) [Size: 0]
notifications.xml    (Status: 200) [Size: 1138]
pages.xml            (Status: 200) [Size: 95]
plugins              (Status: 301) [Size: 339] [--> http://nibbles.htb/nibbleblog/content/private/plugins/]
posts.xml            (Status: 200) [Size: 93]
shadow.php           (Status: 200) [Size: 0]
tags.xml             (Status: 200) [Size: 97]
users.xml            (Status: 200) [Size: 503]
Progress: 102405 / 102405 (100.00%)
===============================================================
Finished
===============================================================
```

If we visit `users.xml` file, we can get some interesting data.
1. We can find a proper user (Username - admin).
2. The website has some blocking mechanisms even with first incorrect login attempt.

```
<users>
<user username="admin">
<id type="integer">0</id>
<session_fail_count type="integer">2</session_fail_count>
<session_date type="integer">1779092901</session_date>
</user>
<blacklist type="string" ip="10.10.10.1">
<date type="integer">1512964659</date>
<fail_count type="integer">1</fail_count>
</blacklist>
</users>
```

We can't brute force the password field or even test our random password. We need a correct password for the access.

Next, I tried checking other files for a clue (hard-coded password or hash) but no information there.

I googled for the default credentials but found that we can set a password during the setup. I got a clue for the demo account it's `admin` and `demo` as username and password. But that's not correct in our case ...

We need correct password to login and also for the exploit to run. From the website we can only get the username. BTW it's an easy machine/challenge...

Our next option, we have to note-down all important keywords we can get from the website. And, luckily `nibbles` is the password for `admin` user (Keep in mind to restart the machine for every failed attempt !!!). Well, that was an easy password.

👉 Note: Sometimes the password we are looking maybe not in the wordlist used during the bruteforcing attack. We can generate a custom wordlist by using the keywords mentioned in the website (e.g. names, numbers, etc.).

# ⚝ Exploitation

Let's login with the username - `admin` and password - `nibbles` :

![Admin Login Page](/Assets/Images/nibbles-2.png)

Well, we got the access. Now let's find where we can upload our php reverse shell. If we check `Plugins > My image > configure`, we will find our intended page. Check the below image - 

![File Upload](/Assets/Images/nibbles-3.png)

```
Note : At this moment we can simply use the above exploit i.e. from exploit-db CVE-2015-6967 as we get our username and password.

Otherwise, let's break it down and do it manually probably we will take some reference if it's require.
```

I used this excellent php reverse shell file from - https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php and yes changed the IP and PORT as intended.

After uploading our payload - 
![Warnings](/Assets/Images/nibbles-4.png)

Now, a few things here - 
- We can see a few warnings from `resize.class.php`. I was a bit confuse about `imagedestroy()` mentioned in the warnings but that's not affecting our file upload. We can fix those by changing the `Content-Type` from `multipart/form-data` to `application/x-www-form-urlencoded` in the `burpsuite`.
- The directory (full path) where the file is placed i.e. `http://nibbles.htb/nibbleblog/content/private/plugins/my_image/`.
- Finally, the file name getting changed e.g. from `rev.php` to `image.php`. We can detect that from a gobuster scan.

# ⚝ Initial Access

Let's focus on getting our shell now. First, start a listener on the specified port and visit `http://nibbles.htb/nibbleblog/content/private/plugins/my_image/image.php` to trigger our payload.

![NC Listner](/Assets/Images/nibbles-5.png)

We can get our first flag from user home directory - 

![User Flag](/Assets/Images/nibbles-6.png)

# ⚝ Privilege Escalation

We can check the `personal.zip` file for further inspection. But, before that I simply ran `sudo -l` just to check for commands `nibbler` can run with root privilege.

Check the image - 
![Sudo -l](/Assets/Images/nibbles-7.png)

Now, we can unzip and edit the monitor.sh file inside the mentioned folder. Or, simple follow my steps - 

![Script Craetion](/Assets/Images/nibbles-8.png)

Explanation -
- I created the folders manually `personal/stuff` and also a file named `monitor.sh` just to maintain the above format.
- `cp /bin/bash /tmp/bash && chmod u+s /tmp/bash` command will copy the root owned bash binary and place in the `/tmp`. Also, sets the SUID bit so whoever runs the file will get root privilege / root shell.
- Finally, executable permission using `chmod +x`.
- A simple and easy privilege escalation technique for this kind of scenario.

We have to keep in mind when executing the file mention the full path as shown in the `sudo -l` output.

![Root flag](/Assets/Images/nibbles-9.png)
The `-p` flag prevents bash from dropping privileges, spawning a root shell (https://gtfobins.org/gtfobins/bash/).

Finally, we can retrieve our root flag.

! Happy Hacking !