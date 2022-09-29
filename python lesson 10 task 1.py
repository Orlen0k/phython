# Урок 10. Возможна ли жизнь без PIP? Продолжение
# Прикрутить бота к задачам с предыдущего семинара или модернизировать бота с текущего семинара
#
# отработал команды с семинара


from telegram import ReplyKeyboardMarkup, Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext
from credits import bot_token


bot = Bot(token=bot_token)
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

GENDER = 0
PHOTO = 1
BIO = 2
VIDEO = 3

def start(update, context):
    reply_keyboard = [['Мужчина', 'Женщина']]
    update.message.reply_text('Добрый день! Мы ООО "Рога и Копыта". Укажите свой пол',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return GENDER

def gender(update, context):
    update.message.reply_text('Супер! Теперь отправьте свое фото, или нажмите /skip чтобы пропустить')
    return PHOTO

def photo(update, context):
    user = str(update.message.from_user['username'])
    photo_file = update.message.document.get_file()
    photo_file.download(user + '_photo.jpg')
    update.message.reply_text('Супер! Мы получили Ваше фото. Тепепрь отправьте краткое резюме о себе или нажмите /skip чтобы пропустить')
    return BIO

def skip_photo(update, context):
    update.message.reply_text(
        'Значит без фото! Теперь отправьте краткое резюме о себе или нажмите /skip чтобы пропустить')
    return BIO

def bio(update, context):
    user = str(update.message.from_user['username'])
    update.message.reply_text(
        'Супер! Мы получили Ваше резюме. Теперь  отправьте краткое видео о себе, или нажмите /skip чтобы пропустить')
    f = open(user + '_bio.txt', 'w')
    f.write(update.message.reply_text)
    f.close()
    return VIDEO

def skip_bio(update, context):
    update.message.reply_text(
        'Значит без Резюме! Теперь отправьте краткое резюме о себе или нажмите /skip чтобы пропустить')
    return VIDEO


def video(update, context):
    user = str(update.message.from_user['username'])
    video_file = update.message.document.get_file()
    video_file.download(user + 'video.mp4')
    update.message.reply_text('Супер! Мы получили Ваше видео. Мы свяжемся с Вами')
    return ConversationHandler.END

def skip_video(update, context):
    update.message.reply_text(
        'Значит без Видео! Мы свяжемся с Вами')
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text(
        'Надеюсь еще напишете нам')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
gender_handler = MessageHandler(Filters.regex('^(Мужчина|Женщина$'), gender)
photo_handler = MessageHandler(Filters.photo, photo)
skip_photo_handler = CommandHandler('skip', skip_photo)
bio_handler = MessageHandler(Filters.text, bio)
skip_bio_handler = CommandHandler('skip', skip_bio)
video_handler = MessageHandler(Filters.video, video)
skip_video_handler = CommandHandler('skip', skip_video)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        GENDER:[gender_handler],
        PHOTO: [photo_handler, skip_photo_handler],
        BIO: [bio_handler, skip_bio_handler],
        VIDEO: [video_handler, skip_video_handler]},
    fallbacks=[cancel_handler]
)

dispatcher.add_handler(conv_handler)


updater.start_polling()
updater.idle()

