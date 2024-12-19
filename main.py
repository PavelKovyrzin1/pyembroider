import os
import re
import uuid
from io import BytesIO

from PIL import Image
import telebot
from telebot import types

from color_data import floss_colors, color_groups, RGB
from color_process import show_color_brands, show_color_groups, add_color_brands
from color_show import create_color_grid
from colors_database import *
from process_images import send_photo_list, create_scheme

API_TOKEN = '8174585257:AAHIAJbSk_SqWaf-2MD-wTECq_aVi9INGcs'

bot = telebot.TeleBot(API_TOKEN)

db_name = "colors.db"
create_database(db_name)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.chat.id

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
        "3️⃣ Генерировать схему только на основе тех цветов, которые есть у Вас.\n\n"
        "Давайте начнем! Для загрузки изображения нажмите 'Загрузить изображение' на клавиатуре."
    )


# Главное меню
def main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    upload_button = types.KeyboardButton("📤 Загрузить изображение")
    view_photos_button = types.KeyboardButton("📂 Посмотреть мои фото")
    add_colors_button = types.KeyboardButton("🌈 Добавить цвета")
    show_colors_button = types.KeyboardButton("✅ Показать добавленные цвета")
    keyboard.add(upload_button, view_photos_button, add_colors_button, show_colors_button)
    return keyboard


# Обработчик кнопок и текстовых сообщений от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.chat.id

    if message.text == "📤 Загрузить изображение":
        bot.send_message(user_id, "Отправьте мне изображение, которое вы хотите преобразовать в схему.")
    elif message.text == "📂 Посмотреть мои фото":
        send_photo_list(bot, user_id)
    elif message.text == "🌈 Добавить цвета":
        add_color_brands(bot, message)
    elif message.text == "✅ Показать добавленные цвета":
        show_color_brands(bot, message)
    else:
        bot.send_message(user_id, "Пожалуйста, используйте кнопки меню для взаимодействия.")


# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.chat.id

    # Скачивание изображения на сервер
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Проверка подписи к изображению
    if message.caption:
        photo_caption = message.caption
        photo_caption = re.sub(r'[^\w\s-]', '', photo_caption).strip().replace(' ', '_')
    else:
        photo_caption = str(uuid.uuid4())

    user_folder = f'photos/{user_id}'
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

    bot.send_message(user_id, f"Изображение сохранено под именем: {os.path.basename(file_path)}")

    image = Image.open(BytesIO(downloaded_file))

    filename = f"Scheme_{os.path.basename(file_path)}.pdf"
    create_scheme(image, RGB, filename)

    bot.send_message(user_id, "Схема на основе всех возможных цветов:")

    with open(filename, 'rb') as pdf_file:
        bot.send_document(user_id, pdf_file)

    os.remove(filename)

    # Извлечение доступных пользователю цветов
    available_rgbs = get_user_colors(db_name, user_id)

    # Пикселизация только по доступным цветам
    if not available_rgbs:
        bot.send_message(user_id,
                         "Сформировать схему на основе ваших цветов невозможно. Вы не добавили ни одного цвета.")
        return

    create_scheme(image, available_rgbs, filename)

    bot.send_message(user_id, "Схема на основе Ваших цветов:")

    with open(filename, 'rb') as pdf_file:
        bot.send_document(user_id, pdf_file)

    os.remove(filename)


@bot.callback_query_handler(func=lambda call: call.data.startswith('brand_'))
def handle_brand_selection(call):
    """Обработчик выбора бренда"""
    brand = call.data.split('_')[1]
    show_color_groups(bot, call.message, brand)


@bot.callback_query_handler(func=lambda call: call.data.startswith('group_'))
def handle_group_selection(call):
    """Обработчик выбора группы цветов"""
    _, brand, group = call.data.split('_')

    temp_dir = 'temp_colors'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Собираем цвета выбранной группы
    group_colors = []
    keywords = color_groups.get(group, [])

    for color_name, color_data in floss_colors[brand].items():
        if any(keyword in color_name for keyword in keywords):
            group_colors.append({
                'name': color_name,
                'code': color_data['code'],
                'rgb': color_data['rgb']
            })

    # Проверяем, есть ли найденные цвета
    if group_colors:
        output_path = f"{temp_dir}/{brand}_{group}.png"
        create_color_grid(brand, group_colors, output_path)

        # Отправляем изображение с сеткой цветов
        with open(output_path, 'rb') as photo:
            caption = f"Цвета группы '{group}' бренда {brand}. Выберите коды цветов:"
            message = bot.send_photo(call.message.chat.id, photo, caption=caption)

            # Клавиатура для выбора кодов цветов
            color_keyboard = types.InlineKeyboardMarkup()
            for color in group_colors:
                color_button = types.InlineKeyboardButton(
                    text=color['name'] + " " + color['code'],
                    callback_data=f"color_{brand}_{color['code']}_{color['name']}"
                )
                color_keyboard.add(color_button)

            bot.send_message(call.message.chat.id, "Выберите коды цветов:", reply_markup=color_keyboard)

        os.remove(output_path)
    else:
        bot.send_message(call.message.chat.id, f"Цвета группы '{group}' не найдены для бренда {brand}")

    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith('color_'))
def handle_color_selection(call):
    """Обработчик выбора кода цвета"""
    color_brand = call.data.split('_')[1]
    color_code = call.data.split('_')[2]
    color_name = call.data.split('_')[3]
    user_id = call.message.chat.id

    color_info = floss_colors[color_brand][color_name]
    color_info['name'] = color_name

    if not check_user_color_exists(db_name, user_id, color_brand, color_code):
        add_user_color(db_name, user_id, color_brand, color_code)
        bot.send_message(call.message.chat.id, f"Цвет '{color_code}' добавлен.")
        return

    delete_user_color(db_name, user_id, color_brand, color_code)
    bot.send_message(call.message.chat.id, f"Цвет '{color_code}' удалён.")


# Обработчик нажатий на inline кнопки
@bot.callback_query_handler(func=lambda call: call.data.startswith("view_") or call.data.startswith("delete_"))
def handle_callback(call):
    user_id = call.message.chat.id
    user_folder = f'photos/{user_id}'

    # Просмотр
    if call.data.startswith("view_"):
        filename = call.data.replace("view_", "")
        file_path = os.path.join(user_folder, filename)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as photo:
                bot.send_photo(user_id, photo, caption=f"Вот ваше фото: {filename}")
        else:
            bot.send_message(user_id, "Файл не найден. Возможно, он был удален.")

    # Удаление
    elif call.data.startswith("delete_"):
        filename = call.data.replace("delete_", "")
        file_path = os.path.join(user_folder, filename)

        if os.path.exists(file_path):
            os.remove(file_path)
            bot.send_message(user_id, f"Фото {filename} успешно удалено.")
        else:
            bot.send_message(user_id, "Файл не найден. Возможно, он уже был удален.")

    bot.answer_callback_query(call.id)


# Обработчик для видео
@bot.message_handler(content_types=['video'])
def video_handler(message):
    bot.send_message(message.chat.id, "Формат видео не поддерживается. Пожалуйста, отправьте изображение.")


# Обработчик для GIF
@bot.message_handler(content_types=['animation'])
def gif_handler(message):
    bot.send_message(message.chat.id, "Формат GIF не поддерживается. Пожалуйста, отправьте изображение.")


# Обработчик для GIF
@bot.message_handler(content_types=['document'])
def gif_handler(message):
    bot.send_message(message.chat.id, "Формат файлов не поддерживается. Пожалуйста, отправьте изображение.")


# Основной обработчик ошибок и прочих типов сообщений
@bot.message_handler(func=lambda message: True)
def default_handler(message):
    bot.send_message(
        message.chat.id,
        "Я вас не понял. Попробуйте воспользоваться кнопками для взаимодействия."
    )


if __name__ == '__main__':
    bot.infinity_polling()
