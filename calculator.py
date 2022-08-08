x = ''

#infinite loop
while True:
	choice = input(f'Apakah ingin menggunakan kalkulator{x}? (y/n) ')

	if choice.lower().strip() == 'y':
		print ('')
		print ('----------------')
		print ('CALCULATOR')
		print ('----------------')
		print ('')

		angkapertama = int(input ('Masukkan angka pertama : '))
		print ('Angka pertama adalah ' + str(angkapertama))

		angkakedua = int(input ('Masukkan angka kedua : '))
		print ('Angka kedua adalah ' + str(angkakedua))

		print ('1 = tambah')
		print ('2 = kurang')
		print ('3 = kali')
		print ('4 = bagi')

		while True:
			operasi = int(input('Masukkan operasi hitung : '))

			if operasi == 1:
				hasil = angkapertama + angkakedua
				break
				
			elif operasi == 2:
				hasil = angkapertama - angkakedua
				break
				
			elif operasi == 3:
				hasil = angkapertama * angkakedua
				break
				
			elif operasi == 4:
				hasil = float(angkapertama) / float(angkakedua)
				break

			else:
				continue

		print ('Hasil : ' + str(hasil))

		print ('----------------')

		
	elif choice.lower().strip() == 'n':
		break

	else:
		continue

	x = ' lagi'
	continue
