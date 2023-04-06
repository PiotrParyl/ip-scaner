from ip_monitoring import server_menager
import time


global email_sendet
email_sendet = False

def siemanko():
    

    while True:

        server1 = server_menager.Server_Menager('44.204.151.112', 'server VPN')

        if server1.server_status:
            print('Server działa')
            email_sendet == False
        else:
            print('error')
            if email_sendet == False:
                server1.send_email()
                email_sendet == True
            else:
                pass


        time.sleep(3.0)


siemanko()