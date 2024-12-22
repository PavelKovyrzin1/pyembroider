import numpy as np
import cv2

QUOTIENT = 20
NORM = 255.0


async def find_noise_pixels(image, threshold: int = 150) -> np.array:
    img_array = np.array(image)

    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    abs_laplacian = np.abs(laplacian)

    discordant_pixels = np.where(abs_laplacian > threshold)
    coordinates = list(zip(discordant_pixels[1], discordant_pixels[0]))  # (x, y)

    return coordinates
