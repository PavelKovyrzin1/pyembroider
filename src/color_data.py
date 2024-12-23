"""
DMC color database containing color numbers, names, and RGB values.
Data sourced from https://lavkamasterovshop.ru/blog/poleznoe/tablitsa-sootvetstviya-tsvetov-muline/
"""

from enum import Enum


class Brands(Enum):
    DMC = "DMC"
    ANCHOR = "Anchor"
    COSMO = "Cosmo"


floss_colors = {
    Brands.DMC.value: {
        'Snow White': {'code': 'B5200', 'rgb': (255, 255, 255)},
        'White': {'code': 'White', 'rgb': (252, 251, 248)},
        'Ecru': {'code': 'ECRU', 'rgb': (240, 234, 218)},
        'Light Beige Gray': {'code': '822', 'rgb': (231, 226, 211)},
        'Medium Beige Gray': {'code': '644', 'rgb': (221, 216, 204)},
        'Dark Beige Gray': {'code': '642', 'rgb': (196, 190, 172)},
        'Very Dark Beige Gray': {'code': '640', 'rgb': (167, 159, 139)},
        'Ultra Very Light Mocha': {'code': '3866', 'rgb': (250, 246, 240)},
        'Very Light Mocha': {'code': '3865', 'rgb': (248, 247, 241)},
        'Light Mocha': {'code': '3864', 'rgb': (235, 234, 231)},
        'Medium Mocha': {'code': '3863', 'rgb': (207, 205, 201)},
        'Dark Mocha': {'code': '3862', 'rgb': (177, 171, 163)},
        'Very Dark Mocha': {'code': '3031', 'rgb': (75, 60, 42)},
        # Красные оттенки
        'Bright Red': {'code': '666', 'rgb': (227, 29, 66)},
        'Red': {'code': '321', 'rgb': (199, 43, 59)},
        'Medium Red': {'code': '304', 'rgb': (183, 31, 51)},
        'Dark Red': {'code': '498', 'rgb': (167, 19, 43)},
        'Very Dark Red': {'code': '816', 'rgb': (151, 11, 35)},
        'Garnet': {'code': '814', 'rgb': (123, 0, 27)},
        'Dark Garnet': {'code': '815', 'rgb': (135, 7, 31)},
        'Very Dark Garnet': {'code': '902', 'rgb': (130, 0, 27)},
        # Розовые оттенки
        'Ultra Very Light Dusty Rose': {'code': '963', 'rgb': (255, 215, 226)},
        'Very Light Dusty Rose': {'code': '3716', 'rgb': (255, 189, 202)},
        'Light Dusty Rose': {'code': '761', 'rgb': (255, 154, 172)},
        'Medium Dusty Rose': {'code': '760', 'rgb': (245, 173, 173)},
        'Dark Dusty Rose': {'code': '3328', 'rgb': (238, 84, 110)},
        'Very Dark Dusty Rose': {'code': '309', 'rgb': (214, 43, 91)},
        # Оранжевые оттенки
        'Light Pumpkin': {'code': '970', 'rgb': (247, 139, 19)},
        'Pumpkin': {'code': '971', 'rgb': (246, 127, 0)},
        'Deep Pumpkin': {'code': '972', 'rgb': (247, 127, 0)},
        'Bright Pumpkin': {'code': '973', 'rgb': (255, 131, 0)},
        'Burnt Orange': {'code': '947', 'rgb': (255, 123, 0)},
        'Dark Burnt Orange': {'code': '946', 'rgb': (235, 99, 7)},
        # Желтые оттенки
        'Light Yellow': {'code': '743', 'rgb': (255, 231, 147)},
        'Pale Yellow': {'code': '744', 'rgb': (255, 214, 0)},
        'Light Pale Yellow': {'code': '745', 'rgb': (255, 233, 0)},
        'Deep Canary': {'code': '972', 'rgb': (255, 181, 0)},
        'Topaz': {'code': '726', 'rgb': (253, 215, 85)},
        'Light Topaz': {'code': '727', 'rgb': (255, 241, 175)},
        # Зеленые оттенки
        'Very Light Jade': {'code': '564', 'rgb': (167, 205, 175)},
        'Light Jade': {'code': '563', 'rgb': (143, 192, 152)},
        'Medium Jade': {'code': '562', 'rgb': (83, 151, 106)},
        'Dark Jade': {'code': '505', 'rgb': (51, 131, 98)},
        'Very Dark Jade': {'code': '895', 'rgb': (35, 113, 82)},
        'Forest Green': {'code': '890', 'rgb': (23, 73, 35)},
        'Dark Forest Green': {'code': '898', 'rgb': (27, 83, 0)},
        # Синие оттенки
        'Very Light Blue': {'code': '827', 'rgb': (189, 221, 237)},
        'Light Blue': {'code': '813', 'rgb': (161, 194, 215)},
        'Medium Blue': {'code': '826', 'rgb': (107, 158, 191)},
        'Dark Blue': {'code': '825', 'rgb': (71, 129, 165)},
        'Very Dark Blue': {'code': '824', 'rgb': (57, 105, 135)},
        'Navy Blue': {'code': '336', 'rgb': (37, 59, 115)},
        'Very Dark Navy Blue': {'code': '823', 'rgb': (33, 48, 99)},
        # Фиолетовые оттенки
        'Very Light Blue Violet': {'code': '3747', 'rgb': (211, 200, 232)},
        'Light Blue Violet': {'code': '3746', 'rgb': (188, 177, 213)},
        'Medium Blue Violet': {'code': '3745', 'rgb': (163, 151, 191)},
        'Dark Blue Violet': {'code': '3744', 'rgb': (132, 115, 175)},
        'Very Dark Blue Violet': {'code': '333', 'rgb': (102, 73, 157)},
        'Ultra Dark Blue Violet': {'code': '208', 'rgb': (72, 47, 109)},
        # Черные и серые оттенки
        'Black': {'code': '310', 'rgb': (0, 0, 0)},
        'Light Gray': {'code': '762', 'rgb': (219, 219, 219)},
        'Medium Gray': {'code': '415', 'rgb': (180, 180, 180)},
        'Dark Gray': {'code': '413', 'rgb': (128, 128, 128)},
        'Very Dark Gray': {'code': '414', 'rgb': (90, 90, 90)}
    },

    Brands.ANCHOR.value: {
        # Базовые цвета
        'White': {'code': '1', 'rgb': (255, 255, 255)},
        'Black': {'code': '403', 'rgb': (0, 0, 0)},
        'Ecru': {'code': '387', 'rgb': (240, 234, 218)},
        # Красные
        'Christmas Red': {'code': '46', 'rgb': (227, 29, 66)},
        'Cardinal Red': {'code': '47', 'rgb': (199, 43, 59)},
        'Ruby Red': {'code': '48', 'rgb': (183, 31, 51)},
        # Розовые
        'Baby Pink': {'code': '23', 'rgb': (255, 215, 226)},
        'Shell Pink': {'code': '24', 'rgb': (255, 189, 202)},
        'Rose Pink': {'code': '25', 'rgb': (255, 154, 172)},
        # Оранжевые
        'Light Orange': {'code': '304', 'rgb': (246, 127, 0)},
        'Tangerine': {'code': '305', 'rgb': (255, 131, 0)},
        'Pumpkin': {'code': '306', 'rgb': (235, 99, 7)},
        # Желтые
        'Lemon Yellow': {'code': '290', 'rgb': (255, 214, 0)},
        'Canary Yellow': {'code': '291', 'rgb': (255, 233, 0)},
        'Golden Yellow': {'code': '292', 'rgb': (255, 181, 0)},
        # Зеленые
        'Mint Green': {'code': '226', 'rgb': (83, 151, 106)},
        'Forest Green': {'code': '227', 'rgb': (51, 131, 98)},
        'Dark Green': {'code': '228', 'rgb': (35, 113, 82)},
        # Синие
        'Sky Blue': {'code': '128', 'rgb': (161, 194, 215)},
        'Medium Blue': {'code': '129', 'rgb': (107, 158, 191)},
        'Dark Blue': {'code': '130', 'rgb': (71, 129, 165)},
        # Фиолетовые
        'Light Violet': {'code': '110', 'rgb': (163, 151, 191)},
        'Medium Violet': {'code': '111', 'rgb': (132, 115, 175)},
        'Dark Violet': {'code': '112', 'rgb': (102, 73, 157)}
    },

    Brands.COSMO.value: {
        # Базовые цвета
        'White': {'code': '0000', 'rgb': (255, 255, 255)},
        'Black': {'code': '0500', 'rgb': (0, 0, 0)},
        'Ecru': {'code': '0100', 'rgb': (240, 234, 218)},
        # Красные
        'Bright Red': {'code': '600', 'rgb': (227, 29, 66)},
        'Christmas Red': {'code': '601', 'rgb': (199, 43, 59)},
        'Dark Red': {'code': '602', 'rgb': (183, 31, 51)},
        # Розовые
        'Light Pink': {'code': '700', 'rgb': (255, 215, 226)},
        'Medium Pink': {'code': '701', 'rgb': (255, 189, 202)},
        'Dark Pink': {'code': '702', 'rgb': (255, 154, 172)},
        # Оранжевые
        'Light Orange': {'code': '800', 'rgb': (246, 127, 0)},
        'Medium Orange': {'code': '801', 'rgb': (255, 131, 0)},
        'Dark Orange': {'code': '802', 'rgb': (235, 99, 7)},
        # Желтые
        'Light Yellow': {'code': '900', 'rgb': (255, 214, 0)},
        'Medium Yellow': {'code': '901', 'rgb': (255, 233, 0)},
        'Dark Yellow': {'code': '902', 'rgb': (255, 181, 0)},
        # Зеленые
        'Light Green': {'code': '1000', 'rgb': (83, 151, 106)},
        'Medium Green': {'code': '1001', 'rgb': (51, 131, 98)},
        'Dark Green': {'code': '1002', 'rgb': (35, 113, 82)},
        # Синие
        'Light Blue': {'code': '1100', 'rgb': (161, 194, 215)},
        'Medium Blue': {'code': '1101', 'rgb': (107, 158, 191)},
        'Dark Blue': {'code': '1102', 'rgb': (71, 129, 165)},
        # Фиолетовые
        'Light Purple': {'code': '1200', 'rgb': (163, 151, 191)},
        'Medium Purple': {'code': '1201', 'rgb': (132, 115, 175)},
        'Dark Purple': {'code': '1202', 'rgb': (102, 73, 157)}
    }
}

# Словарь для группировки цветов по ключевым словам
color_groups = {
    'Белые': ['White', 'Snow', 'Ecru', 'Beige', 'Mocha'],
    'Красные': ['Red', 'Garnet', 'Christmas', 'Cardinal', 'Ruby'],
    'Розовые': ['Pink', 'Rose', 'Dusty Rose'],
    'Оранжевые': ['Orange', 'Pumpkin', 'Tangerine', 'Burnt'],
    'Желтые': ['Yellow', 'Topaz', 'Canary', 'Lemon', 'Golden'],
    'Зеленые': ['Green', 'Jade', 'Forest', 'Mint'],
    'Синие': ['Blue', 'Navy', 'Sky'],
    'Фиолетовые': ['Violet', 'Purple'],
    'Серые': ['Gray'],
    'Черные': ['Black']
}

RGB = [(252, 251, 248), (161, 194, 215), (231, 226, 211), (130, 0, 27), (214, 43, 91), (167, 159, 139), (255, 241, 175),
       (167, 19, 43), (71, 129, 165), (57, 105, 135), (163, 151, 191), (196, 190, 172), (180, 180, 180), (255, 233, 0),
       (255, 215, 226), (255, 123, 0), (143, 192, 152), (128, 128, 128), (151, 11, 35), (37, 59, 115), (167, 205, 175),
       (245, 173, 173), (23, 73, 35), (255, 255, 255), (255, 131, 0), (240, 234, 218), (183, 31, 51), (235, 99, 7),
       (75, 60, 42), (177, 171, 163), (135, 7, 31), (189, 221, 237), (221, 216, 204), (247, 127, 0), (83, 151, 106),
       (33, 48, 99), (248, 247, 241), (132, 115, 175), (0, 0, 0), (107, 158, 191), (211, 200, 232), (199, 43, 59),
       (27, 83, 0), (255, 181, 0), (255, 214, 0), (255, 154, 172), (72, 47, 109), (207, 205, 201), (238, 84, 110),
       (227, 29, 66), (255, 231, 147), (255, 189, 202), (235, 234, 231), (219, 219, 219), (188, 177, 213),
       (253, 215, 85), (247, 139, 19), (102, 73, 157), (51, 131, 98), (35, 113, 82), (250, 246, 240), (90, 90, 90),
       (123, 0, 27), (246, 127, 0)]

RGB_codes = {(252, 251, 248): 1, (161, 194, 215): 2, (231, 226, 211): 3, (130, 0, 27): 4, (214, 43, 91): 5,
             (167, 159, 139): 6, (255, 241, 175): 7, (167, 19, 43): 8, (71, 129, 165): 9, (57, 105, 135): 10,
             (163, 151, 191): 11, (196, 190, 172): 12, (180, 180, 180): 13, (255, 233, 0): 14, (255, 215, 226): 15,
             (255, 123, 0): 16, (143, 192, 152): 17, (128, 128, 128): 18, (151, 11, 35): 19, (37, 59, 115): 20,
             (167, 205, 175): 21, (245, 173, 173): 22, (23, 73, 35): 23, (255, 255, 255): 24, (255, 131, 0): 25,
             (240, 234, 218): 26, (183, 31, 51): 27, (235, 99, 7): 28, (75, 60, 42): 29, (177, 171, 163): 30,
             (135, 7, 31): 31, (189, 221, 237): 32, (221, 216, 204): 33, (247, 127, 0): 34, (83, 151, 106): 35,
             (33, 48, 99): 36, (248, 247, 241): 37, (132, 115, 175): 38, (0, 0, 0): 39, (107, 158, 191): 40,
             (211, 200, 232): 41, (199, 43, 59): 42, (27, 83, 0): 43, (255, 181, 0): 44, (255, 214, 0): 45,
             (255, 154, 172): 46, (72, 47, 109): 47, (207, 205, 201): 48, (238, 84, 110): 49, (227, 29, 66): 50,
             (255, 231, 147): 51, (255, 189, 202): 52, (235, 234, 231): 53, (219, 219, 219): 54, (188, 177, 213): 55,
             (253, 215, 85): 56, (247, 139, 19): 57, (102, 73, 157): 58, (51, 131, 98): 59, (35, 113, 82): 60,
             (250, 246, 240): 61, (90, 90, 90): 62, (123, 0, 27): 63, (246, 127, 0): 64}

transformed_color_data = {(Brands.DMC.value, 'B5200'): {'name': 'Snow White', 'code': 'B5200', 'rgb': (255, 255, 255)},
                          (Brands.DMC.value, 'White'): {'name': 'White', 'code': 'White', 'rgb': (252, 251, 248)},
                          (Brands.DMC.value, 'ECRU'): {'name': 'Ecru', 'code': 'ECRU', 'rgb': (240, 234, 218)},
                          (Brands.DMC.value, '822'): {'name': 'Light Beige Gray', 'code': '822',
                                                      'rgb': (231, 226, 211)},
                          (Brands.DMC.value, '644'): {'name': 'Medium Beige Gray', 'code': '644',
                                                      'rgb': (221, 216, 204)},
                          (Brands.DMC.value, '642'): {'name': 'Dark Beige Gray', 'code': '642', 'rgb': (196, 190, 172)},
                          (Brands.DMC.value, '640'): {'name': 'Very Dark Beige Gray', 'code': '640',
                                                      'rgb': (167, 159, 139)},
                          (Brands.DMC.value, '3866'): {'name': 'Ultra Very Light Mocha', 'code': '3866',
                                                       'rgb': (250, 246, 240)},
                          (Brands.DMC.value, '3865'): {'name': 'Very Light Mocha', 'code': '3865',
                                                       'rgb': (248, 247, 241)},
                          (Brands.DMC.value, '3864'): {'name': 'Light Mocha', 'code': '3864', 'rgb': (235, 234, 231)},
                          (Brands.DMC.value, '3863'): {'name': 'Medium Mocha', 'code': '3863', 'rgb': (207, 205, 201)},
                          (Brands.DMC.value, '3862'): {'name': 'Dark Mocha', 'code': '3862', 'rgb': (177, 171, 163)},
                          (Brands.DMC.value, '3031'): {'name': 'Very Dark Mocha', 'code': '3031', 'rgb': (75, 60, 42)},
                          (Brands.DMC.value, '666'): {'name': 'Bright Red', 'code': '666', 'rgb': (227, 29, 66)},
                          (Brands.DMC.value, '321'): {'name': 'Red', 'code': '321', 'rgb': (199, 43, 59)},
                          (Brands.DMC.value, '304'): {'name': 'Medium Red', 'code': '304', 'rgb': (183, 31, 51)},
                          (Brands.DMC.value, '498'): {'name': 'Dark Red', 'code': '498', 'rgb': (167, 19, 43)},
                          (Brands.DMC.value, '816'): {'name': 'Very Dark Red', 'code': '816', 'rgb': (151, 11, 35)},
                          (Brands.DMC.value, '814'): {'name': 'Garnet', 'code': '814', 'rgb': (123, 0, 27)},
                          (Brands.DMC.value, '815'): {'name': 'Dark Garnet', 'code': '815', 'rgb': (135, 7, 31)},
                          (Brands.DMC.value, '902'): {'name': 'Very Dark Garnet', 'code': '902', 'rgb': (130, 0, 27)},
                          (Brands.DMC.value, '963'): {'name': 'Ultra Very Light Dusty Rose', 'code': '963',
                                                      'rgb': (255, 215, 226)},
                          (Brands.DMC.value, '3716'): {'name': 'Very Light Dusty Rose', 'code': '3716',
                                                       'rgb': (255, 189, 202)},
                          (Brands.DMC.value, '761'): {'name': 'Light Dusty Rose', 'code': '761',
                                                      'rgb': (255, 154, 172)},
                          (Brands.DMC.value, '760'): {'name': 'Medium Dusty Rose', 'code': '760',
                                                      'rgb': (245, 173, 173)},
                          (Brands.DMC.value, '3328'): {'name': 'Dark Dusty Rose', 'code': '3328',
                                                       'rgb': (238, 84, 110)},
                          (Brands.DMC.value, '309'): {'name': 'Very Dark Dusty Rose', 'code': '309',
                                                      'rgb': (214, 43, 91)},
                          (Brands.DMC.value, '970'): {'name': 'Light Pumpkin', 'code': '970', 'rgb': (247, 139, 19)},
                          (Brands.DMC.value, '971'): {'name': 'Pumpkin', 'code': '971', 'rgb': (246, 127, 0)},
                          (Brands.DMC.value, '972'): {'name': 'Deep Canary', 'code': '972', 'rgb': (255, 181, 0)},
                          (Brands.DMC.value, '973'): {'name': 'Bright Pumpkin', 'code': '973', 'rgb': (255, 131, 0)},
                          (Brands.DMC.value, '947'): {'name': 'Burnt Orange', 'code': '947', 'rgb': (255, 123, 0)},
                          (Brands.DMC.value, '946'): {'name': 'Dark Burnt Orange', 'code': '946', 'rgb': (235, 99, 7)},
                          (Brands.DMC.value, '743'): {'name': 'Light Yellow', 'code': '743', 'rgb': (255, 231, 147)},
                          (Brands.DMC.value, '744'): {'name': 'Pale Yellow', 'code': '744', 'rgb': (255, 214, 0)},
                          (Brands.DMC.value, '745'): {'name': 'Light Pale Yellow', 'code': '745', 'rgb': (255, 233, 0)},
                          (Brands.DMC.value, '726'): {'name': 'Topaz', 'code': '726', 'rgb': (253, 215, 85)},
                          (Brands.DMC.value, '727'): {'name': 'Light Topaz', 'code': '727', 'rgb': (255, 241, 175)},
                          (Brands.DMC.value, '564'): {'name': 'Very Light Jade', 'code': '564', 'rgb': (167, 205, 175)},
                          (Brands.DMC.value, '563'): {'name': 'Light Jade', 'code': '563', 'rgb': (143, 192, 152)},
                          (Brands.DMC.value, '562'): {'name': 'Medium Jade', 'code': '562', 'rgb': (83, 151, 106)},
                          (Brands.DMC.value, '505'): {'name': 'Dark Jade', 'code': '505', 'rgb': (51, 131, 98)},
                          (Brands.DMC.value, '895'): {'name': 'Very Dark Jade', 'code': '895', 'rgb': (35, 113, 82)},
                          (Brands.DMC.value, '890'): {'name': 'Forest Green', 'code': '890', 'rgb': (23, 73, 35)},
                          (Brands.DMC.value, '898'): {'name': 'Dark Forest Green', 'code': '898', 'rgb': (27, 83, 0)},
                          (Brands.DMC.value, '827'): {'name': 'Very Light Blue', 'code': '827', 'rgb': (189, 221, 237)},
                          (Brands.DMC.value, '813'): {'name': 'Light Blue', 'code': '813', 'rgb': (161, 194, 215)},
                          (Brands.DMC.value, '826'): {'name': 'Medium Blue', 'code': '826', 'rgb': (107, 158, 191)},
                          (Brands.DMC.value, '825'): {'name': 'Dark Blue', 'code': '825', 'rgb': (71, 129, 165)},
                          (Brands.DMC.value, '824'): {'name': 'Very Dark Blue', 'code': '824', 'rgb': (57, 105, 135)},
                          (Brands.DMC.value, '336'): {'name': 'Navy Blue', 'code': '336', 'rgb': (37, 59, 115)},
                          (Brands.DMC.value, '823'): {'name': 'Very Dark Navy Blue', 'code': '823',
                                                      'rgb': (33, 48, 99)},
                          (Brands.DMC.value, '3747'): {'name': 'Very Light Blue Violet', 'code': '3747',
                                                       'rgb': (211, 200, 232)},
                          (Brands.DMC.value, '3746'): {'name': 'Light Blue Violet', 'code': '3746',
                                                       'rgb': (188, 177, 213)},
                          (Brands.DMC.value, '3745'): {'name': 'Medium Blue Violet', 'code': '3745',
                                                       'rgb': (163, 151, 191)},
                          (Brands.DMC.value, '3744'): {'name': 'Dark Blue Violet', 'code': '3744',
                                                       'rgb': (132, 115, 175)},
                          (Brands.DMC.value, '333'): {'name': 'Very Dark Blue Violet', 'code': '333',
                                                      'rgb': (102, 73, 157)},
                          (Brands.DMC.value, '208'): {'name': 'Ultra Dark Blue Violet', 'code': '208',
                                                      'rgb': (72, 47, 109)},
                          (Brands.DMC.value, '310'): {'name': 'Black', 'code': '310', 'rgb': (0, 0, 0)},
                          (Brands.DMC.value, '762'): {'name': 'Light Gray', 'code': '762', 'rgb': (219, 219, 219)},
                          (Brands.DMC.value, '415'): {'name': 'Medium Gray', 'code': '415', 'rgb': (180, 180, 180)},
                          (Brands.DMC.value, '413'): {'name': 'Dark Gray', 'code': '413', 'rgb': (128, 128, 128)},
                          (Brands.DMC.value, '414'): {'name': 'Very Dark Gray', 'code': '414', 'rgb': (90, 90, 90)},
                          (Brands.ANCHOR.value, '1'): {'name': 'White', 'code': '1', 'rgb': (255, 255, 255)},
                          (Brands.ANCHOR.value, '403'): {'name': 'Black', 'code': '403', 'rgb': (0, 0, 0)},
                          (Brands.ANCHOR.value, '387'): {'name': 'Ecru', 'code': '387', 'rgb': (240, 234, 218)},
                          (Brands.ANCHOR.value, '46'): {'name': 'Christmas Red', 'code': '46', 'rgb': (227, 29, 66)},
                          (Brands.ANCHOR.value, '47'): {'name': 'Cardinal Red', 'code': '47', 'rgb': (199, 43, 59)},
                          (Brands.ANCHOR.value, '48'): {'name': 'Ruby Red', 'code': '48', 'rgb': (183, 31, 51)},
                          (Brands.ANCHOR.value, '23'): {'name': 'Baby Pink', 'code': '23', 'rgb': (255, 215, 226)},
                          (Brands.ANCHOR.value, '24'): {'name': 'Shell Pink', 'code': '24', 'rgb': (255, 189, 202)},
                          (Brands.ANCHOR.value, '25'): {'name': 'Rose Pink', 'code': '25', 'rgb': (255, 154, 172)},
                          (Brands.ANCHOR.value, '304'): {'name': 'Light Orange', 'code': '304', 'rgb': (246, 127, 0)},
                          (Brands.ANCHOR.value, '305'): {'name': 'Tangerine', 'code': '305', 'rgb': (255, 131, 0)},
                          (Brands.ANCHOR.value, '306'): {'name': 'Pumpkin', 'code': '306', 'rgb': (235, 99, 7)},
                          (Brands.ANCHOR.value, '290'): {'name': 'Lemon Yellow', 'code': '290', 'rgb': (255, 214, 0)},
                          (Brands.ANCHOR.value, '291'): {'name': 'Canary Yellow', 'code': '291', 'rgb': (255, 233, 0)},
                          (Brands.ANCHOR.value, '292'): {'name': 'Golden Yellow', 'code': '292', 'rgb': (255, 181, 0)},
                          (Brands.ANCHOR.value, '226'): {'name': 'Mint Green', 'code': '226', 'rgb': (83, 151, 106)},
                          (Brands.ANCHOR.value, '227'): {'name': 'Forest Green', 'code': '227', 'rgb': (51, 131, 98)},
                          (Brands.ANCHOR.value, '228'): {'name': 'Dark Green', 'code': '228', 'rgb': (35, 113, 82)},
                          (Brands.ANCHOR.value, '128'): {'name': 'Sky Blue', 'code': '128', 'rgb': (161, 194, 215)},
                          (Brands.ANCHOR.value, '129'): {'name': 'Medium Blue', 'code': '129', 'rgb': (107, 158, 191)},
                          (Brands.ANCHOR.value, '130'): {'name': 'Dark Blue', 'code': '130', 'rgb': (71, 129, 165)},
                          (Brands.ANCHOR.value, '110'): {'name': 'Light Violet', 'code': '110', 'rgb': (163, 151, 191)},
                          (Brands.ANCHOR.value, '111'): {'name': 'Medium Violet', 'code': '111',
                                                         'rgb': (132, 115, 175)},
                          (Brands.ANCHOR.value, '112'): {'name': 'Dark Violet', 'code': '112', 'rgb': (102, 73, 157)},
                          (Brands.COSMO.value, '0000'): {'name': 'White', 'code': '0000', 'rgb': (255, 255, 255)},
                          (Brands.COSMO.value, '0500'): {'name': 'Black', 'code': '0500', 'rgb': (0, 0, 0)},
                          (Brands.COSMO.value, '0100'): {'name': 'Ecru', 'code': '0100', 'rgb': (240, 234, 218)},
                          (Brands.COSMO.value, '600'): {'name': 'Bright Red', 'code': '600', 'rgb': (227, 29, 66)},
                          (Brands.COSMO.value, '601'): {'name': 'Christmas Red', 'code': '601', 'rgb': (199, 43, 59)},
                          (Brands.COSMO.value, '602'): {'name': 'Dark Red', 'code': '602', 'rgb': (183, 31, 51)},
                          (Brands.COSMO.value, '700'): {'name': 'Light Pink', 'code': '700', 'rgb': (255, 215, 226)},
                          (Brands.COSMO.value, '701'): {'name': 'Medium Pink', 'code': '701', 'rgb': (255, 189, 202)},
                          (Brands.COSMO.value, '702'): {'name': 'Dark Pink', 'code': '702', 'rgb': (255, 154, 172)},
                          (Brands.COSMO.value, '800'): {'name': 'Light Orange', 'code': '800', 'rgb': (246, 127, 0)},
                          (Brands.COSMO.value, '801'): {'name': 'Medium Orange', 'code': '801', 'rgb': (255, 131, 0)},
                          (Brands.COSMO.value, '802'): {'name': 'Dark Orange', 'code': '802', 'rgb': (235, 99, 7)},
                          (Brands.COSMO.value, '900'): {'name': 'Light Yellow', 'code': '900', 'rgb': (255, 214, 0)},
                          (Brands.COSMO.value, '901'): {'name': 'Medium Yellow', 'code': '901', 'rgb': (255, 233, 0)},
                          (Brands.COSMO.value, '902'): {'name': 'Dark Yellow', 'code': '902', 'rgb': (255, 181, 0)},
                          (Brands.COSMO.value, '1000'): {'name': 'Light Green', 'code': '1000', 'rgb': (83, 151, 106)},
                          (Brands.COSMO.value, '1001'): {'name': 'Medium Green', 'code': '1001', 'rgb': (51, 131, 98)},
                          (Brands.COSMO.value, '1002'): {'name': 'Dark Green', 'code': '1002', 'rgb': (35, 113, 82)},
                          (Brands.COSMO.value, '1100'): {'name': 'Light Blue', 'code': '1100', 'rgb': (161, 194, 215)},
                          (Brands.COSMO.value, '1101'): {'name': 'Medium Blue', 'code': '1101', 'rgb': (107, 158, 191)},
                          (Brands.COSMO.value, '1102'): {'name': 'Dark Blue', 'code': '1102', 'rgb': (71, 129, 165)},
                          (Brands.COSMO.value, '1200'): {'name': 'Light Purple', 'code': '1200',
                                                         'rgb': (163, 151, 191)},
                          (Brands.COSMO.value, '1201'): {'name': 'Medium Purple', 'code': '1201',
                                                         'rgb': (132, 115, 175)},
                          (Brands.COSMO.value, '1202'): {'name': 'Dark Purple', 'code': '1202', 'rgb': (102, 73, 157)}}
