import telebot
from telebot import types

# Укажите здесь токен вашего бота
API_TOKEN = '8174585257:AAHIAJbSk_SqWaf-2MD-wTECq_aVi9INGcs'

bot = telebot.TeleBot(API_TOKEN)

# Словарь для хранения данных пользователей (в целях демонстрации)
user_data = {}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.chat.id
    user_data[user_id] = {'colors': [], 'image': None}

    bot.send_message(user_id,
                     "Добро пожаловать в PyEmbroider! 👋\n"
                     "Я помогу преобразовать изображения в схемы для вышивания крестиком.\n"
                     "Напишите /help, чтобы узнать больше, или начнем загрузку!",
                     reply_markup=main_menu_keyboard())


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🤖 Что я умею:n"
        "1️⃣ Преобразовывать изображения в схемы для вышивки.\n"
        "2️⃣ Показывать недостающие цвета ниток и давать рекомендации по их покупке.\n"
        "3️⃣ Расчитывать длину ниток для проекта.\n\n"
        "Давайте начнем! Для загрузки изображения нажмите 'Загрузить изображение' на клавиатуре."
    )


# Главное меню
def main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    upload_button = types.KeyboardButton("📤 Загрузить изображение")
    select_colors_button = types.KeyboardButton("🎨 Ввести доступные цвета")
    keyboard.add(upload_button, select_colors_button)
    return keyboard


# Обработчик кнопки "Загрузить изображение"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.chat.id

    if message.text == "📤 Загрузить изображение":
        bot.send_message(user_id, "Отправьте мне изображение, которое вы хотите преобразовать в схему.")
    elif message.text == "🎨 Ввести доступные цвета":
        bot.send_message(user_id, "Напишите список доступных цветов ниток (например: красный, синий, зеленый).")
    else:
        bot.send_message(user_id, "Пожалуйста, используйте кнопки меню для взаимодействия.")


# Обработчик изображения
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.chat.id

    # Скачивание изображения на сервер
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    user_data[user_id]['image'] = downloaded_file

    # Здесь будет вызов функции для обработки изображения
    bot.send_message(user_id, "Изображение успешно загружено. Начинаю обработку...")
    # TODO: вызов функции для пикселизации и анализа изображения


# Обработчик выбора доступных ниток
@bot.message_handler(content_types=['text'])
def handle_colors(message):
    user_id = message.chat.id

    # Сохранение указанных цветов в структуру
    if 'colors' in user_data[user_id]:
        user_data[user_id]['colors'] = message.text.split(',')
        bot.send_message(user_id, "Цвета сохранены! Продолжайте использовать кнопки меню.")
    else:
        bot.send_message(user_id, "Ошибка! Пожалуйста, начните с команды /start.")


# Основной обработчик ошибок и прочих типов сообщений
@bot.message_handler(func=lambda message: True)
def default_handler(message):
    bot.send_message(
        message.chat.id,
        "Я вас не понял. Попробуйте воспользоваться кнопками для взаимодействия."
    )


# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()
