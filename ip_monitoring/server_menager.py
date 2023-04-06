import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os
from .email_send import *


class Server_Menager():

    def __init__(self,server_ip,short_description):

        self.server_ip = server_ip
        self.server_status = bool
        self.set_server_status()
        self.short_description = short_description
        


    def set_server_status(self):
    
        hostname = self.server_ip #example
        response = os.system("ping -n 1 " + hostname)

        
        if response == 0:
            self.server_status = True
        else:
            self.server_status = False



    def server_up_down(self):
        ip_address = self.server_ip
        result = subprocess.run(['ping', '-n', '1', ip_address], stdout=subprocess.PIPE)
        if result:
            return f'Serwer with IP {self.server_ip} is UP'
        else:
            return 'Server is DOWN'
    


    def print_ip(self):
        return self.server_ip

    def print_desc(self):
        return self.short_description

    

    def server_description(self):
        print(f"IP server: {self.server_ip} \n Server statur: {self.server_status} \n Description: {self.print_desc()}")


    def send_email(self):
        send_email(self.server_ip)





"""server1 = Server_Menager('52.207.176.69','serwer baz danych')
server2 = Server_Menager('34.239.128.130', 'server VPN')
server3 = Server_Menager('44.203.77.35', 'server bramka sms/email')"""







