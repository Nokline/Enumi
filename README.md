# Enumi
An enumeration bot for lazy people (like me) who don't wanna type a bunch of repetitive commands.

Warning: You are more than welcome to modify and edit the code as you wish, however, it is very messy and I didn't spend much time trying to make it neat. 

# What does this do?
Enumi automates the usage of tools like nmap and gobuster and saves each scan to a file so you can read it later on. Basically, if you don't wanna write a bunch of the same commands to do the same thing you are already doing for each box,you can just use enumi. All you need to do is give it the IP and it will do the rest for you.  

# How does this work?
I tried to make this as simple and easy as possible. All you have to do is run the script, give it the IP you wanna target (it will ask you, don't worry), choose between automatic or manual, and let it do it's thing.

- Automatic mode will just run everything without asking you, just to make your life a whole lot easier. It will save the scan results in the directory that you ran it in, so you can view it later on
- Manual mode will just ask you for permission before running each scan

# What scans does Enumi run?
- starts off with an nmap scan: nmap -A -sC -T4 -oN nmap-aggresive-scan.txt <ip> -v
- opens target in browser
- moves on to a basic gobuster scan with big.txt: gobuster dir -u http://<IP> -w /usr/share/dirb/wordlists/big.txt -t 50 -o gobuster-dir-bigtxt-scan.txt 
- starts a gobuster file scan, again with big.txt: gobuster dir -u http://<IP>/<dir> -w /usr/share/dirb/wordlists/big.txt -x 'php, txt, sh' -t 50 -o gobuster-file-bigtxt-scan.txt
- does another dir scan just to make sure with the dirbuster medium 2.3 wordlist: gobuster dir -u http://<IP> -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -o gobuster-dir-dirbustermedium-scan.txt

# Requirments
- Perferably Kali Linux, but should work on anything else too. (I customized this script for myself so maybe file locations and other stuff would be different on a different distro or OS)
- Nmap
- Gobuster
- Python3
