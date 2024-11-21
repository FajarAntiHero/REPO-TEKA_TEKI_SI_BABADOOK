"""
=================== HALAMAN UTAMA DARI PROGRAM TEKA TEKI SI BABADOOK =====================
"""
import os 
import theModule as tm


def main():
    #VARIABLE ASSETS
    garis = tm.line()
    judul = tm.title()

    tm.clearTerminal()
    
    #MAIN DASHBOARD GAME
    print(garis.duaGaris())
    print(judul.mainTitle())
    print(garis.duaGaris())
    print(judul.menuTitle())
    print(garis.satuGaris())
    print("")
    print("\t 1. Mulai Permainan [MP]")
    print("\t 2. Cerita [C]")
    print("\t 3. Pengaturan [P]")
    print("")
    print(garis.satuGaris())
    
    #INPUT ACTION
    while True:
        menuAction = str(input("Masukkan Pilihan Anda dari menu [MP/C/P]: "))
        if menuAction == "MP" or menuAction == "mp" or menuAction == "1":
            action = "Mulai Game"
            break
        elif menuAction == "C" or menuAction == "c" or menuAction == "2":
            action = "Cerita"
            break
        elif menuAction == "P" or menuAction == "p" or menuAction == "3":
            action = "Pengaturan"
            break
        else:
            print("Pilihan tidak terdapat dalam Menu, Ulangi Lagi!")
    

    #AFTER ACTION
    match action:
        case "Mulai Game" : tm.permainan()
        case "Cerita" : tm.story()
        case "Peraturan" : pass

    tm.clearTerminal()

    print(garis.duaGaris())
    print(judul.endTitle())
    print(garis.duaGaris())
    print("")

if __name__ == "__main__":
    main()

    