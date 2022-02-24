import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    """for index, colum_header in enumerate(header_row):
        print(index, colum_header)"""

    dates, procipitationIn = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            procipitation = int(row[18])
            dates.append(current_date)
        except ValueError:
            print('Missing data for {current_date}')
        else:
            procipitationIn.append(procipitation)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, procipitationIn, c='red')

    plt.title('Procipitation in 2014 in a Sitka', fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Procipitation', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
