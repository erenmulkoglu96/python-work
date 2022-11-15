from pytube import YouTube

#Kaydedilecek Yer

SAVE_PATH = "C:/"

#İndirilecek Video linki

link = "https://www.youtube.com/watch?v=K69tbUo3vGs"

try:
    #Youtube kullanarak nesne oluşturmak
    #Başlangıçta Yüklenen Hangisiydi

    yt = YouTube(link)

except:
    print("Baglantı Hatası") #İstisna

#"mp4" uzantılı tüm dosyaları filtreler

mp4files = yt.filter('mp4')

#Dosyanın adını ayarlamak için

yt.set_filename('GeeksforGeeks Video')

#Uzantılı videoyu alın ve
#get() fonksiyonunda geçirilen çözünürlüğü

d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
try:

    #Video indiriliyor

    d_video.download(SAVE_PATH)

except:
    print("Bazı Hatalar Var!")
print('Gorev Tamamlandı!')






