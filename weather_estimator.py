"""This script fills in gaps in temp data with estimates"""
# This produces a temp-data-scrubbed.csv and pop-data-scrubbed.csv
# Those are used as inputs for the main driver program

from datetime import datetime, date, timedelta
import re

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
 
with open("temp-data-scrubbed.csv") as file:
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

data_list = sorted(data_list, key=lambda x:[x.city, x.tempDate])
prev_date = ""
new_data_list = []

for i, _ in enumerate(data_list):
    if i == 0:
        if data_list[i].tempDate == datetime(2015,1,1):
            prev_date = datetime(2015,1,1)
    else:
        if not prev_date + timedelta(1) == data_list[i].tempDate:    
#            print("Nope! " + str(prev_date) + " " + data_list[i].city + " Prev: " + data_list[i-1].city)
            if data_list[i].tempDate == datetime(2015,1,1):
                prev_date = datetime(2015,1,1)
            elif data_list[i].tempDate == datetime(2015,1,2):
                prev_date = datetime(2015,1,2)
                new_data_list.append(tempRecord(data_list[i].city,data_list[i].country,data_list[i].countryCode,data_list[i].continent,data_list[i].stationCode,datetime(2015,1,1),data_list[i].tempMean,data_list[i].tempMin,data_list[i].tempMax,"Y"))
            else:
                prev_date = data_list[i].tempDate
                new_data_list.append(tempRecord(data_list[i].city,data_list[i].country,data_list[i].countryCode,data_list[i].continent,data_list[i].stationCode,data_list[i].tempDate - timedelta(1),data_list[i].tempMean,data_list[i].tempMin,data_list[i].tempMax,"Y"))
        else:
            prev_date = prev_date + timedelta(1)

big_data_list = data_list + new_data_list

big_data_list = sorted(big_data_list, key=lambda x:[x.city, x.tempDate])

with open("temp-data-interpolated.csv","w") as file2:
    for newln in big_data_list:
        file2.writelines(newln.city + "," + newln.country + "," + newln.countryCode + "," + newln.continent + "," + newln.stationCode + "," + newln.tempDate.strftime("%m/%d/%Y") + "," + str(newln.tempMean) + "," + str(newln.tempMin) + "," + str(newln.tempMax) + "," + newln.interpolated + "\n")
