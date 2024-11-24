from PIL import Image
def pixelate(image, pixel_size=9, draw_margin=True):
    margin_color = (0, 0, 0)

    # Уменьшение и увеличение изображения для пикселизации
    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()

    # Рисуем черную границу между пикселями
    if draw_margin:
        for i in range(0, image.size[0], pixel_size):
            for j in range(0, image.size[1], pixel_size):
                for r in range(pixel_size):
                    if i + r < image.size[0] and j < image.size[1]:
                        pixel[i + r, j] = margin_color
                    if i < image.size[0] and j + r < image.size[1]:
                        pixel[i, j + r] = margin_color

    return image