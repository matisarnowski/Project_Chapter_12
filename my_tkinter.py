#! /bin/python3

import tkinter as tk


class Window:

    def __init__(self, parent, to_display, area, population, counting):
        self.parent = parent
        self.to_display = to_display
        self.area = area
        self.population = population
        self.counting = counting
        self.parent.geometry('850x800')
        self.parent.title('Miasta w Polsce.')
        self.parent.config(bg='black')

        # self.str_variable = tk.StringVar(parent)
        self.label = tk.Label(
            parent, text='Tu wyświetlą się miasta, a poniżej jeszcze ich łączna liczba i łączna powierzchnia oraz łączna liczba ludności w miastach Polski.')
        self.label.grid(row=0, column=0)
        self.label_with_finish = tk.Label(parent, bg='black', fg='green', text="Łączna liczba miast, to: " + str(
            counting) + ", łączna liczba mmieszkańców w miastach, to: " + str(population) + " łączna powierzchnia miast, to: " + str(area) + 'km2')
        self.label_with_finish.grid(row=1, column=0)
        self.text_field = tk.Text(parent)
        self.text_field.config(bg='black', fg='green')
        self.text_field.grid(row=2, column=0)

        self.button = tk.Button(
            parent, text='Naciśnij, aby wyświetlić. ', command=parent.destroy)
        self.button.config(bg='black', fg='green')
        self.button.grid(row=3, column=0)

        self.to_display = str(self.to_display)
        self.to_display.replace('List', '\n')
        self.text_field.insert('1.0', self.to_display)
