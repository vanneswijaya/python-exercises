import requests
import csv

url = "http://localhost:3000/graphql/"

with open('namasiswa.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        payload = "{\"query\":\"mutation{\\n  addMahasiswa(\\n    nama: \\\"%s\\\",\\n    nim: \\\"%s\\\",\\n    rfid: \\\"TEST3\\\",\\n    pelajarans: [],\\n    jadwals: []\\n  ){\\n    nama\\n    nim\\n    rfid\\n    _id\\n  }\\n}\"}"%(f'{row["nama"]}',f'{row["nim"]}')
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print(f'\t{row["nim"]} , {row["nama"]} , {row["presence"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

