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
    
    # def 
    
garis = ast.line()
judul = ast.title()

class karakter(pemain):
    pass

def inputKarakter() -> pemain:
    ast.clearTerminal()

    print(garis.duaGaris())
    print(judul.inputTitle())
    print(garis.duaGaris())
    print("")
    nama = ast.name()        # Memanggil fungsi name() dari assets
    tinggi = ast.tinggi()     # Memanggil fungsi tinggi() dari assets
    jenisKelamin = ast.kelamin()  # Memanggil fungsi kelamin() dari assets
    print("")
    print(garis.satuGaris())

    # Membuat objek pemain dengan nama, tinggi, dan jenis kelamin
    karakterUtama = pemain(nama, tinggi, jenisKelamin)

    return karakterUtama

"""
class babadook:
    def __init__(self) -> None:
        self.__name = "Babadook"
        self.__tinggi = 200
"""