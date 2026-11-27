import os
import platform
import time

os.system("pip install requests")
fuck = platform.architecture()[0]
if fuck == '64bit':
    os.system('git pull')
    os.system('clear')
    print('[•] YOUR DEVICE IS 64 BIT')
    time.sleep(2)
    from ccc import GREEN, RED, CYAN, ORANGE, LINE, autom_main
    autom_main()
if fuck == '32bit':
    os.system('git pull')
    os.system('clear')
    print('[•] YOUR DEVICE IS 32 BIT')
    time.sleep(2)
    from ccc import GREEN, RED, CYAN, ORANGE, LINE, autom_main
    autom_main()
os.system('clear')
print('\x1b[1;97m Soon Your Device Support')
