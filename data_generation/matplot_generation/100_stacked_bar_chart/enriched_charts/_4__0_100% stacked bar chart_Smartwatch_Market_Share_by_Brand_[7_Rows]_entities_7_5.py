
import matplotlib.pyplot as plt
import numpy as np

# Dataset
groups = ['Children', 'Teens', 'Young Adults', 'Adults', 'Seniors']
data_science = [5, 20, 35, 25, 15]
web_development = [5, 30, 25, 25, 15]
mobile_development = [10, 25, 20, 30, 15]
ai_ml = [5, 15, 30, 35, 15]
cloud_computing = [5, 10, 40, 30, 15]

# Calculating the cumulative sums
cum_data_science = np.array(data_science)
cum_web_development = cum_data_science + np.array(web_development)
cum_mobile_development = cum_web_development + np.array(mobile_development)
cum_ai_ml = cum_mobile_development + np.array(ai_ml)

# Converting to percentages
total = [sum(x) for x in zip(data_science, web_development, mobile_development, ai_ml, cloud_computing)]
data_science_pct = [i / j * 100 for i, j in zip(data_science, total)]
web_development_pct = [i / j * 100 for i, j in zip(web_development, total)]
mobile_development_pct = [i / j * 100 for i, j in zip(mobile_development, total)]
ai_ml_pct = [i / j * 100 for i, j in zip(ai_ml, total)]
cloud_computing_pct = [i / j * 100 for i, j in zip(cloud_computing, total)]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#F3FF33']

# Setting the bar width
bar_width = 0.6

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

ax.bar(groups, data_science_pct, color=colors[0], edgecolor='white', width=bar_width, label='Data Science')
ax.bar(groups, web_development_pct, bottom=data_science_pct, color=colors[1], edgecolor='white', width=bar_width, label='Web Development')
ax.bar(groups, mobile_development_pct, bottom=[i + j for i, j in zip(data_science_pct, web_development_pct)], color=colors[2], edgecolor='white', width=bar_width, label='Mobile Development')
ax.bar(groups, ai_ml_pct, bottom=[i + j + k for i, j, k in zip(data_science_pct, web_development_pct, mobile_development_pct)], color=colors[3], edgecolor='white', width=bar_width, label='AI/ML')
ax.bar(groups, cloud_computing_pct, bottom=[i + j + k + l for i, j, k, l in zip(data_science_pct, web_development_pct, mobile_development_pct, ai_ml_pct)], color=colors[4], edgecolor='white', width=bar_width, label='Cloud Computing')

# Adding labels and title
ax.set_ylabel('Percentage')
ax.set_title('Technology Preferences by Age Group')
plt.yticks(np.arange(0, 101, 10))
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

# Display the plot
plt.tight_layout()
plt.show()