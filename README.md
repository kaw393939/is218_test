# is117_test
Hello world

## Basic file operations and navigation on Linux and macOS

Open a terminal to use these commands. The examples work in common Linux shells and the default macOS shell, zsh.

### Find your way around

| Command | What it does |
| --- | --- |
| `pwd` | Print the full path of your current directory. |
| `ls` | List files and directories in the current directory. |
| `ls -la` | Show a detailed list, including hidden files whose names start with `.`. |
| `cd Documents` | Move into the `Documents` directory inside your current directory. |
| `cd ..` | Move up to the parent directory. |
| `cd ~` | Go to your home directory. |
| `cd -` | Return to the previous directory. |

An **absolute path** starts at the filesystem root, `/`, such as `/Users/alex/Documents` on macOS or `/home/alex/Documents` on Linux. A **relative path** starts from your current directory, such as `notes/today.txt`. The shortcut `.` means the current directory, `..` means its parent, and `~` means your home directory.

Put paths containing spaces in quotes: `cd "Class Notes"`. Press **Tab** to complete a file or directory name and the **Up Arrow** to recall a previous command.

### Create, copy, move, and remove files

| Command | What it does |
| --- | --- |
| `mkdir notes` | Create a directory named `notes`. |
| `mkdir -p coursework/week1` | Create nested directories, including any missing parents. |
| `touch notes.txt` | Create an empty file if it does not exist; otherwise update its timestamps. |
| `cp -i notes.txt backup.txt` | Copy a file, asking before overwriting an existing destination. |
| `cp -Ri notes notes-backup` | Copy a directory and its contents, asking before overwriting files. |
| `mv -i notes.txt lesson.txt` | Rename a file, asking before overwriting an existing destination. |
| `mv -i lesson.txt notes/` | Move a file into an existing directory. |
| `rm -i backup.txt` | Ask for confirmation before deleting a file. |
| `rmdir empty-folder` | Remove a directory only if it is empty. |

Terminal deletion with `rm` bypasses the Trash. Check your location with `pwd` and the contents with `ls` before deleting. To remove a directory and everything inside it, use `rm -ri directory-name`; it asks for confirmation as it works.

### Read and find files

| Command | What it does |
| --- | --- |
| `cat notes.txt` | Print an entire text file. |
| `less notes.txt` | Read a text file one screen at a time; press `q` to exit. |
| `head -n 10 notes.txt` | Show the first 10 lines. |
| `tail -n 10 notes.txt` | Show the last 10 lines. |
| `find . -name '*.txt'` | Find files or directories with names ending in `.txt` under the current directory. |
| `grep -n 'hello' notes.txt` | Show lines containing `hello`, along with their line numbers. |

Keep the pattern in the `find` example quoted so the shell passes it directly to `find`. To learn more about a command, use its manual page, such as `man cp`; press `q` to exit.

### Try it yourself

Run these commands one line at a time. Start in your home directory and use a new practice folder so the exercise stays separate from your other files. If `mkdir` reports that the folder already exists, choose a different name before continuing.

```sh
cd ~
mkdir terminal-practice
cd terminal-practice
pwd
mkdir notes
touch notes/lesson.txt
printf 'Hello from the terminal!\n' > notes/lesson.txt
cat notes/lesson.txt
cp -i notes/lesson.txt notes/backup.txt
mv -i notes/backup.txt notes/review.txt
ls -la notes
find . -name '*.txt'
rm -i notes/review.txt
cd ..
```

The `>` operator writes command output to a file and **replaces any existing contents**. Use `>>` instead to append. When `rm -i` asks whether to remove the practice copy, enter `y` to confirm or `n` to keep it. Your original `notes/lesson.txt` remains in `~/terminal-practice`.
