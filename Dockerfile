FROM python:3.9

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


RUN ["mkdir", "~/.config"]
RUN ["mkdir", "~/.config/gspread"]

COPY service_account ~/.config/gspread/


CMD ["python", "main.py"]