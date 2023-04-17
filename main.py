#import ip_monitoring
import add_to_ignore.utils as utils
from server_menager import Server_Menager
import time
import datetime
from add_to_ignore.utils import Ip_Info_Heandle
import os


SERWER_IP = []

global email_sended
email_sended = False


     

def monitoring_server(servers):
    program_status= True

    servers_list = []

    for i in servers:
        ip_ = i.server_ip
        servers_list.append(ip_)


    print(f"Welcome to IP-Monitor-Tool by https://github.com/PiotrParyl  ")
    print(f"Servers being monitored. \n If one stops working you will receive an email to: siemanko@gmail.com ")
    print("If you want stop and back press 'CTR+C'")
    print('------'*10)

    try:
            while True:
                
                for i in servers_list:
                    response = os.system("ping -n 1 " + i)

                    if response == 0:
                        print(f'serwer {i} działa ')
                    else:
                        print(f'serwer {i} no nie dizała  ')

                time.sleep(1.0)

                

    
    
    
    
    
    
    
    
    
    
    
    except KeyboardInterrupt:
            monitoring_server_tool()
                



def monitoring_server_tool():

    

    program_status = True
    while program_status:
        print("======"*10)
        print(f" Welcome to IP-Monitor-Tool by https://github.com/PiotrParyl  ")
        print("Monitorowane servery:")
        print('------'*10)

        print("| IP servera | Server Online | Description |")
        print('------'*10)
        for i in SERWER_IP:
            
            print ("|",i.server_ip,"|",i.server_status,"|",i.short_description)

        print('------'*10)
        print("Dodaj server (1) ")
        print("Usuń server (2) ")
        print("Włącz monitorowanie serwerów (3)")
        print("Powrót (4) ")
        print("======"*10)

        anser = input("==>")

        if anser == '1':
            ip_server = input('Podaj IP servera: ')
            des_server = input('Podaj krótki opis: ')
            server = Server_Menager(ip_server,des_server)
            SERWER_IP.append(server)



        if anser == '2':
            pass

        if anser == '3':
            monitoring_server(SERWER_IP)

        if anser == '3':
            run_program()

        else:
            print('Unknown command')



def run_program():
 
    my_ip = Ip_Info_Heandle()
    program_status = True

    
    #network_adress = utils.your_network_address()
    while program_status:
        print("======="*10)
        print(f" Welcome to IP-Monitor-Tool by https://github.com/PiotrParyl  \n Your ip address is: {my_ip.return_ip()} \n Your network addres: będzie potem ")
        print(f"What do You want to do buddy ?: ")
        print(f"Scan all IP from {my_ip.return_ip()} subnet and export .csv file (1)")
        print('Go to monitoring server tool(Super Cool) (2)')
        print("Show me the time(3)")
        print("What was the 20th president of the USA(4)")
        print("Back to run_program (5)")
        print("======="*10)

        anser = str(input("==>"))
        if anser == "1":
            ip_list = target
            print(ip_list)
        if anser == "2":
            monitoring_server_tool()
        if anser == '3':
            curent_time = datetime.datetime.now()
            print(f"Curent time is: {curent_time}")
        if anser == '4':
            print("Prezydentem Stanów Zjednoczonych był James A. Garfield. \n  Pełnił on swoją funkcję od 4 marca 1881 roku  \n do swojej śmierci 19 września 1881 roku, zaledwie \n po 200 dniach urzędowania.")

        else:
            print('Unknown command')



if __name__ == "__main__":
    run_program()