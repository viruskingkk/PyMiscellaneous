import os
import requests
import re
from bs4 import BeautifulSoup
import platform
import socket
from dnsknife.scanner import Scanner

ssr=platform.system()
if ssr=="Linux":
    sudo='sudo'
    print("OS:{}".format('Linux'))
elif ssr=="windows":
    sudo=""
    print("OS:{}".format('windows'))

def greedy():
    banner="""
          ________________________________________________   
     /  _____/\______   \_   _____/\_   _____/\______ \  
    /   \  ___ |       _/|    __)_  |    __)_  |    |  \ 
    \    \_\  \|    |   \|        \ |        \ |    `   \
     \______  /|____|_  /_______  //_______  //_______  /
            \/        \/        \/         \/         \/ 
    .___  _________.____       _____    _______  ________   
    |   |/   _____/|    |     /  _  \   \      \ \______ \  
    |   |\_____  \ |    |    /  /_\  \  /   |   \ |    |  \ 
    |   |/        \|    |___/    |    \/    |    \|    `   \
    |___/_______  /|_______ \____|__  /\____|__  /_______  /
                \/         \/       \/         \/        \/ """
    cist=['[1]自動收集基本偵察（即whois，ping，DNS等）,NMAP埠掃描,自動暴力收集子域，收集DNS資訊並檢查區域傳輸','[2]NMap腳本']
    civsd={'1':wds,
           '2':nmap_script}

    while True:
        print()
        print(banner)
        for c in cist:
            print(c)
        user=input('haq>')

        if user in civsd:
            civsd.get(user)()

def wds():
    user=input('查詢的url是:')
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url='https://www.whois.com/search.php?query={}'.format(user)
    reqt=requests.get(url=url,headers=headers)
    bd=BeautifulSoup(reqt.content.decode('utf-8'),'html.parser')
    print('[+]whois信息')
    print('========================================================')
    for pre in bd.find_all('pre'):
        print(pre.get_text())
    print('========================================================')

    guids = []
    guids2 = []
    print('[+]超級ping，判斷是否有CDN')
    print('')
    print('========================================================')
    urli = 'http://ping.chinaz.com/{}'.format(user)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    datas = {'host': '{}'.format(user), 'checktype': '0', 'linetype': '電信',
    'linetype': '多線',
    'linetype': '聯通',
    'linetype': '移動',
    'linetype': '海外'}
    rev = requests.post(url=urli, headers=headers, data=datas)
    bd = BeautifulSoup(rev.text, 'html.parser')
    tr = bd.find_all('div')
    for v in tr:
        guids.append(v.get('id'))

    for key in guids:
        qz = re.findall(
            '[0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z]-[0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z]-[0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z]-[0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z]-[0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z][0-9-a-z-A-Z]',
            str(key))
        for r in qz:
            guids2.append(r + '')

    url = 'http://ping.chinaz.com/iframe.ashx?t=ping&callback=jQuery111306709270458227905_1535617821100'
    for v in guids2:
        data = {'guid': '{}'.format(v),
                'host': 'www.baidu.com/',
                'ishost': 'false',
                'encode': 'uZVguOxtxhFU4L0rQ|zXgulyePFesj4w',
                'checktype': '0'}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        reqt = requests.get(url=url, headers=headers, data=data)
        hostname = re.findall("ip:'.*'", reqt.text)
        for l in hostname:
            print('[+]節點:{}'.format(l))

    print('===========================================================')
    print('')
    print('===========================================================')
    print('[+]dns查詢')
    dnscer = Scanner('{}'.format(user.replace('www.','')).strip()).scan()
    for l in dnscer:
        print(l)
    dnscer.close()
    print('===========================================================')
    print('')
    print('===========================================================')
    print('[+]nmap埠掃描')
    ml="{} nmap -sS -sC -T4 -A {}".format(sudo,socket.gethostbyname(user)).strip()
    os.system(ml)
    print('===========================================================')
    print('')
    print('===========================================================')
    print('[+]子功能變數名稱查詢')
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'http://site.ip138.com/{}/domain.htm'.format(user.replace('www.','').strip())
    reqt = requests.get(url=url, headers=headers)
    domain = re.findall('<a href=".*" target="_blank">.*</a></p>', reqt.content.decode('utf-8'))
    for i in domain:
        bd = BeautifulSoup(i, 'html.parser')
        print(bd.get_text())
    print('===========================================================')

def nmap_script():
    nmap_list=['[1]負責處理鑒權證書（繞開鑒權）的腳本,也可以作為檢測部分應用弱口令','[2]提供暴力破解的方式  可對資料庫，smb，snmp等進行簡單密碼的暴力猜解','[3]檢查是否存在常見漏洞','[4]在局域網內探查更多服務開啟狀況','[5]檢查vnc bypass','[6]smb掃描','[7]Mssql掃描','[8]Mysql掃描','[9]中介軟體檢測']
    while True:
        for k in nmap_list:
            print(k)

        ip=input('IP:')
        user2=input('選擇:')
        if user2=='1':
            print('============================================')
            print('[+]負責處理鑒權證書（繞開鑒權）的腳本,也可以作為檢測部分應用弱口令')
            print('[+]{} nmap --script=auth {}'.format(sudo,ip))
            os.system('{} nmap --script=auth {}'.format(sudo,ip))
            print('============================================')
        elif user2=='2':
            print('============================================')
            print('[+]暴力破解')
            print('[+]{} nmap --script=brute {}'.format(sudo,ip))
            os.system('{} nmap --script=brute {}'.format(sudo,ip))
            print('============================================')
        elif user2=='3':
            print('============================================')
            print('[+]檢查是否存在常見漏洞')
            print('[+]{} nmap --script=vuln {}'.format(sudo,ip))
            os.system('{} nmap --script=vuln {}'.format(sudo,ip))
            print('============================================')
        elif user2=='4':
            print('============================================')
            print('[+]在局域網內探查更多服務開啟狀況')
            print('[+]{} nmap --script=broadcast {}'.format(sudo,ip))
            os.system('{} nmap --script=broadcast {}'.format(sudo,ip))
            print('============================================')
        elif user2=='5':
            print('============================================')
            print('[+]檢查vnc bypass')
            print('[+]{} nmap --script=realvnc-auth-bypass {}'.format(sudo,ip))
            os.system('{} nmap --script=realvnc-auth-bypass {}'.format(sudo,ip))
            print('============================================')
            print('')
            print('============================================')
            print('[+]{} nmap --script=vnc-auth {}'.format(sudo,ip))
            os.system('{} nmap --script=vnc-auth {}'.format(sudo,ip))
            print('============================================')
            print('[+]{} nmap --script=vnc-info  {}'.format(sudo,ip))
            os.system('nmap --script=vnc-info  {}'.format(sudo,ip))
            print('============================================')
        elif user2=='6':
            print('============================================')
            print('[+]smb掃描')
            print('[+]smb破解')
            print('[+]{} nmap  --script=smb-brute.nse {}'.format(sudo,ip))
            os.system('{} nmap  --script=smb-brute.nse {}'.format(sudo,ip))
            print('============================================')
            print('[+]smb已知幾個嚴重漏')
            print('[+]{} nmap  --script=smb-check-vulns.nse --script-args=unsafe=1 {}'.format(sudo,ip))
            os.system('{} nmap  --script=smb-check-vulns.nse --script-args=unsafe=1 {}'.format(sudo,ip))
            print('============================================')
            print('')
            print('============================================')
            print('[+]系統資訊')
            print('[+]{} nmap -n -p445 --script=smb-os-discovery.nse --script-args=smbuser=test,smbpass=test {}'.format(sudo,ip))
            os.system('{} nmap -n -p445 --script=smb-os-discovery.nse --script-args=smbuser=test,smbpass=test {}'.format(sudo,ip))
            print('============================================')
            print('')
            print('============================================')
            print('[+]掃描smb漏洞')
            print('[+]{} nmap --script smb-vuln-ms* {}'.format(sudo,ip))
            os.system('{} nmap --script smb-vuln-ms* {}'.format(sudo,ip))
            print('============================================')
        elif user2=='7':
            print('============================================')
            print('[+]猜解mssql用戶名和密碼')
            isw=input('mssqlport:')
            username=input('mssqlusername.txt:')
            passwd=input('mssqlpasswd.txt:')
            print('{} nmap -p {} --script=ms-sql-brute --script-args=userdb={},passdb={} {}'.format(sudo,isw,username,passwd,ip))
            os.system('{} nmap -p {} --script=ms-sql-brute --script-args=userdb={},passdb={} {}'.format(sudo,isw,username,passwd,ip))
            print('=============================================')
        elif user2=='8':
            print('============================================')
            print('')
            print('============================================')
            print('[+]掃描root空口令')
            mysqlport=input('mysqlport:')
            print('{} nmap -p {} --script=mysql-empty-password.nse {}'.format(sudo,mysqlport,ip))
            os.system('{} nmap -p {} --script=mysql-empty-password.nse {}'.format(sudo,mysqlport,ip))
            print('============================================')
            print('[+]列出所有mysql用戶')
            print('{} nmap -p {} --script=mysql-users.nse --script-args=mysqluser=root {} '.format(sudo,mysqlport,ip))
            os.system('{} nmap -p {} --script=mysql-users.nse --script-args=mysqluser=root {} '.format(sudo,mysqlport,ip))
            print('============================================')
        elif user2=='9':
            print('===========================================')
            print('[+]掃描1-65535埠')
            print('[+]{} nmap -p 1-65535 -T4 {}'.format(sudo,ip))
            os.system('{} nmap -p 1-65535 -T4 {}'.format(sudo,ip))
            print('===========================================')
            print('')
            print('===========================================')
            print('[+]檢測http服務拒絕')
            print('[+]{} nmap --max-parallelism 800--script http-slowloris {}'.format(sudo,ip))
            os.system('{} nmap --max-parallelism 800--script http-slowloris {}'.format(sudo,ip))
            print('===========================================')
            print('')
            print('===========================================')
            print('[+]使用nmap 進行利用協力廠商的資料庫或資源進行資訊收集或者攻擊')
            print('[+]{} nmap --script external {}'.format(sudo,ip))
            print('===========================================')
            print('')
            print('===========================================')
            print('[+]使用nmap 進行模糊測試，發送異常的包到目的機，探測出潛在漏洞')
            print('[+]{} nmap --script fuzzer {}'.format(sudo,ip))
            os.system('{} nmap --script fuzzer {}'.format(sudo,ip))
            print('============================================')
            print('')
            print('============================================')
            print('[+]nmap進行CVE漏洞掃描')
            print('[+]{} nmap --script vulscan -sV {}'.format(sudo,ip))
            os.system('{} nmap --script vulscan -sV {}'.format(sudo,ip))
            print('============================================')
        elif user2 or ip=='q':
            print('[+]退出nmap掃描功能')
            break
        else:
            continue


if __name__ == '__main__':
    greedy()