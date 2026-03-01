import sys
import socket
import pyfiglet
import time


ascii_banner = pyfiglet.figlet_format("Port Recon Pro", font = "cybermedium")
ascii_banner2 = pyfiglet.figlet_format("By Jawun L. Boyd", font = "term")
print(ascii_banner)
print(ascii_banner2)

# Port Scanner While Loop
while True:
    # User IP Address input
    ip = input("Enter IP Address or type 'quit' to quit: ").lower()
    if not ip:
        print("Please enter an IPv4 address")
        print(ip)
    elif ip == "quit":
        print(pyfiglet.figlet_format("Goodbye!", font = "cybermedium"))
        break

    # IPv4 Check
    print("IPv4 Address Verification....")
    parts = ip.split(".")
    if len(parts) != 4:
        time.sleep(1.5)
        print("Not a valid IPv4 address! You 4 numbers separated by dots.")
        continue
    else:
        time.sleep(1.5)
        print("IPv4 Verified!")

    # Iterating through each octet in the IP Address to verify that input is an integer and less than 255
    try:
        for p in parts:
            if  not (0<= int(p) <= 255):
                raise ValueError
            break
    except ValueError:
        print("Invalid IPv4 address - numbers must be 0-255")
        continue

# Ports Verification
    open_ports = []

    # Starting Port
    time.sleep(1)
    portA = input("Starting Port: ")
    if not portA:
        portA = input("Enter Starting Port: ")
        continue

    # Ending Port
    time.sleep(1)
    portZ = input("Ending Port: ")
    if not portZ:
        portZ = input("Enter Ending Port: ")
        continue

    time.sleep(1)
    print(f"Scanning {ip} ports {portA} - {portZ}") # Displays User's IP Address, and Ports to be scanned
    def probe_port(ip, port, result = 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            r = sock.connect_ex((ip, port))
            if r == 0:
                result = r
            sock.close()
        except Exception as e:
            pass
        return result

    # Iterating through the ports
    ports = range(int(portA), int(portZ) + 1)
    for port in ports:
        sys.stdout.flush()
        response = probe_port(ip, port)
        if response == 0:
            open_ports.append(port)

    if open_ports:
        print("Open Ports are: ", sorted(open_ports))
    else:
        print ("Looks like no ports are open :(")

