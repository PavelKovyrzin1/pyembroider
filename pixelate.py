from PIL import Image


def closest_color(requested_color, available_colors):
    """
    Находит ближайший цвет из списка available_colors для заданного цвета requested_color.
    """
    r, g, b = requested_color
    closest_color = min(available_colors, key=lambda color: (color[0] - r) ** 2 + (color[1] - g) ** 2 + (color[2] - b) ** 2)
    return closest_color


def pixelate(image, available_colors, pixel_size=9):
    margin_color = (0, 0, 0)

    # Уменьшение и увеличение изображения для пикселизации
    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)

    # Подбор цвета
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            current_color = image.getpixel((x, y))
            new_color = closest_color(current_color, available_colors)
            image.putpixel((x, y), new_color)

    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()

    # Рисуем черную границу между пикселями
    for i in range(0, image.size[0], pixel_size):
        for j in range(0, image.size[1], pixel_size):
            for r in range(pixel_size):
                if i + r < image.size[0] and j < image.size[1]:
                    pixel[i + r, j] = margin_color
                if i < image.size[0] and j + r < image.size[1]:
                    pixel[i, j + r] = margin_color

    return image
