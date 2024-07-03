
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data = [
    {'Date': '2023-06-01', 'Stars Observed': 4500, 'Cosmic Ray Intensity': 250},
    {'Date': '2023-06-02', 'Stars Observed': 4700, 'Cosmic Ray Intensity': 245},
    {'Date': '2023-06-03', 'Stars Observed': 4800, 'Cosmic Ray Intensity': 240},
    {'Date': '2023-06-04', 'Stars Observed': 4900, 'Cosmic Ray Intensity': 235},
    {'Date': '2023-06-05', 'Stars Observed': 5000, 'Cosmic Ray Intensity': 230},
    {'Date': '2023-06-06', 'Stars Observed': 5150, 'Cosmic Ray Intensity': 225},
    {'Date': '2023-06-07', 'Stars Observed': 5300, 'Cosmic Ray Intensity': 220}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(df['Date'], df['Stars Observed'], color='#1f77b4', marker='o', linestyle='-', linewidth=2, label='Stars Observed')
ax.plot(df['Date'], df['Cosmic Ray Intensity'], color='#ff7f0e', marker='s', linestyle='--', linewidth=2, label='Cosmic Ray Intensity')

ax.set_title('Weekly Astronomy Observations', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('Count')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)

ax.legend(loc='upper right')

for i, txt in enumerate(df['Stars Observed']):
    ax.annotate(txt, (df['Date'][i], df['Stars Observed'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Cosmic Ray Intensity']):
    ax.annotate(txt, (df['Date'][i], df['Cosmic Ray Intensity'][i]), textcoords="offset points", xytext=(0,10), ha='center')

ax.invert_yaxis()

plt.tight_layout()
plt.show()