# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt

x_list = []
y_list = []

for x in range(-10,11):
    y = 5*x**2+10*x-30
    x_list.append(x)
    y_list.append(y)
plt.axhline(y=0,color='r',linestyle='dashdot')
plt.plot(y_list,color='k',linestyle='solid',label='f(x)=5x^2+10x-30')# дали название линии графика для вывода в легенду
plt.title('График функции f(x)', color='g')# дали название графику
plt.xlim([0., 20.])# скорректировали погрешность оси y, притянули в ноль
plt.xlabel('Ось x', fontsize=12,color='r')# назвали горизонтальную ось
plt.ylabel('Ось y', fontsize=12,color='r')# назвали вертикальную ось
plt.grid(which='major')# включили основную сетку

plt.minorticks_on()# включили дополнительные (более детальные) отметки на осях

plt.grid(which='minor', linestyle=':')# включили дополнительную сетку

plt.legend(fontsize=12)# вывели легенду
plt.tight_layout()

plt.show()