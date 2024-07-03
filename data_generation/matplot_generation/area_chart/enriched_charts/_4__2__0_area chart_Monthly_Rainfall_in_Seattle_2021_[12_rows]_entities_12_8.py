
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': list(range(1, 61)),
    'Distance Covered': [
        2.5, 3.0, 2.8, 3.5, 3.2, 4.0, 3.8, 4.5, 4.2, 4.7,
        5.0, 5.2, 5.5, 5.8, 6.0, 6.2, 6.5, 6.8, 7.0, 7.2,
        7.5, 7.8, 8.0, 8.2, 8.5, 8.8, 9.0, 9.2, 9.5, 9.8,
        10.0, 10.3, 10.5, 10.7, 11.0, 11.2, 11.5, 11.7, 12.0, 12.3,
        12.5, 12.8, 13.0, 13.2, 13.5, 13.7, 14.0, 14.3, 14.5, 14.8,
        15.0, 15.2, 15.5, 15.8, 16.0, 16.3, 16.5, 16.8, 17.0, 17.3
    ]
}
df = pd.DataFrame(data)

color = "#3498DB"

plt.figure(figsize=(16, 8))
plt.plot(df['Day'], df['Distance Covered'], color=color, linewidth=2)
plt.fill_between(df['Day'], df['Distance Covered'], color=color, alpha=0.3)

max_distance_day = df['Distance Covered'].idxmax() + 1
max_distance = df['Distance Covered'].max()
plt.text(max_distance_day, max_distance + 0.5, f'Peak: {max_distance} km', horizontalalignment='center', color='black')

plt.title('Distance Covered by Cyclist Over 2 Months')
plt.xlabel('Day')
plt.ylabel('Distance Covered (km)')

plt.show()