from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple, Dict

from color_data import floss_colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

A = 0.299
B = 0.587
C = 0.114
THRESHOLD = 128

# Параметры шрифта
MIN_FONT_SIZE = 8
FONT_SIZE = 40
TEXT_OFFSET = 10
SQUARE_SIZE_LEGEND = 130

# Параметры изображения
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 2551
PADDING = 10
SCALE_FACTOR = 2
SQUARE_SIZE = 10
MARGIN_THICKNESS = 1


async def make_number_scheme(image: Image, available_rgbs: List[Tuple], pixel_size: int) -> Tuple:
    unique_colors = set()
    numbers_colors = dict()
    numbers_counter = 1

    width, height = image.size

    # Проверяем уникальные цвета внутри каждого квадратика
    for x in range(1, width, pixel_size):
        for y in range(1, height, pixel_size):
            rgb = image.getpixel((x, y))
            unique_colors.add(rgb)

    if BLACK not in available_rgbs:
        unique_colors.discard(BLACK)

    # Увеличиваем размер шрифта
    font_size = max(pixel_size, MIN_FONT_SIZE)  # Минимальный размер шрифта
    font = ImageFont.load_default(size=font_size)

    for rgb in available_rgbs:
        if rgb in unique_colors:
            numbers_colors[rgb] = numbers_counter
            numbers_counter += 1

    new_width = (width + (SQUARE_SIZE * pixel_size) - width % (SQUARE_SIZE * pixel_size)) + 1
    new_height = (height + (SQUARE_SIZE * pixel_size) - height % (SQUARE_SIZE * pixel_size)) + 1

    # Увеличиваем изображение
    scale_factor = 2
    new_width *= scale_factor
    new_height *= scale_factor
    new_image = Image.new("RGB", (new_width, new_height), WHITE)
    draw = ImageDraw.Draw(new_image)

    for x in range(1, width, pixel_size):
        for y in range(1, height, pixel_size):
            rgb = image.getpixel((x, y))
            unique_colors.add(rgb)
            x0 = x * scale_factor
            y0 = y * scale_factor

            # Пишем номер цвета в центр квадрата
            text = str(numbers_colors[rgb])

            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            text_x = x0 + (pixel_size * scale_factor - text_width) / 2
            text_y = y0 + (pixel_size * scale_factor - text_height) / 2

            draw.rectangle((x0, y0, x0 + pixel_size * SCALE_FACTOR, y0 + pixel_size * SCALE_FACTOR),
                           fill=rgb)

            readable_rgb = await get_readable_text_color(rgb)
            draw.text((text_x, text_y), text, fill=readable_rgb, font=font)

    pixel = new_image.load()
    margin_color = BLACK

    for i in range(0, new_image.size[0], pixel_size * scale_factor):
        for j in range(0, new_image.size[1], pixel_size * scale_factor):
            for r in range(MARGIN_THICKNESS):
                if i + r < new_image.size[0] and j < new_image.size[1]:
                    pixel[i + r, j] = margin_color
                if j + r < new_image.size[1] and i < new_image.size[0]:
                    pixel[i, j + r] = margin_color

    for i in range(0, new_image.size[0], SQUARE_SIZE * pixel_size * scale_factor):
        for j in range(0, new_image.size[1], SQUARE_SIZE * pixel_size * scale_factor):
            for r in range(SQUARE_SIZE * pixel_size * scale_factor):
                if i + r < new_image.size[0] and j < new_image.size[1]:
                    pixel[i + r, j] = margin_color
                if i < new_image.size[0] and j + r < new_image.size[1]:
                    pixel[i, j + r] = margin_color

    return new_image, numbers_colors


async def get_readable_text_color(background_rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
    brightness = A * background_rgb[0] + B * background_rgb[1] + C * background_rgb[2]

    if brightness > THRESHOLD:
        return BLACK
    else:
        return WHITE


async def make_legend_number(image: Image, available_rgbs: List[Tuple], numbers_colors: Dict) -> Image:
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(image)

    # Шрифт
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except IOError:
        font = ImageFont.load_default(size=FONT_SIZE)

    try:
        font_2 = ImageFont.truetype("arial.ttf", 2 * FONT_SIZE)
    except IOError:
        font_2 = ImageFont.load_default(size=2 * FONT_SIZE)

    # Квадраты с цветами и их названиями
    x, y = PADDING, PADDING
    for brand in floss_colors:
        draw.text((x + TEXT_OFFSET, y + TEXT_OFFSET), brand, fill="black", font=font)
        y += SQUARE_SIZE_LEGEND + PADDING
        for color_name, color_info in floss_colors[brand].items():
            rgb = color_info['rgb']
            if not rgb in numbers_colors:
                continue

            # Цветной квадрат
            text = str(numbers_colors[rgb])
            draw.rectangle(
                [x, y, x + SQUARE_SIZE_LEGEND, y + SQUARE_SIZE_LEGEND],
                outline=BLACK,
                width=MARGIN_THICKNESS
            )

            draw.rectangle([x, y, x + SQUARE_SIZE_LEGEND, y + SQUARE_SIZE_LEGEND],
                           fill=rgb)  # Белый фон

            readable_rgb = await get_readable_text_color(rgb)
            draw.text((x + PADDING, y + PADDING), text, fill=readable_rgb, font=font_2)

            # Название цвета
            draw.text((x + TEXT_OFFSET, y + SQUARE_SIZE_LEGEND + TEXT_OFFSET), color_info['code'], fill="black",
                      font=font)

            # Обновляем координаты для следующего квадрата
            x += SQUARE_SIZE_LEGEND + PADDING
            if x + SQUARE_SIZE_LEGEND > IMAGE_WIDTH:
                x = PADDING
                y += SQUARE_SIZE_LEGEND + PADDING + 2 * FONT_SIZE
            if y + SQUARE_SIZE_LEGEND > IMAGE_HEIGHT:
                break
        y += SQUARE_SIZE_LEGEND + PADDING + FONT_SIZE
        x = PADDING

    return image
