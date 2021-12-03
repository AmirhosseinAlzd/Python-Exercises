from typing import Counter
from telebot import TeleBot
from telebot import types
import random  
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode 

bot = TeleBot('5009688596:AAH1oUIXp1I7LR0s94ql3K8Ja-r_iJUU_pw')

number_rand = random.randint(0,100)
Guess_game = types.ReplyKeyboardMarkup(row_width=1)
game_Button = types.KeyboardButton('بازی جدید')
Guess_game.add(game_Button)
salavat_counter =[0]
NewSalavat = types.ReplyKeyboardMarkup(row_width=1)
salavat_Button = types.KeyboardButton('صلوات جدید')
NewSalavat.add(salavat_Button)

@bot.message_handler(commands=['start'])
def Hello_sender(message):
    bot.reply_to(message, ' سلام و درود خدا بر عزیز دل برادر  '  +  message.from_user.first_name)
    bot.send_message(
        message.chat.id, ' به بات امیرحسین خوش اومدی \n حالا انتخاب کن که چی دوست داری :\n\n/game : بازی حدس عدد \n/age : محاسبه سنت با تقویم شمسی\n/voice : متن انگلیسیت رو برات بخونم \n/max : بزرگترین عدد رو انتخاب بکنم\n/argmax : اندیس بزرگترین عدد رو انتخاب بکنم \n/qrcode : کیو ار کدت رو بسازم \n/Salavat : برنامه صلوات شمار\n/help : راهنمایی مجدد')


@bot.message_handler(commands=['game'])
def start_game(message):
    user_guess = bot.send_message(message.chat.id, 'به بازی حدس عدد خوش اومدی\nیک عدد که فکر میکنی جواب منه بنویس !\nدر هر مرحله برای خروج این کامند  زیر رو بزن \n/Exit',reply_markup=Guess_game)
    bot.register_next_step_handler(user_guess, guess_number)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '\n/game : بازی حدس عدد \n/age : محاسبه سنت با تقویم شمسی\n/voice : متن انگلیسیت رو برات بخونم \n/max : بزرگترین عدد رو انتخاب بکنم\n/argmax : اندیس بزرگترین عدد رو انتخاب بکنم \n/qrcode : کیو ار کدت رو بسازم \n/Salavat : برنامه صلوات شمار\n/help : راهنمایی مجدد')


@bot.message_handler(commands=['age'])
def send_age(message):
    user_age = bot.send_message(message.chat.id, 'تاریخ تولدت رو قشنگ به فرمی که می گم بنویس : درست بنویسی هااا \n   نحوه درست نوشتن :         روز   /   ماه   /   سال  \n/Exit تو هر مرحله برای خروج \n')
    bot.register_next_step_handler(user_age, salshomar)


@bot.message_handler(commands=['voice'])
def send_voice(message):
    user_txt = bot.send_message(message.chat.id, ' یه چیز انگلیسی تایپ کن که برات ویسش رو بفرستم\nاگر هم می خوای خارج بشی کامند زیر رو بزن\n\n/Exit')
    bot.register_next_step_handler(user_txt, txt_to_voice)


@bot.message_handler(commands=['max'])
def send_max(message):
    list_number = bot.send_message(message.chat.id, ' می خوام بهت بگم کدوم عددت از همه بزرگتره \n چند تا عدد به فرمی که میگم بنویس مثلا \n 12,13,14,2,1,... \n\nاگر هم می خوای خارج بشی کامند زیر رو بزن  \n\n/Exit')
    bot.register_next_step_handler(list_number, max_number)


@bot.message_handler(commands=['argmax'])
def send_argmax(message):
    list_number = bot.send_message(message.chat.id, ' می خوام بهت بگم عدد چندمیه از همه بزرگتره \n چند تا عدد به فرمی که میگم بنویس مثلا \n 12,13,14,2,1,... \n\nاگر هم می خوای خارج بشی کامند زیر رو بزن  \n\n/Exit')
    bot.register_next_step_handler(list_number, find_index)


@bot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    user_qr = bot.send_message(message.chat.id, 'یه چیزی بنویس که برات کیو ار کدش رو  بفرستم \n\nاگر هم می خوای خارج بشی کامند زیر رو بزن \n\n/Exit')
    bot.register_next_step_handler(user_qr, Qr_Code)


@bot.message_handler(commands=['Salavat'])
def send_qrcode(message):
    salavat_counter[0] = 0
    user_sa = bot.send_message(message.chat.id, 'به صلوات شمار خوش اومدی . هربار که فرستادی دکمه زیر رو بزن \n/salavat \n\nاگر هم می خوای خارج بشی کامند زیر رو بزن \n\n/Exit', reply_markup=NewSalavat)
    bot.register_next_step_handler(user_sa, Salavat_shomar)



#game
def guess_number(message):
    if message.text != '/Exit':
        try:
            if message.text == 'بازی جدید':
                global random_number
                random_number = random.randint(0, 100)
                bot.send_message(message.chat.id, 'یک عدد بین صفر تا صد که فکر میکنی جوابه حدس بزن :', reply_markup=Guess_game)
                bot.register_next_step_handler_by_chat_id(message.chat.id, guess_number)
            elif int(message.text) < number_rand:
                user_guess = bot.send_message(message.chat.id, 'برو بالاتررر', reply_markup=Guess_game)
                bot.register_next_step_handler(user_guess, guess_number)
            elif int(message.text) > number_rand:
                msg = bot.send_message(message.chat.id, 'نه اونقدر زیاد هم ، بیا پایین تررر', reply_markup=Guess_game)
                bot.register_next_step_handler(msg, guess_number)
            else:
                bot.send_message(message.chat.id, 'باریکلااااا !',
                                 reply_markup=types.ReplyKeyboardRemove(selective=True))
                bot.send_message( message.chat.id, 'بازیت رو هم دیگه انجام دادی . برای خارج شدن دکمه زیر رو بزن   \n\n/help')
        except:
            msg = bot.send_message(
                message.chat.id, 'دوست عزیزم یا عدد وارد کن یا هم از دست من کاری بر نمیاد و میتونی برای خارج شدن دکمه زیر رور بزنی  \n\help', reply_markup=Guess_game)
            bot.register_next_step_handler(msg, guess_number)
    else :
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help')





def salshomar(message):
    if message.text != '/Exit':
        if len(message.text.split('/')) == 3:
            date_difference = JalaliDatetime.now() - JalaliDatetime(message.text.split('/')[0], message.text.split('/')[1], message.text.split('/')[2])
            bot.send_message(message.chat.id, ' شما' + str(date_difference.days // 365) + 'سال دارید')
            bot.send_message(message.chat.id, 'اگر هنوز از من کمکی بر میاد دکمه زیر رو بزن  \n\n/help')
        else:
            user_age = bot.send_message(message.chat.id, ' دوست عزیزم لطفا به فرمی که درخواست کردم وارد کن . اگر هم می خوای خارج بشی دکمه زیر رو بزن \n /help')
            bot.register_next_step_handler(user_age, salshomar)
    
    else :
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help')




def txt_to_voice(message):
    if message.text != '/Exit':
        language = 'en'
        sentence = gTTS(text=message.text , lang = language , slow=False)
        sentence.save('txt_voice.ogg')
        sentence = open('txt_voice.ogg', 'rb')
        bot.send_voice(message.chat.id, sentence)
        bot.send_message( message.chat.id, 'با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی   \n\n /help')
    else:
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help')





def max_number(message):
    if message.text != '/Exit':
        try:
            numbers = list(map(int, message.text.split(',')))
            bot.send_message(message.chat.id, 'بزرگترین عدد: ' + str(max(numbers)))
            bot.send_message(message.chat.id, 'اینم از بزرگترین عدد . برای خارج شدن دکمه زیر رو بزن   \n\n/help')
        except:
            list_number = bot.send_message(message.chat.id, 'لطفا به فرمی که خواسته بودم وارد کن وگرنه از پسش بر نمیام و مجبوری دکمه زیر رو بزنی \n\n/Exit') 
            bot.register_next_step_handler(list_number, max_number)
    else :
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help')





def find_index(message):
    
    if message.text != '/Exit':
        try:
            numbers = list(map(int, message.text.split(',')))
            bot.send_message(message.chat.id, 'اندیس عدد بزرگتر ' + str(numbers.index(max(numbers))+1))
            bot.send_message(message.chat.id, 'اینم از  اندیس بزرگترین عدد . برای خارج شدن دکمه زیر رو بزن   \n\n/help')
        except:
            list_number = bot.send_message(message.chat.id, 'لطفا به فرمی که خواسته بودم وارد کن وگرنه از پسش بر نمیام و مجبوری دکمه زیر رو بزنی \n\n/Exit')
            bot.register_next_step_handler(list_number, find_index)
    else :
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help')



def Qr_Code(message):

    if message.text != '/Exit':
        try:
            qr_img = qrcode.make(message.text)
            qr_img.save('QRCode.png')
            photo = open('QRCode.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'کیو ار کدت ساخته شد . اگر کار دیگه ای نیست دکمه زیر رو بزن  \n\n/help')
        except :
            user_qr = bot.send_message(message.chat.id, 'یه جای کار میلینگه که من نمی تونم برات تبدیلش کنم . به نظرم یکبار دیگه با حروف درست انتخاب کن در غیر این صورت میتونی دکمه زیر رو بزنی که خارج بشی  \n\n/Exit')
            bot.register_next_step_handler(user_qr, Qr_Code)
    else :
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help')



def Salavat_shomar(message):
    if message.text != '/Exit' :
        if message.text == 'صلوات جدید' :
            salavat_counter[0] += 1
            sala = bot.send_message(message.chat.id, 'تعداد صلوات شما :       ' + str(salavat_counter[0]) + '\n\nبرای خروج دکمه زیر را بزنید  \n\n/Exit'  , reply_markup=NewSalavat)
            bot.register_next_step_handler(sala, Salavat_shomar)
    else :
        bot.send_message(message.chat.id, 'با موفقیت خارج شدی . با زدن دکمه زیر مجموعه ای از کار هایی که می تونم انجام بدم رو میتونی مشاهده کنی  \n\n/help' , reply_markup=types.ReplyKeyboardRemove(selective=True))

bot.infinity_polling()