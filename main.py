import csv

def spreadsheet():
    field_names = ['Pattern Name', 'Category', 'Size', 'Printed Pattern', 'Completed', 'Notes']

    with open('data.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)

    return spreadsheet

def add_data():
    name = input('Enter pattern name: ')
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

'''def run():
    spreadsheet = spreadsheet()
    data = read_data()
    total = 0
    for row in data:
        total += 1
    print('Total Patterns: {}'.format(total))

run()'''