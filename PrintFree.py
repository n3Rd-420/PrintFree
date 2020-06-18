import os
import sys
import time

print('-=-=-=-Welcome To FreePrint!-=-=-=-')
  

printerName = input("[!] Enter The Printer Name [E.G. e4042s01sv006\Parsons-LibStuPhotocopier-VI-C4471_x64]: ")
fileName = (sys.argv[1])
os.system("lpr -P" + printerName + '' + fileName)

animation = "|/-\\"
idx = 0
while (idx < 25):
    print("[*] Processing Print " + animation[idx % len(animation)], end="\r")
    idx += 1
    time.sleep(0.1)
print("[+] Go pick up your print now")









