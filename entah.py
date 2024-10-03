from random import randint

luck = randint(1-10)
if(luck<=2): print("Maaf bang kesialan akan menimpamu")
elif(luck<=5): print("Keberuntungan anda lagi tidak baik")
elif(luck<=7): print("Lumayan keberuntungan anda normal")
elif(luck<=9): print("Keberuntungan ada ditangan anda")
else: print("Geloooo, Hari ini lu bakal beruntung banget brooo")
