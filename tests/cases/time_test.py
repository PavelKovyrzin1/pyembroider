import pytest
import asyncio
import time
from typing import List, Tuple
from PIL import Image

from src.color_data import floss_colors, color_groups, RGB
from src.pixelate import pixelate


@pytest.mark.asyncio
async def main():
    image_path = "../resources/images/цветок.jpg"
    loaded_image = Image.open(image_path)
    universal_colors: List[Tuple[int, int, int]] = [
        (252, 251, 248),
        (214, 43, 91),
        (57, 105, 135),
        (130, 0, 27),
        (255, 215, 226)
    ]

    for compression in range(15, 100):
        start_time = time.time()
        image = await pixelate(image=loaded_image, available_colors=RGB, percent=compression)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Сжатие: {compression}. Время выполнения функции: {execution_time} секунд")


if __name__ == "__main__":
    asyncio.run(main())
