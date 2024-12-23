import pytest
import asyncio
from PIL import Image

from src.color_data import floss_colors, color_groups, RGB
from src.pixelate import pixelate

#Проверка, что получаем стабильное изображение

DIAMETER_RGB = (255 ** 2 + 255 ** 2 + 255 ** 2) ** 0.5

@pytest.mark.asyncio
async def test_image_pixelation():
    # Загрузка изображения
    image_path = "../resources/images/wide.jpg"
    loaded_image = Image.open(image_path)

    # Асинхронный вызов функции пикселизации
    for compression in range(15, 100, 30):
        images = []
        width, height = [0, 0]
        pixel_size = 0

        # Генерируем 10 изображений с одинаковыми параметрами
        for n in range(10):
            image = await pixelate(image=loaded_image, available_colors=RGB, percent=compression)
            width, height = image[0].size
            pixel_size = image[1]
            images.append(image[0])

        max_dist = 0
        dist = 0

        for first in range(10):
            for second in range(first + 1, 10):
                dist = 0
                for y in range(height):
                    for x in range(width):
                        # Получаем значение пикселя (R, G, B)
                        r1, g1, b1 = images[first].getpixel((x, y))
                        r2, g2, b2 = images[second].getpixel((x, y))
                        dist += ((r1 - r2) * 2 + (g1 - g2) * 2 + (b1 - b2) * 2) * 0.5

                max_dist = max(dist, max_dist)
        # Проверяем, что на сумма расстояний между изображениями не больше чем диаметр RGB пространства
        assert DIAMETER_RGB > (max_dist / (pixel_size ** 4))

# Запуск тестов с помощью pytest
if __name__ == "__main__":
    asyncio.run(test_image_pixelation())
