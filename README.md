
<img src="" alt="WlanHound" width="700" height="500">

# FTP Aries - Check Anonymous Login Bruteforce FTP
<img src="https://skillicons.dev/icons?i=py" alt="Skills" />

## Overview
Tool to find out if it is possible to access certain hosts with anonymous FTP, also using bruteforce, and more

## Purpose

FTP (File Transfer Protocol) is a network protocol used to transfer files between computers, such as over the Internet. 

!ftp image

"Anonymous login" is a feature of FTP servers where uses connect without a personal username and password, using "anonymous" as the username and any email address as the password.
It's often used for downloading public files like open-source software or documentation. 
However, using anonymous login can expose vulnerabilities in the server, so it's not suitable for transferring sensitive or confidential data.


## Usage
1. Install the required dependencies listed in `requirements.txt`.
   
 ```sh
   pip install -r requirements.txt
 ```

2. Run the main.py script to start.
   
 ```sh
  python main.py
 ```

3. You can choose to scan IP/Domains single target or multiple targets (put the list in /list/[type] , type stands for ip list or domain list)
!image example

## Releases
#### v1.0
-  Single IP or Domain
-  Multiple IP or Domain with Lists 

!image example2
!image example3
