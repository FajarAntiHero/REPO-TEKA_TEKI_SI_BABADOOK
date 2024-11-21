import os

def name():
    inputNama = str(input("Masukkan Nama Karakter : "))
    return inputNama

def tinggi():
    while True:
        try:
            inputTinggi = int(input("Masukkan Tinggi Badan Karakter [CM]: "))
            if inputTinggi > 200 :
                print("Tinggi Badan tidak masuk akal. Ulangi!")
            elif inputTinggi <= 0:
                print("Tinggi Badan tidak boleh 0 atau negatif")
            else:
                return inputTinggi  
        except:
            print("Data harus berupa angka, Ulangi kembali!")

def kelamin():
    while True:
        inputKelamin = str(input("Masukkan Jenis Kelamin Karakter [LK/PR] : "))
        if inputKelamin == "LK" or inputKelamin == "lk" or inputKelamin == "Laki-laki" or inputKelamin == "laki=laki":
            jeniskelamin = "Laki-laki"
            break
        elif inputKelamin == "PR" or inputKelamin == "pr" or inputKelamin == "Perempuan" or inputKelamin == "perempuan":
            jeniskelamin = "Perempuan"
            break
        else:
            print("Jenis Kelamin tidak sesuai kriteria")

    return jeniskelamin

def clearTerminal():
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

def next():
    while True:
        inputNext = str(input("Lanjut [Y] : "))
        if inputNext == "Y" or inputNext == "y" or inputNext == "yes" or inputNext == "YES":
            break
        else:
            print("Input tidak sesuai. Ulangi!")

def openDocument(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except:
        print("File tidak ditemukan!")

# def openBigDocument(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 print(line.strip())
#     except:
#         print("File tidak ditemukan!")

#======================= PROSES QUESTION 1 ==========================            

def hasilJawaban1(jawaban):
    if jawaban == "1":
        hasil = "benar"
        return hasil
    elif jawaban == "2":
        hasil = "salah"
        return hasil
    elif jawaban == "3":
        hasil = "salah"
        return hasil
    elif jawaban == "4":
        hasil = "benar"
        return hasil
    elif jawaban == "5":
        hasil = "salah"
        return hasil
    
def afterJawaban1(firstJawaban):
    if firstJawaban == "1" or firstJawaban == "4": #True
        openDocument(listPathAnswer[0]) 
    elif firstJawaban == "2" or firstJawaban == "3" or firstJawaban == "5": #False
        openDocument(listPathAnswer[5]) 


def lore1(indexLore):
    if indexLore == "1":
        openDocument(listPathLore[0])
    elif indexLore == "4":
        openDocument(listPathLore[5])


#=========================== PROSES QUESTION 2 ===============================
def hasilJawaban2(jawaban):
    if jawaban == "1":
        hasil = "salah"
        return hasil
    elif jawaban == "2":
        hasil = "salah"
        return hasil
    elif jawaban == "3":
        hasil = "benar"
        return hasil
    elif jawaban == "4":
        hasil = "salah"
        return hasil
    elif jawaban == "5":
        hasil = "benar"
        return hasil
    
def afterJawaban2(secondJawaban):
    if secondJawaban == "5" or secondJawaban == "3": #True
        openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "5": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5": #True
    #     openDocument(listPathAnswer[1])
    elif secondJawaban == "1" or secondJawaban == "2" or secondJawaban == "4": #False
        openDocument(listPathAnswer[6])


def lore2(firstJawaban, secondJawaban):
    if firstJawaban == "1" and secondJawaban == "3":
        openDocument(listPathLore[1])
    elif firstJawaban == "1" and secondJawaban == "5":
        openDocument(listPathLore[6])
    elif firstJawaban == "4" and secondJawaban == "3":
        openDocument(listPathLore[1])
    elif firstJawaban == "4" and secondJawaban == "5":
        openDocument(listPathLore[6])


#=========================== PROSES QUESTION 3 ===============================
def hasilJawaban3(jawaban):
    if jawaban == "1":
        hasil = "salah"
        return hasil
    elif jawaban == "2":
        hasil = "benar"
        return hasil
    elif jawaban == "3":
        hasil = "benar"
        return hasil
    elif jawaban == "4":
        hasil = "salah"
        return hasil
    elif jawaban == "5":
        hasil = "salah"
        return hasil
    
def afterJawaban3(thirdJawaban):
    if thirdJawaban == "2" and thirdJawaban == "3": #True
        openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "2": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3": #True
    #     openDocument(listPathAnswer[1])
    elif thirdJawaban == "1" or thirdJawaban == "4" or thirdJawaban == "5": #False
        openDocument(listPathAnswer[7])


def lore3(firstJawaban, secondJawaban, thirdJawaban):
    if firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2":
        openDocument(listPathLore[2])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3":
        openDocument(listPathLore[2])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2":
        openDocument(listPathLore[7])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3":
        openDocument(listPathLore[2])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "2":
        openDocument(listPathLore[7])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3":
        openDocument(listPathLore[8])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2":
        openDocument(listPathLore[2])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3":
        openDocument(listPathLore[2])


#=========================== PROSES QUESTION 4 ===============================
def hasilJawaban4(jawaban):
    if jawaban == "1":
        hasil = "salah"
        return hasil
    elif jawaban == "2":
        hasil = "salah"
        return hasil
    elif jawaban == "3":
        hasil = "salah"
        return hasil
    elif jawaban == "4":
        hasil = "benar"
        return hasil
    elif jawaban == "5":
        hasil = "benar"
        return hasil
    
def afterJawaban4(firstJawaban, secondJawaban, thirdJawaban, fourJawaban):
    if fourJawaban == "4" or fourJawaban == "5": #True
        openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "2" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "4": #True
    #     openDocument(listPathAnswer[1])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "5": #True
    #     openDocument(listPathAnswer[1])
    elif fourJawaban == "1" or fourJawaban == "2" or fourJawaban == "3": #False
        openDocument(listPathAnswer[8])


def lore4(firstJawaban, secondJawaban, thirdJawaban, fourJawaban):
    if firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2" and fourJawaban == "4":
        openDocument(listPathLore[3])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2" and fourJawaban == "5":
        openDocument(listPathLore[3])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "4":
        openDocument(listPathLore[8])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "5":
        openDocument(listPathLore[8])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "4":
        openDocument(listPathLore[8])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "5":
        openDocument(listPathLore[9])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "4":
        openDocument(listPathLore[9])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "5":
        openDocument(listPathLore[8])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "2" and fourJawaban == "4":
        openDocument(listPathLore[10])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "4":
        openDocument(listPathLore[8])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourJawaban == "5":
        openDocument(listPathLore[7])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "4":
        openDocument(listPathLore[7])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourJawaban == "5":
        openDocument(listPathLore[3])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "4":
        openDocument(listPathLore[11])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourJawaban == "5":
        openDocument(listPathLore[3])


#=========================== PROSES QUESTION 5 ===============================
def hasilJawaban5(jawaban):
    if jawaban == "1":
        hasil = "salah"
        return hasil
    elif jawaban == "2":
        hasil = "salah"
        return hasil
    elif jawaban == "3":
        hasil = "benar"
        return hasil
    elif jawaban == "4":
        hasil = "salah"
        return hasil
    elif jawaban == "5":
        hasil = "salah"
        return hasil
    
def afterJawaban5(firstJawaban, secondJawaban, thirdJawaban, fourthJawaban, fifthJawaban):
    if fifthJawaban == "3": #True
        openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    # elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3": #True
    #     openDocument(listPathAnswer[0])
    elif fourthJawaban == "1" or fourthJawaban == "2" or fourthJawaban == "4" or fifthJawaban == "5": #False
        openDocument(listPathAnswer[9])


def lore5(firstJawaban, secondJawaban, thirdJawaban, fourthJawaban, fifthJawaban):
    if firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[10])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "2" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[11])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[14])
    elif firstJawaban == "1" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[13])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[4])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[8])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[4])
    elif firstJawaban == "1" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[9])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[9])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[9])
    elif firstJawaban == "4" and secondJawaban == "3" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[8])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[11])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "2" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[12])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "4" and fifthJawaban == "3":
        openDocument(listPathLore[4])
    elif firstJawaban == "4" and secondJawaban == "5" and thirdJawaban == "3" and fourthJawaban == "5" and fifthJawaban == "3":
        openDocument(listPathLore[4])



#=================================== CLASS =======================================
class line:
    def __init__(self) -> None:
        pass
    def duaGaris(self):
        garis = "="*80
        return garis
    def satuGaris(self):
        garis = "-"*80
        return garis

class title:
    def __init__(self) -> None:
        pass
    def mainTitle(self):
        judulGame = "{:^80}".format("pecahkan teka teki si babadook".upper())
        return judulGame
    def characterTitle(self):
        judulCharacter = "{:^80}".format("biodata karakter".upper())
        return judulCharacter
    def inputTitle(self):
        judulGame = "{:^80}".format("menulis karakter pemain".upper())
        return judulGame
    def menuTitle(self):
        judulMenu = "{:^80}".format("menu game".upper())
        return judulMenu
    def questionTitle(self, chapter):
        judulTanya = "{:^80}".format(f"Pertanyaan Teka Teki Dari Si Babadook {chapter}")
        return judulTanya
    def loreTitle(self,chapter):
        judulLore = "{:^80}".format(f"Rahasia Si Babadook ke - {chapter}")
        return judulLore
    def storyTitle(self, chapter):
        judulStory = "{:^80}".format(f"Kisah Si Babadook ke - {chapter}")
        return judulStory
    def answerTitle(self):
        judulAnswer = "{:^80}".format(f"Pilih Jawaban!")
        return judulAnswer
    def endTitle(self):
        judulEnd = "{:^80}".format(f"terimakasih".upper())
        return judulEnd
    def storyChapterTitle(self, chapter):
        judulChapter = "{:^80}".format(f"chapter {chapter}".upper())
        return judulChapter
    


#========================= Attribute =========================
pathStory1 = "theStory/story1.txt"
pathStory2 = "theStory/story2.txt"
pathStory3 = "theStory/story3.txt"
pathStory4 = "theStory/story4.txt"
pathStory5 = "theStory/story5.txt"
pathQuest1 = "theQuestion/pertanyaan1.txt"
pathQuest2 = "theQuestion/pertanyaan2.txt"
pathQuest3 = "theQuestion/pertanyaan3.txt"
pathQuest4 = "theQuestion/pertanyaan4.txt"
pathQuest5 = "theQuestion/pertanyaan5.txt"
listPath = [
    pathStory1, pathStory2, pathStory3, pathStory4, pathStory5, 
    pathQuest1, pathQuest2, pathQuest3, pathQuest4, pathQuest5
]

pathAnswerRight1 = "theAnswer/theAR/ar1.txt"
pathAnswerRight2 = "theAnswer/theAR/ar2.txt"
pathAnswerRight3 = "theAnswer/theAR/ar3.txt"
pathAnswerRight4 = "theAnswer/theAR/ar4.txt"
pathAnswerRight5 = "theAnswer/theAR/ar5.txt"

pathAnswerWrong1 = "theAnswer/theAW/aw1.txt"
pathAnswerWrong2 = "theAnswer/theAW/aw2.txt"
pathAnswerWrong3 = "theAnswer/theAW/aw3.txt"
pathAnswerWrong4 = "theAnswer/theAW/aw4.txt"
pathAnswerWrong5 = "theAnswer/theAW/aw5.txt"
listPathAnswer = [
    pathAnswerRight1, pathAnswerRight2, pathAnswerRight3, pathAnswerRight4, pathAnswerRight5, 
    pathAnswerWrong1, pathAnswerWrong2, pathAnswerWrong3, pathAnswerWrong4, pathAnswerWrong5    
]
 


pathLoreDefault1 = "theLore/theDefault/loreD1.txt"
pathLoreDefault2 = "theLore/theDefault/loreD2.txt"
pathLoreDefault3 = "theLore/theDefault/loreD3.txt"
pathLoreDefault4 = "theLore/theDefault/loreD4.txt"
pathLoreDefault5 = "theLore/theDefault/loreD5.txt"

pathLoreSecret1 = "theLore/theSecret/loreS1.txt"
pathLoreSecret2 = "theLore/theSecret/loreS2.txt"
pathLoreSecret3 = "theLore/theSecret/loreS3.txt"
pathLoreSecret4 = "theLore/theSecret/loreS4.txt"
pathLoreSecret5 = "theLore/theSecret/loreS5.txt"
pathLoreSecret6 = "theLore/theSecret/loreS6.txt"
pathLoreSecret7 = "theLore/theSecret/loreS7.txt"
pathLoreSecret8 = "theLore/theSecret/loreS8.txt"
pathLoreSecret9 = "theLore/theSecret/loreS9.txt"
pathLoreSecret10 = "theLore/theSecret/lore10.txt"
listPathLore = [
    pathLoreDefault1, pathLoreDefault2, pathLoreDefault3, pathLoreDefault4, pathLoreDefault5, 
    pathLoreSecret1, pathLoreSecret2, pathLoreSecret3, pathLoreSecret4, pathLoreSecret5,
    pathLoreSecret6, pathLoreSecret7, pathLoreSecret8, pathLoreSecret9, pathLoreSecret10
]
