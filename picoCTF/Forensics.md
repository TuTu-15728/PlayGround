## Binary Digits

> This file doesn't look like much... just a bunch of 1s and 0s. But maybe it's not just random noise. Can you recover anything meaningful from this?
> Download the file [here](https://challenge-files.picoctf.net/c_plain_mesa/fc041c019da080f2d57c4f5e082de1f34261258b063e3c2cc6e42808b30463f9/digits.bin).

```python
# Convert binary string to bytes
binary_str = open('digits.bin').read().strip()
bytes_data = int(binary_str, 2).to_bytes(len(binary_str) // 8, 'big')

# Write to JPEG
with open('output.jpg', 'wb') as f:
    f.write(bytes_data)
```

Flag - 

```
picoCTF{h1dd3n_1n_th3_b1n4ry_2f96e9a1}
```

## Riddle Registry

> Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
> Find the PDF file here [Hidden Confidential Document](https://challenge-files.picoctf.net/c_amiable_citadel/ec88ce83253c1bd53af98533a401b9ea0b37602fd6276271c724d5cdd126b285/confidential.pdf) and uncover the flag within the metadata.

Flag - 

```shell
$ exiftool confidential.pdf

ExifTool Version Number         : 13.25
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2026:08:18 04:45:17+01:00
File Access Date/Time           : 2026:08:18 04:45:17+01:00
File Inode Change Date/Time     : 2026:08:18 04:45:17+01:00
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV8wZTJkZTVhMX0=

$ echo cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV8wZTJkZTVhMX0= | base64 -d
picoCTF{puzzl3d_m3tadata_f0und!_0e2de5a1}
```

## Hidden in plainsight

> You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

```shell
$ exiftool img.jpg 

ExifTool Version Number         : 13.25
File Name                       : img.jpg
Directory                       : .
File Size                       : 74 kB
File Modification Date/Time     : 2026:08:18 04:54:14+01:00
File Access Date/Time           : 2026:08:18 04:54:24+01:00
File Inode Change Date/Time     : 2026:08:18 04:54:14+01:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
Image Width                     : 640
Image Height                    : 640
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 640x640
Megapixels                      : 0.410
```

Clue - 

```
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
```

```shell
$ echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 -d
steghide:cEF6endvcmQ=

$ echo "cEF6endvcmQ=" | base64 -d
pAzzword
```

Extract flag - 

```shell
$ steghide extract -sf img.jpg -p pAzzword
wrote extracted data to "flag.txt".

$ cat flag.txt 
picoCTF{h1dd3n_1n_1m4g3_54e31417}
```

## Flag in Flame

> The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
> Download the encoded data here: [Logs Data](https://challenge-files.picoctf.net/c_amiable_citadel/3c1d1fea48e203c9c5d64c32d94aa1f091a6b72b4cebd35a761b09d4f9c0f0d2/logs.txt). Be prepared—the file is large, and examining it thoroughly is crucial .

```shell
$ cat logs.txt | base64 -d
```

`xxd` shows png data. saved the png file and got the following hex data - 

```
7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F35646161346132667D
```

```shell
$ echo "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F35646161346132667D" | xxd -r -p

picoCTF{forensics_analysis_is_amazing_5daa4a2f}
```

## Corrupted file

> This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?

```shell
$ xxd file | head -n 10
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
00000010: 0001 0000 ffdb 0043 0008 0606 0706 0508  .......C........
00000020: 0707 0709 0908 0a0c 140d 0c0b 0b0c 1912  ................
00000030: 130f 141d 1a1f 1e1d 1a1c 1c20 242e 2720  ........... $.' 
00000040: 222c 231c 1c28 3729 2c30 3134 3434 1f27  ",#..(7),01444.'
00000050: 393d 3832 3c2e 3334 32ff db00 4301 0909  9=82<.342...C...
00000060: 090c 0b0c 180d 0d18 3221 1c21 3232 3232  ........2!.!2222
00000070: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000080: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000090: 3232 3232 3232 3232 3232 3232 3232 ffc0  22222222222222..
```

It's a jpg file but the magic bytes are different.

```shell
$ xxd -p file | sed 's/^5c78ffe0/ffd8ffe0/' | xxd -r -p > output.jpg
```

Replaced the dummy data with proper magic bytes.

Flag - 

```
picoCTF{r3st0r1ng_th3_by73s_2326ca93}
```

## DISKO 1

> Can you find the flag in this disk image?

```shell
$ gzip -d disko-1.dd.gz

$ strings disko-1.dd | grep picoCTF*
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
```

## RED

> RED, RED, RED, RED
> Download the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)

```shell
$ zsteg -a red.png
```

Flag - 

```shell
$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

## Ph4nt0m 1ntrud3r

> A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.
> To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!
> Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/a681faccaaa199ce75c3abeef9525f813b6451644a8d8d27cc097e4b1ccb741a/myNetworkTraffic.pcap) and try to get the flag.

TSHARK - 

```shell
$ tshark -r myNetworkTraffic.pcap -Y "frame.time_relative >= 0" -T fields -e frame.time_relative -e tcp.payload | sort -n | awk '{print $2}' | xxd -r -p | base64 -d

{1t_w4snt_th4t_34sy_tbh_4r_d1065384}
```

## Verify

> People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

Clue - 

```
`ssh -p 60408 [ctf-player@rhea.picoctf.net](mailto:ctf-player@rhea.picoctf.net)`

Using the password `f3b61b38`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

- Checksum: fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
- To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.
```

Custom Script - 

```bash
cat > check_hash.sh << 'EOF'
#!/bin/bash

my_hash=$(cat checksum.txt)

for file in files/*; do
    if [ -f "$file" ]; then
        file_hash=$(sha256sum "$file" | awk '{print $1}')
        if [ "$file_hash" == "$my_hash" ]; then
            echo "Match found: $file"
        fi
    fi
done
EOF
```

Flag - 

```
ctf-player@pico-chall$ ./check_hash.sh 
Match found: files/87590c24

ctf-player@pico-chall$ ./decrypt.sh files/87590c24
picoCTF{trust_but_verify_87590c24}
```

## Scan Surprise

> I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?

Reading QR using `zbarimg` - 

```shell
$ sudo apt install zbar-tools

$ zbarimg flag.png
QR-Code:picoCTF{p33k_@_b00_3f7cf1ae}
scanned 1 barcode symbols from 1 images in 0.01 seconds
```

## Secret of the Polyglot

> The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

`xxd` shows it's a combination of `png` and `pdf` . `pdf` magic bytes starts at `25 50 44 46`.

```shell
$ xxd -p flag2of2-final.pdf | tr -d '\n' | sed 's/\(.*\)25504446.*/\1/' | xxd -r -p > extracted.png

$ xxd -p flag2of2-final.pdf | tr -d '\n' | sed 's/^.*\(25504446\)/\1/' | xxd -r -p > extracted.pdf
```

Flag - 

```
picoCTF{f1u3n7_1n_pn9_&_pdf_90974127}
```

## CanYouSee

> How about some hide and seek?

```shell
$ exiftool ukn_reality.jpg 
ExifTool Version Number         : 13.25
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:03:12 00:05:51+00:00
File Access Date/Time           : 2026:08:18 17:38:43+01:00
File Inode Change Date/Time     : 2026:08:18 17:38:35+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4

$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_3b9209a2}
```

