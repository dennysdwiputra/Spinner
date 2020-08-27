List_awal =[[1,2,3],
      [4,5,6],
      [7,8,9]]
def counterClockwise(List_awal):
    #Memisahkan elemen pada List_awal
    a=List_awal[0]
    b=List_awal[1]
    c=List_awal[2]
    #membuat list kosong untuk diisi list baru yang akan di counterclockwise
    fill1=[]
    fill2=[]
    fill3=[]
    fill4=[]
    
    # swap menjadi [3,6,9]
    fill1.append(a[2])
    fill1.append(b[2])
    fill1.append(c[2])
    
    # swap menjadi [2,5,8]
    fill2.append(a[1])
    fill2.append(b[1])
    fill2.append(c[1])
    
    #swap menjadi [1,4,7]
    fill3.append(a[0])
    fill3.append(b[0])
    fill3.append(c[0])
    
    #gabungin semua yang sudah di counter clockwise menjadi satu list kembali
    fill4.append(fill1)
    fill4.append(fill2)
    fill4.append(fill3)
    print(fill4)

counterClockwise(List_awal)