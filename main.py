import telebot
from telebot import types
from pathlib import Path
import numpy as np
from PIL import Image
from docopt import docopt
from pixelate import pixelate
import os
from color_show import show_color, save_color_sample, create_color_grid
from color_data import floss_colors, color_groups

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
    show_colors_button = types.KeyboardButton("🌈 Показать цвета")
    keyboard.add(upload_button, select_colors_button, show_colors_button)
    return keyboard

# Обработчик кнопки "Загрузить изображение"
@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.chat.id

    if message.text == "📤 Загрузить изображение":
        bot.send_message(user_id, "Отправьте мне изображение, которое вы хотите преобразовать в схему.")
    elif message.text == "🎨 Ввести доступные цвета":
        bot.send_message(user_id, "Напишите список доступных цветов ниток (например: красный, синий, зеленый).")
    elif message.text == "🌈 Показать цвета":
        show_color_brands(message)
    else:
        bot.send_message(user_id, "Пожалуйста, используйте кнопки меню для взаимодействия.")

# Обработчик изображения
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.chat.id

    # Получаем информацию о файле
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    """
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
    """
    # Сохраняем изображение во временный файл
    temp_file_path = 'temp_image.jpg'
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(downloaded_file)

    # Сохраняем путь к изображению в user_data
    user_data[user_id] = {}
    user_data[user_id]['image'] = temp_file_path

    bot.send_message(user_id, "Изображение успешно загружено. Начинаю обработку...")

    # Обработка изображения
    image = Image.open(temp_file_path).convert('RGB')
    pixelated_image = pixelate(image, 16)

    # Сохранение обработанного изображения
    output_path = 'pixelated_image.jpg'
    pixelated_image.save(output_path)

    # Отправка обработанного изображения
    with open(output_path, 'rb') as output_file:
        bot.send_photo(user_id, output_file)

    # Удаление временных файлов
    os.remove(temp_file_path)
    os.remove(output_path)

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

def show_color_brands(message):
    """Показывает доступные бренды ниток"""
    keyboard = types.InlineKeyboardMarkup()
    for brand in floss_colors.keys():
        callback_button = types.InlineKeyboardButton(text=brand, callback_data=f"brand_{brand}")
        keyboard.add(callback_button)
    
    bot.send_message(message.chat.id, "Выберите бренд ниток:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('brand_'))
def handle_brand_selection(call):
    """Обработчик выбора бренда"""
    brand = call.data.split('_')[1]
    show_color_groups(call.message, brand)

def show_color_groups(message, brand):
    """Показывает группы цветов для выбранного бренда"""
    keyboard = types.InlineKeyboardMarkup()
    for group_name in color_groups.keys():
        callback_button = types.InlineKeyboardButton(
            text=group_name, 
            callback_data=f"group_{brand}_{group_name}"
        )
        keyboard.add(callback_button)
    
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"Выберите группу цветов для бренда {brand}:",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('group_'))
def handle_group_selection(call):
    """Обработчик выбора группы цветов"""
    _, brand, group = call.data.split('_')
    
    # Создаем временный файл для образца цвета
    temp_dir = 'temp_colors'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Собираем цвета выбранной группы
    group_colors = []
    keywords = color_groups.get(group, [])
    
    for color_name, color_data in floss_colors[brand].items():
        # Проверяем, содержит ли название цвета любое из ключевых слов группы
        if any(keyword in color_name for keyword in keywords):
            group_colors.append({
                'name': color_name,
                'code': color_data['code'],
                'rgb': color_data['rgb']
            })

    if group_colors:
        # Создаем сетку цветов
        output_path = f"{temp_dir}/{brand}_{group}.png"
        create_color_grid(brand, group_colors, output_path)
        
        # Отправляем изображение с сеткой цветов
        with open(output_path, 'rb') as photo:
            caption = f"Цвета группы '{group}' бренда {brand}"
            bot.send_photo(call.message.chat.id, photo, caption=caption)
        
        # Удаляем временный файл
        os.remove(output_path)
    else:
        bot.send_message(call.message.chat.id, f"Цвета группы '{group}' не найдены для бренда {brand}")

    bot.answer_callback_query(call.id)

# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()
