import csv
from datetime import datetime
from multiprocessing.sharedctypes import Value

import matplotlib.pyplot as plt

filename = './data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
        
    dates, highs, lows = [],[],[]
    for row in reader:              # loop through each row
        
        # Convert the date information to a date-time object
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
        try:
            high = int(row[4])      # pull data from index 5 (high temps)
            low = int(row[5])       # pull data from index 6 (low temps)
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs, c='red', alpha=0.5)   # passing dates and high temps
ax.plot(dates,lows,c='blue', alpha=0.5)    # passing dates and low temps
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temperatures - 2018\nDeathValley, CA"
ax.set_title(title, fontsize=16)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()                 # draw the data labels with no overlapping
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()