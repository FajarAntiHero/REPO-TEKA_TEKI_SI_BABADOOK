from . import assets as ast

class pemain:
    def __init__(self, nameKarakter : str, heightKarakter : int, sexKarakter : str):
        self.__name = nameKarakter
        self.__tinggi = heightKarakter
        self.__kelamin = sexKarakter

    @property
    def getName(self):
        name = self.__name
        return name
    
    @property
    def getTinggi(self):
        tinggi = self.__tinggi
        return tinggi
    
    @property
    def getKelamin(self):
        kelamin = self.__kelamin
        return kelamin
    
garis = ast.line()
judul = ast.title()    

def inputKarakter():
    ast.clearTerminal()

    print(garis.duaGaris())
    print(judul.inputTitle())
    print(garis.duaGaris())
    nama = ast.name()        # Memanggil fungsi name() dari assets
    tinggi = ast.tinggi()     # Memanggil fungsi tinggi() dari assets
    jenisKelamin = ast.kelamin()  # Memanggil fungsi kelamin() dari assets
    

    # Membuat objek pemain dengan nama, tinggi, dan jenis kelamin
    karakterUtama = pemain(nama, tinggi, jenisKelamin)

    print(garis.satuGaris())
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


"""
class babadook:
    def __init__(self) -> None:
        self.__name = "Babadook"
        self.__tinggi = 200
"""