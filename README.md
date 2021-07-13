# pop-weighted-temperature-bp22
Solution to Bill Perkins' population-weighted temperature question - see https://twitter.com/bp22/status/1409278019886370838

Part 1 involves creating a data set of population weighted national temperature data by day,
given the provided data sets.  These are temp-data.csv and pop-data.csv

The first script to run is scrubber.py 
* It runs through the data in temp-data.csv and pop-data.csv, cleaning them up.
There are several issues with the initial data set, mostly centered around unclear city
and airport designations.  This script makes several small assumptions about the data
and ensures that there are entries in pop-data for each entry in temp-data.
* This script produces temp-data-scrubbed.csv and pop-data-scrubbed.csv

The second script to run is weather_estimator.py
* This goes through temp-data-scrubbed.py and fills in holes in the weather data.
* If a date is missing, I simply copied the temperature data from the same location 
from the day before.  This is extremely simple, of course, but a more complex 
strategy can be easily popped in.
* I also added a field indicating whether the temperature data for that day and 
location was real or interpolated.
* This script produces temp-data-interpolated.csv, which is useful for Part 2

The third script to run is national_pop_weighted_estimator.py
* This goes through the interpolated temperature data and produces a population-
weighted daily national temperature record.  It draws on the data in pop-data-scrubbed.csv
and temp-data-interpolated.csv to produce this.
* The program produces national-pop-weighted-temps.csv, which is both the answer to Part 1
and a needed input for Part 2 
