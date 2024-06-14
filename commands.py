#Main Commands module

import ftplib #lib useful for Connect via FTP and handle responses
import socket #lib used for check ip addresses of domains
from ui import * #ui design
from colorama import * #colors
from datetime import datetime


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



def scan_type_selector():
    print(Fore.GREEN + scan_art)
    print(Fore.LIGHTWHITE_EX + scan_choice)
    scan_type = int(input(Fore.CYAN + "Choose an Option: "))
    # exit option
    if scan_type == 0:
        clear_screen()
        message = Fore.RED + exiting
        return message
    return int(scan_type)



def get_current_datetime_string():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
    return formatted_datetime