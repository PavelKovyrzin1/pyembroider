from PIL import Image, ImageDraw, ImageFont
from color_data import floss_colors
from typing import List, Tuple

SQUARE_SIZE = 130
PADDING = 10
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 2551

FONT_SIZE = 40
TEXT_OFFSET = 10


async def make_legend_image(image: Image, available_rgbs: List[Tuple]) -> Image:
    unique_colors = set()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            rgb = image.getpixel((x, y))
            unique_colors.add(rgb)

    # Удаляем черный цвет, если его нет
    if (0, 0, 0) not in available_rgbs:
        unique_colors.remove((0, 0, 0))

    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(image)

    # Шрифт
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()

    # Квадраты с цветами и их названиями
    x, y = PADDING, PADDING
    for brand in floss_colors:
        draw.text((x + TEXT_OFFSET, y + TEXT_OFFSET), brand, fill="black", font=font)
        y += SQUARE_SIZE + PADDING
        for color_name, color_info in floss_colors[brand].items():
            rgb = color_info['rgb']
            if not rgb in unique_colors:
                continue
            # Цветной квадрат
            draw.rectangle([x, y, x + SQUARE_SIZE, y + SQUARE_SIZE], fill=rgb)

            # Название цвета
            draw.text((x + TEXT_OFFSET, y + SQUARE_SIZE + TEXT_OFFSET), color_info['code'], fill="black", font=font)

            # Обновляем координаты для следующего квадрата
            x += SQUARE_SIZE + PADDING
            if x + SQUARE_SIZE > IMAGE_WIDTH:
                x = PADDING
                y += SQUARE_SIZE + PADDING + 2 * FONT_SIZE
            if y + SQUARE_SIZE > IMAGE_HEIGHT:
                break
        y += SQUARE_SIZE + PADDING + FONT_SIZE
        x = PADDING

    return image
