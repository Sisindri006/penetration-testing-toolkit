from port_scanner import scan_ports
from brute_forcer import ftp_brute_force

print("1. Port Scanner\n2. FTP Brute Force")
choice = input("Select tool (1 or 2): ")

if choice == '1':
    ip = input("Enter IP: ")
    ports = [21, 22, 80, 443]
    scan_ports(ip, ports)

elif choice == '2':
    ip = input("Enter FTP IP: ")
    user = input("Username: ")
    with open("passwords.txt") as f:
        pwds = f.readlines()
    ftp_brute_force(ip, user, pwds)
