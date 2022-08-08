import requests
import csv

url = "http://localhost:3000/graphql/"

with open('pelajaran.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        payload = "{\"query\":\"mutation{\\n  addPelajaran(\\n    nama: \\\"%s\\\",\\n    guru: \\\"%s\\\",\\n    female: false,\\n    mahasiswas:[]\\n  ){\\n    nama\\n    guru\\n    female\\n  }\\n}\"}"%(f'{row["nama"]}',f'{row["guru"]}')
        headers = {'content-type': 'application/json'}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        print(f'\t{row["kode"]} , {row["nama"]} , {row["guru"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')