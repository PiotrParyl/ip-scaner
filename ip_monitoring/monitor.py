from utils import *




def run_program():
    target = Ip_Info_Heandle()
    program_status = True

    ip = target.print_ip()
    #network_adress = utils.your_network_address()
    while program_status:
        print("======="*10)
        print(f" Welcome to IP-Monitor-Tool by https://github.com/PiotrParyl  \n Your ip address is: {ip}  Your network addres: będzie potem ")
        print(f"What do You want to do buddy ?: ")
        print(f"Scan all IP from {ip} subnet and export .csv file (1)")
        print("Show me the time(2)")
        print("What was the 20th president of the USA(3)")
        print("======="*10)

        anser = str(input("==>"))
        if anser == "1":
            ip_list = your_network_addres()
            print(ip_list)
        if anser == "2":
            pass
        if anser == '3':
            pass    
        



if __name__ == "__main__":
    run_program()