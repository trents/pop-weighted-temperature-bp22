"""This script creates a national population weighted temperature data set"""
# This produces national_pop_weighted_temps.csv 

from datetime import datetime, date, timedelta
import re

class popRecord:
        def __init__(self, city, state, pop, lat, long):
                self.city = city
                self.state = state
                self.pop = int(pop)
                self.long = long
                self.lat = lat

        def __str__(self):
                return self.city

        def __repr__(self):
                return self.city

class tempRecord:
    def __init__ (self, name, country, countryCode, continent, stationCode, newDate, tempMean, tempMin, tempMax, interpolated):
        self.city = name.strip() 
        self.country = country
        self.countryCode = countryCode
        self.continent = continent
        self.stationCode = stationCode

        if type(newDate) is datetime:
            self.tempDate = newDate
        else:
            splitDate = newDate.split("/")
            month = int(splitDate[0])
            day = int(splitDate[1])
            year = int(splitDate[2])

            self.tempDate = datetime(year, month, day)
        self.tempMean = float(tempMean)
        self.tempMin = float(tempMin)
        self.tempMax = float(tempMax)
        self.interpolated = interpolated

    def __str__(self):
        return self.city + "," + self.country + "," + self.countryCode + "," + self.continent + "," + self.stationCode + "," + str(self.tempDate) + "," +  str(self.tempMean) + "," + str(self.tempMin) + "," +  str(self.tempMax) + "," + self.interpolated + "\n"

    def __repr__(self):
        return self.city + "," + self.country + "," + self.countryCode + "," + self.continent + "," + self.stationCode + "," + str(self.tempDate) + "," +  str(self.tempMean) + "," + str(self.tempMin) + "," +  str(self.tempMax) + "," + self.interpolated + "\n"
 
with open("temp-data-interpolated.csv") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

t_d = []
data_list = []

for i, _ in enumerate(new_arr):
    if i > 0:
        t_d = new_arr[i].split(",")
        data_list.append(tempRecord(t_d[0],t_d[1],t_d[2],t_d[3],t_d[4],t_d[5],t_d[6],t_d[7],t_d[8],"N"))

data_list = sorted(data_list, key=lambda x:[x.tempDate])

# print(data_list)

list_of_dates = []

for i in data_list:
    if i.tempDate not in list_of_dates:
       list_of_dates.append(i.tempDate)

list_of_cities = []

with open("pop-data.csv","r") as popDataFile:
    next(popDataFile)
    for line in popDataFile:
        stripped_line = line.strip()
        x = stripped_line.split(",")
        list_of_cities.append(popRecord(x[0],x[1],x[2],x[3],x[4]))

list_of_dates = sorted(list_of_dates)
national_temperatures = ["Date,Mean Temp,Min Temp,Max Temp"]

for i in list_of_dates:
    todays_temperatures = []
    for j in data_list:
        if i == j.tempDate:
            todays_temperatures.append(j)
    pop_count = 0
    temporary_min_temp = 0
    temporary_max_temp = 0
    temporary_mean_temp = 0
    for j in todays_temperatures:
        for k in list_of_cities:
            if j.city == k.city:
                pop_count += k.pop
                temporary_min_temp += j.tempMin * k.pop
                temporary_max_temp += j.tempMax * k.pop
                temporary_mean_temp += j.tempMean * k.pop
    national_min_temp = temporary_min_temp / pop_count
    national_max_temp = temporary_max_temp / pop_count
    national_mean_temp = temporary_mean_temp / pop_count
    national_temperatures.append(i.strftime("%m/%d/%Y") + "," + str(national_mean_temp) + "," + str(national_min_temp) + "," + str(national_max_temp))

with open("national-pop-weighted-temps.csv","w") as output_data:
    for i in national_temperatures:
        output_data.writelines(i + "\n")
