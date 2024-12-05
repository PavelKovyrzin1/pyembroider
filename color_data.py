"""
DMC color database containing color numbers, names, and RGB values.
Data sourced from https://lavkamasterovshop.ru/blog/poleznoe/tablitsa-sootvetstviya-tsvetov-muline/
"""

floss_colors = {
    'DMC': {
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

    'Anchor': {
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

    'Cosmo': {
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
