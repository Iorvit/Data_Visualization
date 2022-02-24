from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint

class Die():
    """Класс, предстовляющий один кубик."""

    def __init__(self, num_sides=6):
        """Поумолчанию используется шестигранный кубик."""
        self.num_sides = num_sides

    def roll(self):
        """Возращает случайное число от 1 до числа граней."""
        return randint(1, self.num_sides)


# Создание двух кубиков.
die_1 = Die()
die_2 = Die()
die_3 = Die()
i = 1000

# Моделирование серии бросков с сохранение результатов в списке.
results = []
for roll_num in range(i):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Анализ результата.
frequencise = []
max_result = die_1.num_sides + die_2.num_sides + die_2.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencise.append(frequency)

# Визуализация результатов.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencise)]

x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'frequency of Result'}
my_layout = Layout(title=f'Result of rolling thre D6 {i} times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')    
