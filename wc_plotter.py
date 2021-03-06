import pandas as pd
import pytz
from pandas.tseries.offsets import BDay
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
import sys

target = 46616

fname = "word_counts.csv"
data = pd.read_csv(fname)
data['Date'] = pd.to_datetime(data['Date'])
data = data[~data['PageCount'].isna()]

timescale = BDay(15)#pd.Timedelta(5, 'days')
today = pd.Timestamp.now(tz=pytz.timezone('Europe/London')).normalize()
#print(today, today-timescale)
last_week = data['WordCount'][data['Date'] < today-timescale]
#print('Last week:', data['Date'][data['Date'] < today-timescale].iloc[-1], last_week.iloc[-1])
delta_y = data['WordCount'][data['Date'] == data['Date'].iloc[-1]]-last_week.iloc[-1]
delta_x = timescale
words_per_day = delta_y/delta_x.n#.days
#words_left_60 = 60000-data['WordCount'][data['Date'] == data['Date'].iloc[-1]]
words_left_50 = target-data['WordCount'][data['Date'] == data['Date'].iloc[-1]]
#days_left_60 = words_left_60/words_per_day
days_left_50 = words_left_50/words_per_day
print('Only', round(days_left_50.values[0]/5, 1), 'weeks left until FREEDOM!')
done_date_50 = today+BDay(int(1+days_left_50.values[0]))
print('(', done_date_50.date(), ')', sep='')
#done_date_50 = today+BDay(int(1+days_left_50.values[0]))
#print('(or ', round(days_left_50.values[0]/5,1), ' weeks to target, on ', done_date_50.date(), '...)', sep='')

#print(data.head())
fig = plt.figure(dpi=100)
ax1 = fig.add_subplot(111)
#days = np.array([x.days for x in (data['Date']-data['Date'][0])])
#print(days)
temp = data['Date'].iloc[0].normalize() - pd.Timedelta(data['Date'].iloc[0].normalize().weekday(), 'day')
while temp<data['Date'].iloc[-1]:
    ax1.vlines(temp, 0, target, linestyles='dashed')
    temp += pd.Timedelta(7, 'day')
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
ax1.set_ylim(0, target)
ax2.set_ylim(0, int(data['PageCount'].iloc[-1]*target/data['WordCount'].iloc[-1]))
plt.tight_layout()
plt.show()
