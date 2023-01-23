from tkinter import *
from tkinter import ttk
import csv

DOLLARS_TO_EUROS = 0.92
DOLLARS_TO_YEN = 128.74
EUROS_TO_YEN = 139.37

def check_diff_currencies(from_currency, to_currency):
    if from_currency == to_currency:
        print("Conversion impossible entre deux mêmes devises")
        return False
    return True

def calculate_conversion(amount, from_currency, to_currency):
    if from_currency == 'Dollars':
        if to_currency == 'Euros':
            return amount * DOLLARS_TO_EUROS
        elif to_currency == 'Yen':
            return amount * DOLLARS_TO_YEN
    elif from_currency == 'Euros':
        if to_currency == 'Dollars':
            return amount / DOLLARS_TO_EUROS
        elif to_currency == 'Yen':
            return amount * EUROS_TO_YEN
    elif from_currency == 'Yen':
        if to_currency == 'Dollars':
            return amount / DOLLARS_TO_YEN
        elif to_currency == 'Euros':
            return amount / EUROS_TO_YEN

def on_convert_clicked():
    amount = float(amount_field.get())
    from_currency = combo.get()
    to_currency = combo2.get()
    if check_diff_currencies(from_currency, to_currency):
        result = calculate_conversion(amount, from_currency, to_currency)
        convert_field.delete(0, END)
        convert_field.insert(0, result)
    with open("historique.csv", 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([amount, from_currency, to_currency, result])

fenetre = Tk()
fenetre.geometry("300x300")
fenetre.title("Convertisseur de monnaie")

amount_label = Label(fenetre, text="Montant :")
amount_label.pack()
amount_field = Entry(fenetre)
amount_field.pack()

from_label = Label(fenetre, text="De :")
from_label.pack()
from_currencies = ["Dollars", "Euros", "Yen"]
combo = ttk.Combobox(fenetre, values=from_currencies)
combo.current(0)
combo.pack()

to_label = Label(fenetre, text="À :")
to_label.pack()
to_currencies = ["Dollars", "Euros", "Yen"]
combo2 = ttk.Combobox(fenetre, values=to_currencies)
combo2.current(0)
combo2.pack()

convert_button = Button(fenetre, text="Convertir", command=on_convert_clicked)
convert_button.pack()

result_label = Label(fenetre, text="Résultat :")
result_label.pack()
convert_field = Entry(fenetre)
convert_field.pack()

fenetre.mainloop()

