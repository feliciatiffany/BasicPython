#author : Felicia Tiffany H

def daftarkontak(kontak):
    if len(kontak) == 0:
        print ("Belum ada kontak didaftarkan")
        print (" ")
        return
    for i in range(len(kontak)):
        mydict=kontak[str(i+1)]
        print ("Nama : ", mydict["nama"])
        print ("No Telepon : ", mydict["no"])
        print (" ")
        
def tambahkontak(kontak):
        mydict = {
            "nama": "lala",
            "no": "000",
            
        }
        print ("Tambah Kontak ")
        print (" ")
        mydict["nama"] = input("Nama : ")
        mydict["no"] = input("No Telepon: ")
        kontak[str(len(kontak)+1)] = mydict
        return kontak

kontak={}
while True:
    print ("Selamat Datang\n")
    print ("--- Menu ---")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Keluar")
    print (" ")
    i=input("Pilih Menu : ")
    print (" ")
    
    if int(i) == 1:
        daftarkontak(kontak)
    elif int(i)==2:
        kontak=tambahkontak(kontak)
        print ("Kontak berhasil ditambahkan")
        print (" ")
    elif int(i)==3:
        print ("Program selesai, sampai jumpa!")
        break
    else:
        print ("Menu tidak tersedia")
        print (" ")
        
        