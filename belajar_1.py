#file python

print("CETAK DATA")

a = 5

b = 6

c = a + b

print("NILAI c = ", c)

def tambahData(a, b):

    return a + b

d = tambahData(a, b)

print("NILAI d =", d)

if(a > b):

    print("NILAI a LEBIH BESAR DARI b")

else:

    print("NILAI b LEBIH BESAR DARI a")

nilai_mahasiswa = [80, 75, 84, 90]

#print(range(len(nilai_mahasiswa)))

#print(range(5))

for i in range(len(nilai_mahasiswa)):

    print("NILAI MAHASISWA", i, " = ", nilai_mahasiswa[i])

#####

def rataNilai(nilai_a):

    jumlah = 0

    for i in range(len(nilai_a)):

        jumlah+=nilai_a[i]

    return jumlah/len(nilai_a)

print("RATA-RATA =", rataNilai(nilai_mahasiswa))
