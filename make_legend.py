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
    square_size = 100  # размер квадрата
    padding = 10       # отступ между квадратами
    image_width = 800  # ширина изображения
    image_height = 600  # высота изображения

    # Создание нового изображения
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Шрифт для текста
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        font = ImageFont.load_default()

    # Рисуем квадраты с цветами и их названиями
    x, y = padding, padding
    for color_name, color_info in floss_colors['DMC'].items():
        rgb = color_info['rgb']
        if not rgb in unique_colors:
            continue
        # Рисуем цветной квадрат
        draw.rectangle([x, y, x + square_size, y + square_size], fill=rgb)

        # Рисуем название цвета
        draw.text((x + 5, y + square_size + 5), color_name, fill="black", font=font)

        # Обновляем координаты для следующего квадрата
        x += square_size + padding
        if x + square_size > image_width:
            x = padding
            y += square_size + padding + 20  # 20 - высота текста
        
        # Проверка превышения высоты
        if y + square_size > image_height:
            break  # Прекращаем, если не хватает места
    
    # Преобразуем множество в список и возвращаем его
    return image