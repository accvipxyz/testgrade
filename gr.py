import requests
import csv
import telebot

# إعداد البوت
API_TOKEN = '7001561376:AAEyQ87BexG9O-L78TutddHdJhc1A3Ck-VU'
bot = telebot.TeleBot(API_TOKEN)

# رابط Google Sheets بصيغة CSV
CSV_URL = 'https://docs.google.com/spreadsheets/d/1QPgryKD7ms_7Mt9cKxbYU5vdMn0mbBLPrHoVC7jEJpE/export?format=csv'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا! من فضلك أرسل رقم هويتك.")

@bot.message_handler(func=lambda message: True)
def check_student_id(message):
    student_id = message.text
    response = requests.get(CSV_URL)
    response.encoding = 'utf-8'
    csv_data = response.text.splitlines()

    reader = csv.reader(csv_data)
    for row in reader:
        if len(row) >= 3 and row[1] == student_id:
            grade = row[2]
            bot.reply_to(message, f"درجتك هي: {grade}")
            return

    bot.reply_to(message, "لم يتم العثور على رقم الهوية. يرجى التأكد من صحة الرقم والمحاولة مرة أخرى.")

bot.polling()
