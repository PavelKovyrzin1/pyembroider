import os
import aspose.words as aw
from io import BytesIO
from PIL import Image
from typing import List, Tuple

from aiogram import Bot, types

from pixelate import pixelate
from make_legend import make_legend_image


# Отправка списка фотографий пользователю
async def send_photo_list(bot: Bot, user_id: int) -> None:
    user_folder = f'../photos/{user_id}'
    if not os.path.exists(user_folder) or not os.listdir(user_folder):
        await bot.send_message(user_id, "У вас пока нет сохранённых фотографий.")
        return

    photo_list = os.listdir(user_folder)

    # inline клавиатура с файлами
    keyboard = types.InlineKeyboardMarkup()
    for photo in photo_list:
        view_button = types.InlineKeyboardButton(f"🖼 {photo}", callback_data=f"view_{photo}")
        delete_button = types.InlineKeyboardButton(f"❌ Удалить {photo}", callback_data=f"delete_{photo}")
        keyboard.add(view_button, delete_button)

    await bot.send_message(user_id, "Выберите действие с фото:", reply_markup=keyboard)


async def create_scheme(image: Image, available_colors: List[Tuple], filename: str) -> None:
    # Пикселизация
    pixelated_image = await pixelate(image, available_colors=available_colors)
    legend_image = await make_legend_image(pixelated_image, available_colors)

    # Сохранение и отправка изображения
    output_io = BytesIO()
    pixelated_image.save(output_io, format='JPEG')
    output_io.seek(0)

    byte_output = output_io.getvalue()

    # Теперь мы можем записать его в файл
    with open("output_image.jpg", "wb") as file:
        file.write(byte_output)

    # Легенда
    legend_io = BytesIO()
    legend_image.save(legend_io, format='JPEG')
    legend_io.seek(0)

    byte_legend = legend_io.getvalue()

    with open("legend_image.jpg", "wb") as file:
        file.write(byte_legend)

    fileNames = ["output_image.jpg", "legend_image.jpg"]

    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)

    for fileName in fileNames:
        builder.insert_image(fileName)
        # Вставляем разрыв абзаца, чтобы изображения не перекрывались.
        builder.writeln()

    doc.save(filename)

    os.remove("output_image.jpg")
    os.remove("legend_image.jpg")
