import pandas as pd
from pandas.tseries.offsets import BDay
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import sys
fname = "word_counts.csv"
data = pd.read_csv(fname)
data['Date'] = pd.to_datetime(data['Date'])

timescale = BDay(2)#pd.Timedelta(5, 'days')
last_week = data['WordCount'][data['Date'] > data['Date'].iloc[-1]-timescale]
delta_y = data['WordCount'][data['Date'] == data['Date'].iloc[-1]]-last_week.iloc[0]
delta_x = timescale
words_per_day = delta_y/delta_x.n#.days
words_left = 60000-data['WordCount'][data['Date'] == data['Date'].iloc[-1]]
days_left = words_left/words_per_day
print('Weeks left:', days_left.values[0]/5)

#print(data.head())
fig = plt.figure()
ax1 = fig.add_subplot(111)
#days = np.array([x.days for x in (data['Date']-data['Date'][0])])
#print(days)
ax1.plot(data['Date'], data['WordCount'], 'bx-', label='Word count')
ax1.set_ylabel('Word count')
ax2 = ax1.twinx()
ax2.plot(data['Date'], data['PageCount'], 'rx-', label='Page count')
ax2.set_ylabel('Page count')
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")
date_form = DateFormatter("%m-%d %Hh")
ax1.xaxis.set_major_formatter(date_form)
ax2.xaxis.set_major_formatter(date_form)
ax1.set_ylim(0, 60000)
ax2.set_ylim(0, 200)
plt.tight_layout()
plt.show()
