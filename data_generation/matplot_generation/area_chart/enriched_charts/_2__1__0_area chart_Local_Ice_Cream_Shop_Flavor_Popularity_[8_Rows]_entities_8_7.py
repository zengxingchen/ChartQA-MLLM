
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
             "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
             "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
             "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
             "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
             "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30",
             "2023-01-31"],
    "Value": [100, 120, 115, 130, 140, 150, 145, 160, 155, 170, 165, 180, 175, 190, 185, 200, 195, 210, 205, 220, 215, 230, 225, 240, 235, 250, 245, 260, 255, 270, 265]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(12, 8))
ax.fill_between(df['Date'], df['Value'], color='#FF5733', alpha=0.6)

for i, txt in enumerate(df['Value']):
    ax.annotate(txt, (df['Date'][i], df['Value'][i]), textcoords="offset points", xytext=(0,5), ha='center')

ax.set_title('Monthly Steps Count', fontsize=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Steps Count', fontsize=14)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()