"""Run this scrubber first to fix the data files so that they're compatible"""
# This produces a temp-data-scrubbed.csv and pop-data-scrubbed.csv
# Those are used as inputs for the main driver program

import re

def line_fixer(line):
    """Fixing the cities in each line in temp-data so they match the pop-data"""
    line = re.sub('Windsor Locks','Hartford',line)
    line = re.sub('Covington','Cincinnati',line)
    line = re.sub('Detroit/Wayne','Detroit',line)
    line = re.sub('NYC/LaGuardia','New York',line)
    line = re.sub('Chicago O\'Hare','Chicago',line)
    line = re.sub('Phoenix/Sky HRBR','Phoenix',line)
    line = re.sub('Raleigh/Durham','Raleigh',line)
    line = re.sub('Sacramento/Execu','Sacramento',line)
    line = re.sub('St Louis/Lambert','St. Louis',line)
    line = re.sub('Wash DC/Dulles','Dulles',line)
    portland_me = "KPWM"
    if portland_me in line:
        line = re.sub('Portland','PortlandM',line)
    return line

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
