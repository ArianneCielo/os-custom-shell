# Activity 1 - Syscall Analysis

## Part 2: Syscall Analysis with strace

I ran the `shell_act1.py` program using the following command:

```bash
strace -f -e trace=read,write,clone,fork,exit_group python3 shell_act1.py
