import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    """for index, column_header in enumerate(header_row):
        print(index, column_header)"""

    highs, lows, dates = [], [], []
    # Чтение: даты, минимальной и максимальной температуры из файла.
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

    # Нанесение данных на диограмму.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Форматирование диограммы.
    plt.title("Daily high and lows temperatures-2014\nDeath Valley, CA",
        fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

