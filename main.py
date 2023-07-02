import csv
import tkinter
from tkinter import ttk

def create_spreadsheet(data_toadd):
    data = data_toadd
    field_names = ['Pattern Name', 'Category', 'Size', 'Printed Pattern', 'Sewn', 'Notes']
    count = 0
    with open('data.csv', 'r') as data_csv:
        base_spreadsheet = csv.DictReader(data_csv)
        for row in base_spreadsheet:
            count += 1
        data_csv.close()
    with open('data.csv', 'a') as data_csv:
        base_spreadsheet = csv.DictWriter(data_csv, fieldnames=field_names)
        if count == 0:
            base_spreadsheet.writeheader()
            base_spreadsheet.writerow(data)
        else:
            base_spreadsheet.writerow(data)
    return base_spreadsheet

def enter_data():
    master = tkinter.Tk()
    master.title('Add pattern information')
    frame = ttk.Frame(master, padding=5)
    frame.grid()

    label_1 = tkinter.Label(frame, text='Pattern Name:', pady=10)
    label_1.grid(row=0, column=0, sticky='W')
    e1 = tkinter.Entry(frame)
    e1.grid(row=0, column=1, columnspan=2, pady=2)

    label_2 = tkinter.Label(frame, text='Pattern Categories:', pady=10)
    label_2.grid(row=1, column=0, sticky='W')
    CheckVar1 = tkinter.IntVar()
    CheckVar2 = tkinter.IntVar()
    CheckVar3 = tkinter.IntVar()
    CheckVar4 = tkinter.IntVar()
    CheckVar5 = tkinter.IntVar()
    CheckVar6 = tkinter.IntVar()
    CheckVar7 = tkinter.IntVar()
    CheckVar8 = tkinter.IntVar()
    C1 = tkinter.Checkbutton(frame, text='Bathers', variable=CheckVar1, onvalue=1, offvalue=0, width=10)
    C2 = tkinter.Checkbutton(frame, text='Bottoms', variable=CheckVar2, onvalue=1, offvalue=0, width=10)
    C3 = tkinter.Checkbutton(frame, text='Dresses', variable=CheckVar3, onvalue=1, offvalue=0, width=10)
    C4 = tkinter.Checkbutton(frame, text='Jumpers', variable=CheckVar4, onvalue=1, offvalue=0, width=10)
    C5 = tkinter.Checkbutton(frame, text='Male', variable=CheckVar5, onvalue=1, offvalue=0, width=7)
    C6 = tkinter.Checkbutton(frame, text='Misc', variable=CheckVar6, onvalue=1, offvalue=0, width=7)
    C7 = tkinter.Checkbutton(frame, text='Rompers', variable=CheckVar7, onvalue=1, offvalue=0, width=10)
    C8 = tkinter.Checkbutton(frame, text='Tops', variable=CheckVar8, onvalue=1, offvalue=0, width=7)
    C1.grid(row=1, column=1, sticky='W')
    C2.grid(row=2, column=1, sticky='W')
    C3.grid(row=1, column=2, sticky='W')
    C4.grid(row=2, column=2, sticky='W')
    C5.grid(row=1, column=3, sticky='W')
    C6.grid(row=2, column=3, sticky='W')
    C7.grid(row=1, column=4, sticky='W')
    C8.grid(row=2, column=4, sticky='W')

    label_3 = tkinter.Label(frame, text='Pattern Size:', pady=10)
    label_3.grid(row=3, column=0, sticky='W')
    e3 = tkinter.Entry(frame)
    e3.grid(row=3, column=1, columnspan=2, pady=2)

    label_4 = tkinter.Label(frame, text='Pattern Printed?', pady=10)
    label_4.grid(row=4, column=0, sticky='W')
    PrintVar1 = tkinter.IntVar()
    PrintVar2 = tkinter.IntVar()
    P1 = tkinter.Checkbutton(frame, text='Yes', variable=PrintVar1, onvalue=1, offvalue=0, width=6)
    P2 = tkinter.Checkbutton(frame, text='No', variable=PrintVar2, onvalue=1, offvalue=0, width=6)
    P1.grid(row=4, column=1, sticky='W')
    P2.grid(row=4, column=2, sticky='W')

    label_5 = tkinter.Label(frame, text='Pattern Sewn?', pady=10)
    label_5.grid(row=5, column=0, sticky='W')
    SewnVar1 = tkinter.IntVar()
    SewnVar2 = tkinter.IntVar()
    S1 = tkinter.Checkbutton(frame, text='Yes', variable=SewnVar1, onvalue=1, offvalue=0, width=6)
    S2 = tkinter.Checkbutton(frame, text='No', variable=SewnVar2, onvalue=1, offvalue=0, width=6)
    S1.grid(row=5, column=1, sticky='W')
    S2.grid(row=5, column=2, sticky='W')

    label_6 = tkinter.Label(frame, text='Pattern Notes:', pady=10)
    label_6.grid(row=6, column=0, sticky='W')
    e6 = tkinter.Entry(frame, width=38)
    e6.grid(row=6, column=1, columnspan=4, pady=2, ipady=15)

    def get_data():
        global data_toadd
        name = e1.get()

        category = []
        add_bathers = CheckVar1.get()
        add_bottoms = CheckVar2.get()
        add_dresses = CheckVar3.get()
        add_jumpers = CheckVar4.get()
        add_male = CheckVar5.get()
        add_misc = CheckVar6.get()
        add_rompers = CheckVar7.get()
        add_tops = CheckVar8.get()

        if add_bathers == 1:
            category.append('Bathers')
        if add_bottoms == 1:
            category.append('Bottoms')
        if add_dresses == 1:
            category.append('Dresses')
        if add_jumpers == 1:
            category.append('Jumpers')
        if add_male == 1:
            category.append('Male')
        if add_misc == 1:
            category.append('Misc')
        if add_rompers == 1:
            category.append('Rompers')
        if add_tops == 1:
            category.append('Tops')

        x = len(category)
        categories_toadd = ''
        for cats in category:
            index = category.index(cats)
            if index == (x - 1):
                categories_toadd += cats
            else:
                categories_toadd += cats + ', '

        size = e3.get()
        is_printed = PrintVar1.get()
        if is_printed == 1:
            printed = 'Y'
        else:
            printed = 'N'
        is_sewn = SewnVar1.get()
        if is_sewn == 1:
            sewn = 'Y'
        else:
            sewn = 'N'
        notes = e6.get()

        check = check_data(name)
        if check == True:
            data_toadd = 'Cannot Enter'
        else:
            data_toadd = {'Pattern Name': name, 'Category': categories_toadd, 'Size': size, 'Printed Pattern': printed,
                      'Sewn': sewn, 'Notes': notes}

        master.destroy()

    finish = tkinter.Button(frame, text='Finished', command=get_data, height=2, width=14, pady=2)
    finish.grid(row=7, column=3, columnspan=2, sticky='W')

    master.mainloop()

    return data_toadd

def check_data(name):
    with open('data.csv', 'r') as data_csv:
        spreadsheet = csv.DictReader(data_csv)
        for row in spreadsheet:
            if row['Pattern Name'] == name:
                return True

def search():
    parameter = input('Do you want to search by pattern category (A) or printed patterns (B)? ').upper()
    if parameter == 'A':
        item = 'Yay'
        print('The pattern/s that match the search are {}'.format(item))

def update():
    print('Done')

def already_exists():
    print('This pattern already exists')
    next_steps = input('Do you want to do something else? Y/N ').upper()
    if next_steps == 'Y':
        run()
    else:
        quit()

def run():
    run_option = input('Do you want to search (S), add (A), update (U) a pattern or quit (Q)? ').upper()
    if run_option == 'S':
        return search()
    elif run_option == 'A':
        data_toadd = enter_data()
        if data_toadd == 'Cannot Enter':
            already_exists()
        else:
            spreadsheet = create_spreadsheet(data_toadd)
            return spreadsheet
    elif run_option == 'U':
        return update()
    elif run_option == 'Q':
        return None
    else:
        print('Invalid response, please try again')
        run()

run()
