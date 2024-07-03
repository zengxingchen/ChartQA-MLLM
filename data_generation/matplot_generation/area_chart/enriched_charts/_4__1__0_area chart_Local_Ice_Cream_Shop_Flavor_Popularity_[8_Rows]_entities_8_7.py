
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
             "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
             "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
             "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
             "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
             "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30"],
    "Value": [110, 125, 130, 140, 145, 155, 150, 165, 160, 175, 170, 185, 180, 195, 190,
              205, 200, 215, 210, 225, 230, 220, 235, 240, 250, 255, 260, 270, 275, 280]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(12, 8))
ax.fill_between(df['Date'], df['Value'], color='#ff7f0e', alpha=0.7)

for i, txt in enumerate(df['Value']):
    ax.annotate(txt, (df['Date'][i], df['Value'][i]), textcoords="offset points", xytext=(0,5), ha='center')

ax.set_title('Monthly Sales Revenue ($)', fontsize=18)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Revenue ($)', fontsize=14)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()