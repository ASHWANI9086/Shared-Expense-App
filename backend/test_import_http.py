import requests
from pathlib import Path

csv_path = Path(__file__).resolve().parent.parent / 'data' / 'Expenses Export.csv'
print('csv_path', csv_path)
print('exists', csv_path.exists())
with open(csv_path, 'rb') as f:
    files = {'file': ('Expenses Export.csv', f, 'text/csv')}
    r = requests.post('http://127.0.0.1:8002/import/csv', files=files)
    print('status', r.status_code)
    print(r.headers.get('content-type'))
    print(r.text)
