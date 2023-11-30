# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 11:27:23 2022

@author: Roman Semenov
"""

''' 
Программа рассичитывает средние количество по продажам, выручке и ценам.
Показывает максимальное и минимальное значение, самый продаваемый товар, самый непопулярный товар. 
Всю статистику выводит в консоль и сохраняет в отдельный файл.

Для запуска требуется dataset с названием продукта, ценой и кол-вом продаж.

Пример рассчета:

Имеются данные о продажах некоторой аптеки:
    
    Товары проданные на неделе:
    
    1. Спазмалгон (300 руб, купили 10 раз), 
    2. Нурофн (500 руб, купили 6 раз), 
    3. Тизин (124 руб, купили 12 раз), 
    4. Назонекс (750 руб, купили 4 раза), 
    5. Грипферон (567 руб, купили 5 раз), 
    6. Боярышник (320 руб., купили 20 раз).
    
    Необходимо создать файл csv, который содержит название товара, стоимость и количество покупок.

Алгоритм скрипта:
    1. Импортировать модуль работы с csv - import csv;
    2. Создать список словарей с товарами;
    3. Записать новый файл с данными из списка словарей;
    4. Создать переменные - пустые списки, для записи данных из файла csv;
    4. Обратиться к файлу;
    5. Выполнить расчеты через функцию;
    6. Создать новый словарь, объеденив полученную статистику с новыми метками;
    8. Вывести словарь в консоль;
    7. Записать итог в отдельный файл csv.

'''


import csv # импортируем модуль


pharma_sales = [{'Товар': 'Спазмалгон', 'Цена': 300, 'Кол-во продаж': 10},
                {'Товар': 'Нурофен', 'Цена': 500, 'Кол-во продаж': 6},
                {'Товар': 'Тизин', 'Цена': 124, 'Кол-во продаж': 12},
                {'Товар': 'Назонекс', 'Цена': 750, 'Кол-во продаж': 4},
                {'Товар': 'Грипферон', 'Цена': 567, 'Кол-во продаж': 5},
                {'Товар': 'Боярышник', 'Цена': 320, 'Кол-во продаж': 20}] # создаем список словарей


with open ('pharma_sales.csv', 'w') as pharm_sales:
    headers = ['Товар', 'Цена', 'Кол-во продаж']
    pharm_sales_writer = csv.DictWriter(pharm_sales, fieldnames = headers)
    pharm_sales_writer.writeheader() # записываем заголовки
    for item in pharma_sales:
        pharm_sales_writer.writerow(item) # через цикл записываем строки данных 
        

list_of_product = [] 
list_of_price = []
list_of_sales = [] # объявляем пустые списки для записи значений


with open ('pharma_sales.csv', newline = '') as pharm_sales:
    pharm_sales_dict = csv.DictReader(pharm_sales)
    for row in pharm_sales_dict:
        list_of_product.append (str (row ['Товар']))
        list_of_price.append (int (row ['Цена']))
        list_of_sales.append (int (row ['Кол-во продаж'])) # записываем значения в пустые списки


def statistics (product, price, sales):
    
        mean_sales = sum (list_of_sales) / len (list_of_sales)
        mean_price = round (sum (list_of_price) / len (list_of_price), 2)
        max_revenue = max ([list_of_price[index] * list_of_sales[index]\
                        for index in range (len (list_of_product))])
        mean_revenue = round (sum ([list_of_price[index] * list_of_sales[index]\
                        for index in range (len (list_of_product))]) /\
                        len (list_of_product), 2)
        min_revenue = min ([list_of_price[index] * list_of_sales[index]\
                        for index in range (len (list_of_product))])
        max_price = max (list_of_price)
        min_price = min (list_of_price)
        max_sales = max (list_of_sales)
        min_sales = min (list_of_sales)
        most_popular_product = list_of_product [5]
        least_popular_product = list_of_product [3]
        
        return mean_sales, mean_price, max_revenue,\
                mean_revenue, min_revenue, max_price,\
                min_price, max_sales, min_sales,\
                most_popular_product, least_popular_product # выполняем и возвращаем расчеты

stat = list (statistics(list_of_product, list_of_price, list_of_sales)) # записываем расчеты


keys = ['Среднее кол-во продаж', 'Средняя цена', 'Максимальная выручка за один товар',
        'Средняя выручка', 'Минимальная выручка', 'Самый дорогой товар', 
        'Самый дешевый товар', 'Максимальные продажи', 'Минимальные продажи', 
        'Самый популярный товар', 'Самый непопулярный товар'] # создаем ключи словаря

values = stat # присваиваем новой переменной результаты выполнения функции
statistic = dict (zip (keys, values)) # создаем новый словарь со статистикой добавляя ключ:значение
print (statistic) # выводим словарь со статистикой


with open ('pharma_statistic.csv', 'w') as pharm_stat:
    
    headers = keys # объявляем заголовки взяв ключи от ранее созданного словаря
    pharm_stat_dict_writer = csv.DictWriter(pharm_stat, fieldnames = headers) # создаем экземпляр для записи и подаем заголовки
    pharm_stat_dict_writer.writeheader() # записываем заголовки
    pharm_stat_dict_writer.writerow(statistic) # записываем поля в файл 

   
