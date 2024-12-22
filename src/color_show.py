from PIL import Image, ImageDraw, ImageFont
from color_data import floss_colors

COLS = 7
PADDING = 10
TEXT_HEIGHT = 60
TEXT_OFFSET = 5
FONT_SIZE = 15


async def show_color(brand: str, color_name: str, size: tuple = (200, 200)) -> Image:
    """
    Создает изображение заданного цвета.
    
    Args:
        brand (str): Бренд нити (например, 'DMC', 'Anchor', 'Cosmo')
        color_name (str): Название цвета
        size (tuple): Размер изображения в пикселях (ширина, высота)
    
    Returns:
        Image: Объект изображения PIL
    """
    try:
        # Получаем RGB значения цвета из базы данных
        color_data = floss_colors[brand][color_name]
        rgb_color = color_data['rgb']

        # Создаем новое изображение заданного размера
        img = Image.new('RGB', size, rgb_color)

        return img

    except KeyError:
        raise ValueError(f"Цвет '{color_name}' бренда '{brand}' не найден в базе данных")


async def create_color_grid(brand: str, colors: list, output_path: str, cell_size: int = 200) -> Image:
    """
    Создает сетку с образцами цветов и их описанием.
    
    Args:
        brand (str): Бренд нити
        colors (list): Список словарей с информацией о цветах
        output_path (str): Путь для сохранения файла
        cell_size (int): Размер одной ячейки в пикселях
    """
    # Определяем количество столбцов и строк
    rows = (len(colors) + COLS - 1) // COLS  # Округление вверх

    # Создаем новое изображение
    cell_height = cell_size + TEXT_HEIGHT + PADDING
    img_width = COLS * (cell_size + PADDING) + PADDING
    img_height = rows * cell_height + PADDING

    # Создаем белое изображение
    img = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default(size=FONT_SIZE)

    # Размещаем цвета в сетке
    for i, color_info in enumerate(colors):
        row = i // COLS
        col = i % COLS

        # Координаты для цветного квадрата
        x = col * (cell_size + PADDING) + PADDING
        y = row * cell_height + PADDING

        # Создаем цветной квадрат
        color_square = Image.new('RGB', (cell_size, cell_size), color_info['rgb'])
        img.paste(color_square, (x, y))

        # Добавляем текст под квадратом
        text_y = y + cell_size + TEXT_OFFSET
        text = f"{color_info['name']}\nCode: {color_info['code']}"
        draw.text((x, text_y), text, fill='black', font=font)

    # Сохраняем изображение
    img.save(output_path)
    return img


async def save_color_sample(brand: str, color_name: str, output_path: str, size: tuple = (200, 200)) -> None:
    """
    Создает и сохраняет образец цвета в файл.
    
    Args:
        brand (str): Бренд нити
        color_name (str): Название цвета
        output_path (str): Путь для сохранения файла
        size (tuple): Размер изображения в пикселях
    """
    img = show_color(brand, color_name, size)
    img.save(output_path)
