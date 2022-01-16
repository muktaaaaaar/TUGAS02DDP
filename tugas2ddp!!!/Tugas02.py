import random, string

def menu():
    print(
    """***** SELAMAT DATANG DI NF LIBRARY *****
MENU:
[1] Tambah Anggota Baru
[2] Tambah Buku Baru
[3] Pinjam Buku
[4] Kembalikan Buku
[5] Lihat Data Peminjaman
[6] Keluar""")
  #fitur 1  
def daftarAnggota(kode, nama, status):
    myfile = open("anggota.txt", 'a+')
    myfile.write("\n"+kode +","+nama+","+status)
    myfile.close()
 #fitu2 
def nambahBuku(kode,judul,penulis, stok):
    myfile = open("buku.txt", 'a+')
    myfile.write(kode +","+judul+","+penulis+","+stok+"\n")
    myfile.close()

def readBuku():
    dataBuku = []
    b = open('buku.txt')
    for each_line in b:
        dataBuku.append(each_line.strip())
    b.close()
    return dataBuku
 #fitur 3       
def cek_buku(kd_buku):
    for i in readBuku():
        if i[:6] == kd_buku:
            return True
    return False

def readAnggota():
    dataAnggota = []
    a = open('anggota.txt')
    for each_line in a:
        dataAnggota.append(each_line.strip())
    a.close()
    return dataAnggota

def cek_anggota(kd_anggota):
    for r in readAnggota():
        if r[:6] == kd_anggota:
            return True
    return False

def cek_stok(kd_buku):
    dataBuku = readBuku()
    for r in range (len(dataBuku)):
        if dataBuku [r][:6] == kd_buku:
            dataBuku[r] = dataBuku[r].split(",")# Mengubah string menjadi list
            if int(dataBuku[r][-1]) > 0: #Untuk mengubah stok, jika stok dikurang 1 dan hasilnya lebih dari 0, maka mengmbalikan hasilnya
                return True
    return False
def pinjamBuku(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku()
    ada = 0
    for n in range(len(dataPinjam)): #Ini adalah perulangan 
        if dataPinjam[n][:6] == kd_buku:
            dataPinjam[n] = dataPinjam[n]+","+kd_anggota
            ada = 1
    if ada == 1:
        p = open('peminjaman.txt',"w+")
        for n in dataPinjam:
            p.write(n+"\n")
        p.close()
    else:
        p = open('peminjaman.txt',"a+")
        p.write(kd_buku+","+kd_anggota+"\n")
        p.close()

def kurangStok(kd_buku):
    dataBuku = readBuku()
    for n in range(len(dataBuku)): #Ini adalah perulangan 
        if dataBuku[n][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
            dataBuku[n] = dataBuku[n].split(",") #Ini untuk mengubah jadi list (mengambil stok)
            dataBuku[n][-1] = str(int(dataBuku[n][-1]) - 1)# Untuk mengubah stok
            dataBuku[n] = ",".join(dataBuku[n])#Mengembalikan data menjadi str
    myfile = open('buku.txt', 'w+')
    for n in dataBuku:
        myfile.write(n+"\n")
    myfile.close()
# fitur 4

def readPinjamBuku():    
    b_list = []
    p = open("peminjaman.txt",  "r")
    for line in p:
        b_list.append(line.strip())
    return b_list
    
def cek_statusAngggota(kd_anggota):
    dataAnggota = readAnggota()
    for r in range(len(dataAnggota)):
        if dataAnggota[r][:6] == kd_anggota:
            if dataAnggota[r][-1] == "1":
                return True
            else:
                return False
def anggota_pinjam(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku()
    for p in range(len(dataPinjam)):
        if dataPinjam[p][:6] == kd_buku:
            dataPinjam[p] = dataPinjam[p].split(",") #Untuk mengubah data menjadi tipe data list 
            if dataPinjam[p].count(kd_anggota) == 1:
                return True
            else:
                return False
    
def remove_anggota(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku()
    for p in range(len(dataPinjam)):
        if dataPinjam[p][:6] == kd_buku: # Cek buku ada atau tidak di dalam file 
            dataPinjam[p] = dataPinjam[p].split(",") #Untuk mengubah data menjadi tipe data list 
            dataPinjam[p].remove(kd_anggota)
            if len(dataPinjam[p]) == 1 : # Untuk Menghapus anggota apabila sudah selesai melakukan peminjaman
                del dataPinjam[p]
            else:
                dataPinjam[p] = ",".join(dataPinjam[p])#Mengembalikan data menjadi str
        
    myfile = open('peminjaman.txt', 'w+')
    for p in dataPinjam:
        myfile.write(p+"\n")
    myfile.close()
# fitur 5
def lihatPeminjaman():
    # Mengubah data text menjadi tipe data list lalu diuubah lagi menjadi tipe data dictionary
    # Data buku
    buku = []
    dataBuku = {}
    myfile = open("buku.txt")
    for r in myfile:
        buku = r.split(",") # Untuk mengubah menjadi multiple list
        dataBuku[buku[0]] = [buku[1],buku[2],str(int(buku[3]))] #Mengubah multi list menjadi dict
    # Data Anggota
    anggota = []
    dataAnggota = {}
    myfile = open("anggota.txt", "r")
    for r in myfile:
        anggota = r.split(",") # Untuk mengubah menjadi multiple list
        dataAnggota[anggota[0]] = [anggota[1],str(int(anggota[2]))] #Mengubah multi list menjadi dict
    # Data Pinjam
    pinjam = []
    dataPinjam = {}
    myfile = open("peminjaman.txt", "r")
    for r in myfile:
        pinjam = r.split(",") # Untuk mengubah menjadi multiple list
        pinjam[-1] = pinjam[-1][0:-1]
        dataPinjam[pinjam[0]] = pinjam[1:] # Untuk mengubah multi list menjadi dict
    print("*** DAFTAR PEMINJAMAN BUKU ***\n")

    for p in dataPinjam.keys():
        no = 0
        print("Judul : "+dataBuku[p][0])
        print("Penulis : "+dataBuku[p][1])
        print("Daftar Pinjam:")
        for n in dataPinjam[p]:
            no +=1
            print(str(no)+". "+str(dataAnggota[n][0])+("(*)" if dataAnggota[n][1] == "1" else ""))
        print()


menu()
while True:
    option = input("\nMasukkan menu pilihan Anda : ")
    # Fitur 1
    if option == "1":
        print("\n*** PENDAFTARAN ANGGOTA BARU ***")
        nama = input("Masukkan nama: ")
        status = input("Apakah merupakan karyawan NF Group? (Y/T): ")
        status = "1" if status == "Y" else  "2"
        kode = "LIB" + ''.join(random.choice(string.digits) for _ in range(3))
        daftarAnggota(kode,nama,status)
        print("Pendaftaran anggota dengan kode " + kode + " atas nama " + nama + " berhasil. \n")

    # Fitur 2
    elif option == "2":
        print("\n*** PENAMBAHAN BUKU BARU ***\n")
        judul = input("Judul: ")
        penulis = input("Penulis: ")
        stok = input("Stok: ")

        penulis = penulis.split()
        penulis = "".join(penulis)
        kode = penulis[:3].upper() + ''.join(random.choice(string.digits)for _ in range(3))

        nambahBuku(kode,judul, penulis, stok)
        print("Penambahan buku baru dengan kode " + kode + " dan judul " + judul + " berhasil.\n")

    # Fitur 3
    elif option == "3":
        print("\n*** PEMINJAMAN BUKU ***")
        kd_buku = input("Kode buku: ")
        if cek_buku(kd_buku):
            kd_anggota = input("Kode anggota: ")
            if cek_anggota(kd_anggota):
                if cek_stok(kd_buku):
                    pinjamBuku(kd_buku,kd_anggota)
                    kurangStok(kd_buku)
                    print("Peminjaman buku "+kd_buku+" oleh "+kd_anggota+" berhasil.\n")
                else:
                    print("Stok buku kosong. Peminjaman gagal.\n")
            else:
                print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
        else:
            print("Kode buku tidak ditemukan. Peminjaman gagal.\n")

    # Fitur 4
    elif option == "4":
        print("\n*** PENGEMBALIAN BUKU ***")
        kd_buku = input("Kode buku: ")
        if cek_buku(kd_buku):
            kd_anggota = input("Kode anggota: ")
            if anggota_pinjam(kd_buku,kd_anggota):
                denda = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))
                if cek_statusAngggota(kd_anggota):
                    denda = 1000 * denda
                else:
                    denda = 2500 * denda
                print("Total denda = ", denda, "\n")
                print("Silakan membayar denda keterlambatan di kasir.\n")
                remove_anggota(kd_buku,kd_anggota)
                print("Pengembalian buku "+kd_buku+" oleh "+kd_anggota+" berhasil.\n")

            else:
                print("Kode anggota tidak terdaftar sebagai peminjam buku tersebut. Pengembalian buku gagal.\n")
        else:
            print("Kode buku salah. Pengembalian buku gagal.\n")

    # Fitur 5        
    elif option == "5":
        lihatPeminjaman()
    # Fitur 6 (keluar)
    elif option == "6":
        print("Terima kasih atas kunjungan Anda...\n")
        break
    else:
        print("Pilihan Anda salah. Ulangi.\n")
    menu()