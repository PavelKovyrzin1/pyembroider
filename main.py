import os
import telebot
from telebot import types
import uuid
import re
from pixelate import pixelate
from io import BytesIO
from PIL import Image

# Укажите здесь токен вашего бота
API_TOKEN = '7860027518:AAF-l2_PMQh_QwiFPwmsNfWit1NXIP4WCyM'

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
        "🤖 Что я умею:\n"
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
    view_photos_button = types.KeyboardButton("📂 Посмотреть мои фото")
    menu_button = types.KeyboardButton("🏠 Меню")
    keyboard.add(upload_button, select_colors_button, view_photos_button, menu_button)
    return keyboard


# Обработчик кнопок и текстовых сообщений от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.chat.id

    if message.text == "📤 Загрузить изображение":
        bot.send_message(user_id, "Отправьте мне изображение, которое вы хотите преобразовать в схему.")
    elif message.text == "🎨 Ввести доступные цвета":
        bot.send_message(user_id, "Напишите список доступных цветов ниток (например: красный, синий, зеленый).")
    elif message.text == "📂 Посмотреть мои фото":
        send_photo_list(user_id)
    elif message.text == "🏠 Меню":
        bot.send_message(user_id, "Вы вернулись в главное меню.", reply_markup=main_menu_keyboard())
    else:
        bot.send_message(user_id, "Пожалуйста, используйте кнопки меню для взаимодействия.")


# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.chat.id

    # Скачивание изображения на сервер
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Проверяем подпись к изображению
    if message.caption:
        photo_caption = message.caption  # Подпись к изображению от пользователя
        # Убираем запрещенные символы из названия
        photo_caption = re.sub(r'[^\w\s-]', '', photo_caption).strip().replace(' ', '_')
    else:
        photo_caption = str(uuid.uuid4())  # Генерируем уникальный ключ

    # Уведомляем пользователя
    bot.send_message(user_id, "Изображение успешно загружено. Начинаю обработку...")

    # Определяем путь до директории пользователя
    user_folder = f'photos/{user_id}'
    # Проверяем, существует ли директория, и создаём её при отсутствии
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    # Путь до файла, изначальное имя
    file_path = os.path.join(user_folder, f'{photo_caption}.jpg')

    # Если файл с таким именем уже существует, добавляем числовой индекс к имени
    index = 1
    while os.path.exists(file_path):
        file_path = os.path.join(user_folder, f'{photo_caption}_{index}.jpg')
        index += 1

    # Сохраняем изображение в файл
    with open(file_path, 'wb') as file:
        file.write(downloaded_file)

    # Сообщаем об успешном сохранении
    bot.send_message(user_id, f"Изображение сохранено под именем: {os.path.basename(file_path)}")

    # Открываем изображение с помощью PIL
    image = Image.open(BytesIO(downloaded_file))

    # Пикселизируем изображение
    pixelated_image = pixelate(image)

    # Сохраняем пикселизированное изображение во временный файл
    output_io = BytesIO()
    pixelated_image.save(output_io, format='JPEG')
    output_io.seek(0)

    # Отправляем пикселизированное изображение пользователю
    bot.send_photo(user_id, output_io)

    # TODO: вызов функции для пикселизации и анализа изображения


# Отправка списка фотографий пользователю
def send_photo_list(user_id):
    user_folder = f'photos/{user_id}'
    if not os.path.exists(user_folder) or not os.listdir(user_folder):
        bot.send_message(user_id, "У вас пока нет сохранённых фотографий.")
        return

    photo_list = os.listdir(user_folder)

    # Генерируем inline клавиатуру с файлами
    keyboard = types.InlineKeyboardMarkup()
    for photo in photo_list:
        view_button = types.InlineKeyboardButton(f"🖼 {photo}", callback_data=f"view_{photo}")
        delete_button = types.InlineKeyboardButton(f"❌ Удалить {photo}", callback_data=f"delete_{photo}")
        keyboard.add(view_button, delete_button)

    bot.send_message(user_id, "Выберите действие с фото:", reply_markup=keyboard)


# Обработчик нажатий на inline кнопки
@bot.callback_query_handler(func=lambda call: call.data.startswith("view_") or call.data.startswith("delete_"))
def handle_callback(call):
    user_id = call.message.chat.id
    user_folder = f'photos/{user_id}'

    # Обработка действия просмотра
    if call.data.startswith("view_"):
        filename = call.data.replace("view_", "")
        file_path = os.path.join(user_folder, filename)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as photo:
                bot.send_photo(user_id, photo, caption=f"Вот ваше фото: {filename}")
        else:
            bot.send_message(user_id, "Файл не найден. Возможно, он был удален.")

    # Обработка действия удаления
    elif call.data.startswith("delete_"):
        filename = call.data.replace("delete_", "")
        file_path = os.path.join(user_folder, filename)

        if os.path.exists(file_path):
            os.remove(file_path)
            bot.send_message(user_id, f"Фото {filename} успешно удалено.")
        else:
            bot.send_message(user_id, "Файл не найден. Возможно, он уже был удален.")

    # Удаляем уведомление о нажатии кнопки
    bot.answer_callback_query(call.id)


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
