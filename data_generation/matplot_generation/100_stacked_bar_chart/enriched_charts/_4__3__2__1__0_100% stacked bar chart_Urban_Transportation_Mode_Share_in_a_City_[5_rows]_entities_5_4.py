
import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
social_media_use = np.array([30, 25, 20, 15, 10, 5])
tv_streaming = np.array([25, 20, 25, 20, 15, 10])
outdoor_activities = np.array([20, 25, 30, 25, 20, 15])
reading = np.array([15, 20, 15, 25, 35, 45])
gaming = np.array([10, 10, 10, 15, 20, 25])

# Calculate percentages
totals = social_media_use + tv_streaming + outdoor_activities + reading + gaming
social_media_percentage = social_media_use / totals * 100
tv_streaming_percentage = tv_streaming / totals * 100
outdoor_activities_percentage = outdoor_activities / totals * 100
reading_percentage = reading / totals * 100
gaming_percentage = gaming / totals * 100

# Plotting
fig, ax = plt.subplots(figsize=(10, 14))
bar_width = 0.5

# Vertical bar plot
age_indices = np.arange(len(age_groups))

p1 = plt.bar(age_indices, social_media_percentage, color='#FF5733', edgecolor='white', width=bar_width)
p2 = plt.bar(age_indices, tv_streaming_percentage, bottom=social_media_percentage, color='#33FF57', edgecolor='white', width=bar_width)
p3 = plt.bar(age_indices, outdoor_activities_percentage, bottom=social_media_percentage+tv_streaming_percentage, color='#3357FF', edgecolor='white', width=bar_width)
p4 = plt.bar(age_indices, reading_percentage, bottom=social_media_percentage+tv_streaming_percentage+outdoor_activities_percentage, color='#FF33A6', edgecolor='white', width=bar_width)
p5 = plt.bar(age_indices, gaming_percentage, bottom=social_media_percentage+tv_streaming_percentage+outdoor_activities_percentage+reading_percentage, color='#33FFF5', edgecolor='white', width=bar_width)

plt.ylabel('Percentage')
plt.title('Leisure Activities Among Different Age Groups', pad=20)
plt.xticks(age_indices, age_groups)
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Social Media Use', 'TV/Streaming', 'Outdoor Activities', 'Reading', 'Gaming'), loc='upper right')
plt.show()