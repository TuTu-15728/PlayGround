
## StegoRSA

> A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message?
> Download the [flag](https://challenge-files.picoctf.net/c_plain_mesa/cd9616cb1438a2015db0304064b5aa01eea61b24b2f57b0559c257d798c9fc0c/flag.enc) and [image](https://challenge-files.picoctf.net/c_plain_mesa/cd9616cb1438a2015db0304064b5aa01eea61b24b2f57b0559c257d798c9fc0c/image.jpg).

`file` command shows - 

```
flag.enc:  data

image.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d494945766749424144414e42676b71686b6947397730424151454641415343424b67", baseline, precision 8, 512x512, components 3
```

A `hex` value of the private key - 

```
b'-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKg'

```


Draft Code - 

```python

# import pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.Random import get_random_bytes

private_key_hex = "2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d494945766749424144414e42676b71686b6947397730424151454641415343424b67776767536b41674541416f49424151444658326d6838754467515354670a6166765a307a59767250504b2f664a4b6772505855364d6d616139534132504c7377317074565a497a514b6d4c6b2b774375325744524d6e37557252765870610a452f517552475869547a5a704e6942434e6c4c595276424d4f496a3479724e6568674f544b6c6a725273467a72747932305332593847444934476a55674866560a306f7739786e774c414865463646304e456468486c434b554a6655484e79436d75505a3270474b4c596a4737723836796f5766667358794d486f4d69704d2f4f0a5271536e69536646663138382b6e46664e4a475745575848526b72416d2f415a6e666a6146754754596c45644e45634367695667516b3032486d307646702f540a7036327a62756347664e357679437566544357777a313445794d5046374d4371315154365531346468366152795550715a7739424c46374f5668334a3837584e0a484271326753757641674d424141454367674541482f4c6b5a666372534a477939764b67396d38576a3977577349367632446a56424b2b417374696272524a6f0a5a704a4b777767372b64665a724733467233447461594d665454432f6b6a6a7949372b6b494a4d6f7a4e7657716d7739423472456d55624f59674171783938440a37764b52684a4a7678314879515a675747532b2b436b6f7132496c653372735736744645713046455667475331325734486b503774775a334848555364304b2f0a75643670664179507367484f5939676944754761386650674c6f773670664e7a4552412b664341653465723072715a447341694e732f4f49702b6e467469445a0a316f43644b752f797a666d693358766469445637784e52673630355458504465594d503757584a68714f36312f45595939675a594d32596276514668785067360a453876566a41707630736e4f4a6c775875756d786438315878724f6d6d376d37396e46564a76685542514b4267514451346458354b7138436d617547344536630a4a4a75545679366d36536632354b38697665523958785a354667316b694176624e6a4b3362594941536875754e314b33734338724768786639396d49776b44320a766c6f544a7a766e2f6d506234395050586e43466f58567949772f71497372494b2f4c2b65466c655664364c2b336761645649774b446368596f7053456937560a695a42796b5950506e563768383874595661666c3343555178514b426751447835504b39493057436951477276775a466f575742444846634b505331687437300a715944415375483649622b596e784875592b48726e685a636f6b6857725835306d5833335943786554677958337a76354c344c326e7565756b734a683068704e0a505457622f504173364968565a514c446e38526a654b533942466d55487a533249715274495676644378457848686638565131492b556e6158306171336e5a320a592b6d4c5265447034774b42674533694a747045354152674c2b6957636a6b654854514f366349715a5642566245665437674968466b7748774f3666473279640a424d51482f4e55477a4e4e6b70563841506c5966346a79574f5849596e41686b61556d433833394a427772534a41504a2f734b5574536e646b4f3249453377580a687638432b4b2b4837506263794b6430337a5139696e445551536267794c32754555486d702f4d64686d6452633578344d3659744d315452416f4742414b466c0a38644468522b2f68476f784e3252463872773138442b632b4c496b79684845613642316c32594863497372693245514877535a4652515a71415870554b4a77450a446c695167776f70615a32734259677565324f7967304f6f434b7263565642554677454e732f4e43394453475157486c714650326d335444416b496930446a320a7846394d6373373649323579646536586b565776662b65457974495876564d684e794d4762527568416f4742414a54614f48464f57495332306c506247524a510a7251532b454d6754484933693732303043424c687733444548594266473141652b7a3735367a4f574a31595632476761527850354765376e45513171384155530a482b50484a486a3337694862572b5a7571556a576434643056646b632b315041757257726a6e362f6756496d6c585342456b76544546712b704336414f7469550a75486e6d495375493476676d5753614b6f576363674f6a520a2d2d2d2d2d454e442050524956415445204b45592d2d2d2d2d0a"
# private_key = (bytes.fromhex(private_key_hex))
# print(private_key)

with open("flag.enc", 'rb') as f:
	ciphertext = f.read()
	# print(ciphertext)

# def rsa_decrypt(data, private_key):
# 	private_key = RSA.import_key(private_key)
# 	cipher = PKCS1_OAEP.new(private_key)
# 	decrypted = cipher.decrypt(data)
# 	return decrypted.decode()

# def rsa_decrypt(ciphertext, private_key):
# 	rsa_private_key = RSA.importKey(private_key)
# 	rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
# 	decrypted_text = rsa_private_key.decrypt(ciphertext)
# 	# private_key = RSA.import_key(private_key)
# 	# cipher = PKCS1_OAEP.new(private_key)
# 	# decrypted = cipher.decrypt(ciphertext)
# 	return decrypted.decode()



def rsa_decrypt(ciphertext, private_key_hex):
	# Convert hex to bytes
	private_key_bytes = bytes.fromhex(private_key_hex)

	# Import the key (works for DER format too)
	rsa_private_key = RSA.import_key(private_key_bytes)

	cipher = PKCS1_v1_5.new(rsa_private_key)
	decrypted = cipher.decrypt(ciphertext, None)
	print(decrypted.decode())


	# # Try OAEP first
	# try:
	# 	cipher = PKCS1_OAEP.new(rsa_private_key)
	# 	decrypted = cipher.decrypt(ciphertext)
	# 	print(decrypted.decode())
	# except:
	# 	# Try v1.5
	# 	cipher = PKCS1_v1_5.new(rsa_private_key)
	# 	decrypted = cipher.decrypt(ciphertext, None)
	# 	print(decrypted.decode())

	# cipher = PKCS1_OAEP.new(rsa_private_key)
	# decrypted_text = cipher.decrypt(ciphertext)
	# return decrypted_text.decode()

print(rsa_decrypt(ciphertext, private_key_hex))

# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
# from Crypto.Util.number import bytes_to_long, long_to_bytes

# private_key_bytes = bytes.fromhex(private_key_hex)
# private_key = RSA.import_key(private_key_bytes)

# with open('file.enc', 'rb') as f:
#     ciphertext = f.read()

# print(f"Key size: {private_key.size_in_bytes()} bytes")
# print(f"Ciphertext size: {len(ciphertext)} bytes")
# print("-" * 40)

# # 1. Try OAEP
# try:
#     cipher = PKCS1_OAEP.new(private_key)
#     decrypted = cipher.decrypt(ciphertext)
#     print("✓ OAEP SUCCESS:")
#     print(decrypted.decode())
#     exit()
# except Exception as e:
#     print(f"✗ OAEP failed: {e}")

# # 2. Try PKCS1_v1_5
# try:
#     cipher = PKCS1_v1_5.new(private_key)
#     decrypted = cipher.decrypt(ciphertext, None)
#     if decrypted:
#         print("✓ PKCS1_v1_5 SUCCESS:")
#         print(decrypted.decode())
#         exit()
#     else:
#         print("✗ PKCS1_v1_5 failed: Decryption returned None")
# except Exception as e:
#     print(f"✗ PKCS1_v1_5 failed: {e}")

# # 3. Try Raw RSA
# try:
#     cipher_int = bytes_to_long(ciphertext)
#     decrypted_int = pow(cipher_int, private_key.d, private_key.n)
#     decrypted = long_to_bytes(decrypted_int)
#     print("✓ RAW RSA SUCCESS:")
#     print(decrypted.decode())
# except Exception as e:
#     print(f"✗ Raw RSA failed: {e}")

# print("\nAll padding schemes failed!")
```

Flag - `picoCTF{rs4_k3y_1n_1mg_6fdc126c}` - Padding `PKCS1_v1_5`

Ref:
- https://nhoyle-unsw.github.io/learn-encryption-with-python/rsa
- https://github.com/Jsujanchowdary/RSA-Encryption-and-Decryption-with-Python/blob/main/README.md
- https://github.com/Jsujanchowdary/RSA-Encryption-and-Decryption-with-Python/blob/main/rsa.py
- https://www.pycryptodome.org/src/examples

## Shared Secrets

> A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?
> Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/c8a5539995f5df2ced4781eae39980d1aae02329b3aadfcce172854a0ea27f98/message.txt) . And source [code](https://challenge-files.picoctf.net/c_plain_mesa/c8a5539995f5df2ced4781eae39980d1aae02329b3aadfcce172854a0ea27f98/encryption.py)

Source Code Logic - 

```python
from Crypto.Util.number import getPrime
from random import randint

# Public parameters
g = 2
p = getPrime(1048)

# Server's secret
a = randint(2, p-2)
A = pow(g, a, p)

# Client secret
b = '???'  

B = pow(g, b, p)

# Shared key
shared = pow(A, b, p)

# Encrypt flag
flag = b"picoCTF{...}"
enc = bytes([x ^ (shared % 256) for x in flag])

# Write challenge info
with open("file.txt", "w") as f:
    f.write(f"g = {g}\n")
    f.write(f"p = {p}\n")
    f.write(f"A = {A}\n")
    f.write(f"b = {b} \n")
    f.write(f"enc = {enc.hex()}\n")

```

From the `message.txt` file we can recover important data - 


Decryption Code - 

```python
from Crypto.Util.number import getPrime
from random import randint


p = 2132004026303109138960419370582104845382939159231816273620696701294630284403386465532863373769144582236949856392667504369986764250039517010152815931140874682590496582913679422125500008296870534246366594745735993256988714723377030293374496770744770410547817411606458596058022709758993968788819254528632650187419776389
A = 1141933368749651547285106584770022946598556294532255484018234071279017284493261458304303078441814350280055235938839850330392924394827971935746684756724106154783529866206686364342391780819577389806835022154187096665229978275413748714049243740736779489018438278478708068573511338451873371736513057724525994219285563327
b = 738623211561746372624170944030870485944978187433844583412325760777341380867104112487743286812112394661187612902430214202202766378016375904891604068375412515990443266634874912487423407082997026224391496763715710675145163967715339675283689424507137408425143581496186446869723885557865390662886201409684909929549168034


shared = pow(A, b, p)

print(shared)

enc_hex = "928b818da1b6a499868abd91d18190d196bdd1d08781d0d4d5db9f"
enc = bytes.fromhex(enc_hex)


flag = bytes([x ^ (shared % 256) for x in enc])

print(flag.decode())
```

Flag - `picoCTF{dh_s3cr3t_32ec2679}`

## hashcrack

> A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

```shell
nc verbal-sleep.picoctf.net 51785
```

```
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: 
```

Crack - 

```shell
hashcat -m 0 -a 0 "482c811da5d5b4bc6d497ffa98491e38" /usr/share/wordlists/rockyou.txt
```

MD5 - 

```
482c811da5d5b4bc6d497ffa98491e38:password123              
```

```
Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: 
```

```shell
hashcat -m 100 -a 0 "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3" /usr/share/wordlists/rockyou.txt
```

SHA1 - 
```
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3:letmein          
```

```
Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: 
```

```shell
hashcat -m 1400 -a 0 "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745" /usr/share/wordlists/rockyou.txt
```

```
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745:qwerty098
```

Flag - 

```
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_eb2f8459}
```

## EVEN RSA CAN BE BROKEN???

> This service provides you an encrypted flag. Can you decrypt it with just N & e?

Source Code - 

```python
from sys import exit
from Crypto.Util.number import bytes_to_long, inverse
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()

```

Data - 

```
N: 23897311148756791090076109004524867456885030504047423716053705064280914657734477469662651797765567296805094489350279294591307677217797633969785697006732282
e: 65537
cyphertext: 15689246967244292829534272511981580226097597423308492404425942632434927015670066927659133297872624077425623709533010457169674589926419544405403501584313597
```

Flag - 

```python

from Crypto.Util.number import bytes_to_long, long_to_bytes
import sympy

N = 23897311148756791090076109004524867456885030504047423716053705064280914657734477469662651797765567296805094489350279294591307677217797633969785697006732282
e = 65537
ciphertext = 15689246967244292829534272511981580226097597423308492404425942632434927015670066927659133297872624077425623709533010457169674589926419544405403501584313597


# Step 1: Factor N to get p and q
p, q = sympy.factorint(N).keys()

print(p, q)

# Step 2: Calculate private key d
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

# Step 3: Decrypt
decrypted_int = pow(ciphertext, d, N)
message = long_to_bytes(decrypted_int).decode('utf-8')

print(message)
```

```
picoCTF{tw0_1$_pr!m3de643ad5}
```

Ref:
- https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/

## interencdec

> Can you get the real meaning from this file. Download the file [here](https://artifacts.picoctf.net/c_titan/3/enc_flag)

```
enc_flag:  YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==
```

Base64 and Base64 decode - 

```
wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}
```

ROT19 - 

```
picoCTF{caesar_d3cr9pt3d_b204adc6}
```

## Mod 26

> Cryptography can be easy, do you know what ROT13 is? [values.txt](https://challenge-files.picoctf.net/c_wily_courier/7308d0feb679bd59640c496b1c30bbeebeea746a0d58a6054189aa33b7706388/values.txt)

```
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}
```

ROT13 - 

```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
```

## The Numbers

> The numbers... what do they mean? [numbers.png](https://challenge-files.picoctf.net/c_fickle_tempest/7b39deba4212c233b1628c93f16639ed02ad90f51436d2a8914bb11f74a982d3/the_numbers.png)

```
16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14
```

Alphabet positions - 

```
picoctf{thenumbersmason}
```

## 13

> Cryptography can be easy, do you know what ROT13 is?

```
 cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
```

ROT13 - 
```
picoCTF{not_too_bad_of_a_problem}
```

## Timestamped Secrets

> Someone encrypted a message using AES in ECB mode but they weren’t very careful with their key. Turns out it’s derived from something as simple as the current time! Can you uncover the key and decrypt the flag?
> Download the encrypted message: [message](https://challenge-files.picoctf.net/c_plain_mesa/95b5340b7c7992206c61b8092b01ab36a563e2df91c5fb36aee43b647d720dbe/message.txt)
> You may also find the encryption script helpful: [code](https://challenge-files.picoctf.net/c_plain_mesa/95b5340b7c7992206c61b8092b01ab36a563e2df91c5fb36aee43b647d720dbe/encryption.py)


