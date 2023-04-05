import socket
import subprocess
import socket


class Ip_Info_Heandle():


    def __init__(self):
        hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(hostname)
        


    def print_ip(self):
        #print(self.ip_address)
        return self.ip_address

    def export_data_to_csv(self):
        pass


















def my_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Adres IP twojego komputera to: {ip_address}")




def your_ip_addres():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    str_ip = str(ip_address)
    return str_ip



def your_network_addres():

    # Tworzenie listy adresów IP do sprawdzenia
    up_ip = []
    down_ip = []
    up_ip_int = 0
    down_ip_int = 0

    ip_list = []
    for i in range(1, 255):
        ip = "192.168.1." + str(i)
        ip_list.append(ip)

    # Przejście po liście adresów IP i wywołanie komendy ping dla każdego adresu
    for ip in ip_list:
        result = subprocess.call(["ping", "-n", "1", "-w", "500", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result == 0:
            print(ip + " is UP")
            up_ip.append(ip)
            up_ip_int += 1
        else:
            print(ip + " is DOWN")
            down_ip.append(ip)
            down_ip_int += 1
    print(f"Ther is {up_ip_int} UP hosts and {down_ip_int} DOWN hosts")

    return up_ip