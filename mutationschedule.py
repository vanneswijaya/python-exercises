import requests
import csv

url = "http://localhost:3000/graphql/"

with open('jadwal.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        payload = "{\"query\":\"mutation{\\n  addJadwal(\\n    nama: \\\"%s\\\",\\n    tanggal: \\\"%s\\\",\\n    mulai: \\\"%s\\\",\\n    selesai: \\\"%s\\\",\\n    tempat: \\\"test\\\",\\n    pelajaran: \\\"test\\\",\\n    mahasiswas:[]\\n  ){\\n    nama\\n    tanggal\\n    mulai\\n    selesai\\n    tempat\\n  }\\n}\"}"%(f'{row["nama"]}',f'{row["tanggal"]}',f'{row["mulai"]}',f'{row["selesai"]}')
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print(f'\t{row["nama"]} , {row["tanggal"]} , {row["mulai"]}, {row["selesai"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')