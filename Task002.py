# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список 
# подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import random
import numpy as np
import matplotlib.pyplot as plt

count = 15

sq_houses = np.random.randint(100,300,count)
prices = np.random.randint(3, 20,count)
av_price_sq_m = [round(prices[i]/sq_houses[i]*1000000) for i in range(len(prices))]
print(av_price_sq_m)

h_names = ['Дом 1','Дом 2','Дом 3','Дом 4','Дом 5','Дом 6','Дом 7','Дом 8','Дом 9','Дом 10','Дом 11','Дом 12','Дом 13','Дом 14','Дом 15']

plt.axhline(y=50000, color ='g',linestyle='dashed')
plt.bar(h_names, av_price_sq_m, 0.9) #добавили столбчатую диаграмму с толщиной столбцов 0.9
plt.grid(which='major')
plt.minorticks_on()

plt.grid(which='minor', linestyle=':')

plt.title('Стоимость квадратного метра (руб.)', color='b')

plt.show()