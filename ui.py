#UI ANIMATION AND GRAPHICS
import time
import threading
from colorama import *

#UI
start_menu = r'''
                                                                                     
                        @@@@@@@@@                   @@@@@@@@                         
                      @@@@@@@@@@@@@              @@@@@@@@@@@@                        
                      @@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@                       
                     @@@@@@@@@@@@@@@@@@ @@@@ @@@@@@@@@@@@@@@@@@                      
                     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                      @@@@@@   @@@@@@@@@@@@@@@@@@@@@@   @@@@@@                       
                      @@@@@@@   @@@@@@@@@@@@@@@@@@@@   @@@@@@@                       
                       @@@@@@     @@@@@@@@@@@@@@@@     @@@@@@                        
                       @@@@@@@    @@@@@@@@@@@@@@@@    @@@@@@                         
                        @@@@@@    @@@@@@@@@@@@@@@@    @@@@@@                         
                         @@@@@@   @  @@@@@@@@@@  @   @@@@@@                          
                         @@@@@@   @   @@@@@@@@  @@   @@@@@@                          
                         @@@@@@   @@@@ @@@@@@ @@@@   @@@@@@                          
                @         @@@@@    @@@@@@@@@@@@@@    @@@@@         @                 
                 @@@    @@@@@@      @@@@@@@@@@@@      @@@@@@     @@                  
                  @@@@@@@@@@@        @@@@@@@@@@        @@@@@@@@@@@                   
                     @@@@@            @@@@@@@@            @@@@@                      
                                      @@@@@@@                                        
                                       @@@@@@                                        
                                         @@                                                      
                    ________________      ___    ____  _______________
                   / ____/_  __/ __ \    /   |  / __ \/  _/ ____/ ___/
                  / /_    / / / /_/ /   / /| | / /_/ // // __/  \__ \ 
                 / __/   / / / ____/   / ___ |/ _, _// // /___ ___/ / 
                /_/     /_/ /_/       /_/  |_/_/ |_/___/_____//____/  
                
    https://github.com/gerhash/FTP_Aries                           by G#sh  
                                                            
Tool to find out if it is possible to access certain hosts with anonymous FTP, also using Lists   
'''

scan_art = r'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::                                                        ::
::                                                        ::
::                                                        ::
::    ___ ___ _    ___ ___ _____                          ::
::   / __| __| |  | __/ __|_   _|                         ::
::   \__ \ _|| |__| _| (__  | |                           ::
::   |___/___|____|___\___| |_|                           ::
::    ___ ___     __  ___   ___  __  __   _   ___ _  _    ::
::   |_ _| _ \   / / |   \ / _ \|  \/  | /_\ |_ _| \| |   ::
::    | ||  _/  / /  | |) | (_) | |\/| |/ _ \ | || .` |   ::
::   |___|_|   /_/   |___/ \___/|_|  |_/_/ \_\___|_|\_|   ::
::                                                        ::
::                                                        ::
::                                                        ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''

scan_single_art_ip = r'''
                                                           _,'/
                                                      _.-''._:
                                              ,-:`-.-'    .:.|
                                             ;-.''       .::.|
                              _..------.._  / (:.       .:::.|
                           ,'.   .. . .  .`/  : :.     .::::.|
                         ,'. .    .  .   ./    \ ::. .::::::.|
                       ,'. .  .    .   . /      `.,,::::::::.;\
                      /  .            . /       ,',';_::::::,:_:
                     / . .  .   .      /      ,',','::`--'':;._;
                    : .             . /     ,',',':::::::_:'_,'
                    |..  .   .   .   /    ,',','::::::_:'_,'
                    |.              /,-. /,',':::::_:'_,'
                    | ..    .    . /) /-:/,'::::_:',-'
                    : . .     .   // / ,'):::_:',' ;
                     \ .   .     // /,' /,-.','  ./
                      \ . .  `::./,// ,'' ,'   . /
                       `. .   . `;;;,/_.'' . . ,'
                        ,`. .   :;;' `:.  .  ,'
                       /   `-._,'  ..  ` _.-'
                      (     _,'``------''  

 ____  _             _        ___         _____                    _   
/ ___|(_)_ __   __ _| | ___  |_ _|_ __   |_   _|_ _ _ __ __ _  ___| |_ 
\___ \| | '_ \ / _` | |/ _ \  | || '_ \    | |/ _` | '__/ _` |/ _ \ __|
 ___) | | | | | (_| | |  __/  | || |_) |   | | (_| | | | (_| |  __/ |_ 
|____/|_|_| |_|\__, |_|\___| |___| .__/    |_|\__,_|_|  \__, |\___|\__|
               |___/             |_|                    |___/          
'''

scan_single_art_domain = r'''
                                                ,-.
                                             / \  `.  __..-,O
                                            :   \ --''_..-'.'
                                            |    . .-' `. '.
                                            :     .     .`.'
                                             \     `.  /  ..
                                              \      `.   ' .
                                               `,       `.   \
                                              ,|,`.        `-.\
                                             '.||  ``-...__..-`
                                              |  |
                                              |__|
                                              /||\
                                             //||\\
                                            // || \\
                                         __//__||__\\__
                                        '--------------'
 ____  _             _           ____                        _         _____                    _   
/ ___|(_)_ __   __ _| | ___     |  _ \  ___  _ __ ___   __ _(_)_ __   |_   ___ _ _ __ __ _  ___| |_ 
\___ \| | '_ \ / _` | |/ _ \    | | | |/ _ \| '_ ` _ \ / _` | | '_ \    | |/ _` | '__/ _` |/ _ | __|
 ___) | | | | | (_| | |  __/    | |_| | (_) | | | | | | (_| | | | | |   | | (_| | | | (_| |  __| |_ 
|____/|_|_| |_|\__, |_|\___|    |____/ \___/|_| |_| |_|\__,_|_|_| |_|   |_|\__,_|_|  \__, |\___|\__|
               |___/                                                                 |___/          

'''
scan_multiple_art_ip = r'''
                                                           _,'/
                                                      _.-''._:
                                              ,-:`-.-'    .:.|
                                             ;-.''       .::.|
                              _..------.._  / (:.       .:::.|
                           ,'.   .. . .  .`/  : :.     .::::.|
                         ,'. .    .  .   ./    \ ::. .::::::.|
                       ,'. .  .    .   . /      `.,,::::::::.;\
                      /  .            . /       ,',';_::::::,:_:
                     / . .  .   .      /      ,',','::`--'':;._;
                    : .             . /     ,',',':::::::_:'_,'
                    |..  .   .   .   /    ,',','::::::_:'_,'
                    |.              /,-. /,',':::::_:'_,'
                    | ..    .    . /) /-:/,'::::_:',-'
                    : . .     .   // / ,'):::_:',' ;
                     \ .   .     // /,' /,-.','  ./
                      \ . .  `::./,// ,'' ,'   . /
                       `. .   . `;;;,/_.'' . . ,'
                        ,`. .   :;;' `:.  .  ,'
                       /   `-._,'  ..  ` _.-'
                      (     _,'``------''  


 __  __       _ _   _       _        ___         _____                    _   
|  \/  |_   _| | |_(_)_ __ | | ___  |_ _|_ __   |_   _|_ _ _ __ __ _  ___| |_ 
| |\/| | | | | | __| | '_ \| |/ _ \  | || '_ \    | |/ _` | '__/ _` |/ _ \ __|
| |  | | |_| | | |_| | |_) | |  __/  | || |_) |   | | (_| | | | (_| |  __/ |_ 
|_|  |_|\__,_|_|\__|_| .__/|_|\___| |___| .__/    |_|\__,_|_|  \__, |\___|\__|
                     |_|                |_|                    |___/          
'''

scan_multiple_art_domain = r'''
                                                    ,-.
                                                 / \  `.  __..-,O
                                                :   \ --''_..-'.'
                                                |    . .-' `. '.
                                                :     .     .`.'
                                                 \     `.  /  ..
                                                  \      `.   ' .
                                                   `,       `.   \
                                                  ,|,`.        `-.\
                                                 '.||  ``-...__..-`
                                                  |  |
                                                  |__|
                                                  /||\
                                                 //||\\
                                                // || \\
                                             __//__||__\\__
                                            '--------------'
 __  __       _ _   _       _           ____                        _            _____                    _   
|  \/  |_   _| | |_(_)_ __ | | ___     |  _ \  ___  _ __ ___   __ _(_)_ __      |_   ___ _ _ __ __ _  ___| |_ 
| |\/| | | | | | __| | '_ \| |/ _ \    | | | |/ _ \| '_ ` _ \ / _` | | '_ \       | |/ _` | '__/ _` |/ _ | __|
| |  | | |_| | | |_| | |_) | |  __/    | |_| | (_) | | | | | | (_| | | | | |      | | (_| | | | (_| |  __| |_ 
|_|  |_|\__,_|_|\__|_| .__/|_|\___|    |____/ \___/|_| |_| |_|\__,_|_|_| |_|      |_|\__,_|_|  \__, |\___|\__|
                     |_|                                                                       |___/          
'''



main_menu = r'''

[1] Single Anonymous FTP Login | Single target
[2] Multiple Anonymous FTP Login | Multiple target
[3] Exit
'''



scan_choice = r'''

[1] IP Scan | Attempt with IP
[2] Domain Scan |  Attempt with DOMAIN
[3] Exit
'''

exiting = r'''
Don't Waste my Time...
'''


domain_message_alert = r'''
Insert the domain/domains in this format "www.example.com" or it won't work properly
'''

ip_message_alert = r'''
Insert the ip/ip's in this format "10.10.10.10" or it won't work properly
'''

found_file = r'''
[+] File Found...
'''


#ANIMATIONS

def clear_screen():
    print("\n\n\n\n\n\n\n")
loading_complete = False  # Global flag to control loading animation

def loading():
    animation = "|/-\\"  # Characters for the loading animation
    idx = 0  # Index to track current animation character
    while not loading_complete:  # Loop until loading_complete is True
        # Print loading animation in Cyan color, overwrite the current line (Carriage return \r),
        # and flush to ensure immediate display
        print(Fore.CYAN + "\r" + "Loading... " + animation[idx % len(animation)], end="", flush=True)
        idx += 1  # Move to the next animation character
        time.sleep(0.1)  # Pause for a short time to control animation speed
    # Clear the loading line after completion
    print("\r" + " " * (len("Loading... ") + 1 + len(animation)), end="", flush=True)

#I did this because the animation loop forever if i dont use threads
def start_loading_animation():
    global loading_complete  # Access global variable loading_complete
    loading_complete = False  # Set loading_complete to False to start animation
    loading_thread = threading.Thread(target=loading)  # Create a new thread for the loading animation
    loading_thread.start()  # Start the thread
    return loading_thread  # Return the thread object to the caller

def stop_loading_animation(loading_thread):
    global loading_complete  # Access global variable loading_complete
    loading_complete = True  # Set loading_complete to True to stop the animation loop
    loading_thread.join()  # Wait for the loading thread to complete