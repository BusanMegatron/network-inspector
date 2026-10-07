import socket

domain = input("Enter the domain: ")

ip = socket.gethostbyname(domain)

print("Domain:", domain)
print("IP", ip)