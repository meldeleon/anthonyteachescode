## signals
- method for OS to msg programs ("hey girl, hey").
- most common is signal interrupt `SIGINT`, when you type `ctrl + c`. 
- kill is a command to send signals, `kill -9` each signal has a name/number.
- kill -l will print signals.
- `ctrl + z` does `SIGSTOP` and `SIGCONT`.
- `ctrl + \` sends `SIGQUIT`, very rarely caught, more likely to kill the process.
