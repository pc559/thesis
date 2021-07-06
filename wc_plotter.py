import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np
fname = "word_counts.csv"
data = pd.read_csv(fname)
data['Date'] = pd.to_datetime(data['Date'])
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
date_form = DateFormatter("%d-%m")
ax1.xaxis.set_major_formatter(date_form)
ax2.xaxis.set_major_formatter(date_form)
plt.tight_layout()
plt.show()
