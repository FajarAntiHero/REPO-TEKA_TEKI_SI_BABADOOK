from . import karakter as kr
from . import assets as ast
from . import peraturan as prt

garis = ast.line()
judul = ast.title()

def permainan():
    karakterUtama = kr.inputKarakter()
    ast.next()

    ast.clearTerminal()
    print(garis.duaGaris())
    print(judul.characterTitle())
    print(garis.duaGaris())
    print("")
    print(f"Nama Karakter : {karakterUtama.getName}")
    print(f"Tinggi Karakter : {karakterUtama.getTinggi} cm")
    print(f"Jenis Kelamin Karakter : {karakterUtama.getKelamin}")
    print("")
    print(garis.satuGaris())

    while True:
        startGame = str(input("Mulai Game! [Y] : "))
        if startGame == "Y" or startGame == "y":
            break
        else:
            print("Data yang dimasukkan tidak sesuai. Ulangi Kembali!")

    print(garis.satuGaris())
    ast.jeda(1)

    prt.peraturanSingkat()

    
    while True:
        #================== CHAPTER ONE =================
        ast.clearTerminal()
        print(garis.duaGaris())
        print(judul.storyTitle(1))
        print(garis.satuGaris())
        print("")
        indexS = ast.listPath[0] #Indeks Story 1
        ast.openDocument(indexS)
        print("")
        print(garis.satuGaris())

        ast.next()
        ast.clearTerminal()

        print(garis.duaGaris())
        print(judul.questionTitle(1))
        print(garis.satuGaris())
        print("")
        indexQ = ast.listPath[5]
        ast.openDocument(indexQ)
        print("")
        print(garis.satuGaris())
        print(judul.answerTitle())
        print(garis.satuGaris())
        print("")
        print("\t 1. Berdoa [1]")
        print("\t 2. Mendatangi Sumber Suara [2]")
        print("\t 3. Tidur [3]")
        print("\t 4. Keluar Rumah [4]")
        print("\t 5. Duduk Menonton TV [5]")
        print("")
        print(garis.satuGaris())
        while True:
            try:
                inputJawaban = int(input("Masukkan Pilihan Jawaban! ANGKA [1/2/3/4/5]: "))
                if inputJawaban == 1 or inputJawaban == 2 or inputJawaban == 3 or inputJawaban == 4 or inputJawaban == 5 :
                    jawaban = str(inputJawaban)
                    break
                else:
                    print("Pilihan tidak sesuai kriteria. Ulangi!")
            except:
                print("Pilihan kamu bukan angka. Ulangi!")

        jawaban1 = jawaban
        hasil = ast.hasilJawaban1(jawaban)
        
        if hasil == "benar":
            print(garis.satuGaris())
            ast.afterJawaban1(jawaban1)
            print(garis.satuGaris())
            ast.next()
            ast.clearTerminal()

            print(garis.duaGaris())
            print(judul.loreTitle(1))
            print(garis.duaGaris())
            print("")
            ast.lore1(jawaban1)
            print("")
            print(garis.satuGaris())

            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            ast.clearTerminal()
        else:
            print(garis.satuGaris())
            ast.afterJawaban1(jawaban1)
            print(garis.satuGaris())
            ast.next()
            ast.gameLost()
            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            break

        #===== SLEEP =======

        #================== CHAPTER TWO =================
        print(garis.duaGaris())
        print(judul.storyTitle(2))
        print(garis.satuGaris())
        print("")
        indexS = ast.listPath[1] #Indeks Story 2
        ast.openDocument(indexS)
        print("")
        print(garis.satuGaris())

        ast.next()
        ast.clearTerminal()

        print(garis.duaGaris())
        print(judul.questionTitle(2))
        print(garis.satuGaris())
        print("")
        indexQ = ast.listPath[6]
        ast.openDocument(indexQ)
        print("")
        print(garis.satuGaris())
        print(judul.answerTitle())
        print(garis.satuGaris())
        print("")
        print("\t 1. Arvel menginjak sesuatu tanpa sengaja [1]")
        print("\t 2. Suara dari angin yang melintasi reruntuhan [2]")
        print("\t 3. Rantai kuno yang bergerak sendiri [3]")
        print("\t 4. Gemericik air dari dalam gua [4]")
        print("\t 5. Sosok bayangan yang memanggil Arvel [5]")
        print("")
        print(garis.satuGaris())
        while True:
            try:
                inputJawaban = int(input("Masukkan Pilihan Jawaban! ANGKA [1/2/3/4/5]: "))
                if inputJawaban == 1 or inputJawaban == 2 or inputJawaban == 3 or inputJawaban == 4 or inputJawaban == 5 :
                    jawaban = str(inputJawaban)
                    break
                else:
                    print("Pilihan tidak sesuai kriteria. Ulangi!")
            except:
                print("Pilihan kamu bukan angka. Ulangi!")

        jawaban2 = jawaban
        hasil = ast.hasilJawaban2(jawaban)
        
        if hasil == "benar":
            print(garis.satuGaris())
            ast.afterJawaban2(jawaban2)
            print(garis.satuGaris())
            ast.next()
            ast.clearTerminal()

            print(garis.duaGaris())
            print(judul.loreTitle(2))
            print(garis.duaGaris())
            print("")
            ast.lore2(jawaban1, jawaban2)
            print("")
            print(garis.satuGaris())

            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            ast.clearTerminal()
        else:
            print(garis.satuGaris())
            ast.afterJawaban2(jawaban2)
            print(garis.satuGaris())
            ast.next()
            ast.gameLost()
            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            break

        #====== SLEEP =======


        #======================== CHAPTER THREE ========================
        print(garis.duaGaris())
        print(judul.storyTitle(3))
        print(garis.satuGaris())
        print("")
        indexS = ast.listPath[2] #Indeks Story 3
        ast.openDocument(indexS)
        print("")
        print(garis.satuGaris())

        ast.next()
        ast.clearTerminal()

        print(garis.duaGaris())
        print(judul.questionTitle(3))
        print(garis.satuGaris())
        print("")
        indexQ = ast.listPath[7]
        ast.openDocument(indexQ)
        print("")
        print(garis.satuGaris())
        print(judul.answerTitle())
        print(garis.satuGaris())
        print("")
        print("\t 1. Hantu yang mengintaimu [1]")
        print("\t 2. Makhluk tak kasat mata [2]")
        print("\t 3. Setan yang meniru langkahmu [3]")
        print("\t 4. Arwah penasaran [4]")
        print("\t 5. Bayangan masa lalu [5]")
        print("")
        print(garis.satuGaris())
        while True:
            try:
                inputJawaban = int(input("Masukkan Pilihan Jawaban! ANGKA [1/2/3/4/5]: "))
                if inputJawaban == 1 or inputJawaban == 2 or inputJawaban == 3 or inputJawaban == 4 or inputJawaban == 5 :
                    jawaban = str(inputJawaban)
                    break
                else:
                    print("Pilihan tidak sesuai kriteria. Ulangi!")
            except:
                print("Pilihan kamu bukan angka. Ulangi!")

        jawaban3 = jawaban
        hasil = ast.hasilJawaban3(jawaban)
        
        if hasil == "benar":
            print(garis.satuGaris())
            ast.afterJawaban3(jawaban3)
            print(garis.satuGaris())
            ast.next()
            ast.clearTerminal()

            print(garis.duaGaris())
            print(judul.loreTitle(3))
            print(garis.duaGaris())
            print("")
            ast.lore3(jawaban1, jawaban2, jawaban3)
            print("")
            print(garis.satuGaris())

            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            ast.clearTerminal()
        else:
            print(garis.satuGaris())
            ast.afterJawaban3(jawaban3)
            print(garis.satuGaris())
            ast.next()
            ast.gameLost()
            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            break

        #======================== CHAPTER FOUR ========================
        print(garis.duaGaris())
        print(judul.storyTitle(4))
        print(garis.satuGaris())
        print("")
        indexS = ast.listPath[3] #Indeks Story 4
        ast.openDocument(indexS)
        print("")
        print(garis.satuGaris())

        ast.next()
        ast.clearTerminal()

        print(garis.duaGaris())
        print(judul.questionTitle(4))
        print(garis.satuGaris())
        print("")
        indexQ = ast.listPath[8]
        ast.openDocument(indexQ)
        print("")
        print(garis.satuGaris())
        print(judul.answerTitle())
        print(garis.satuGaris())
        print("")
        print("\t 1. Rawa-rawa [1]")
        print("\t 2. Jalur Kawat [2]")
        print("\t 3. Lorong panjang yang kecil [3]")
        print("\t 4. Sungai Dangkal [4]")
        print("\t 5. Jembatan Kayu [5]")
        print("")
        print(garis.satuGaris())
        while True:
            try:
                inputJawaban = int(input("Masukkan Pilihan Jawaban! ANGKA [1/2/3/4/5]: "))
                if inputJawaban == 1 or inputJawaban == 2 or inputJawaban == 3 or inputJawaban == 4 or inputJawaban == 5 :
                    jawaban = str(inputJawaban)
                    break
                else:
                    print("Pilihan tidak sesuai kriteria. Ulangi!")
            except:
                print("Pilihan kamu bukan angka. Ulangi!")

        jawaban4 = jawaban
        hasil = ast.hasilJawaban4(jawaban)
        
        if hasil == "benar":
            print(garis.satuGaris())
            ast.afterJawaban4(jawaban4)
            print(garis.satuGaris())
            ast.next()
            ast.clearTerminal()

            print(garis.duaGaris())
            print(judul.loreTitle(4))
            print(garis.duaGaris())
            print("")
            ast.lore4(jawaban1, jawaban2, jawaban3, jawaban4)
            print("")
            print(garis.satuGaris())

            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            ast.clearTerminal()
        else:
            print(garis.satuGaris())
            ast.afterJawaban4(jawaban4)
            print(garis.satuGaris())
            ast.next()
            ast.gameLost()
            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            break


        #======================== CHAPTER FIVE ========================
        print(garis.duaGaris())
        print(judul.storyTitle(5))
        print(garis.satuGaris())
        print("")
        indexS = ast.listPath[4] #Indeks Story 5
        ast.openDocument(indexS)
        print("")
        print(garis.satuGaris())

        ast.next()
        ast.clearTerminal()

        print(garis.duaGaris())
        print(judul.questionTitle(5))
        print(garis.satuGaris())
        print("")
        indexQ = ast.listPath[9]
        ast.openDocument(indexQ)
        print("")
        print(garis.satuGaris())
        print(judul.answerTitle())
        print(garis.satuGaris())
        print("")
        print("\t 1. Berlari sekencang-kencangnya ke arah hutan tanpa melihat ke belakang [1]")
        print("\t 2. Melemparkan barang bawaanmu ke jurang sebagai persembahan untuk menenangkan Babadook. [2]")
        print("\t 3. Menghadap Babadook dan meminta maaf dengan tulus atas kesalahanmu [3]")
        print("\t 4. Berlari sekencang-kencangnya ke arah hutan tanpa melihat ke belakang [4]")
        print("\t 5. Melompat ke dalam jurang, berharap bisa menemukan jalan keluar di bawah [5]")
        print("")
        print(garis.satuGaris())
        while True:
            try:
                inputJawaban = int(input("Masukkan Pilihan Jawaban! ANGKA [1/2/3/4/5]: "))
                if inputJawaban == 1 or inputJawaban == 2 or inputJawaban == 3 or inputJawaban == 4 or inputJawaban == 5 :
                    jawaban = str(inputJawaban)
                    break
                else:
                    print("Pilihan tidak sesuai kriteria. Ulangi!")
            except:
                print("Pilihan kamu bukan angka. Ulangi!")

        jawaban5 = jawaban
        hasil = ast.hasilJawaban5(jawaban)
        
        if hasil == "benar":
            print(garis.satuGaris())
            ast.afterJawaban5(jawaban5)
            print(garis.satuGaris())
            ast.next()
            ast.clearTerminal()

            print(garis.duaGaris())
            print(judul.loreTitle(5))
            print(garis.duaGaris())
            print("")
            ast.lore5(jawaban1, jawaban2, jawaban3,jawaban4, jawaban5)
            print("")
            print(garis.satuGaris())

            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            ast.clearTerminal()
        else:
            print(garis.satuGaris())
            ast.afterJawaban5(jawaban5)
            print(garis.satuGaris())
            ast.next()
            ast.gameLost()
            ast.next()
            print(garis.satuGaris())
            ast.jeda(1)
            break

        #==================== BERHASIL MEMENANGKAN PERMAINAN =================
        print(garis.duaGaris())
        print(judul.theTitle("kamu berhasil!".upper()))
        print(garis.duaGaris())
        print("")
        print("{:^80}".format("Selamat kamu telah melewati seluruh teka teki nya"))
        print("{:^80}".format("Kamu adalah orang hebat, cerdas dan bijaksana"))
        print("{:^80}".format("Temukan lebih banyak jawaban teka teki si Babadook"))
        print("{:^80}".format("Sebenarnya kamu hanya menemukan beberapa jawaban saja...."))
        print("")
        print(garis.duaGaris())
        ast.next()
        ast.clearTerminal()
        print(garis.duaGaris())
        print(judul.theTitle("sertifikat juara".upper()))
        print(garis.duaGaris())
        print("")
        print("{:^80}".format("Selamat kepada sang juara"))
        print("")
        print("{:^80}".format(karakterUtama.getName.upper()))
        print("{:^80}".format("-"*len(karakterUtama.getName)))
        print("")
        print("{:^80}".format("Predikat untuk sang Juara"))
        print("{:^80}".format("Pahlawan yang Berani dan Bijaksana"))
        print("")
        print(garis.duaGaris())
        ast.next()
        print(garis.satuGaris())
        ast.jeda(1)


        break # -> Game Berakhir