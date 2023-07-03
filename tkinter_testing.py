import csv
import tkinter
from tkinter import ttk

'''def test_function():
    print('yay')

from tkinter_testing import test_function
def run():
    test_function()
run()'''

with open('data.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    pattern_names = []
    for row in spreadsheet:
        if option == 'Y' in row['Printed Pattern']:
            pattern_names.append(row['Pattern Name'])
pattern_names = list(dict.fromkeys(pattern_names))
finalnames_byavail = ''
x = len(pattern_names)
for name in pattern_names:
    index = pattern_names.index(name)
    if index == 0:
        finalnames_byavail += name
    else:
        finalnames_byavail += '\n' + name
if x == 0:
    output_statement = 'There are no pattern matches.'
elif x == 1:
    output_statement = 'There is 1 pattern match.\n\nThe pattern is: {}.'.format(finalnames_byavail)
else:
    output_statement = 'There are {} pattern matches.\n\nThe patterns are:\n{}'.format(x, finalnames_byavail)

return output_statement