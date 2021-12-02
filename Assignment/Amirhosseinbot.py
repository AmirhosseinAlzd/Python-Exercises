from telebot import TeleBot
from telebot import types
import random  
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode 

bot = TeleBot('5009688596:AAH1oUIXp1I7LR0s94ql3K8Ja-r_iJUU_pw')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'سلام و درود خدا بر عزیز دل برادر  '  +  message.from_user.first_name)
    bot.send_message(
        message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')


number_rand = random.randint(0,100)
markup = types.ReplyKeyboardMarkup(row_width=1)
Button = types.KeyboardButton('New Game')
markup.add(Button)


@bot.message_handler(commands=['game'])
def start_game(message):
    msg = bot.send_message(
        message.chat.id, 'به بازی حدس عدد خوش اومدی\nیک عدد که فکر میکنی جواب منه بنویس !\nدر هر مرحله برای خروج این کامند  زیر رو بزن \n/Exit',
        reply_markup=markup)
    bot.register_next_step_handler(msg, guess_nuber)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     '/start به بات امیرحسین خوش اومدی \n حال انتخاب کن که چی دوست داری :\n\n/game -->> بازی حدس عدد \n/age -> محاسبه سنت با تقویم شمسی\n/voice ->متن ت رو برات می خونم \n/max -> بزرگترین عدد رو انتخاب میکنم\n/argmax -> اندیس بزرگترین عدد رو انتخاب میکنم \n/qrcode -> کیو ار کدت رو می سازم \n/help -> راهنمایی مجدد')


@bot.message_handler(commands=['age'])
def send_age(message):
    msg = bot.send_message(
        message.chat.id, 'تاریخ تولدت رو قشنگ به فرمی که می گم بنویس : درست بنویسی هااا : year/month/day\nتو هر مرحله برای خروج ')
    bot.register_next_step_handler(msg, salshomar)
@bot.message_handler(commands=['voice'])
def send_voice(message):
    msg = bot.send_message(
        message.chat.id, 'یه چیز انگلیسی تایپ کن\nدر هر مرحله برای خروج این کامند  زیر رو بزن \n/Exit')
    bot.register_next_step_handler(msg, txt_to_voice)
@bot.message_handler(commands=['max'])
def send_max(message):
    msg = bot.send_message(
        message.chat.id, 'چند تا عدد به فرمی که میگم بنویس x,x,x,x,x,....\nدر هر مرحله برای خروج این کامند  زیر رو بزن \n/Exit')
    bot.register_next_step_handler(msg, max_number)
@bot.message_handler(commands=['argmax'])

def send_argmax(message):
    msg = bot.send_message(
        message.chat.id, 'چند تا عدد به فرمی که میگم بنویس x,x,x,x,x,....\nدر هر مرحله برای خروج این کامند  زیر رو بزن \n/Exit')
    bot.register_next_step_handler(msg, find_andis)
@bot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    msg = bot.send_message(
        message.chat.id, 'یه چیزی بگو که برات کیو ار کدش رو برات بفرستم \nدر هر مرحله برای خروج این کامند  زیر رو بزن \n/Exit')
    bot.register_next_step_handler(msg, Qr_Code)








#game
def guess_nuber(message):
    if message.text != 'Exit':
        try:
            if message.text == 'New Game':
                global random_number
                random_number = random.randint(0, 100)
                bot.send_message(message.chat.id, '[بارگزاری مجدد]. حدس بزن :',
                                 reply_markup=markup)
                bot.register_next_step_handler_by_chat_id(
                    message.chat.id, guess_nuber)
            elif int(message.text) < number_rand:
                msg = bot.send_message(
                    message.chat.id, 'برو بالاتررر', reply_markup=markup)
                bot.register_next_step_handler(msg, guess_nuber)
            elif int(message.text) > number_rand:
                msg = bot.send_message(
                    message.chat.id, 'نه اونقدر زیاد هم ، بیا پایین تررر', reply_markup=markup)
                bot.register_next_step_handler(msg, guess_nuber)
            else:
                bot.send_message(message.chat.id, 'باریکلااااا !',
                                 reply_markup=types.ReplyKeyboardRemove(selective=True))
                bot.send_message(
                    message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
        except:
            msg = bot.send_message(
                message.chat.id, 'دوست عزیز یا عدد وارد کن یا دکمه مارو بزن بریم /Exit', reply_markup=markup)
            bot.register_next_step_handler(msg, guess_nuber)
    else :
        bot.send_message(message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help',
                         reply_markup=types.ReplyKeyboardRemove(selective=True))



#message
def salshomar(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
    else:
        try:
            if len(message.text.split('/')) == 3:
                date_difference = JalaliDatetime.now(
                ) - JalaliDatetime(message.text.split('/')[0], message.text.split('/')[1], message.text.split('/')[2])
                bot.send_message(message.chat.id, 'شما' +
                                 str(date_difference.days // 365) + ' سال دارید')
                bot.send_message(
                    message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
            else:
                msg = bot.send_message(
                    message.chat.id, 'دوست عزیز یا عدد وارد کن یا دکمه مارو بزن بریم\n/Exit')
                bot.register_next_step_handler(msg, salshomar)
        except:
            msg = bot.send_message(
                message.chat.id, 'دوست عزیز یا عدد وارد کن یا دکمه مارو بزن بریم\n/Exit')
            bot.register_next_step_handler(msg, salshomar)




def txt_to_voice(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
    else:
        try:
            content = gTTS(text=message.text, slow=False)
            content.save('voice.ogg')
            content = open('voice.ogg', 'rb')
            bot.send_voice(message.chat.id, content)
            bot.send_message(
                message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
        except:
            msg = bot.send_message(
                message.chat.id, 'دوست عزیز یا عدد وارد کن یا دکمه مارو بزن بریم\n/Exit')
            bot.register_next_step_handler(msg, txt_to_voice)





def max_number(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
    else:
        try:
            numbers = list(map(int, message.text.split(',')))
            bot.send_message(
                message.chat.id, 'Maximum number is: ' + str(max(numbers)))
            bot.send_message(
                message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
        except:
            msg = bot.send_message(
                message.chat.id, 'دوست عزیز یا عدد وارد کن یا دکمه مارو بزن بریم\n/Exit')
            bot.register_next_step_handler(msg, max_number)





def find_andis(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
    else:
        try:
            numbers = list(map(int, message.text.split(',')))
            bot.send_message(message.chat.id, 'انندیس عدد بزرگتره ' +
                             str(numbers.index(max(numbers))))
            bot.send_message(
                message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
        except:
            msg = bot.send_message(
                message.chat.id, 'دوست عزیز یا عدد وارد کن یا دکمه مارو بزن بریم\n/Exit')
            bot.register_next_step_handler(msg, find_andis)




def Qr_Code(message):
    if message.text == 'Exit':
        bot.send_message(
            message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
    else:
        try:
            qrcode_img = qrcode.make(message.text)
            qrcode_img.save('QR.png')
            photo = open('QR.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(
                message.chat.id, 'اگر هنوز با ما کار داری دستور زیر رو انتخاب کن \n/help')
        except:
            msg = bot.send_message(
                message.chat.id, 'یه جای کار میلنگه . برای خروج دکمه زیر بزن \n /Exit')
            bot.register_next_step_handler(msg, Qr_Code)




bot.polling(none_stop=True)