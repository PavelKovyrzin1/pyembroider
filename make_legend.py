from PIL import Image, ImageDraw, ImageFont
from color_data import floss_colors


def make_legend_image(image, available_rgbs):
    unique_colors = set()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            rgb = image.getpixel((x, y))
            unique_colors.add(rgb)

    # Удаляем черный цвет, если его нет
    if (0, 0, 0) not in available_rgbs:
        unique_colors.remove((0, 0, 0))

    square_size = 75  # размер квадрата
    padding = 10  # отступ между квадратами
    image_width = 1920  # ширина изображения
    image_height = 1080  # высота изображения

    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Шрифт
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except IOError:
        font = ImageFont.load_default()

    # Квадраты с цветами и их названиями
    x, y = padding, padding
    for brand in floss_colors:
        draw.text((x + 5, y + 5), brand, fill="black", font=font)
        y += square_size + padding
        for color_name, color_info in floss_colors[brand].items():
            rgb = color_info['rgb']
            if not rgb in unique_colors:
                continue
            # Цветной квадрат
            draw.rectangle([x, y, x + square_size, y + square_size], fill=rgb)

            # Название цвета
            draw.text((x + 5, y + square_size + 5), color_info['code'], fill="black", font=font)

            # Обновляем координаты для следующего квадрата
            x += square_size + padding
            if x + square_size > image_width:
                x = padding
                y += square_size + padding + 50  # 20 - высота текста
            if y + square_size > image_height:
                break
        y += square_size + padding + 50
        x = padding

    return image
