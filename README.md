
<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/c44cbaaa-3b6d-4c80-ba67-3207a215fefe" alt="WlanHound" width="700" height="500">

# FTP Aries - Check Anonymous Login Bruteforce FTP
<img src="https://skillicons.dev/icons?i=py" alt="Skills" />

## Overview
Tool to find out if it is possible to access certain hosts with anonymous FTP, also using bruteforce, and more

## Purpose

FTP (File Transfer Protocol) is a network protocol used to transfer files between computers, such as over the Internet. 

<img src="https://private-user-images.githubusercontent.com/62940515/339332439-6f34696a-81e8-41e5-8106-7f932b3c8c4f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgyNzY1ODgsIm5iZiI6MTcxODI3NjI4OCwicGF0aCI6Ii82Mjk0MDUxNS8zMzkzMzI0MzktNmYzNDY5NmEtODFlOC00MWU1LTgxMDYtN2Y5MzJiM2M4YzRmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjEzVDEwNTgwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThjZjM2OTNlYjYzNDVmMTdhZGI3ODgxZGQ4M2RjNmViOThjYzdiOThmNjA2ZGIzZTM0NjUxNmRkZWUxNGZlYTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.rVKb3H5yqDMJFJrUWojMa6HRANG3GRw3_nQzs6q7Dtw" alt="FTP" width="700" height="200">


"Anonymous login" is a feature of FTP servers where uses connect without a personal username and password, using "anonymous" as the username and any email address as the password.
It's often used for downloading public files like open-source software or documentation. 
However, using anonymous login can expose vulnerabilities in the server, so it's not suitable for transferring sensitive or confidential data.

<div>
<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/5519fb95-b11e-4a65-a9a4-06a8b5fc083f" alt="single" width="500" height="200">
<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/7d31fa7c-da0e-4c8e-9471-a86efff8ad58" alt="multiple" width="500" height="200">
   
</div>


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
   
<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/11e411e2-7173-4f73-9979-0aecec8775d6" alt="ipdomainselect" width="500" height="500">


## Releases

#### v1.1
-  Domain List to IP, transform all domains into txt file in ip list
-  
<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/c8e63e24-7e80-41d2-aff0-aabaad309d50" alt="multiple" width="500" height="400" >


#### v1.0
-  Single IP or Domain
-  Multiple IP or Domain with Lists 

<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/225e3503-1cea-4d7f-a6cd-045d693b074c" alt="single" width="500" height="500" >
<img src="https://github.com/gerhash/FTP_Aries/assets/62940515/b7a39f73-e190-4264-886b-a08f78da70a7" alt="multiple" width="500" height="400" >



