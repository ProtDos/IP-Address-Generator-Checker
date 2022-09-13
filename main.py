from faker import Faker
import socket
import threading, time

amount = int(input("Enter amount ('0' for unlimited): "))
output = input("Output file destination (press enter for none): ")
plain = input("Plain output (y/n)? ")
threads = int(input("How many threads? "))

if threads >= amount / 40:
    print("Too many threads. Less threads recommended.")
    a = input("Exit (y/n)? ")
    if a == "y":
        exit()
    else:pass

ips = []

def check(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error:
        return False
count = 0
def start():
    global count
    while True:
        count += 1
        if amount != 0:    
            if plain == "n":
                if output == "" or output == None:

                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print("[+] Valid: ", ip)
                            ips.append(ip)
                        else:
                            count -= 1
                            pass
                            #print("[-] Invalid: ", ip)
                else:

                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                           # print("[+] Valid: ", ip)
                            ips.append(ip)
                            with open(output, "a") as f:
                                f.write(ip+"\n")                
                        else:
                            count -= 1
                            pass
                            #print("[-] Invalid: ", ip)
            else:
                if output == "" or output == None:

                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print(ip, end="\n")
                            ips.append(ip)
                        else:
                            count -= 1
                            pass
                else:

                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print(ip, end="\n")
                            ips.append(ip)
                            with open(output, "a") as f:
                                f.write(ip+"\n")                
                        else:
                            count -= 1
                            pass
        else:
            if plain == "n":
                if output == "" or output == None:
                    while True:
                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print("[+] Valid: ", ip)
                            ips.append(ip)
                        else:
                            count -= 1
                            pass
                            #print("[-] Invalid: ", ip)
                else:
                    while True:
                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print("[+] Valid: ", ip)
                            ips.append(ip)
                            with open(output, "a") as f:
                                f.write(ip+"\n")                
                        else:
                            count -= 1
                            pass
                            #print("[-] Invalid: ", ip)
            else:
                if output == "" or output == None:
                    while True:
                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print( ip, end="\n")
                            ips.append(ip)
                        else:
                            count -= 1
                            pass
                else:
                    while True:
                        ex = Faker()
                        ip = ex.ipv4()
                        if check(ip):
                            #print(ip, end="\n")
                            ips.append(ip)
                            with open(output, "a") as f:
                                f.write(ip+"\n")                
                        else:
                            count -= 1
                            pass
        if count >= amount:
            break

t = []
for i in range(threads):
    t.append(threading.Thread(target=start))

for item in t:
    item.start()
    
print("Started...")

while True:
    if count >= amount:
        for item in ips:
            print(item)
        break
    time.sleep(5)
