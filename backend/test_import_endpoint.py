from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Expenses Export.csv')
print('csv_path', csv_path)
print('exists', os.path.exists(csv_path))
with open(csv_path, 'rb') as f:
    files = {'file': ('Expenses Export.csv', f, 'text/csv')}
    r = client.post('/import/csv', files=files)
    print('status', r.status_code)
    print(r.text)
