import csv
import tkinter
from tkinter import ttk

'''def test_function():
    print('yay')

from tkinter_testing import test_function
def run():
    test_function()
run()'''


def search_bycategory():
    global search_option
    fourth.destroy()
    search_option = 'Cat'
    return search_option

def search_byavailability():
    global search_option
    fourth.destroy()
    search_option = 'Avail'
    return search_option


def quit_program():
    global search_option
    fourth.destroy()
    search_option = 'Quit'
    return search_option


fourth = tkinter.Tk()
fourth.title('Database Search')
frame = ttk.Frame(fourth, padding=5)
frame.grid()

instructions = tkinter.Label(frame, text='Please select how you want to search the database',
                             font=('Helvetica 18'), pady=10)
instructions.grid(row=0, column=0, columnspan=4)

by_category = tkinter.Button(frame, text='By Category', command=try_again, height=2, width=14, pady=2)
by_category.grid(row=1, column=0, columnspan=2, sticky='W')

by_availability = tkinter.Button(frame, text='By Availability', command=quit_program, height=2, width=14, pady=2)
by_availability.grid(row=1, column=2, columnspan=2, sticky='E')

exit_database = tkinter.Button(frame, text='Quit', command=quit_program, height=1, width=7, pady=2)
exit_database.grid(row=8, column=3, columnspan=1, sticky='E')

fourth.mainloop()

if search_option == 'Cat':
    print('cat')
elif search_option == 'Avail':
    print('avail')
elif search_option == 'Quit':
    return None
else:
    return None