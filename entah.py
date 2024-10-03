from display import print_menu as pm
from random import randint

luck = randint(1-10)
if(luck<=2): pm("Maaf bang kesialan akan menimpamu")
elif(luck<=5): pm("Keberuntungan anda lagi tidak baik")
elif(luck<=7): pm("Lumayan keberuntungan anda normal")
elif(luck<=9): pm("Keberuntungan ada ditangan anda")
else: pm("Geloooo, Hari ini lu bakal beruntung banget brooo")
