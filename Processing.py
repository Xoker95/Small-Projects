from time import sleep 

cursor_left = "\033[1D"
#[1A = 1 Zeile nach oben, B nach unten, C nach Rechts, D nach Links
clear = "\x1b[2K"
#Kein Plan, hab kopiert https://youtu.be/fClsWAnnliE?si=tal4k3eTA2p3q54I
clear_line = cursor_left + clear

for i in range(3):
    print ("Processing",sep="", end="", flush=True)
    for i in range(3):
        print(".", sep= "", end="", flush=True)
        sleep(0.5)
    print(clear_line * 15, end="")
# die Zahl nach clear_line sagt wieviele zeilen links es gehen soll    


print("Done!", sep=" ")
