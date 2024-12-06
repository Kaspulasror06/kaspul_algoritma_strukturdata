listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Masukkan anama kota yang di cari; ')

i = 0
while i < len(listKota):
    if listKota[i].lower() == kotaYangDicari.lower():
        print('Ketemu di index', )
        break
    print('Bukan ', listKota[i])
    i += 1
else:
    print('Maaf, Kota yang anda cari tidak di temukan. ')