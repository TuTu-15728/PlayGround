| ![Kitten](/Assets/Images/bandit.png) | Platform - OverTheWire<br>Name - Bandit<br>Type - Challenge<br>Target - Unix/Linux<br>Difficulty - Easy&Medium |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------- |

📌 **Note for beginners :**

This game is organised in levels. You start at Level 0 and try to "beat" or "finish" it. Finishing a level results in information on how to start the next level. Currently, there are 33 levels to practice your skill.

The pages on this website (https://overthewire.org/wargames/bandit/) for 'Level X' contain information on how to start level X from the previous level. E.g. The page for 'Level 1' (https://overthewire.org/wargames/bandit/bandit1.html) has information on how to gain access from 'Level 0' (https://overthewire.org/wargames/bandit/bandit0.html) to 'Level 1'.

If you’ve never used the command line before, a good first read is this 'introduction to user commands' (https://manpages.ubuntu.com/manpages/noble/man1/intro.1.html).

First, if you know a command, but don’t know how to use it, try the 'manual (man page)' by entering 'man <command>'. For example, 'man ls' to learn about the "ls" command.

👉 **TIP:** Create a file for notes and passwords on your local machine. Passwords for levels are _not_ saved automatically. If you do not save them yourself, you will need to start over from bandit0.

📋 **Challenges**

|         [Level 0](#Level0)          |     |     |
| :---------------------------------: | :-: | :-: |
| [Level 0 - Level 1](#Level0-Level1) |     |     |
| [Level 1- Level 2](#Level1-Level2)  |     |     |
| [Level 2 - Level 3](#Level2-Level3) |     |     |
| [Level 3 - Level 4](#Level3-Level4) |     |     |
| [Level 4 - Level 5](#Level4-Level5) |     |     |
|                                     |     |     |

# Level0

🎯 **Level Goal :**
- The goal of this level is for you to log into the game using SSH. The host to which you need to connect is **bandit.labs.overthewire.org**, on port 2220. The username is **bandit0** and the password is **bandit0**. Once logged in, go to the [Level 1](https://overthewire.org/wargames/bandit/bandit1.html) page to find out how to beat Level 1.

💡 **Command :**
- [ssh](https://manpages.ubuntu.com/manpages/noble/man1/ssh.1.html)

👨🏻‍💻 **Solution :**

Let's fire up our terminal and login with the given credentials. Check the command below - 

```shell
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

When it shows the password prompt `bandit0@bandit.labs.overthewire.org's password:` then enter `bandit0` as password for `Level 0`.

After the above steps, we will find our shell changes to `bandit0@bandit:~$` i.e. a successful login as user `bandit0`.

![bandit0](/Assets/Images/banditL0.png)

# Level0-Level1

🎯 **Level Goal :**
- The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

💡 **Command :**
- [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)

👨🏻‍💻 **Solution :**

![Level 1](/Assets/Images/banditL1.png)

**Bonus Commands:**
- I used `pwd (print working directory)` command here just to check the current directory. (Although, the `~` sign between `:` and `$` was an indication that we are currently in user home directory.)
- `ls -la` command used here to get more information about the files.
- Finally, we can get the password for next level using `cat readme` command.

# Level1-Level2

🎯 **Level Goal :**
- The password for the next level is stored in a file called **-** located in the home directory.

💡 **Command :**
- [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)

👨🏻‍💻 **Solution :**

Let's login as `bandit1` user with the looted password.

```shell
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

![Level 2](/Assets/Images/banditL2.png)

**Explanation :**
- First, I checked the file and it's permissions using the `ls -la` command.
- We can see a file named as `-` but we can't simply read it's content using the `cat` command. With `cat -`, the dash (`-`) is a convention meaning "read from stdin".  As you can see in the above image, I typed `hello` and the terminal returned `hello`.
- The `^C` (Ctrl+C) terminates the command.
- Finally, `cat ./-`  command explicitly references a file with that name in the current directory.

# Level2-Level3

🎯 **Level Goal :**

💡 **Command :**

👨🏻‍💻 **Solution :**

# Level3-Level4

🎯 **Level Goal :**

💡 **Command :**

👨🏻‍💻 **Solution :**

# Level4-Level5

🎯 **Level Goal :**

💡 **Command :**

👨🏻‍💻 **Solution :**