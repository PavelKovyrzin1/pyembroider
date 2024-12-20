import sqlite3
from typing import List, Tuple

from color_data import transformed_color_data


def create_database(db_name: str) -> None:
    """Создать базу данных и таблицу для цветов с пользователями."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_colors (
                user_id INTEGER,
                brand TEXT NOT NULL,
                color_code TEXT NOT NULL,
                PRIMARY KEY (user_id, brand, color_code)
            )
        ''')
        conn.commit()


async def check_user_color_exists(db_name: str, user_id: int, brand: str, color_code: str) -> bool:
    """Проверить наличие записи по user_id, бренду и коду цвета."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_colors WHERE user_id = ? AND brand = ? AND color_code = ?',
                       (user_id, brand, color_code))
        return cursor.fetchone() is not None


async def delete_user_color(db_name: str, user_id: int, brand: str, color_code: str) -> None:
    """Удалить запись о цвете пользователя по ID, бренду и коду цвета."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM user_colors WHERE user_id = ? AND brand = ? AND color_code = ?',
                       (user_id, brand, color_code))
        conn.commit()


async def add_user_color(db_name: str, user_id: int, brand: str, color_code: str) -> None:
    """Добавить запись о цвете, который пользователь добавил."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_colors (user_id, brand, color_code) VALUES (?, ?, ?)',
                       (user_id, brand, color_code))
        conn.commit()


async def get_user_colors(db_name: str, user_id: int) -> List[Tuple]:
    """Получить все цвета пользователя по его ID."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT brand, color_code FROM user_colors WHERE user_id = ?', (user_id,))
        colors = cursor.fetchall()
        return [transformed_color_data[color]['rgb'] for color in colors]


async def get_user_colors_by_brand(db_name: str, user_id: int, brand: str) -> List[Tuple]:
    """Получить все цвета пользователя по его ID."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT brand, color_code FROM user_colors WHERE user_id = ? AND brand = ?',
                       (user_id, brand))
        colors = cursor.fetchall()
        return colors
