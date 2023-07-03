import csv
import tkinter
from tkinter import ttk

'''def test_function():
    print('yay')

from tkinter_testing import test_function
def run():
    test_function()
run()'''

six = tkinter.Tk()
six.title('Search Results')
frame = ttk.Frame(six, padding=5)
frame.grid()

label_1 = tkinter.Label(frame, text=x, pady=10)
label_1.grid(row=0, column=0, sticky='W')