#MAIN FILE, WHO HANDLES START and the main Menu
from commands import * # import commands.py
from modes import *
from colorama import init, Fore # import colorama for UI Design


init() #init colorama


#handle user choices
def command(choice):
    if choice == 1:
        scan_type = scan_type_selector()
        single_anonymous_ftp_login(scan_type)
    elif choice == 2:
        scan_type = scan_type_selector()
        multiple_anonymous_ftp_logins(scan_type)
    elif choice == 3:
        domain_list_to_ip_list()

#Menu Function
def menu():
    while True: # Looping for make the Tool always on
        print(Fore.GREEN + start_menu) # Start menu UI
        print(Fore.LIGHTWHITE_EX + main_menu)


        #Choose the first command, if u have single target or multiple targets
        choice = int(input(Fore.CYAN + "Choose an Option: "))

        #exit option
        if choice == 0:
            clear_screen()
            print(Fore.RED + exiting)
            break

        clear_screen() #make space
        command(choice) # choice handler

#start app
if __name__ == '__main__':
    menu()

