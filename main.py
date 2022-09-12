from faker import Faker
import socket

amount = int(input("Enter amount: "))
output = input("Output file destination: ")

def check(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False

if output == "" or output == None:
    for i in range(amount):
        ex = Faker()
        ip = ex.ipv4()
        if check(ip):
            print("[+] Valid: ", ip)
        else:
            print("[-] Invalid: ", ip)
else:
    for i in range(amount):
        ex = Faker()
        ip = ex.ipv4()
        if check(ip):
            print("[+] Valid: ", ip)
            with open(output, "a") as f:
                f.write(ip+"\n")                
        else:
            print("[-] Invalid: ", ip)
