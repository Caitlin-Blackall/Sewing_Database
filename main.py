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

    def go_back():
        global data_toadd
        master.destroy()
        data_toadd = 'Go Back'
        return data_toadd
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
        try:
            size = size.upper()
        except:
            size = size

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

        name = name.title()
        check = check_data(name)
        if check == True:
            data_toadd = 'Cannot Enter'
        else:
            data_toadd = {'Pattern Name': name, 'Category': categories_toadd, 'Size': size, 'Printed Pattern': printed,
                      'Sewn': sewn, 'Notes': notes}

        master.destroy()

    go_back = tkinter.Button(frame, text='Go Back', command=go_back, height=1, width=7, pady=2)
    go_back.grid(row=7, column=0, columnspan=1, sticky='W')

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

    def go_back():
        global search_option
        fourth.destroy()
        search_option = 'Go Back'
        return search_option

    fourth = tkinter.Tk()
    fourth.title('Database Search')
    frame = ttk.Frame(fourth, padding=5)
    frame.grid()

    instructions = tkinter.Label(frame, text='Please select how you want to search the database',
                                 font=('Helvetica 18'), pady=10)
    instructions.grid(row=0, column=0, columnspan=4)

    by_category = tkinter.Button(frame, text='By Category', command=search_bycategory, height=2, width=14, pady=2)
    by_category.grid(row=1, column=0, columnspan=2, sticky='W')

    by_availability = tkinter.Button(frame, text='By Availability', command=search_byavailability, height=2, width=14, pady=2)
    by_availability.grid(row=1, column=2, columnspan=2, sticky='E')

    go_back = tkinter.Button(frame, text='Go Back', command=go_back, height=1, width=7, pady=2)
    go_back.grid(row=8, column=0, columnspan=1, sticky='W')

    fourth.mainloop()

    if search_option == 'Cat':
        x = by_cat()

        def start_again():
            six.destroy()
            run()

        def quit_program():
            six.destroy()
            quit()

        six = tkinter.Tk()
        six.title('Search Results')
        frame = ttk.Frame(six, padding=5)
        frame.grid()

        label_1 = tkinter.Label(frame, text=x, pady=10,  font=('Helvetica 18'))
        label_1.grid(row=0, column=0, columnspan=2, sticky='W')

        start_again = tkinter.Button(frame, text='Start Again', command=start_again, height=1, width=7, pady=2)
        start_again.grid(row=1, column=0, columnspan=1, sticky='W')

        exit_database = tkinter.Button(frame, text='Quit', command=quit_program, height=1, width=7, pady=2)
        exit_database.grid(row=1, column=1, columnspan=1, sticky='E')

        six.mainloop()

    elif search_option == 'Avail':
        print('avail')
    elif search_option == 'Go Back':
        run()
    else:
        return None

def by_cat():
    def go_back():
        five.destroy()
        search()

    def cats_tosearchby():
        global output_statement
        categories_tosearch = []
        add_bathers = CheckVar1.get()
        add_bottoms = CheckVar2.get()
        add_dresses = CheckVar3.get()
        add_jumpers = CheckVar4.get()
        add_male = CheckVar5.get()
        add_misc = CheckVar6.get()
        add_rompers = CheckVar7.get()
        add_tops = CheckVar8.get()

        if add_bathers == 1:
            categories_tosearch.append('Bathers')
        if add_bottoms == 1:
            categories_tosearch.append('Bottoms')
        if add_dresses == 1:
            categories_tosearch.append('Dresses')
        if add_jumpers == 1:
            categories_tosearch.append('Jumpers')
        if add_male == 1:
            categories_tosearch.append('Male')
        if add_misc == 1:
            categories_tosearch.append('Misc')
        if add_rompers == 1:
            categories_tosearch.append('Rompers')
        if add_tops == 1:
            categories_tosearch.append('Tops')
        with open('data.csv', 'r') as csv_file:
            spreadsheet = csv.DictReader(csv_file)
            pattern_names = []
            for row in spreadsheet:
                for category in categories_tosearch:
                    if category in row['Category']:
                        pattern_names.append(row['Pattern Name'])
        pattern_names = list(dict.fromkeys(pattern_names))
        finalnames_bycat = ''
        x = len(pattern_names)
        for name in pattern_names:
            index = pattern_names.index(name)
            if index == 0:
                finalnames_bycat += name
            else:
                finalnames_bycat += '\n' + name
        if x == 0:
            output_statement = 'There are no pattern matches.'
        elif x == 1:
            output_statement = 'There is 1 pattern match.\n\nThe pattern is: {}.'.format(finalnames_bycat)
        else:
            output_statement = 'There are {} pattern matches.\n\nThe patterns are:\n{}'.format(x, finalnames_bycat)

        five.destroy()
        return output_statement

    five = tkinter.Tk()
    five.title('Search by Category')
    frame = ttk.Frame(five, padding=5)
    frame.grid()

    label_1 = tkinter.Label(frame, text='Select category / categories to search by:', pady=10)
    label_1.grid(row=0, column=0, columnspan=3, sticky='W')
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
    C1.grid(row=1, column=0, sticky='W')
    C2.grid(row=2, column=0, sticky='W')
    C3.grid(row=1, column=1, sticky='W')
    C4.grid(row=2, column=1, sticky='W')
    C5.grid(row=1, column=2, sticky='W')
    C6.grid(row=2, column=2, sticky='W')
    C7.grid(row=1, column=3, sticky='W')
    C8.grid(row=2, column=3, sticky='W')

    go_back = tkinter.Button(frame, text='Go Back', command=go_back, height=1, width=7, pady=2)
    go_back.grid(row=3, column=0, columnspan=1, sticky='SW')

    start_search = tkinter.Button(frame, text='Start Search', command=cats_tosearchby, height=2, width=14, pady=2)
    start_search.grid(row=3, column=3, columnspan=1, sticky='E')

    five.mainloop()

    return output_statement

def update():
    print('Done')

def already_exists():
    def try_again():
        third.destroy()
        run()

    def quit_program():
        third.destroy()
        quit()

    third = tkinter.Tk()
    third.title('Error')
    frame = ttk.Frame(third, padding=5)
    frame.grid()

    message = tkinter.Label(frame, text='Error - This pattern already exists', font=('Helvetica 25 bold'), pady=10)
    message.grid(row=0, column=1, columnspan=4)

    instructions = tkinter.Label(frame, text='Please select from the following options to continue',
                                 font=('Helvetica 18'), pady=10)
    instructions.grid(row=1, column=0, columnspan=4)

    try_again = tkinter.Button(frame, text='Try Again', command=try_again, height=2, width=14, pady=2)
    try_again.grid(row=2, column=1, columnspan=2, sticky='W')

    exit_database = tkinter.Button(frame, text='Quit', command=quit_program, height=2, width=14, pady=2)
    exit_database.grid(row=2, column=3, columnspan=2, sticky='E')

    third.mainloop()

def interface():
    def add_pattern():
        global run_option
        sec.destroy()
        run_option = 'A'
        return run_option

    def search_pattern():
        global run_option
        sec.destroy()
        run_option = 'S'
        return run_option

    def update_pattern():
        global run_option
        sec.destroy()
        run_option = 'U'
        return run_option

    def quit_program():
        global run_option
        sec.destroy()
        run_option = 'Q'
        return run_option

    sec = tkinter.Tk()
    sec.title('Sewing Database')
    frm = ttk.Frame(sec, padding=5)
    frm.grid()

    welcome = tkinter.Label(frm, text='Welcome to the Sewing Pattern Database!', font=('Helvetica 25 bold'), pady=10)
    welcome.grid(row=0, column=1, columnspan=7)

    instructions = tkinter.Label(frm, text='Please select from the following options to continue',
                                 font=('Helvetica 18'), pady=10)
    instructions.grid(row=1, column=0, columnspan=7)

    add = tkinter.Button(frm, text='Add Pattern', command=add_pattern, height=2, width=14, pady=2)
    add.grid(row=7, column=1, columnspan=2, sticky='W')

    search = tkinter.Button(frm, text='Search Patterns', command=search_pattern, height=2, width=14, pady=2)
    search.grid(row=7, column=3, columnspan=2, sticky='W')

    update = tkinter.Button(frm, text='Update Pattern', command=update_pattern, height=2, width=14, pady=2)
    update.grid(row=7, column=5, columnspan=2, sticky='W')

    exit_database = tkinter.Button(frm, text='Quit', command=quit_program, height=1, width=7, pady=2)
    exit_database.grid(row=8, column=6, columnspan=1, sticky='E')

    sec.mainloop()

    return run_option

def run():
    #run_option = input('Do you want to search (S), add (A), update (U) a pattern or quit (Q)? ').upper()
    run_option = interface()
    if run_option == 'S':
        return search()
    elif run_option == 'A':
        data_toadd = enter_data()
        if data_toadd == 'Cannot Enter':
            already_exists()
        elif data_toadd == 'Go Back':
            run()
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

'''from tkinter_testing import test_function
def run():
    test_function()
run()'''
