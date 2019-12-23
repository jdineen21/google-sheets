import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Python Test Sheet').sheet1

row = sheet.row_values(3)
col = sheet.col_values(2)
cell = sheet.cell(1, 2).value

print(row)
print(col)

insertRow = ['hello', 5, 'red', 'blue']

sheet.insert_row(insertRow, 7)

print(sheet.get_all_values())

sheet.update_cell(2, 2, 'CHANGED')

numRows = sheet.row_count