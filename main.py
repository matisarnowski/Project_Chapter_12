#! /bin/python3

import openpyxl
import pprint
from my_tkinter import *

if __name__ == "__main__":
    print('Otwieranie skoroszytu...')
    wb = openpyxl.load_workbook(
        'powierzchnia_i_ludnosc_w_przekroju_terytorialnym_w_2021_roku_tablice.xlsx')
    sheet = wb['Sheet']
    countyData = []

    print('Odczyt wierszy...')
    counting = 0
    total_area = 0
    total_population = 0
    for row in range(6, sheet.max_row):
        if not sheet['A' + str(row)].value.startswith('W'):
            town_or_city = sheet['B' + str(row)].value
            area_of_city = sheet['D' + str(row)].value
            population = sheet['F' + str(row)].value
            counting += 1
            countyData.append([town_or_city, 'Powierzchnia miasta w ha: ' +
                               str(area_of_city), 'Populacja miasta: ' + str(population)])
            total_area += int(area_of_city)
            total_population += int(population)
    root = tk.Tk()
    my_gui = Window(root, countyData, total_area, total_population, counting)
    root.mainloop()
