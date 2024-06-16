import gspread
from google.oauth2.service_account import Credentials

def add_to_google_sheet(data):
    client = gspread.service_account()
    sheet = client.open('TelegramBotData').sheet1
    sheet.append_row(data)



