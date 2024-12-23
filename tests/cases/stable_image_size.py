import pytest
import asyncio
from PIL import Image

from src.color_data import floss_colors, color_groups, RGB
from src.pixelate import pixelate

#Проверка, что получаем одинаковый размер изображения

DIAMETER_RGB = (255 ** 2 + 255 ** 2 + 255 ** 2) ** 0.5

@pytest.mark.asyncio
async def test_image_pixelation():
    # Загрузка изображения
    image_path = "../resources/images/цветок.jpg"
    loaded_image = Image.open(image_path)

    # Асинхронный вызов функции пикселизации
    for compression in range(15, 100, 30):
        image_size = [0, 0]
        # Генерируем 10 изображений с одинаковыми параметрами
        for n in range(10):
            image = await pixelate(image=loaded_image, available_colors=RGB, percent=compression)
            if n == 0:
                image_size = image[0].size
            else:
                assert image[0].size == image_size

# Запуск тестов с помощью pytest
if __name__ == "__main__":
    asyncio.run(test_image_pixelation())
