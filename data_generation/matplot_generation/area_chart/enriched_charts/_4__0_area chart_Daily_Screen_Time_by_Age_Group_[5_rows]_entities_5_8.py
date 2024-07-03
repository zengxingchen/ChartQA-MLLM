
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', end='2024-01-31'),
    'NewSubscribers': [50, 80, 70, 90, 65, 75, 85, 95, 60, 110, 100, 120, 130, 115, 125, 135, 140, 150, 145, 155, 160, 170, 165, 180, 190, 200, 195, 205, 210, 220, 225]
})

plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")

ax = sns.lineplot(data=data, x='Date', y='NewSubscribers', color="#FF4500")
ax.fill_between(data.Date, data.NewSubscribers, color="#87CEFA", alpha=0.6)

highest_subs = data.NewSubscribers.max()
highest_day = data.Date[data.NewSubscribers.idxmax()]
plt.annotate(f'Highest\n{highest_subs}', xy=(highest_day, highest_subs), xytext=(highest_day, highest_subs+10),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

plt.title('Daily New Subscribers in January 2024', fontsize=16, pad=20)
plt.xlabel('Date')
plt.ylabel('New Subscribers')

plt.show()