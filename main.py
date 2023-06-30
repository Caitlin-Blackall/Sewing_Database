import csv

def create_spreadsheet():
    field_names = ['Pattern Name', 'Category', 'Size', 'Printed Pattern', 'Completed', 'Notes']

    with open('data.csv', 'w+') as csv_file:
        base_spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        base_spreadsheet.writeheader()
    return base_spreadsheet

def check_data():
    if exists:
        return True
    else:
        return False
def add_data():
    name = input('Enter pattern name: ')

    check = check_data(name)
    if check == True:
        return 'This pattern already exists'

    category = input('Enter category: ')
    size = input('Enter pattern size: ')
    printed = input('Has this pattern been printed? Y/N ')
    completed = input('Has this pattern been sewn? Y/N ')
    notes = input('Any notes to add about this pattern? ')

    data = [{'Pattern Name': name, 'Category': category, 'Size': size, 'Printed Pattern': printed, 'Completed': completed, 'Notes': notes}]

def read_data():
    data = []
    with open('data.csv', 'r') as data_csv:
        spreadsheet = csv.DictReader(data_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    spreadsheet = create_spreadsheet()
    return spreadsheet

run()