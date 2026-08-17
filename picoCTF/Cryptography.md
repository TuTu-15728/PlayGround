
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

Source - 

```python
from hashlib import sha256
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(plaintext: str, timestamp: int) -> str:
    timestamp = int(time.time())
    key = sha256(str(timestamp).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded)
    return ciphertext.hex()

if __name__ == "__main__":
  
    plaintext = "picoCTF{...}"
    result = encrypt(plaintext, key)
    print(f"Hint: The encryption was done around {timestamp} UTC\n")
    print(f"Ciphertext (hex): {ciphertext.hex()}\n")

```

Clue - 

```
Hint: The encryption was done around 1770242606 UTC
Ciphertext (hex): 24162f53d9b29255e635230b821cb8baca14461d54b2955401a049477e201fe9
```

Decryption - 

```python
from hashlib import sha256
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Given values
timestamp = 1770242606
ciphertext_hex = "24162f53d9b29255e635230b821cb8baca14461d54b2955401a049477e201fe9"

# Step 1: Convert hex to bytes
ciphertext = bytes.fromhex(ciphertext_hex)
# print(ciphertext)

# Step 2: Re-generate the key (same as encryption)
key = sha256(str(timestamp).encode()).digest()[:16]

# Step 3: Create AES cipher for decryption
cipher = AES.new(key, AES.MODE_ECB)

# Step 4: Decrypt
decrypted_padded = cipher.decrypt(ciphertext)

# Step 5: Remove padding
plaintext = unpad(decrypted_padded, AES.block_size)

# Step 6: Convert to string
message = plaintext.decode('utf-8')
print(message)
```

```
picoCTF{sa3S_sEc9t_081e3371}
```

## Small Trouble

> Everything seems secure; strong numbers, familiar parameters but something small might ruin it all. Can you recover the message?
> Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/8ed22a97d4a9277782228ea1a112e241287c34f3872ddf451445ebb690f0fe01/message.txt). And source [code](https://challenge-files.picoctf.net/c_plain_mesa/8ed22a97d4a9277782228ea1a112e241287c34f3872ddf451445ebb690f0fe01/encryption.py)

Source - 

```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long
import random

# Generate two large primes (1048 bits each)
p = getPrime(1048)
q = getPrime(1048)
n = p * q
phi = (p - 1) * (q - 1)

# compute d
d = getPrime(256)

# Compute the public exponent
e = inverse(d, phi)

# Encrypt a flag
flag = b'picoCTF{...}'
m = bytes_to_long(flag)
c = pow(m, e, n)

# Output for the challenge
with open("message.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
```

Clue -

```
n = 5594693087516809540399630533662256130165069234399367321216316625813041939300993769469967603569290419832603300499594108772793414518139869665356083286669649260446980521836343923879233640062756943840931863547930310945579712973265137792295790351161076685048473027951375342321268790017586922565818383182756032674465485490251320715340411385624938864566260868602337614069898840915970814299359393740587761535848189108678205178238800280288111230994607337322709256318074861115932027677894091130507029723017060154360297187479229724325679623356440638966942954291313437552982609848032044158878674696384027496524889634696452323607191723997392473
e = 1253741277266526276273737492341769420156287745742446683234137950307473941700753795420946118527838187324934980950852435452652395931456125106860289473635243147451566503774469323896054400225880927948949271325382686728252025525992064502049812510769890170584852893320391805480557992376841338269221082823514780592527932026224041016469532408356349643964521128610552886213674116475363116732306717431311560112424065793590597523162878957727018336437764277170504454532774662559560076329628335685182665402553483091574429654268002692354092642868885921538110973203434318377491643644652734769173448091279268078729903023902968710350828758115786949
c = 1575773147844095818115335246981689507608786190212845187250432450517265485011147541328871869339509244543151221056093233377208864758371954434810015700305579991328875661494910208600661149362933701275626110364421427594488043068010070893043333162678431541790213846097012150446212452859725911076627073141637069389589032187813548754572797526213109169925710036206244271861122294567316906395657015977496683800227620943713798410804779020204823690850145678294088525234958290370183071276300423260384932033932245873934561990566777751374865071948145184698603999279619026875789640532470724368003682471823004876010640755680214225037847875314158626
```

Flag - 

```python

from Crypto.Util.number import long_to_bytes
from owiener import attack

n = 5594693087516809540399630533662256130165069234399367321216316625813041939300993769469967603569290419832603300499594108772793414518139869665356083286669649260446980521836343923879233640062756943840931863547930310945579712973265137792295790351161076685048473027951375342321268790017586922565818383182756032674465485490251320715340411385624938864566260868602337614069898840915970814299359393740587761535848189108678205178238800280288111230994607337322709256318074861115932027677894091130507029723017060154360297187479229724325679623356440638966942954291313437552982609848032044158878674696384027496524889634696452323607191723997392473
e = 1253741277266526276273737492341769420156287745742446683234137950307473941700753795420946118527838187324934980950852435452652395931456125106860289473635243147451566503774469323896054400225880927948949271325382686728252025525992064502049812510769890170584852893320391805480557992376841338269221082823514780592527932026224041016469532408356349643964521128610552886213674116475363116732306717431311560112424065793590597523162878957727018336437764277170504454532774662559560076329628335685182665402553483091574429654268002692354092642868885921538110973203434318377491643644652734769173448091279268078729903023902968710350828758115786949
c = 1575773147844095818115335246981689507608786190212845187250432450517265485011147541328871869339509244543151221056093233377208864758371954434810015700305579991328875661494910208600661149362933701275626110364421427594488043068010070893043333162678431541790213846097012150446212452859725911076627073141637069389589032187813548754572797526213109169925710036206244271861122294567316906395657015977496683800227620943713798410804779020204823690850145678294088525234958290370183071276300423260384932033932245873934561990566777751374865071948145184698603999279619026875789640532470724368003682471823004876010640755680214225037847875314158626


d = attack(e, n)

if d:
    print(f"✅ Found private key d = {d}")
    
    # Decrypt
    m = pow(c, d, n)
    flag = long_to_bytes(m).decode('utf-8')
    print(f"🏁 Flag: {flag}")
else:
    print("❌ Wiener's attack failed")
```

```
picoCTF{sm4ll_d_6ea2db76}
```

## shift registers

> I learned about lfsr today in school so i decided to implement it in my program. It must be safe right? [chall.py](https://challenge-files.picoctf.net/c_plain_mesa/0cd8d68d4aacefd8d1924ea6452a8727990af562d813838e2bc5b4e7a57f79f8/chall.py) [output.txt](https://challenge-files.picoctf.net/c_plain_mesa/0cd8d68d4aacefd8d1924ea6452a8727990af562d813838e2bc5b4e7a57f79f8/output.txt)

Source - 

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes

key = bytes_to_long(get_random_bytes(126))

def steplfsr(lfsr):
    b7 = (lfsr >> 7) & 1
    b5 = (lfsr >> 5) & 1
    b4 = (lfsr >> 4) & 1
    b3 = (lfsr >> 3) & 1

    feedback = b7 ^ b5 ^ b4 ^ b3
    lfsr = (feedback << 7) | (lfsr >> 1)
    return lfsr

def encrypt_lfsr(pt_bytes):
    output = bytearray()
    lfsr = key & 0xFF
    for p in pt_bytes:
        lfsr = steplfsr(lfsr)
        ks = lfsr
        output.append(p ^ ks)
    return bytes_to_long(bytes(output))

pt = b"[redacted]"
ct = encrypt_lfsr(pt)

print(long_to_bytes(ct).hex())
```

```
21c1b705764e4bfdafd01e0bfdbc38d5eadf92991cdd347064e37444e517d661cea9
```

Flag - 

```python

from Crypto.Util.number import long_to_bytes, bytes_to_long
from owiener import attack

flag_hex = "21c1b705764e4bfdafd01e0bfdbc38d5eadf92991cdd347064e37444e517d661cea9"
flag_bytes = (bytes.fromhex(flag_hex))

def steplfsr(lfsr):
    b7 = (lfsr >> 7) & 1
    b5 = (lfsr >> 5) & 1
    b4 = (lfsr >> 4) & 1
    b3 = (lfsr >> 3) & 1

    feedback = b7 ^ b5 ^ b4 ^ b3
    lfsr = (feedback << 7) | (lfsr >> 1)
    return lfsr


def decrypt(flag_bytes, start_lfsr):
    lfsr = start_lfsr
    decrypted = bytearray()
    for c in flag_bytes:
        lfsr = steplfsr(lfsr)
        decrypted.append(c ^ lfsr)
    return bytes(decrypted)

for possible_key in range(256):
	decrypted_bytes = decrypt(flag_bytes, possible_key)
	flag = decrypted_bytes.decode('utf-8', errors='ignore')
	
	if "picoCTF" in flag:
		print(flag)
	else:
		pass


```

```
picoCTF{l1n3ar_f33dback_sh1ft_r3g}
```

## Related Messages

> Oops! I have a typo in my first message so i sent it again! I used RSA twice so this is secure right? [chall.py](https://challenge-files.picoctf.net/c_plain_mesa/8ce9dca037e3d5ab3c3407a3ac601de62442cb7bb022f35c4e61a3ef25a6aeba/chall.py) [output.txt](https://challenge-files.picoctf.net/c_plain_mesa/8ce9dca037e3d5ab3c3407a3ac601de62442cb7bb022f35c4e61a3ef25a6aeba/output.txt)

Source - 

```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

Message = bytes_to_long(b"[redacted]")
Message_fixed = bytes_to_long(b"[redacted]")
e = 0x11
p = getPrime(1024)
q = getPrime(1024)
phi = (p-1) * (q-1)
d = inverse(e, phi)
N = p*q

ciphertext = pow(Message, e, N)
ciphertext2 = pow(Message_fixed, e, N)

print(ciphertext, ciphertext2)
print(Message - Message_fixed)
print(N)

```

```
3486364849772584627692611749053367200656673358261596068549224442954489368512244047032432842601611650021333218776410522726164792063436874469202000304563253268152374424792827960027328885841727753251809392141585739745846369791063025294100126955644910200403110681150821499366083662061254649865214441429600114378725559898580136692467180690994656443588872905046189428367989340123522629103558929469463071363053880181844717260809141934586548192492448820075030490705363082025344843861901475648208157572346004443100461870519699021342998731173352225724445397168276113254405106732294978648428026500248591322675321980719576323749
201982790559548563915678784397933493721879152787419243871599124287434576744055997870874349538398878336345269929647585648144070475012256331468688792105087899416655051702630953882466457932737483198442642588375981620937494661378586614008496182135571457352400128892078765628319466855732569272509655562943410536265866312968101366413636251672211633011159836642751480632253423529271185888171036917413867011031963618529122680143291205470937752671602494831117301480813590683791618751348224964277861127486155552153012612562009905595646626759034581358425916638671884927506025703373056113307665093346439014722219878575598308124
-3
17334845546772507565250479697360218105827285681719530148909779921509619103084219698006014339278818598859177686131922807448182102049966121282308256054696565796008642900453901629937223685292142986689576464581496406676552201407729209985216274086331582917892470955265888718120511814944341755263650688063926284195007148056359887333784052944201212155189546062807573959105963160320187551755272391293705288576724811668369745107148481856135696249862795476376097454818009481550162364943945249601744881676746859305855091288055082626399929893610275614840617858985993338556889612804266896309310999363054134373435198031731045253881

```

Flag - 

```python

from Crypto.Util.number import long_to_bytes
import math


def trim(poly):
    """Remove trailing zeros from polynomial coefficients"""
    while poly and poly[-1] == 0:
        poly.pop()
    return poly

def poly_add(p1, p2, mod):
    """Add two polynomials modulo mod"""
    n = max(len(p1), len(p2))
    res = [0] * n
    for i in range(len(p1)):
        res[i] = (res[i] + p1[i]) % mod
    for i in range(len(p2)):
        res[i] = (res[i] + p2[i]) % mod
    return trim(res)

def poly_sub(p1, p2, mod):
    """Subtract two polynomials modulo mod"""
    n = max(len(p1), len(p2))
    res = [0] * n
    for i in range(len(p1)):
        res[i] = (res[i] + p1[i]) % mod
    for i in range(len(p2)):
        res[i] = (res[i] - p2[i]) % mod
    return trim(res)

def poly_mul(p1, p2, mod):
    """Multiply two polynomials modulo mod"""
    if not p1 or not p2:
        return [0]
    res = [0] * (len(p1) + len(p2) - 1)
    for i, a in enumerate(p1):
        if a == 0:
            continue
        for j, b in enumerate(p2):
            res[i+j] = (res[i+j] + a * b) % mod
    return trim(res)

def poly_pow(poly, exp, mod):
    """Raise polynomial to power exp modulo mod"""
    result = [1]
    base = poly[:]
    while exp > 0:
        if exp & 1:
            result = poly_mul(result, base, mod)
        base = poly_mul(base, base, mod)
        exp >>= 1
    return result

def poly_divmod(p1, p2, mod):
    """Divide p1 by p2, returns (quotient, remainder)"""
    p1 = trim(p1[:])
    p2 = trim(p2[:])
    
    if not p2:
        raise ValueError("Division by zero polynomial")
    
    if len(p1) < len(p2):
        return [0], p1
    
    res = [0] * (len(p1) - len(p2) + 1)
    rem = p1[:]
    
    while len(rem) >= len(p2):
        if rem[-1] == 0:
            rem.pop()
            continue
        
        # Try to invert leading coefficient
        try:
            inv = pow(p2[-1], -1, mod)
        except ValueError:
            # Not invertible - found factor of N
            return None, None, p2[-1]
        
        factor = (rem[-1] * inv) % mod
        shift = len(rem) - len(p2)
        res[shift] = (res[shift] + factor) % mod
        
        for i in range(len(p2)):
            rem[i+shift] = (rem[i+shift] - factor * p2[i]) % mod
        
        while rem and rem[-1] == 0:
            rem.pop()
    
    return trim(res), trim(rem), None

def poly_gcd(p1, p2, mod):
    """GCD of two polynomials modulo composite N"""
    p1 = trim(p1[:])
    p2 = trim(p2[:])
    
    if not p1:
        return p2, None
    if not p2:
        return p1, None
    
    if len(p1) < len(p2):
        p1, p2 = p2, p1
    
    while p2:
        _, rem, factor = poly_divmod(p1, p2, mod)
        
        if factor is not None:
            # Found a factor of N!
            return None, factor
        
        p1, p2 = p2, rem
        p1 = trim(p1)
        p2 = trim(p2)
    
    # Make monic (leading coefficient = 1)
    if p1 and p1[-1] != 1:
        try:
            inv = pow(p1[-1], -1, mod)
            p1 = [(c * inv) % mod for c in p1]
        except ValueError:
            # Leading coefficient not invertible - found factor
            return None, p1[-1]
    
    return p1, None

def build_x_power(e, c, N):
    """Build polynomial x^e - c"""
    poly = [0] * (e + 1)
    poly[e] = 1
    poly[0] = (-c) % N
    return trim(poly)

def build_x_plus_diff_power(diff, e, c, N):
    """Build polynomial (x + diff)^e - c"""
    # Start with 1
    poly = [1]
    
    # Multiply by (x + diff) e times
    for _ in range(e):
        new = [0] * (len(poly) + 1)
        for i, coef in enumerate(poly):
            new[i] = (new[i] + coef * diff) % N
            new[i+1] = (new[i+1] + coef) % N
        poly = trim(new)
    
    # Subtract c from constant term
    poly[0] = (poly[0] - c) % N
    return trim(poly)

def franklin_reiter_attack(c1, c2, e, N, diff):
    """
    Franklin-Reiter Related Message Attack
    
    Given:
        c1 = m1^e mod N
        c2 = m2^e mod N
        m1 = m2 + diff
    
    Returns:
        (m1, m2) as integers, or (None, factor) if N was factored
    """
    print("[*] Building polynomials...")
    print(f"    f1(x) = x^{e} - c1")
    print(f"    f2(x) = (x + {diff})^{e} - c2")
    
    f1 = build_x_power(e, c1, N)          # x^e - c1
    f2 = build_x_plus_diff_power(diff, e, c2, N)  # (x+diff)^e - c2
    
    print(f"[*] f1 degree: {len(f1)-1}")
    print(f"[*] f2 degree: {len(f2)-1}")
    
    print("[*] Computing GCD...")
    g, factor = poly_gcd(f1, f2, N)
    
    if factor is not None:
        print(f"[!] Found factor of N: {factor}")
        return None, None, factor
    
    if not g:
        print("[*] GCD is empty - attack failed")
        return None, None, None
    
    if len(g) == 1:
        print("[*] GCD is constant - attack failed")
        return None, None, None
    
    print(f"[*] GCD degree: {len(g)-1}")
    
    if len(g) == 2:
        # g = x + b (since monic)
        # root = -b
        b = g[0]
        m2 = (-b) % N
        m1 = (m2 + diff) % N
        return m1, m2, None
    
    print("[*] GCD degree > 1 - unexpected")
    return None, None, None

def main():
	N = 17334845546772507565250479697360218105827285681719530148909779921509619103084219698006014339278818598859177686131922807448182102049966121282308256054696565796008642900453901629937223685292142986689576464581496406676552201407729209985216274086331582917892470955265888718120511814944341755263650688063926284195007148056359887333784052944201212155189546062807573959105963160320187551755272391293705288576724811668369745107148481856135696249862795476376097454818009481550162364943945249601744881676746859305855091288055082626399929893610275614840617858985993338556889612804266896309310999363054134373435198031731045253881
	ciphertext = 3486364849772584627692611749053367200656673358261596068549224442954489368512244047032432842601611650021333218776410522726164792063436874469202000304563253268152374424792827960027328885841727753251809392141585739745846369791063025294100126955644910200403110681150821499366083662061254649865214441429600114378725559898580136692467180690994656443588872905046189428367989340123522629103558929469463071363053880181844717260809141934586548192492448820075030490705363082025344843861901475648208157572346004443100461870519699021342998731173352225724445397168276113254405106732294978648428026500248591322675321980719576323749
	ciphertext2 = 201982790559548563915678784397933493721879152787419243871599124287434576744055997870874349538398878336345269929647585648144070475012256331468688792105087899416655051702630953882466457932737483198442642588375981620937494661378586614008496182135571457352400128892078765628319466855732569272509655562943410536265866312968101366413636251672211633011159836642751480632253423529271185888171036917413867011031963618529122680143291205470937752671602494831117301480813590683791618751348224964277861127486155552153012612562009905595646626759034581358425916638671884927506025703373056113307665093346439014722219878575598308124

	e = 17
	c1 = ciphertext
	c2 = ciphertext2
	diff = 3

	print("="*60)
	print("Franklin-Reiter Related Message Attack")
	print("="*60)
	print(f"N = {N}")
	print(f"e = {e}")
	print(f"c1 = {c1}")
	print(f"c2 = {c2}")
	print(f"diff = {diff}")
	print()
    
	m1, m2, factor = franklin_reiter_attack(c1, c2, e, N, diff)
    
	if factor is not None:
			print("\n" + "="*60)
			print("✓ FOUND FACTOR OF N!")
			print("="*60)
			q = N // factor
			print(f"p = {factor}")
			print(f"q = {q}")

			# Compute private key and decrypt
			phi = (factor - 1) * (q - 1)
			d = pow(e, -1, phi)

			m1 = pow(c1, d, N)
			m2 = pow(c2, d, N)

			print(f"\nRecovered m1 = {m1}")
			print(f"Recovered m2 = {m2}")

			flag1 = long_to_bytes(m1)
			flag2 = long_to_bytes(m2)

			print(f"\nFlag 1: {flag1}")
			print(f"Flag 2: {flag2}")

			try:
				print(f"\nFlag 1 text: {flag1.decode('utf-8')}")
				print(f"Flag 2 text: {flag2.decode('utf-8')}")
			except:
				print(f"\nFlag 1 hex: {flag1.hex()}")
				print(f"Flag 2 hex: {flag2.hex()}")

	elif m1 is not None and m2 is not None:
		print("\n" + "="*60)
		print("✓✓✓ ATTACK SUCCESSFUL! ✓✓✓")
		print("="*60)
		print(f"m1 = {m1}")
		print(f"m2 = {m2}")
		print(f"diff = {m1 - m2} (should be {diff})")

		flag1 = long_to_bytes(m1)
		flag2 = long_to_bytes(m2)

		print(f"\nFlag 1 (M1): {flag1}")
		print(f"Flag 2 (M2): {flag2}")

		try:
			print(f"\nFlag 1 text: {flag1.decode('utf-8')}")
			print(f"Flag 2 text: {flag2.decode('utf-8')}")
		except:
			print(f"\nFlag 1 hex: {flag1.hex()}")
			print(f"Flag 2 hex: {flag2.hex()}")

	else:
		print("\n" + "="*60)
		print("✗ ATTACK FAILED")
		print("="*60)
		print("Try these options:")
		print("1. Check if diff is correct")
		print("2. Verify c1 and c2 are correct")
		print("3. Use SageMath instead (it handles this better)")

if __name__ == "__main__":
    main()
```

Core - 

```python
# ============================================================
# MAIN
# ============================================================


from Crypto.Util.number import long_to_bytes

def trim(p): return p[:-1] if p and p[-1] == 0 else p

def divmod_poly(p1, p2, mod):
    p1, p2 = trim(p1[:]), trim(p2[:])
    if len(p1) < len(p2): return [0], p1, None
    q, r = [0]*(len(p1)-len(p2)+1), p1[:]
    while len(r) >= len(p2):
        if r[-1] == 0: r.pop(); continue
        try: inv = pow(p2[-1], -1, mod)
        except ValueError: return None, None, p2[-1]
        factor = (r[-1] * inv) % mod
        shift = len(r) - len(p2)
        q[shift] = (q[shift] + factor) % mod
        for i in range(len(p2)):
            r[i+shift] = (r[i+shift] - factor * p2[i]) % mod
        while r and r[-1] == 0: r.pop()
    return trim(q), trim(r), None

def gcd_poly(p1, p2, mod):
    p1, p2 = trim(p1[:]), trim(p2[:])
    if not p1: return p2, None
    if not p2: return p1, None
    if len(p1) < len(p2): p1, p2 = p2, p1
    while p2:
        _, rem, factor = divmod_poly(p1, p2, mod)
        if factor: return None, factor
        p1, p2 = p2, rem
        p1, p2 = trim(p1) if p1 else [], trim(p2) if p2 else []
    if p1 and p1[-1] != 1:
        try:
            inv = pow(p1[-1], -1, mod)
            p1 = [(c * inv) % mod for c in p1]
        except ValueError:
            return None, p1[-1]
    return p1, None

# f(x) = x^e - c
def f_x(e, c, N):
    poly = [0]*(e+1); poly[e] = 1; poly[0] = (-c) % N; return trim(poly)

# f(x) = (x + d)^e - c
def f_xd(d, e, c, N):
    poly = [1]
    for _ in range(e):
        new = [0]*(len(poly)+1)
        for i, coef in enumerate(poly):
            new[i] = (new[i] + coef*d) % N
            new[i+1] = (new[i+1] + coef) % N
        poly = new
    poly[0] = (poly[0] - c) % N
    return trim(poly)

# ===== YOUR VALUES =====
N = 17334845546772507565250479697360218105827285681719530148909779921509619103084219698006014339278818598859177686131922807448182102049966121282308256054696565796008642900453901629937223685292142986689576464581496406676552201407729209985216274086331582917892470955265888718120511814944341755263650688063926284195007148056359887333784052944201212155189546062807573959105963160320187551755272391293705288576724811668369745107148481856135696249862795476376097454818009481550162364943945249601744881676746859305855091288055082626399929893610275614840617858985993338556889612804266896309310999363054134373435198031731045253881
ciphertext = 3486364849772584627692611749053367200656673358261596068549224442954489368512244047032432842601611650021333218776410522726164792063436874469202000304563253268152374424792827960027328885841727753251809392141585739745846369791063025294100126955644910200403110681150821499366083662061254649865214441429600114378725559898580136692467180690994656443588872905046189428367989340123522629103558929469463071363053880181844717260809141934586548192492448820075030490705363082025344843861901475648208157572346004443100461870519699021342998731173352225724445397168276113254405106732294978648428026500248591322675321980719576323749
ciphertext2 = 201982790559548563915678784397933493721879152787419243871599124287434576744055997870874349538398878336345269929647585648144070475012256331468688792105087899416655051702630953882466457932737483198442642588375981620937494661378586614008496182135571457352400128892078765628319466855732569272509655562943410536265866312968101366413636251672211633011159836642751480632253423529271185888171036917413867011031963618529122680143291205470937752671602494831117301480813590683791618751348224964277861127486155552153012612562009905595646626759034581358425916638671884927506025703373056113307665093346439014722219878575598308124

e = 17
c1 = ciphertext
c2 = ciphertext2
diff = 3

# f1 = x^e - c1, f2 = (x+diff)^e - c2
# Both share root x = m2, so gcd(f1, f2) = x - m2
f1 = f_x(e, c1, N)
f2 = f_xd(diff, e, c2, N)

g, factor = gcd_poly(f1, f2, N)

if factor:
    # Found factor of N, decrypt directly
    q = N // factor
    phi = (factor - 1) * (q - 1)
    d = pow(e, -1, phi)
    m1 = pow(c1, d, N)
    m2 = pow(c2, d, N)
else:
    # g = x - m2 (monic), so m2 = -g[0]
    m2 = (-g[0]) % N
    m1 = (m2 + diff) % N

print("M1:", long_to_bytes(m1))
print("M2:", long_to_bytes(m2))
```

Ref : 
- https://sagecell.sagemath.org/

