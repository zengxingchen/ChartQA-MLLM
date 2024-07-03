
import matplotlib.pyplot as plt

# Provided data
chart_data = [
    {'Age Group': '18-24', ' Calls': 15, ' Social Media': 45, ' Gaming': 25, ' Other': 15},
    {'Age Group': '25-34', ' Calls': 20, ' Social Media': 40, ' Gaming': 20, ' Other': 20},
    {'Age Group': '35-44', ' Calls': 25, ' Social Media': 35, ' Gaming': 15, ' Other': 25},
    {'Age Group': '45-54', ' Calls': 30, ' Social Media': 30, ' Gaming': 10, ' Other': 30},
    {'Age Group': '55+', ' Calls': 35, ' Social Media': 20, ' Gaming': 5, ' Other': 40}
]

# Convert to percentages
age_groups = [data['Age Group'] for data in chart_data]
categories = [' Calls', ' Social Media', ' Gaming', ' Other']
percent_data = {category: [] for category in categories}

for data in chart_data:
    total = sum(data[category] for category in categories)
    for category in categories:
        percent_data[category].append(data[category] / total * 100)

# Plotting the stacked bar chart
fig, ax = plt.subplots()

bottom = [0] * len(age_groups)
for category in categories:
    ax.bar(age_groups, percent_data[category], bottom=bottom, label=category.strip())
    bottom = [bottom[i] + percent_data[category][i] for i in range(len(age_groups))]

# Adding details
ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Distribution of Activities by Age Group')
ax.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()