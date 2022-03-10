#pengecekan bilangan prima atau bukan
angka=int(input("masukkan angka: "))
if angka > 1:
    for i in range (2, angka):
        if angka % i == 0:
            print (angka, "adalah bukan bilangan prima")
            break
    else:
        print (angka, "adalah bilangan prima")
else:
    print (angka, "adalah bukan bilangan prima")
    
