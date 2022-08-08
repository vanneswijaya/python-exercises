# print ("TEMPERATURE CONVERTER")
# print ("Celcius to Fahrenheit")
# print ("---------------------")

#EXCEPTION HANDLING/ERROR HANDLING

# try:
#     celcius = int(input ("Insert temperature in celcius : "))
#     fahrenheit = 9.0/5 * celcius + 32
#     print ("Temperature in fahrenheit : " + str(fahrenheit))
#     print(hasil)
# except ValueError:
#     print('Please input an integer!')
# except:
#     print('Ada variabel yang undefined')

# a = 'halo'
# nama = 'michael'
# umur = 4*2

# print(a + ' ' + nama + ' ' + 'apakabar?')
# print(a, nama, 'apakabar?')

#STRING FORMATTING
#METODE 1 = F STRING
# print(f'{a} {nama} yang berumur {umur}, apakabar?')
# print('{a} {nama} yang berumur {umur}, apakabar?')

# #METODE 2 = %
# print('%s %s yang berumur %s, apakabar?'%(nama, nama, umur))

# list_pertama = [1,2,3,6,8]
# list_kedua = ['cei', 'parning', 'dll']
# list_ketiga = [1,2,'cei',4.5]

# # print(list_ketiga[2])

# for x in list_pertama:
#     print(x)
# print(list_pertama)

# adjo = {
#     'nama':'andreas djohan',
#     'umur':17,
#     'sekolah':'kanisius'
# }
# cei = {
#     'nama':'karol',
#     'umur':18,
#     'sekolah':'lecoq'
# }

# murid = [adjo, cei]

# print(murid[0]['sekolah'])
# print(adjo['nama'])
# print(cei['umur'])

#FOR LOOP



# angka_prima = [2,3,5,7,11]
# for angka in angka_prima:
#     if angka > 5:
#         print(angka*2)

# print(angka_prima)

for x in range(1,101):
    if x%5 == 0 or x%6 == 0:
        print(x)
#STRING FORMATTING
# angka1 = int(input('masukkan angka pertama '))
# angka2 = int(input('masukkan angka kedua '))

# print(f'angka yang anda masukkan berturut2 adalah {angka1} dan {angka2}')
# print('angka yang anda masukkan berturut2 adalah %s dan %s'%(angka1, angka2))
