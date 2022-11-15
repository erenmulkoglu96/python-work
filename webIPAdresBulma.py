# Gerekli modülü içe aktar

import socket as s

#Ana bilgisayar adımı al

my_hostname = s.gethostname()

#Ana bilgisayar adımı göster

print('Your Hostname is: ' + my_hostname)

#IP'mi al

my_ip = s.gethostbyname(my_hostname)

#IP adresimi göster

print('Your IP Address is: ' + my_ip) 

#Ana bilgisayar adını ayarla

host = 'python.org'

#IP'mi getir

ip = s.gethostbyname(host)

#IP'yi göster

print('The IP Address of ' + host + ' is: ' + ip)