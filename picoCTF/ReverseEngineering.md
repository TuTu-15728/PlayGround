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

