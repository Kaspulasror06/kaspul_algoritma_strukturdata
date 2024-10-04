# kita membuat string (nama nama buah)
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

# list yang berisi kumpulan integer
angka_doang = [80, 100]

print('list_buah:', list_buah)

#print('angka_doang:',angka_doang)

#print(list_buah[0])
#print(list_buah[2])
#print(list_buah[1])
#print(list_buah[3])

#print(list_buah[-1])
#print(list_buah[-2])
#print(list_buah[-3])
#print(list_buah[-4])

#print(list_buah[1:3])

list_buah[0] = 'kelapa'

#print(list_buah)

# tambah data baru dibelakang
list_buah.append('naga')
#print(list_buah)

# tambah data baru didepan
list_buah.insert(0, 'alpukat')
#print(list_buah)

# tambah data baru ditengah
list_buah.insert(2, 'mie ayam')
#print(list_buah)

# mengapus data 
list_buah.pop()

'Durian'

#print(list_buah)

list_buah.remove('mie ayam')

#print(list_buah)

#menghapus data menggunakan angka
del list_buah[1]
print(list_buah)

# urutkan secara ascending
list_buah.sort()
print(list_buah)
