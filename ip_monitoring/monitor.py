from utils import *
import time
import datetime
from server_menager import Server_Menager


SERWER_IP = []

global email_sended
email_sended = False


     

def monitoring_server(servers):
    program_status= True

    servers_list = []

    for i in servers:
        ip_ = i.server_ip
        servers_list.append(ip_)

    print(servers_list)

    print(f" Welcome to IP-Monitor-Tool by https://github.com/PiotrParyl  ")
    print(f"Servers being monitored. \n If one stops working you will receive an email to: siemanko@gmail.com ")
    print("If you want stop and back press 'CTR+C'")
    print('------'*10)

    try:
            while True:
                pass


                
    
    
    
    
    
    
    
    
    
    
    
    
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




def run_program():
 
    target = Ip_Info_Heandle()
    program_status = True

    
    #network_adress = utils.your_network_address()
    while program_status:
        print("======="*10)
        print(f" Welcome to IP-Monitor-Tool by https://github.com/PiotrParyl  \n Your ip address is: {target.print_ip()} \n Your network addres: będzie potem ")
        print(f"What do You want to do buddy ?: ")
        print(f"Scan all IP from {target.print_ip()} subnet and export .csv file (1)")
        print('Go to monitoring server tool(Super Cool) (2)')
        print("Show me the time(3)")
        print("What was the 20th president of the USA(4)")
        print("Back to run_program (5)")
        print("======="*10)

        anser = str(input("==>"))
        if anser == "1":
            ip_list = your_network_addres()
            print(ip_list)
        if anser == "2":
            monitoring_server_tool()
        if anser == '3':
            curent_time = datetime.datetime.now()
            print(f"Curent time is: {curent_time}")
        if anser == '4':
            print("Prezydentem Stanów Zjednoczonych był James A. Garfield. \n  Pełnił on swoją funkcję od 4 marca 1881 roku  \n do swojej śmierci 19 września 1881 roku, zaledwie \n po 200 dniach urzędowania.")

        



if __name__ == "__main__":
    run_program()
