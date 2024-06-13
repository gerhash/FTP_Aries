import ftplib
import socket
from ui import *
from colorama import *
def anonLog(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print(Fore.LIGHTGREEN_EX + '\n[+] ' + str(hostname) + ' FTP Login Success \n')
        ftp.quit()
        return True
    except Exception:
        print(Fore.YELLOW + '\n[x] ' + str(hostname) + ' FTP Login Failed \n')
        return True

def domainToIp(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(Fore.LIGHTRED_EX + f"IP Find Error for {domain}: {e}")


