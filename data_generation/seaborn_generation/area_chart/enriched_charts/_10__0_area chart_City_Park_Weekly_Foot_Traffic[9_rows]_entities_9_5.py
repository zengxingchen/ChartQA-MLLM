
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

start = datetime(2023, 1, 1)
end = datetime(2023, 12, 31)
delta = timedelta(days=1)
dates = pd.date_range(start, end, freq=delta)

np.random.seed(42)
hours_spent = 3 + np.sin(np.linspace(0, 2 * np.pi, len(dates))) * 2 + np.random.normal(0, 0.2, len(dates))

data = pd.DataFrame({'date': dates, 'hours_spent': hours_spent})

sns.set(rc={'figure.figsize': (16, 8)})

area_chart = sns.lineplot(x='date', y='hours_spent', data=data, color="#1f77b4")

plt.fill_between(data.date, data.hours_spent, color="#9edae5")

peak_day = data.loc[data['hours_spent'].idxmax()]
plt.text(peak_day.date, peak_day.hours_spent, 'Peak Creativity', horizontalalignment='right', size='medium', color='black')

plt.title('Daily Hours Spent on Creative Activities in 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Hours Spent', fontsize=14)

plt.show()