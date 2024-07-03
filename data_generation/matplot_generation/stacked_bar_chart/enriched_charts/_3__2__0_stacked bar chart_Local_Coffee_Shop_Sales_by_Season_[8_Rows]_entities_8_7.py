
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
mobile_data = [2, 3, 5, 7, 10, 12, 15]
voice_calls = [1500, 1600, 1700, 1800, 1900, 2000, 2100]
sms = [300, 350, 400, 450, 500, 550, 600]

# Plot
fig, ax = plt.subplots(figsize=(8, 10))

ax.barh(years, mobile_data, color='#4c72b0', edgecolor='white', height=0.5, label='Mobile Data (GB)')
ax.barh(years, voice_calls, left=mobile_data, color='#dd8452', edgecolor='white', height=0.5, label='Voice Calls (minutes)')
ax.barh(years, sms, left=[i + j for i, j in zip(mobile_data, voice_calls)], color='#55a868', edgecolor='white', height=0.5, label='SMS (messages)')

# Labels and Title
ax.set_xlabel('Usage')
ax.set_title('Annual Mobile Usage from 2015 to 2021', pad=20)
ax.legend(loc='lower right')

# Display the plot
plt.show()