#Main Commands module

import ftplib #lib useful for Connect via FTP and handle responses
import socket #lib used for check ip addresses of domains
from ui import * #ui design
from colorama import * #colors
from modes import * # function modules

#this function Check if you can Log anonymous FTP
def anonLog(hostname):
    try:#check
        ftp = ftplib.FTP(hostname) #connect ftp
        ftp.login('anonymous') #login
        print(Fore.LIGHTGREEN_EX + '\n[+] ' + str(hostname) + ' FTP Login Success \n')#print result
        ftp.quit() #exit
        return True
    except Exception:#fail result
        print(Fore.YELLOW + '\n[x] ' + str(hostname) + ' FTP Login Failed \n')#print result
        return True

#this function find the main ip of a domain
def domainToIp(domain):
    try:#check
        ip_address = socket.gethostbyname(domain) #get host
        return ip_address #return ip
    except socket.gaierror as e:
        print(Fore.LIGHTRED_EX + f"IP Find Error for {domain}: {e}") #fail


#handle user choices
def command(quantity, scan_type):
    if quantity == 1:
        single_anonymous_ftp_login(scan_type)
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

    elif quantity == 2:
        multiple_anonymous_ftp_logins(scan_type)
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

