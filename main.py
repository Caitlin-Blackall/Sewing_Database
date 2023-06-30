import csv

def add_data():
    field_names = ['Pattern Name', 'Category']
    data = [{'Pattern Name': 'Going Home Sweater', 'Category': 'Jumpers'},
            {'Pattern Name': 'Chapman Cardigan', 'Category': 'Jumpers'},
            {'Pattern Name': 'Tres Belle', 'Category': 'Dresses'}]

    with open('data.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)

    return spreadsheet

def read_data():
    data = []
    with open('data.csv', 'r') as data_csv:
        spreadsheet = csv.DictReader(data_csv)
        for row in spreadsheet:
            data.append(row)
    return data

def run():
    data = read_data()
    spreadsheet = add_data()
    total = 0
    for row in data:
        total += 1
    print('Total Patterns: {}'.format(total))

run()