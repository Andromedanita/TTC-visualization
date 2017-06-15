import numpy as np
import matplotlib.pylab as plt
import csv

plt.ion()

with open('/Users/anita/Documents/Renee_presentation_course/ttc-vis/data/delay_codes_2014-2017.csv', 'rU') as csvfile:
    reader     = csv.reader(csvfile)
    delay_list  = list(reader)

# delay_list[0] is the header
# The data contains:
# "Date", "Time", "Day", "Station", "Code", "Minimum delay", "minimum gap between two trains", "Bound", "Line", "Vehicle"

delay_list.pop(0) # to remove the header from the file
delay_array = np.array(delay_list)

delay_date    = delay_array[:,0] 
delay_time    = delay_array[:,1]
delay_day     = delay_array[:,2]
delay_station = delay_array[:,3]
delay_code    = delay_array[:,4]
delay_min_del = delay_array[:,5]
delay_min_gap = delay_array[:,6]
delay_bound   = delay_array[:,7]
delay_line    = delay_array[:,8]
delay_veh     = delay_array[:,9]

#plt.hist()
from collections import Counter
counts_day  = Counter(delay_day)
centers_day = range(len(counts_day))
labels_day  = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
values_day  = [10585, 10885, 10983, 10985, 10754, 8011, 6840] # because the values orders are changed based on the day of the week
plt.bar(centers_day, values_day, align='center')
plt.xticks(centers_day, labels_day)


counts_line  = Counter(delay_line)
centers_line = range(len(counts_day))


def plot_bar(variable):
    counts  = Counter(variable)
    centers = range(len(counts))
    values  = counts.values()
    labels  = counts.keys()
    plt.bar(centers, values, align='center')
    plt.xticks(centers, labels, rotation='vertical', fontsize=7)


# to get the number of delays happened in each year
years = []
for i in range(len(delay_date)):
    years.append(delay_date[i][0:4])


def stations(station_name, station_list):
    for i in range(len(delay_station)):
        if station_name in delay_station[i]:
            station_list.append(i)


