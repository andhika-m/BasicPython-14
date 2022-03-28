# Author: Andhika Malik

print("Selamat datang!\n")
print("=====================")
print("\tMenu")
print("=====================")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
print("---------------------")

menu = int(input("Masukan pilihan : "))
daftar_kontak = [
    {'Nama':'Fawwaz', 'Telp':'081234567890'}, 
    {'Nama':'Jhon', 'Telp':'089876543210'}]

if menu == 1:
    print('\n==============================')
    print("\tDaftar kontak:")
    print('==============================')
    
    for dk in daftar_kontak:
        print('Nama\t\t:', dk['Nama'])
        print('No Telepon \t:', dk['Telp'], '\n')

elif menu == 2:
    i = 1
    baru = [{}]
    d = []
    banyak = int(input('Berapa banyak kontak yang ingin ditambahkan : '))
    
    while i <= banyak:
        print('\n- Kontak ke', i)
        print('-----------------------------')
        nama = input('Masukan Nama\t\t: ')
        notlp = input('Masukan No Telepon \t: ')
        
        data1 = baru[0]['Nama'] = nama
        data2 = baru[0]['Telp'] = notlp
        
        d.append({'Nama':data1, 'Telp':data2})
        i += 1

    print('\n=============================')
    print('Kontak berhasil ditambahkan!')
    print('=============================')
    for br in d:
        print('-Baru-')
        print('Nama\t\t:', br['Nama'])
        print('No Telepon \t:', br['Telp'], '\n')

    for dk in daftar_kontak:
        print('Nama\t\t:', dk['Nama'])
        print('No Telepon \t:', dk['Telp'], '\n')

elif menu == 3:
    print('Program selesai, sampai jumpa!')

else:
    print('Menu tidak tersedia')