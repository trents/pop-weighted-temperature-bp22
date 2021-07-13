"""Run this scrubber first to fix the data files so that they're compatible"""
# This produces a temp-data-scrubbed.csv and pop-data-scrubbed.csv
# Those are used as inputs for the main driver program

import re

def line_fixer(input_line):
    """Fixing the cities in each line in temp-data so they match the pop-data"""
    input_line = re.sub('Windsor Locks','Hartford',input_line)
    input_line = re.sub('Covington','Cincinnati',input_line)
    input_line = re.sub('Detroit/Wayne','Detroit',input_line)
    input_line = re.sub('NYC/LaGuardia','New York',input_line)
    input_line = re.sub('Chicago O\'Hare','Chicago',input_line)
    input_line = re.sub('Phoenix/Sky HRBR','Phoenix',input_line)
    input_line = re.sub('Raleigh/Durham','Raleigh',input_line)
    input_line = re.sub('Sacramento/Execu','Sacramento',input_line)
    input_line = re.sub('St Louis/Lambert','St. Louis',input_line)
    input_line = re.sub('Wash DC/Dulles','Dulles',input_line)
    portland_me = "KPWM"
    if portland_me in line:
        input_line = re.sub('Portland','PortlandM',input_line)
    return input_line

with open("temp-data.csv") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

for i, _ in enumerate(new_arr):
    new_arr[i] = line_fixer(new_arr[i])

with open("temp-data-scrubbed.csv","w") as file2:
    for newln in new_arr:
        file2.writelines(newln + "\n")

with open("pop-data.csv") as file3:
    g = file3.readlines()
new_arr2 = []
for line in g:
    new_arr2.append(line.strip())

# This adds three lines missing from pop_data so that it matches temp_data

new_arr2.append("Albany,New York,97478,-73.7562,42.6526")
new_arr2.append("Dulles,Virginia,60534,-77.4380,38.9625")
new_arr2.append("PortlandM,Maine,66595,-70.2568,43.6591")

with open("pop-data-scrubbed.csv","w") as file4:
    for newline in new_arr2:
        file4.writelines(newline + "\n")
