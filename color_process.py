from telebot import types
import os

from color_show import create_color_grid
from color_data import floss_colors, color_groups, transformed_color_data
from colors_database import *


def show_brand_colors(bot, message, brand):
    """Отправляет сетку выбранных пользователем цветов данного бренда"""
    temp_dir = 'temp_colors'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    output_path = f"{temp_dir}/{message.chat.id}.png"
    user_id = message.chat.id
    colors = get_user_colors_by_brand("colors.db", user_id, brand)

    if len(colors) == 0:
        bot.send_message(user_id, f"Пока что не добавлено ни одного цвета бренда {brand}.")
        return

    available_colors = [transformed_color_data[color] for color in colors]
    create_color_grid(brand, available_colors, output_path)

    with open(output_path, 'rb') as photo:
        caption = f"Добавленные цвета бренда {brand}"
        bot.send_photo(message.chat.id, photo, caption=caption)

    os.remove(output_path)


def show_color_brands(bot, message):
    for brand in ('DMC', 'Anchor', 'Cosmo'):
        show_brand_colors(bot, message, brand)


def show_color_groups(bot, message, brand):
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


def add_color_brands(bot, message):
    """Показывает доступные бренды ниток"""
    keyboard = types.InlineKeyboardMarkup()
    for brand in floss_colors.keys():
        callback_button = types.InlineKeyboardButton(text=brand, callback_data=f"brand_{brand}")
        keyboard.add(callback_button)

    bot.send_message(message.chat.id, "Выберите бренд ниток:", reply_markup=keyboard)
