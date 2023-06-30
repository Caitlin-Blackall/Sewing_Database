import csv

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
    name = input('Enter pattern name: ')

    check = check_data(name)
    if check == True:
        return 'This pattern already exists'

    category = input('Enter category: ')
    size = input('Enter pattern size: ')
    printed = input('Has this pattern been printed? Y/N ')
    completed = input('Has this pattern been sewn? Y/N ')
    notes = input('Any notes to add about this pattern? ')

    data_toadd = {'Pattern Name': name, 'Category': category, 'Size': size, 'Printed Pattern': printed, 'Completed': completed, 'Notes': notes}

    return data_toadd

def check_data(name):
    with open('data.csv', 'r') as data_csv:
        spreadsheet = csv.DictReader(data_csv)
        for row in spreadsheet:
            if row['Pattern Name'] == name:
                return True
            else:
                return False

def run():
    data_toadd = enter_data()
    spreadsheet = create_spreadsheet(data_toadd)
    return spreadsheet

run()