from PIL import Image, ImageDraw, ImageFont
from color_data import floss_colors


def make_legend_image(image):
    # Создаем пустое множество для хранения уникальных RGB значений
    unique_colors = set()
    
    # Получаем ширину и высоту изображения
    width, height = image.size
    
    # Проходим по каждому пикселю изображения
    for x in range(width):
        for y in range(height):
            # Получаем RGB значение пикселя
            rgb = image.getpixel((x, y))
            # Добавляем RGB значение в множество
            unique_colors.add(rgb)

    # Создаем изображение легенды
    square_size = 75  # размер квадрата
    padding = 10       # отступ между квадратами
    image_width = 1920   # ширина изображения
    image_height = 1080   # высота изображения

    # Создание нового изображения
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Шрифт для текста
    try:
        font = ImageFont.truetype("arial.ttf", 10)
    except IOError:
        font = ImageFont.load_default()

    # Рисуем квадраты с цветами и их названиями
    x, y = padding, padding
    for brand in floss_colors:
        draw.text((x + 5, y + 5), brand, fill="black", font=font)
        y += square_size + padding
        for color_name, color_info in floss_colors[brand].items():
            rgb = color_info['rgb']
            if not rgb in unique_colors:
                continue
            # Рисуем цветной квадрат
            draw.rectangle([x, y, x + square_size, y + square_size], fill=rgb)

            # Рисуем название цвета
            draw.text((x + 5, y + square_size + 5), color_info['code'], fill="black", font=font)

            # Обновляем координаты для следующего квадрата
            x += square_size + padding
            if x + square_size > image_width:
                x = padding
                y += square_size + padding + 50 # 20 - высота текста
            # Проверка превышения высоты
            if y + square_size > image_height:
                break  # Прекращаем, если не хватает места
        y += square_size + padding + 50
        x = padding    
    # Преобразуем множество в список и возвращаем его
    return image