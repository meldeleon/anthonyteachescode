## bash notes

- terminal vs shell.
  - terminal emulator (gnome-terminal) pretends to be a terminal. It used to be a standalone machine to run commands on a mainframe
  - using the bash shell inside of the terminal editor.
  - shell - you type commands in it and it runs things for you.
- du stands for disk usage
- sh means different things in different places, -s (summarize) -h(d)
- `ls -al` is a shortcut for `ls --all`
- `man` will pull up help articles for any bash
- job control -- allows you to background processes, and re-foreground them, or kill them, etc. to background a process type `^z`
- sudo launches commands with super user privileges.
- syntax for writing aliases: `alias ...='cd ../..'`
- ``` `` ``` will try and create a subshell command with whatever is contained in it, you can also use `$()`
- `''` hard quotes are literal quotes, `""` are soft quotes where expansion happens.
- if you want to nest quotes, just create multiple literal strings of the quotes. 
