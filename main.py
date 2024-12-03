import uuid
import re
from io import BytesIO
import telebot
from telebot import types
from PIL import Image
from pixelate import pixelate
from make_legend import make_legend_image
import os
from color_show import show_color, save_color_sample, create_color_grid
from color_data import floss_colors, color_groups, RGB

# Укажите здесь токен вашего бота
API_TOKEN = '8174585257:AAHIAJbSk_SqWaf-2MD-wTECq_aVi9INGcs'

bot = telebot.TeleBot(API_TOKEN)

# Словарь для хранения данных пользователей (в целях демонстрации)
user_data = {}

# Словарь для сохранения выбранных кодов цветов
available_colors = {}


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
        send_photo_list(user_id)
    elif message.text == "🌈 Добавить цвета":
        add_color_brands(message)
    elif message.text == "✅ Показать добавленные цвета":
        show_color_brands(message)
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

    available_rgbs = []
    for brand in ('DMC', 'Anchor', 'Cosmo'):
        if user_id not in available_colors:
            break
        for color in available_colors[user_id][brand]:
            available_rgbs.append(color['rgb'])

    # Пикселизируем изображение
    pixelated_image = pixelate(image, available_colors=RGB)
    legend_image = make_legend_image(pixelated_image)

    # Сохраняем пикселизированное изображение во временный файл
    output_io = BytesIO()
    pixelated_image.save(output_io, format='JPEG')
    output_io.seek(0)

    # Отправляем пикселизированное изображение пользователю
    bot.send_message(user_id, "Схема на основе всех возможных цветов:")
    bot.send_photo(user_id, output_io)

    # Сохраняем легенду во временный файл
    output_io = BytesIO()
    legend_image.save(output_io, format='JPEG')
    output_io.seek(0)

    # Отправляем легенду пользователю
    bot.send_message(user_id, "Легенда:")
    bot.send_photo(user_id, output_io)

    # Пикселизация только по доступным цветам
    if not available_rgbs:
        bot.send_message(user_id, "Сформировать схему на основе ваших цветов невозможно. Вы не добавили ни одного цвета.")
        return

    pixelated_image = pixelate(image, available_colors=available_rgbs)
    legend_image = make_legend_image(pixelated_image)

    # Сохраняем пикселизированное изображение во временный файл
    output_io = BytesIO()
    pixelated_image.save(output_io, format='JPEG')
    output_io.seek(0)

    # Отправляем пикселизированное изображение пользователю
    bot.send_message(user_id, "Схема на основе Ваших цветов:")
    bot.send_photo(user_id, output_io)

     # Сохраняем легенду во временный файл
    output_io = BytesIO()
    legend_image.save(output_io, format='JPEG')
    output_io.seek(0)

    # Отправляем легенду пользователю
    bot.send_message(user_id, "Легенда:")
    bot.send_photo(user_id, output_io)



def add_color_brands(message):
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
    keywords = color_groups.get(group, [])  # извлечь ключевые слова группы

    for color_name, color_data in floss_colors[brand].items():
        # Проверяем, содержит ли название цвета любое из ключевых слов группы
        if any(keyword in color_name for keyword in keywords):
            group_colors.append({
                'name': color_name,
                'code': color_data['code'],
                'rgb': color_data['rgb']
            })

    # Проверяем, есть ли найденные цвета
    if group_colors:
        # Создаем сетку цветов
        output_path = f"{temp_dir}/{brand}_{group}.png"
        create_color_grid(brand, group_colors, output_path)

        # Отправляем изображение с сеткой цветов
        with open(output_path, 'rb') as photo:
            caption = f"Цвета группы '{group}' бренда {brand}. Выберите коды цветов:"
            message = bot.send_photo(call.message.chat.id, photo, caption=caption)

            # Создаем клавиатуру для выбора кодов цветов
            color_keyboard = types.InlineKeyboardMarkup()
            for color in group_colors:
                color_button = types.InlineKeyboardButton(
                    text=color['name'] + " " + color['code'],
                    callback_data=f"color_{brand}_{color['code']}_{color['name']}"
                )
                color_keyboard.add(color_button)

            bot.send_message(call.message.chat.id, "Выберите коды цветов:", reply_markup=color_keyboard)

        # Удаляем временный файл
        os.remove(output_path)
    else:
        bot.send_message(call.message.chat.id, f"Цвета группы '{group}' не найдены для бренда {brand}")

    # Удаляем уведомление о нажатии кнопки
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('color_'))
def handle_color_selection(call):
    """Обработчик выбора кода цвета"""
    color_brand = call.data.split('_')[1]
    color_code = call.data.split('_')[2]
    color_name = call.data.split('_')[3]
    user_id = call.message.chat.id

    if user_id not in available_colors:
        available_colors[user_id] = {
            'DMC': [],
            'Anchor': [],
            'Cosmo': []
        }

    color_info = floss_colors[color_brand][color_name]
    color_info['name'] = color_name

    if color_info not in available_colors[user_id][color_brand]:
        available_colors[user_id][color_brand].append(color_info)
        bot.send_message(call.message.chat.id, f"Цвет '{color_code}' добавлен.")
        return
    available_colors[user_id][color_brand].remove(color_info)
    bot.send_message(call.message.chat.id, f"Цвет '{color_code}' удалён.")


def show_brand_colors(message, brand):
    temp_dir = 'temp_colors'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    output_path = f"{temp_dir}/{message.chat.id}.png"

    user_id = message.chat.id

    if not available_colors[user_id][brand]:
        bot.send_message(user_id, f"Пока что не добавлено ни одного цвета бренда {brand}.")
        return

    create_color_grid(brand, available_colors[user_id][brand], output_path)

    # Отправляем изображение с сеткой цветов
    with open(output_path, 'rb') as photo:
        caption = f"Добавленные цвета бренда {brand}"
        bot.send_photo(message.chat.id, photo, caption=caption)

    # Удаляем временный файл
    os.remove(output_path)


def show_color_brands(message):
    for brand in ('DMC', 'Anchor', 'Cosmo'):
        show_brand_colors(message, brand)


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
