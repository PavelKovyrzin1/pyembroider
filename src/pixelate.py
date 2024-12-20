from PIL import Image
from collections import Counter
from typing import List, Tuple

MIN_SIZE = 700
SQUARE_SIZE = 10
QUOTIENT = 142


async def closest_color(requested_color: Tuple, available_colors: List[Tuple]):
    """
    Находит ближайший цвет из списка available_colors для заданного цвета requested_color.
    """
    r, g, b = requested_color
    closest_color = min(available_colors,
                        key=lambda color: (color[0] - r) ** 2 + (color[1] - g) ** 2 + (color[2] - b) ** 2)
    return closest_color


async def replace_rare_colors(image: Image, rarity_threshold: float = 0.0001) -> Image:
    """
    Заменяет все редко встречающиеся цвета (меньше порога rarity_threshold) на похожие часто встречающиеся цвета.
    """
    pixels = list(image.getdata())  # Получаем все пиксели изображения как [(r, g, b), ...]
    total_pixels = len(pixels)  # Общее количество пикселей
    color_counts = Counter(pixels)  # Считаем количество каждого цвета

    # Разделяем цвета на два списка: редкие и частые
    rare_colors = {color: count for color, count in color_counts.items() if count / total_pixels < rarity_threshold}
    frequent_colors = {color: count for color, count in color_counts.items() if
                       count / total_pixels >= rarity_threshold}

    new_color_map = {}
    for rare_color in rare_colors:
        # Находим ближайший частый цвет
        new_color = await closest_color(rare_color, frequent_colors.keys())
        new_color_map[rare_color] = new_color

    new_image_data = [new_color_map.get(pixel, pixel) for pixel in pixels]  # Заменяем редкие цвета
    image.putdata(new_image_data)  # Обновляем пиксели изображения

    return image


async def pixelate(image: Image, available_colors: List[Tuple[str, str]], margin_thickness: int = 1) -> Image:
    margin_color = (0, 0, 0)

    min_size = min(image.size[0], image.size[1])

    if min_size < MIN_SIZE:
        k = MIN_SIZE // min_size
        image = image.resize((image.size[0] * k, image.size[0] * k), Image.NEAREST)
        min_size *= k

    pixel_size = min_size // QUOTIENT + 2

    # Уменьшение и увеличение изображения для пикселизации
    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)

    # Подбор цвета
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            current_color = image.getpixel((x, y))
            new_color = await closest_color(current_color, available_colors)
            image.putpixel((x, y), new_color)

    # Заменяем редкие цвета на более частые
    image = await replace_rare_colors(image)

    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()

    # Рисуем черную границу между пикселями
    for i in range(0, image.size[0], pixel_size):
        for j in range(0, image.size[1], pixel_size):
            # Рисуем границу по горизонтали
            for r in range(margin_thickness):
                if i + r < image.size[0] and j < image.size[1]:
                    pixel[i + r, j] = margin_color
                if j + r < image.size[1] and i < image.size[0]:
                    pixel[i, j + r] = margin_color

    # Рисуем черную границу между пикселями
    for i in range(0, image.size[0], SQUARE_SIZE * pixel_size):
        for j in range(0, image.size[1], SQUARE_SIZE * pixel_size):
            for r in range(SQUARE_SIZE * pixel_size):
                if i + r < image.size[0] and j < image.size[1]:
                    pixel[i + r, j] = margin_color
                if i < image.size[0] and j + r < image.size[1]:
                    pixel[i, j + r] = margin_color

    return image
