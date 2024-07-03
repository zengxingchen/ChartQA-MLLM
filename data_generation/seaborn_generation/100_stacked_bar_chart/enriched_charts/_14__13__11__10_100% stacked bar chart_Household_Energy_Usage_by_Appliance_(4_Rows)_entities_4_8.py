
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Location': 'Location A', 'Travelers': 200, 'Flights Taken': 40, 'Avg Hotel Rating': 4.5, 'Activities Booked': 150, 'Guided Tours': 10},
    {'Location': 'Location B', 'Travelers': 180, 'Flights Taken': 35, 'Avg Hotel Rating': 4.8, 'Activities Booked': 120, 'Guided Tours': 15},
    {'Location': 'Location C', 'Travelers': 210, 'Flights Taken': 38, 'Avg Hotel Rating': 4.7, 'Activities Booked': 170, 'Guided Tours': 12},
    {'Location': 'Location D', 'Travelers': 220, 'Flights Taken': 45, 'Avg Hotel Rating': 4.6, 'Activities Booked': 160, 'Guided Tours': 14},
    {'Location': 'Location E', 'Travelers': 190, 'Flights Taken': 42, 'Avg Hotel Rating': 4.9, 'Activities Booked': 140, 'Guided Tours': 16}
]

df = pd.DataFrame(data)
df.set_index('Location', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(14, 8))

bottom = np.zeros(len(df))

colors = ['#FF6347', '#4682B4', '#8A2BE2', '#3CB371', '#FFD700']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.xlabel('Locations')
plt.ylabel('Percentage')
plt.title('Travel & Adventure Statistics Breakdown (100% Stacked)', pad=20)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()