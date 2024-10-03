from random import randint

luck = randint(1-10)
if(luck<=20): print("Maaf bang kesialan akan menimpamu")
elif(luck<=50): print("Keberuntungan anda lagi tidak baik")
elif(luck<=70): print("Lumayan keberuntungan anda normal")
elif(luck<=90): print("Keberuntungan ada ditangan anda")
else: print("Geloooo, Hari ini lu bakal beruntung banget brooo")
