from PIL import Image, ImageDraw, ImageFont
from color_data import floss_colors

def show_color(brand: str, color_name: str, size: tuple = (200, 200)) -> Image:
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

def create_color_grid(brand: str, colors: list, output_path: str, cell_size: int = 100):
    """
    Создает сетку с образцами цветов и их описанием.
    
    Args:
        brand (str): Бренд нити
        colors (list): Список словарей с информацией о цветах
        output_path (str): Путь для сохранения файла
        cell_size (int): Размер одной ячейки в пикселях
    """
    # Определяем количество столбцов и строк
    cols = 3  # Фиксированное количество столбцов
    rows = (len(colors) + cols - 1) // cols  # Округление вверх
    
    # Создаем новое изображение
    padding = 10
    text_height = 40
    cell_height = cell_size + text_height + padding
    img_width = cols * (cell_size + padding) + padding
    img_height = rows * cell_height + padding
    
    # Создаем белое изображение
    img = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(img)
    
    try:
        # Попытка загрузить шрифт
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
    except:
        # Если шрифт не найден, используем стандартный
        font = ImageFont.load_default()
    
    # Размещаем цвета в сетке
    for i, color_info in enumerate(colors):
        row = i // cols
        col = i % cols
        
        # Координаты для цветного квадрата
        x = col * (cell_size + padding) + padding
        y = row * cell_height + padding
        
        # Создаем цветной квадрат
        color_square = Image.new('RGB', (cell_size, cell_size), color_info['rgb'])
        img.paste(color_square, (x, y))
        
        # Добавляем текст под квадратом
        text_y = y + cell_size + 5
        text = f"{color_info['name']}\nКод: {color_info['code']}"
        draw.text((x, text_y), text, fill='black', font=font)
    
    # Сохраняем изображение
    img.save(output_path)
    return img

def save_color_sample(brand: str, color_name: str, output_path: str, size: tuple = (200, 200)):
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

# Пример использования:
if __name__ == "__main__":
    # Показать образец красного цвета DMC
    save_color_sample('DMC', 'Bright Red', 'color_sample.png')