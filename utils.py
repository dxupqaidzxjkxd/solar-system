# -*- coding: utf-8 -*-
"""
Модуль вспомогательных функций для программы.
"""

import json
import os


def сохранить_данные(имя_файла, данные):
    """
    Сохраняет данные в JSON файл.
    
    Аргументы:
        имя_файла: имя файла для сохранения
        данные: данные для сохранения
    """
    with open(имя_файла, 'w', encoding='utf-8') as файл:
        json.dump(данные, файл, ensure_ascii=False, indent=4)


def загрузить_данные(имя_файла):
    """
    Загружает данные из JSON файла.
    
    Аргументы:
        имя_файла: имя файла для загрузки
        
    Возвращает:
        Загруженные данные или None при ошибке
    """
    if not os.path.exists(имя_файла):
        return None
    
    try:
        with open(имя_файла, 'r', encoding='utf-8') as файл:
            return json.load(файл)
    except (json.JSONDecodeError, IOError):
        return None