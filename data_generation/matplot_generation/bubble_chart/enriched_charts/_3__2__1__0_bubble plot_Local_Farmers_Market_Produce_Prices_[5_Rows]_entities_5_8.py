
import matplotlib.pyplot as plt

categories = ['Stargazing', 'Meteor Showers', 'Reading Space Books', 'Watching Space Documentaries', 'Space-Themed Video Games']
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
hours = [
    [2.2, 2.4, 2.5, 2.3, 2.1, 1.8],
    [1.8, 2.0, 2.1, 1.9, 1.7, 1.5],
    [1.6, 1.7, 1.6, 1.4, 1.3, 1.1],
    [2.9, 3.0, 3.1, 3.0, 2.8, 2.6],
    [2.0, 1.8, 1.7, 1.5, 1.3, 1.1]
]

flat_age_groups = age_groups * len(categories)
flat_hours = [hour for sublist in hours for hour in sublist]
bubble_sizes = [size * 60 for size in flat_hours]

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

plt.figure(figsize=(16, 12))
plt.scatter(flat_age_groups, flat_hours, s=bubble_sizes, c=colors, alpha=0.6)

plt.title('Average Hours Spent on Astronomy Activities by Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours per Day')

plt.grid(True)

plt.show()