import os
import webbrowser
from threading import Thread
# import nmap3 # add to requirements.txt once it is used

BANNER = """
███████╗███╗   ██╗██╗   ██╗███╗   ███╗██╗
██╔════╝████╗  ██║██║   ██║████╗ ████║██║
█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║██║
██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║██║
███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝

------------------------------------------------------
"""""

yes = {"y", "Y", "yes", "Yes", "Yeah", "yeah", "sure", "Sure", "Of course!", "Of course", "absofuckinlutely", "why not", "YES", "please", "mhm", "I guess", " I already said yes", "Si", "I consent", "ken"}

def gobuster(target_ip, which_dir, args):
    os.system("gobuster dir -u http://" + target_ip + which_dir + args)


#Manual mode function. Asks you for permission right before running a scan
def manual_mode(target_ip, nmap_results):
    if nmap_results in "port 80/tcp":
        answer_gobuster = input("\n [+] Looks like there is an open web port, would you like to run a directory gobuster scan on it? ")
        # Opens target in browser
        browser = input("Do you want to open in the browser? ")
        if browser in yes:
            webbrowser.open("http://" + target_ip, new=2)
        # Starting first gobuster scan. Scannning for files and directories using the big.txt wordlist in dirb
        if answer_gobuster in yes:
            print("[+] running big.txt")
            gobuster_args = " -w /usr/share/dirb/wordlists/big.txt -t 50 -o gobuster-dir-bigtxt-scan.txt"
            gobuster(target_ip, "", gobuster_args)
            
            answer_file_gobuster = input("Would you like to look for files? ")
            if answer_file_gobuster in yes:
                which_dir = input("Which dir would u like to bust? ")
                gobuster_args = " -w /usr/share/dirb/wordlists/big.txt -x 'php, txt, sh' -t 50 -o gobuster-file-bigtxt-scan.txt"
                gobuster(target_ip, which_dir, gobuster_args)
                
                answer_medium_gobuster = input("Would you also like to run a dirbuster medium wordlist? (Despite the name it's actually much longer than big.txt) ")
                if answer_medium_gobuster in yes:
                    gobuster_args = " -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -o gobuster-dir-dirbustermedium-scan.txt"
                    gobuster(target_ip, which_dir, gobuster_args)

                    


def auto_gobuster(target_ip, nmap_results):
    # Gobuster Scan
    if nmap_results in "port 80/tcp":
        webbrowser.open('http://' + target_ip, new=2)

        print("[+] running big.txt")

        which_dir = "/"
        gobuster_args = " -w /usr/share/dirb/wordlists/big.txt -x 'php, txt, sh' -t 50 -o gobuster-file-bigtxt-scan.txt"
        gobuster(target_ip, which_dir, gobuster_args)

        gobuster_args = " -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -o gobuster-dir-dirbustermedium-scan.txt"
        gobuster(target_ip, which_dir, gobuster_args)


def nmap_all_scan(target_ip):
    # scan all ports
    os.system("nmap -p- -A -sC -T2 -oN nmap-all-scan.txt " + IP)


def main():
    print(BANNER)

    target_ip = input("[+] Target IP: ")
    automatic = input("Would you like an automatic scan(y/n)? ")

    #start nmap scan
    nmap_results = str(os.system("nmap -A -sC -T4 -oN nmap-aggresive-scan.txt " + IP + " -v"))

    if automatic not in yes:
        manual_mode(target_ip, nmap_results)
    if automatic in yes:
        auto_gobuster(target_ip, nmap_results)
        nmap_all_scan(target_ip)


if __name__ == '__main__':
    main()
