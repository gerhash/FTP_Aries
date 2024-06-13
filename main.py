#MAIN FILE, WHO HANDLES START and the main Menu
from commands import * # import commands.py
from colorama import init, Fore # import colorama for UI Design


init() #init colorama


#Menu Function
def menu():
    while True: # Looping for make the Tool always on
        print(Fore.GREEN + start_menu) # Start menu UI
        print(Fore.LIGHTWHITE_EX + main_menu)


        #Choose the first command, if u have single target or multiple targets
        quantity = int(input(Fore.CYAN + "Choose an Option: "))
        #exit option
        if quantity == 3:
            clear_screen()
            print(Fore.RED + exiting)
            break
        clear_screen() #make space

        print(Fore.GREEN + scan_art)
        print(Fore.LIGHTWHITE_EX + scan_choice)
        scan_type = int(input(Fore.CYAN + "Choose an Option: "))
        # exit option
        if scan_type == 3:
            clear_screen()
            print(Fore.RED + exiting)
            break
        clear_screen() #make space


        command(quantity, scan_type) # choice handler

#start app
if __name__ == '__main__':
    menu()

