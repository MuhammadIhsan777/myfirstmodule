#versi yang punya saya
#function untuk mendaftar
def Register(Nama, Tanggal , AsalSekolah , NamaOrgTua, Agama, Alamat):
    print("Informasi Pendaftaran:")
    print("Nama             :"+ Nama)
    print("Tanggal Lahir    :"+ Tanggal)
    print("Asal Sekolah     :"+ AsalSekolah)
    print("Nama Orang Tua   :"+ NamaOrgTua)
    print("Agama            :"+ Agama)
    print("Alamat           :"+Alamat)

#versi yang benar(seharusnya)
def daftar(name, tgl , gender , school, parent, religion, address):
    if gender=="Laki-Laki":
        print("Selamat Datang di IE Tuan "+name+ " Biodata kamu adalah sebagai berikut")
    else:
        print("Selamat Datang di IE Nona "+name +" Biodata kamu adalah sebagai berikut")
    print("Nama             : "+name)
    print("Tanggal lahir    : "+tgl)
    print("Jenis Kelamin    : "+gender)
    print("Asal Sekolah     : "+school)
    print("Orang Tua        : "+parent)
    print("Agama            : "+religion)
    print("Alamat           : "+address)
    

daftar("Mujoko","26 June 1980", "Laki-Laki","IPB" , "Wiyono", "Islam", "Kl Benda Cicurug")

#versi punya saya
#ini function untuk absensi
def Absensi(name,tanggal):
    print('Nama             : '+name)
    print('Tanggal          :'+tanggal)

#function untuk kenaikan tingkat/level/kedudukan/posisi/jabatan/takhta
def Promosi(nama, score, lastlevel, nextlevel):
    print('Nama             :' +nama)
    print('Skor             :' +score)
    print('Max Level        :' +lastlevel)
    print('Next Level       :' +nextlevel)

#function untuk bayar SPP
def invoicespp(name, level):
    print("Nama             :"+name)
    print('Level            :'+level)

#function check spp
def checkspp(name):
    print("Nama             :"+name)