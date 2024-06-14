import os
from commands import anonLog,domainToIp,get_current_datetime_string
from ui import *
from colorama import *

loading_complete = False  # Global flag to control loading animation

def single_anonymous_ftp_login(scan_type):
    if scan_type == 1:
        print(Fore.BLUE + scan_single_art_ip)
        print(Fore.LIGHTYELLOW_EX + ip_message_alert)
        target = input("Insert IP Address: ")
        loading_thread = start_loading_animation()
        anonLog(target)
        stop_loading_animation(loading_thread)
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')
    elif scan_type == 2:
        print(Fore.LIGHTMAGENTA_EX + scan_single_art_domain)
        print(Fore.LIGHTYELLOW_EX + domain_message_alert)
        domain = input("Insert Domain Address: ")
        loading_thread = start_loading_animation()
        target = domainToIp(domain)
        anonLog(target)
        stop_loading_animation(loading_thread)
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')


def multiple_anonymous_ftp_logins(scan_type):
    if scan_type == 1:
        path = 'lists/ip/'
        print(Fore.BLUE + scan_multiple_art_ip)
        print(Fore.LIGHTYELLOW_EX + ip_message_alert)
        filename = input(Fore.LIGHTWHITE_EX + "Insert the name of the file containing IP addresses: ")
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            print("found_file")
            with open(file_path, 'r') as file:
                for line in file:
                    target = line.strip()
                    print(Fore.LIGHTYELLOW_EX + f"[+] {target} try...")
                    loading_thread = start_loading_animation()
                    anonLog(target)
            stop_loading_animation(loading_thread)
            input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

        else:
            print(Fore.LIGHTRED_EX + f"File '{file_path}' does not exist.")
            input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')
    elif scan_type == 2:
        path = 'lists/domains/'
        print(Fore.LIGHTMAGENTA_EX + scan_multiple_art_domain)
        print(Fore.LIGHTYELLOW_EX + domain_message_alert)
        filename = input(Fore.LIGHTWHITE_EX + "Insert the name of the file containing Domains: ")
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            print("File Found")
            with open(file_path, 'r') as file:
                for line in file:
                    domain = line.strip()
                    target = domainToIp(domain)
                    print(Fore.LIGHTYELLOW_EX + f"[+] {domain} - {target} try...")
                    loading_thread = start_loading_animation()
                    anonLog(target)
            stop_loading_animation(loading_thread)
            input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

        else:
            print(Fore.LIGHTRED_EX + f"File '{file_path}' does not exist.")
            input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

def domain_list_to_ip_list():
    print(Fore.LIGHTMAGENTA_EX + domain_to_ip_ui)
    print(Fore.LIGHTYELLOW_EX + "Transforms a list of domains into a list of IP addresses, from /domains to /ip")
    path = 'lists/domains/'  # Path where the domain file is located
    filename = input(Fore.LIGHTWHITE_EX + "Insert the name of the file containing Domains: ")
    file_path = os.path.join(path, filename)  # Full path to the domain file

    if os.path.isfile(file_path):
        print("File Found")
        string = get_current_datetime_string()
        filepath_output = f'lists/ip/{string}.txt'  # Path for the output file with current timestamp

        try:
            with open(file_path, 'r') as file, open(filepath_output, 'w') as output_file:
                for line in file:
                    domain = line.strip()
                    target = domainToIp(domain)  # Convert domain to IP using domainToIp function
                    loading_thread = start_loading_animation()
                    output_file.write(f"{target} | {domain} \n")  # Write IP and domain to output file
                    stop_loading_animation(loading_thread)

            print(Fore.GREEN + f"Completed, saved result in '{filepath_output}'.")
            input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

        except Exception as e:
            print(Fore.RED + f"Error occurred during processing: {str(e)}")
            input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

    else:
        print(Fore.LIGHTRED_EX + f"File '{file_path}' does not exist.")
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

    return None