from telebot import types
import os

# Отправка списка фотографий пользователю
def send_photo_list(bot, user_id):
    user_folder = f'photos/{user_id}'
    if not os.path.exists(user_folder) or not os.listdir(user_folder):
        bot.send_message(user_id, "У вас пока нет сохранённых фотографий.")
        return

    photo_list = os.listdir(user_folder)

    # inline клавиатура с файлами
    keyboard = types.InlineKeyboardMarkup()
    for photo in photo_list:
        view_button = types.InlineKeyboardButton(f"🖼 {photo}", callback_data=f"view_{photo}")
        delete_button = types.InlineKeyboardButton(f"❌ Удалить {photo}", callback_data=f"delete_{photo}")
        keyboard.add(view_button, delete_button)

    bot.send_message(user_id, "Выберите действие с фото:", reply_markup=keyboard)