tahun = input("Input tahun: ")

if(tahun%4)==0:
    if(tahun%100)==0:
        if(tahun%400)==0:
            print ("Tahun Kabisat")
        else:
            print ("bukan Tahun Kabisat")
    else:
        print ("Tahun Kabisat")
else:
    print ("Bukan Tahun Kabisat")