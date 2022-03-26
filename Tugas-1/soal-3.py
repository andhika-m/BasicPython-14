up = float(input('Masukan nilai ujian praktek : '))
ut = float(input('Masukan nilai ujian teori : '))

if up >= 70 and ut >= 70:
    print('Selamat, anda lulus!')
elif up >= 70 and ut < 70:
    print('Anda harus mengulang ujian teori')
elif up < 70 and ut >= 70:
    print('Anda harus mengulang ujian praktek')
else:
    print('Anda harus mengulang ujian teori dan praktek')
