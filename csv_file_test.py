import csv

ip_list = ['192.168.1.33','192.168.1.37','192.168.1.3','192.168.1.22']


def create_csv():
    f = open("siemanko.csv",'a',newline="")
    dupa = ("bob",19)
    writer = csv.writer(f)
    writer.writerow(dupa)
    f.close


def seve_to_csv():
    f = open('test_file_siemanko.txt', 'w')
    f.write('siemanko byczki')
    f.close()


