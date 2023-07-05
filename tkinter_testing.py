import csv
import tkinter
from tkinter import ttk
import pandas as pd


def quit_program():
    thirteen.destroy()
    quit()


def start_again():
    thirteen.destroy()
    run()

thirteen = tkinter.Tk()
thirteen.title('Done')
frame = ttk.Frame(thirteen, padding=5)
frame.grid()

label_1 = tkinter.Label(frame, text='Pattern Succesfully Updated!', pady=10, font=('Helvetica 18'))
label_1.grid(row=0, column=0, columnspan=2, sticky='W')

start_again = tkinter.Button(frame, text='Start Again', command=start_again, height=1, width=7, pady=2)
start_again.grid(row=1, column=0, columnspan=1, sticky='W')

exit_database = tkinter.Button(frame, text='Quit', command=quit_program, height=1, width=7, pady=2)
exit_database.grid(row=1, column=1, columnspan=1, sticky='E')

thirteen.mainloop()







'''
from tkinter_testing import test_function
def run():
    test_function()
run()'''