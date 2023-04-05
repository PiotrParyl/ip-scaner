import subprocess

# Tworzenie listy adresów IP do sprawdzenia
ip_list = []
for i in range(1, 255):
    ip = "192.168.1." + str(i)
    ip_list.append(ip)

# Przejście po liście adresów IP i wywołanie komendy ping dla każdego adresu
for ip in ip_list:
    result = subprocess.call(["ping", "-n", "1", "-w", "500", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result == 0:
        print(ip + " is UP")
    else:
        print(ip + " is DOWN")