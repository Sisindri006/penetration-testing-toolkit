import socket

def scan_ports(host, ports):
    print(f"Scanning {host}")
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        if s.connect_ex((host, port)) == 0:
            print(f"Port {port} is OPEN")
        s.close()
