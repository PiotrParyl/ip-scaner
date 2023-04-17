# opis struktury repozytorium:

Opis poszczególnych elementów struktury:

README.md - plik opisujący cel projektu, sposób instalacji i użytkowania,
requirements.txt - plik z listą zależności projektu,

ip_monitoring/ - pakiet zawierający kod źródłowy programu,
    __init__.py - pusty plik inicjalizujący pakiet,
    config.py - plik zawierający konfigurację programu (np. adresy IP, porty, itp.),
    db.py - plik zawierający definicje tabel i funkcje dostępu do bazy danych,
    monitor.py - główny plik programu, który uruchamia monitorowanie adresów IP,
    utils.py - plik zawierający przydatne funkcje pomocnicze,

tests/ - folder z testami jednostkowymi,
    __init__.py - pusty plik inicjalizujący pakiet,
    test_config.py - plik z testami konfiguracji programu,
    test_db.py - plik z testami funkcji dostępu do bazy danych,
    test_monitor.py - plik z testami monitorowania adresów IP,
    test_utils.py - plik z testami funkcji pomocniczych,

scripts/ - folder z przykładowymi skryptami,
    install.sh - skrypt instalujący zależności i konfigurujący program,
    start_monitoring.sh - skrypt uruchamiający monitorowanie adresów IP.


# Set up Ip-Scaner


Run commend:
    python 




















# Server Menager

-----------------------------------------------------------
## Table of contents
* [About Project](#about-project)
* [Set up](#set-up)
* [Technologies](#technologies)
* [Scheme](#scheme)
* [Docker](#docker)

-----------------------------------------------------------
# About Project

The task of the project is to monitor the activity of remote servers. If any stops working we will get information which one and at what time on SMS and email. The project may seem simple but it is the first in which I used (or at least there was such an attempt) OOP (the objects are servers in this case). This is a very early version, and not exact. Rather, the goal is to collect some specific feedback on how to create such projects, create a repo, probably a component, mainly how to improve to make it better !!! 

The general principle of the program at the moment is as follows. At the entrance we give the IP addresses of our servers. After adding servers, we have a small preview of what servers we added and if they are online/offline. After firing "monitoring" the program runs in the background (so we can, for example: go back to the main menu and scan the LAN for ourselves :) addition for fun)

The next step will be to create a user account so that our servers are saved in the DB. Now anyone will be able to download the program, register and monitor the added servers :) 

An interesting addition will be the ability to write with other users from within the program hmm . .

-----------------------------------------------------------
# Set up

Before running the program, you need to install the necessary libraries, they can be found in requaierments.txt files. To install the package you should:
'pip install -r requirements.txt'

## Technologies
-----------------------------------------------------------
Technologies Used
The following technologies have been used in this project:

* Python 3
* RaspberryPi 3
* ESP8266 microcontroller
* Electric water meter with Modbus TCP technology
* Energy consumption meter with MODBUS RS485
* Solar panel manufacturer API
* MySQL database
* Linux Ubuntu OS
* AWS

## Scheme
![image](https://user-images.githubusercontent.com/44020188/187191983-09bdd6a8-7a62-4bd9-ab2f-6382e4290327.png)


## Docker
-- Not Ready Yet --

























