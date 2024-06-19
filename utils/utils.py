import gspread

def add_to_google_sheet(data):
    client = gspread.service_account()
    sheet = client.open('TelegramBotData').sheet1
    sheet.append_row(data)