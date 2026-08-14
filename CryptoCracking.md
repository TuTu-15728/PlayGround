# Complete Cryptography Guide: Mathematical Concepts & Cracking Techniques

**Complete cryptographic weapons kit!** 🎯

|           Concept           |                 What It Does                  |
| :-------------------------: | :-------------------------------------------: |
| **Franklin-Reiter Attack**  |           Recovers related messages           |
|     **Polynomial GCD**      |       Finds common roots in polynomials       |
| **Modular Polynomial Ring** | `Z_N[x]` - polynomials over composite numbers |
|   **Euclidean Algorithm**   |           Finds GCD of polynomials            |
|    **Monic Polynomial**     |           Leading coefficient is 1            |
|     **Root Extraction**     |        Finding solution to `f(x) = 0`         |
## 1. RSA Fundamentals

### Core Mathematical Concepts:

|         Concept         |        Formula         |             Description              |
| :---------------------: | :--------------------: | :----------------------------------: |
| **Modular Arithmetic**  |    `a ≡ b (mod n)`     | Numbers wrap around after reaching n |
|   **Euler's Totient**   |  `φ(n) = (p-1)(q-1)`   |   Number of integers coprime to n    |
| **RSA Key Generation**  | `e * d ≡ 1 (mod φ(n))` |       Public/private key pair        |
|     **Encryption**      |    `c = m^e mod n`     |           Encrypt message            |
|     **Decryption**      |    `m = c^d mod n`     |          Decrypt ciphertext          |
| **Carmichael Function** | `λ(n) = lcm(p-1, q-1)` |         Alternative to φ(n)          |

### Python Functions:

```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
# Key Generation
p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p-1) * (q-1)
e = 65537
d = inverse(e, phi)
# Encode/Decode
m_int = bytes_to_long(b"Hello")
m_bytes = long_to_bytes(m_int)
# Core Operations
c = pow(m_int, e, n)  # Encryption
m = pow(c, d, n)      # Decryption
```

---

## 2. Mathematical Attack Categories

### A. Small Exponent Attacks

#### 1. **Low Public Exponent Attack** (e is small like 3, 17)

**Condition:** `m^e < n` (message smaller than modulus)

**Solution:** Take e-th root of ciphertext

```python
import gmpy2
def low_exponent_attack(c, e):
    m, exact = gmpy2.iroot(c, e)
    if exact:
        return long_to_bytes(int(m))
    return None
```

**Mathematical Name:** **e-th Root Attack**

---

#### 2. **Franklin-Reiter Related Message Attack**

**Condition:** Two messages with known linear relation: `m1 = m2 + diff`

**Math:** Both polynomials share a common root:

```text

f1(x) = x^e - c1
f2(x) = (x + diff)^e - c2
gcd(f1, f2) = x - m2
```

---
#### 3. **Coppersmith's Attack**

**Condition:** Partial knowledge of message (small root)

**Math:** Find small roots of polynomial `f(x) ≡ 0 (mod n)`

```python

# In SageMath
R.<x> = PolynomialRing(Zmod(n))
f = (x + known_bits)^e - c
roots = f.small_roots(X=2^bits, beta=1.0)
```

**Mathematical Name:** **Coppersmith's Theorem** (uses LLL algorithm)

---
#### 4. **Håstad's Broadcast Attack**

**Condition:** Same message sent to multiple recipients with same small e

**Math:** Chinese Remainder Theorem + e-th root


```python

# Given: c1, c2, c3 with moduli n1, n2, n3
# Find: m where m^e ≡ ci (mod ni)
from sage.all import CRT
m_e = CRT([c1, c2, c3], [n1, n2, n3])
m, exact = gmpy2.iroot(m_e, e)
```

**Mathematical Name:** **Håstad's Broadcast Attack**

---
### B. Small Private Key Attacks

#### 5. **Wiener's Attack**

**Condition:** Private key `d` is small (< n^0.25)

**Math:** Use continued fractions of `e/n`

```python

from owiener import attack
d = attack(n, e)  # Finds d if it's small
if d:
    m = pow(c, d, n)
```

**Mathematical Name:** **Wiener's Attack** (Continued Fraction Attack)

---
#### 6. **Boneh-Durfee Attack**

**Condition:** `d < n^0.292` (improvement on Wiener)

**Math:** Uses Coppersmith's method with lattices

```python

# Usually implemented in SageMath
# Uses lattice basis reduction (LLL)
```

**Mathematical Name:** **Boneh-Durfee Attack**

---

### C. Modulus Factorization Attacks

#### 7. **Fermat Factorization**

**Condition:** Primes close together

**Math:** `n = a^2 - b^2` where `a = (p+q)/2`, `b = (q-p)/2`

```python

def fermat_factor(n):
    a = gmpy2.isqrt(n) + 1
    while True:
        b2 = a*a - n
        b = gmpy2.isqrt(b2)
        if b*b == b2:
            return a-b, a+b
        a += 1
```

**Mathematical Name:** **Fermat's Factorization Method**

---

#### 8. **Pollard's Rho Attack**

**Condition:** n has a small factor

**Math:** Floyd's cycle-finding algorithm on polynomial `f(x) = x^2 + 1`

```python

def pollard_rho(n):
    f = lambda x: (x*x + 1) % n
    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    return d
```

**Mathematical Name:** **Pollard's Rho Algorithm**

---

#### 9. **Pollard's p-1 Attack**

**Condition:** `p-1` is smooth (has only small prime factors)

**Math:** `a^(M) ≡ 1 (mod p)` if `M` is multiple of `p-1`

```python

def pollard_p_minus_1(n, B):
    a = 2
    for i in range(2, B):
        a = pow(a, i, n)
        g = gcd(a-1, n)
        if 1 < g < n:
            return g
```

**Mathematical Name:** **Pollard's p-1 Algorithm**

---

#### 10. **Common Modulus Attack**

**Condition:** Same n, same message, two different e values that are coprime

**Math:** Extended Euclidean algorithm

```text

c1 = m^e1 mod n
c2 = m^e2 mod n
Find: a*e1 + b*e2 = 1
Then: m = c1^a * c2^b mod n
```

```python

def common_modulus_attack(c1, c2, e1, e2, n):
    g, a, b = egcd(e1, e2)
    if g == 1:
        m = (pow(c1, a, n) * pow(c2, b, n)) % n
        return long_to_bytes(m)
```

**Mathematical Name:** **Common Modulus Attack**

---

### D. Implementation Attacks

#### 11. **Chosen Ciphertext Attack (CCA)**

**Condition:** Can decrypt chosen ciphertexts

**Math:** Multiplicative property of RSA

```python

# If we know c, choose r, compute:
c2 = (c * pow(r, e, n)) % n
# Decrypt c2 to get m*r mod n
# Then m = (m*r) * inverse(r) mod n
```

**Mathematical Name:** **Adaptive Chosen Ciphertext Attack**

---

#### 12. **Bleichenbacher's Attack**

**Condition:** Padding oracle (server tells if decryption is valid)

**Math:** Iterative narrowing of possible m values

```python
# Complex iterative attack on PKCS#1 v1.5 padding
```

**Mathematical Name:** **Bleichenbacher's Attack** (Padding Oracle)

---

## 3. Key Mathematical Tools

### A. GCD and Extended Euclidean Algorithm

```python

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
# Find modular inverse
def inv_mod(a, m):
    g, x, _ = egcd(a, m)
    if g == 1:
        return x % m
```

**Mathematical Name:** **Extended Euclidean Algorithm**

---

### B. Chinese Remainder Theorem (CRT)

```python

def crt(residues, moduli):
    """Solve: x ≡ r_i (mod m_i) for all i"""
    total = 0
    M = 1
    for m in moduli:
        M *= m
    for r, m in zip(residues, moduli):
        Mi = M // m
        total += r * Mi * inv_mod(Mi, m)
    return total % M
```

**Mathematical Name:** **Chinese Remainder Theorem**

---

### C. Continued Fractions (Wiener Attack)

```python

def continued_fraction(n, d):
    # Used in Wiener's attack
    cf = []
    while d:
        cf.append(n // d)
        n, d = d, n % d
    return cf
```

**Mathematical Name:** **Continued Fraction Expansion**

---

### D. Lattice Reduction (LLL)

```python

# Usually in SageMath
from sage.all import Matrix, ZZ
def coppersmith(f, n, beta, X):
    # LLL algorithm implementation
    # Used for finding small roots
```

**Mathematical Name:** **Lenstra-Lenstra-Lovász (LLL) Lattice Reduction**

---

## 4. Common Crypto Libraries

|        Library         |     Purpose      |                   Key Functions                    |
| :--------------------: | :--------------: | :------------------------------------------------: |
| **Crypto.Util.number** |  RSA utilities   |    `getPrime()`, `bytes_to_long()`, `inverse()`    |
|       **gmpy2**        | Big integer math |     `iroot()`, `isqrt()`, `gcd()`, `powmod()`      |
|    **pycryptodome**    |   Full crypto    |                AES, RSA, DSA, etc.                 |
|      **SageMath**      |  Advanced math   | `PolynomialRing`, `Zmod`, `small_roots()`, `LLL()` |
|      **owiener**       |  Wiener attack   |                   `attack(n, e)`                   |
|       **sympy**        |  Symbolic math   |             `factorint()`, `isprime()`             |

---

## 5. Attack Decision Tree

```text

Is e small (3, 17)?
    ├── Yes: Try Low Exponent Attack (iroot)
    ├── Multiple ciphertexts?
    │   └── Yes: Håstad Broadcast Attack
    └── Related messages?
        └── Yes: Franklin-Reiter Attack
Is d small?
    ├── Yes: Try Wiener's Attack
    └── d < n^0.292? → Boneh-Durfee Attack
Can factor n?
    ├── Primes close? → Fermat Factorization
    ├── Small factor? → Pollard's Rho
    └── p-1 smooth? → Pollard's p-1
Implementation bug?
    ├── Padding oracle? → Bleichenbacher
    ├── Same n, different e? → Common Modulus
    └── Chosen ciphertext? → CCA
Need small roots?
    └── Use Coppersmith's Attack
```

---

## 6. Mathematical Names Quick Reference

|             Name              |         Used For          |
| :---------------------------: | :-----------------------: |
|    **Modular Arithmetic**     |    All RSA operations     |
|      **Euler's Theorem**      |   `a^φ(n) ≡ 1 (mod n)`    |
| **Chinese Remainder Theorem** |   Combining congruences   |
|  **Fermat's Little Theorem**  |   `a^(p-1) ≡ 1 (mod p)`   |
|    **Continued Fractions**    |      Wiener's Attack      |
|       **LLL Algorithm**       | Coppersmith, Boneh-Durfee |
|       **Pollard's Rho**       |  Factoring large numbers  |
|    **Extended Euclidean**     |     Finding inverses      |
|    **Lagrange's Theorem**     |    Group theory in RSA    |
|    **Carmichael Function**    |    Alternative to φ(n)    |
|       **Smooth Number**       |       Pollard's p-1       |
|        **Square-free**        |      Properties of n      |

---

## 7. Complete Attack Cheat Sheet

```python

from Crypto.Util.number import *
import gmpy2
# 1. Low Exponent Attack
def attack_low_e(c, e):
    m, exact = gmpy2.iroot(c, e)
    return long_to_bytes(int(m)) if exact else None
# 2. Wiener Attack
def attack_wiener(n, e, c):
    from owiener import attack
    d = attack(n, e)
    return long_to_bytes(pow(c, d, n)) if d else None
# 3. Common Modulus Attack
def attack_common_mod(c1, c2, e1, e2, n):
    def egcd(a,b):
        if b==0: return a,1,0
        g,x,y = egcd(b,a%b)
        return g,y,x-(a//b)*y
    g,a,b = egcd(e1,e2)
    if g==1:
        m = (pow(c1,a,n)*pow(c2,b,n)) % n
        return long_to_bytes(m)
# 4. Franklin-Reiter (Needs Sage for GCD)
# 5. Fermat Factorization
def factor_fermat(n):
    a = gmpy2.isqrt(n) + 1
    while True:
        b2 = a*a - n
        b = gmpy2.isqrt(b2)
        if b*b == b2:
            return a-b, a+b
        a += 1
# 6. Pollard's Rho
def factor_pollard_rho(n):
    f = lambda x: (x*x + 1) % n
    x = y = 2
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x-y), n)
    return d if d != n else None
# 7. CRT Attack (Håstad)
def attack_broadcast(c_list, n_list, e):
    # c_list = [c1, c2, c3], n_list = [n1, n2, n3]
    from sage.all import CRT
    m_e = CRT(c_list, n_list)
    m, exact = gmpy2.iroot(m_e, e)
    return long_to_bytes(int(m)) if exact else None
```


