from modes import *
from commands import *
from colorama import init, Fore


init()

def command(quantity, scan_type):
    if quantity == 1:
        single_anonymous_ftp_login(scan_type)
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')

    elif quantity == 2:
        multiple_anonymous_ftp_logins(scan_type)
        input(Fore.LIGHTWHITE_EX + 'Press any key to Restart')


def menu():
    while True:
        print(Fore.GREEN + start_menu)
        print(Fore.LIGHTWHITE_EX + main_menu)

        quantity = int(input(Fore.CYAN + "Choose an Option: "))
        if quantity == 3:
            clear_screen()
            print(Fore.RED + exiting)
            break
        clear_screen()

        print(Fore.GREEN + scan_art)
        print(Fore.LIGHTWHITE_EX + scan_choice)
        scan_type = int(input(Fore.CYAN + "Choose an Option: "))
        if scan_type == 3:
            clear_screen()
            print(Fore.RED + exiting)
            break
        clear_screen()


        command(quantity, scan_type)

if __name__ == '__main__':
    menu()

