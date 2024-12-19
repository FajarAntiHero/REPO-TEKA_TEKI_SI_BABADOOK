from .assets import line, title, clearTerminal, next, jeda 

# GLOBAL VARIABLE
garis = line()
judul = title()
peraturanPertama : str = "Permainan akan berisi banyak cerita"
peraturanKedua : str = "Pertanyaan teka teki akan menjebak"
peraturanKetiga : str = "Jika anda gagal menjawab teka teki, permainan akan selesai"
peraturanKeempat : str = "Setiap jawaban yang benar akan memberikan sebuah kejutan"

jumlahPeraturan : list = [peraturanPertama, peraturanKedua, peraturanKetiga, peraturanKeempat]

def peraturanSingkat() -> str:
    while True:
        for x in range(len(jumlahPeraturan)):
            clearTerminal()
            print(garis.duaGaris())
            print(judul.theTitle("peraturan permainan".upper()))
            print(garis.satuGaris())
            print(judul.theTitle(f"peraturan ke {x + 1}"))
            print(garis.satuGaris())
            print("")
            print("{:^80}".format(jumlahPeraturan[x]))
            print("")
            print(garis.satuGaris())
            next()
        print(garis.satuGaris())
        jeda(1)
        break


def peraturanPermainan() -> str:
    while True:
        for x in range(len(jumlahPeraturan)):
            clearTerminal()
            print(garis.duaGaris())
            print(judul.theTitle("peraturan permainan".upper()))
            print(garis.satuGaris())
            print(judul.theTitle(f"peraturan ke {x + 1}"))
            print(garis.satuGaris())
            print("")
            print("{:^80}".format(jumlahPeraturan[x]))
            print("")
            print(garis.satuGaris())
            next()
            print(garis.satuGaris())

        while True:
            lanjut = str(input("Lanjut membaca peraturan? [Y/N] : "))
            if lanjut == "N" or lanjut == "n" or lanjut == "NO" or lanjut == "no" or lanjut == "No":
                result = "No"
                break
            elif lanjut == "Y" or lanjut == "y" or lanjut == "YES" or lanjut == "yes" or lanjut == "Yes":
                result = "Yes"
                break
            else:
                print("Input Tidak sesuai, ulangi lagi!")

        if result == "No":
            jeda(1)
            break
        elif result == "Yes":
            continue
        else:
            continue


    

