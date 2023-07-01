import csv
import tkinter
from tkinter import ttk

def create_spreadsheet(data_toadd):
    data = data_toadd
    field_names = ['Pattern Name', 'Category', 'Size', 'Printed Pattern', 'Completed', 'Notes']
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
    name = input('Enter pattern name: ').title()

    check = check_data(name)
    if check == True:
        print('This pattern already exists')
        next_steps = input('Do you want to do something else? Y/N ').upper()
        if next_steps == 'Y':
            run()
        else:
            return None

    #category = input('Enter category: ').title()
    category = []
    categories_toadd = ''
    new_cat = tkinter.Tk()
    new_cat.title('Pattern Category')
    frm = ttk.Frame(new_cat, padding=20)
    frm.grid()
    l1 = tkinter.Label(frm, text='Please select category or categories of the new pattern')
    l1.grid(row=0, column=0)
    #add widgets here

    CheckVar1 = tkinter.IntVar()
    CheckVar2 = tkinter.IntVar()
    CheckVar3 = tkinter.IntVar()
    CheckVar4 = tkinter.IntVar()
    CheckVar5 = tkinter.IntVar()
    CheckVar6 = tkinter.IntVar()
    CheckVar7 = tkinter.IntVar()
    CheckVar8 = tkinter.IntVar()
    C1 = tkinter.Checkbutton(frm, text = 'Bathers', variable=CheckVar1, onvalue = 1, offvalue = 0, height=3, width=10)
    C2 = tkinter.Checkbutton(frm, text='Bottoms', variable=CheckVar2, onvalue=1, offvalue=0, height=3, width=10)
    C3 = tkinter.Checkbutton(frm, text='Dresses', variable=CheckVar3, onvalue=1, offvalue=0, height=3, width=10)
    C4 = tkinter.Checkbutton(frm, text='Jumpers', variable=CheckVar4, onvalue=1, offvalue=0, height=3, width=10)
    C5 = tkinter.Checkbutton(frm, text='Male', variable=CheckVar5, onvalue=1, offvalue=0, height=3, width=7)
    C6 = tkinter.Checkbutton(frm, text='Misc', variable=CheckVar6, onvalue=1, offvalue=0, height=3, width=7)
    C7 = tkinter.Checkbutton(frm, text='Rompers', variable=CheckVar7, onvalue=1, offvalue=0, height=3, width=10)
    C8 = tkinter.Checkbutton(frm, text='Tops', variable=CheckVar8, onvalue=1, offvalue=0, height=3, width=7)
    finish = tkinter.Button(frm, text = 'Press to finish', command=new_cat.destroy)

    C1.grid(row=1, column=0, sticky='W')
    C2.grid(row=2, column=0, sticky='W')
    C3.grid(row=3, column=0, sticky='W')
    C4.grid(row=4, column=0, sticky='W')
    C5.grid(row=5, column=0, sticky='W')
    C6.grid(row=6, column=0, sticky='W')
    C7.grid(row=7, column=0, sticky='W')
    C8.grid(row=8, column=0, sticky='W')
    finish.grid(row=9, column=2, sticky='E')

    new_cat.mainloop()

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

    #print(category)
    x = len(category)
    for cats in category:
        index = category.index(cats)
        if index == (x - 1):
            categories_toadd += cats
        else:
            categories_toadd += cats + ', '

    #print(categories_toadd)


    size = input('Enter pattern size: ').title()
    printed = input('Has this pattern been printed? Y/N ').upper()
    completed = input('Has this pattern been sewn? Y/N ').upper()
    notes = input('Any notes to add about this pattern? ').capitalize()

    data_toadd = {'Pattern Name': name, 'Category': categories_toadd, 'Size': size, 'Printed Pattern': printed, 'Completed': completed, 'Notes': notes}

    return data_toadd

def check_data(name):
    with open('data.csv', 'r') as data_csv:
        spreadsheet = csv.DictReader(data_csv)
        for row in spreadsheet:
            if row['Pattern Name'] == name:
                return True
            else:
                return False

def search():
    parameter = input('Do you want to search by pattern category (A) or printed patterns (B)? ').upper()
    if parameter == 'A':
        item = 'Yay'
        print('The pattern/s that match the search are {}'.format(item))

def update():
    print('Done')

def run():
    run_option = input('Do you want to search (S), add (A), update (U) a pattern or quit (Q)? ').upper()
    if run_option == 'S':
        return search()
    elif run_option == 'A':
        data_toadd = enter_data()
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