import time






def dupa():

    program_status = True
    while program_status:
        print("menu główne")
        print("start program press (1)")
        print("beck to menu (2)")

        anser = input("==>")

        try:
            while True:
                print('siemanko')
                time.sleep(2.0)
        except KeyboardInterrupt:
            dupa()





def program_1():

    print("if you want stop and go back press CTR+C")
    try:
            while True:
                print('siemanko')
                time.sleep(2.0)
    except KeyboardInterrupt:
            dupa()






def server_menager():
     
    numerek1 = 0 
    numerek2 = 0
    numerek3 = 0 

    server_list = ['32.223.12.43','3.83.150.203','1.1.1.1','8.8.8.8','34.239.128.130','44.203.77.35']

    print("| Added Servers | Online sServer | Offline Serwer | Last Error | Wich Server |")

    while True:
        numerek1 += 1 
        numerek2 += 1
        numerek3 += 1
        
        siemanko = f"| {numerek1} | {numerek2}  |       {numerek3}    |"
        
        print(siemanko ,end='\r')
        time.sleep(2.0)
        
        
        



    

server_menager()

