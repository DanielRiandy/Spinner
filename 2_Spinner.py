x_0 =[[1,2,3],                  #variabel x_0 adalah soal dalam bentuk list
      [4,5,6],
      [7,8,9]]
def counterClockwise(x_0):  #define sebuah function dengan nama counterClockwise, dengan parameter x_0
    sub_1 = []      #variabel sub_1 merupakan list sementara 
    sub_2 = []      #variabel sub_2 merupakan list sementara
    sub_3 = []      #variabel sub_3 merupakan list sementara
    for i in x_0 :  #dilakukan looping untuk mengakses nilai di dalam list
        for j in i: #dilakukan looping untuk mengakses nilai di dalam sublist
            angka = i.index(j) #untuk memperoleh indeks dari sublist, karena saya berencana untuk memproses masing-masing nilai dari sublist ke variabel sub_1/sub_2/sub_3 berdasarkan indexnya
            # print(angka) # hanya untuk melihat nilai indeks
            if angka == 0 : # apabila dia indeks ke-0 dari sublist ke-j :
                sub_3.append(j) # di append ke sub_3
            elif angka == 1 : # apabila dia indeks ke-1 dari sublist ke-j :
                sub_2.append(j) # di append ke sub_2
            elif angka == 2: # apabila dia indeks ke-2 dari sublist ke-j :
                sub_1.append(j) # di append ke sub_1
    x = f"[{sub_1},\n{sub_2},\n{sub_3}]"     # variabel x , menampung sub_1, sub_2 dan sub_3. mengapa saya menggunakan cara ini, agar newline bisa digunakan saya menggunakan bantuan f string , agar tampilan outputnya seperti yang diminta di soal.
    return x                    # mengembalikan nilai x, agar function ketika di print, akan mengeluarkan nilai x.    
print(counterClockwise(x_0)) # untuk mengeluarkan function counterClockwise, dengan fungsi print