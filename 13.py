import numbers
from textwrap import wrap
from urllib.request import Request, urlopen

#import numbers
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

#select randomness & decode 
number = [] 
number.append(data[31:95].decode("UTF-8"))

#separate at every to digits
digits = []
digits = wrap(number[0],2)

#convert to decimal number system & mod 80
decimal = []
final = []
for i in range(len(digits) - 1):
    decimal.append(int(digits[i],16))
    decimal[i] = decimal[i] % 80
final.append(list(set(decimal)))

#import KINO winning numbers
req_kino = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data_url = urlopen(req_kino).read()
data_url = data_url[:350].decode("UTF-8")
a = data_url.index("list")
data_kino = []
data_kino_2 = []
winning_numbers = []
data_kino.append(data_url[a:])
data_kino = data_kino[0].split('"')
data_kino_2.append(data_kino[1])
data_kino_2 = data_kino_2[0][2:-2]
winning_numbers = (list(data_kino_2.split(',')))
winning_numbers = [int(n) for n in winning_numbers]

#check 
last = []
for i in range(len(winning_numbers) - 1):
    if (winning_numbers[i] in final[0]):
        last.append(winning_numbers[i])

if len(last) > 0:
    print("number/s: ",end="")
    for i in range(len(last)):
        print(str(last[i]) + (" "),end="")
    print(" was/were drawn in latest KINO draw")
else:
    print("no number was drawn in latest KINO draw")











